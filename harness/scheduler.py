"""The run loop: claim jobs from the ledger, run them a few at a time, pause on limits, resume.

Rules this loop enforces:
- A job is `done` only after its output file is renamed into place and its row is updated.
- On start-up, stale `running` rows are recovered (if their output was fully written) or reset to pending.
- A usage limit pauses only the model family that hit it. The other family keeps working.
- Limits and transient errors never count toward the retry cap; real failures do (cap 3).
"""
from __future__ import annotations

import os
import time
from concurrent.futures import FIRST_COMPLETED, Future, ThreadPoolExecutor, wait
from dataclasses import dataclass

from . import stages
from .claude_cli import CallResult, kill_stale
from .config import MAX_REAL_FAILURES, MAX_TRANSIENT, MODEL_FAMILY, Paths, STAGE_MODEL
from .ledger import Ledger
from .notify import Notifier


def _keep_awake(on: bool):
    """Ask Windows not to idle-sleep while the harness has work (released on exit). No settings are changed."""
    if os.name != "nt":
        return
    try:
        import ctypes
        ES_CONTINUOUS, ES_SYSTEM_REQUIRED = 0x80000000, 0x00000001
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | (ES_SYSTEM_REQUIRED if on else 0))
    except Exception:
        pass


def family_of(model: str) -> str:
    return MODEL_FAMILY.get(model, "fable" if "fable" in model else "opus")


@dataclass
class RunOptions:
    concurrency: int = 2
    resume_buffer_s: float = 120.0
    probe_interval_s: float = 20 * 60
    exit_when_idle: bool = True
    keep_awake: bool = True
    max_jobs: int | None = None      # stop after starting this many (debugging)


class Scheduler:
    def __init__(self, paths: Paths, backend, notifier: Notifier, opts: RunOptions):
        self.p = paths
        self.backend = backend
        self.n = notifier
        self.opts = opts
        self.ledger = Ledger(paths.ledger)
        self.cases = stages.load_cases(paths)
        self.started = 0

    # ------------------------------------------------------------ start-up
    def recover(self):
        for job in self.ledger.stale_running():
            meta = stages.recover_output(self.p, job)
            if meta:
                self.ledger.mark_done(job["id"], output_path=stages.output_path(self.p, job),
                                      tokens_in=meta.get("tokens_in", 0), tokens_out=meta.get("tokens_out", 0),
                                      cost=meta.get("cost_usd", 0), duration=meta.get("duration_s", 0),
                                      family=family_of(job["model"]))
                self.n.event("recover", f"{job['id']} output was already saved; marked done")
                continue
            if job["pid"] and kill_stale(job["pid"]):
                self.n.event("recover", f"killed leftover claude process {job['pid']} for {job['id']}")
            self.ledger.reset_stale(job["id"])
            self.n.event("recover", f"{job['id']} was running when the harness stopped; reset to pending")

    # ------------------------------------------------------------ worker (runs in a thread)
    def _work(self, job) -> tuple[CallResult, dict | None]:
        spec = stages.build_call(self.p, job, self.cases)
        sp_file = self.p.tmp / f"system_{job['stage']}_{abs(hash(spec['system'])) % 10**10}.md"
        if not sp_file.exists():
            stages.atomic_write(sp_file, spec["system"], self.p.tmp)
        res = self.backend.call(model=job["model"], system_prompt_file=sp_file, user_text=spec["user"],
                                effort=spec["effort"], timeout_s=spec["timeout"],
                                on_pid=lambda pid: self._pids.append((job["id"], pid)), job_tag=job["id"])
        if res.kind != "ok":
            return res, None
        meta = {
            "job_id": job["id"], "stage": job["stage"], "case_id": job["case_id"], "seed": job["seed"],
            "model": job["model"], "effort": spec["effort"], "tokens_in": res.tokens_in, "tokens_out": res.tokens_out,
            "cost_usd": res.cost_usd, "duration_s": round(res.duration_s, 1), "finished_at": time.time(),
            "models_used": {k: {kk: v.get(kk) for kk in ("inputTokens", "outputTokens", "costUSD")}
                            for k, v in res.models_used.items()},
        }
        if job["stage"] == "run":
            # The skill version is logged with the run, never sent to the judge.
            meta["skill_version"] = job["version"]
            meta["skill_sha"] = stages.skill_hash(self.p, job["version"])
        if getattr(self.backend, "__class__", None).__name__ == "FakeBackend":
            meta["fake"] = True
        content, err = stages.validate_and_render(job, res.text, meta)
        if err:
            return CallResult("failure", error=err, tokens_in=res.tokens_in, tokens_out=res.tokens_out), None
        stages.write_output(self.p, job, content, meta)
        return res, meta

    # ------------------------------------------------------------ limits
    def _on_limit(self, job, res: CallResult):
        fam = family_of(job["model"])
        now = time.time()
        if res.reset_at:
            resume_at, next_probe = res.reset_at + self.opts.resume_buffer_s, None
            when = time.strftime("%H:%M:%S", time.localtime(resume_at))
            detail = f"reset time given; resuming at {when}"
        else:
            resume_at, next_probe = None, now + self.opts.probe_interval_s
            detail = f"no reset time given; probing every {int(self.opts.probe_interval_s / 60)} min"
        self.ledger.mark_limit(job["id"], res.error)
        new = self.ledger.set_paused(fam, resume_at, next_probe, res.error[:300])
        models = [m for m in set(STAGE_MODEL.values()) if family_of(m) == fam]
        self.ledger.pause_family_jobs(models)
        if new:
            self.n.event("pause", f"{fam} limit hit on {job['id']}: {detail}", toast=True)

    def _check_resume(self):
        now = time.time()
        for fam in list(self.ledger.paused_families()):
            lim = self.ledger.get_limit(fam)
            ready = False
            if lim["resume_at"] is not None and now >= lim["resume_at"]:
                ready = True
            elif lim["resume_at"] is None and lim["next_probe"] is not None and now >= lim["next_probe"]:
                model = next(m for m in set(STAGE_MODEL.values()) if family_of(m) == fam)
                pr = self.backend.probe(model)
                if pr.kind == "ok":
                    ready = True
                else:
                    self.ledger.set_paused(fam, None, now + self.opts.probe_interval_s, lim["reason"])
                    self.n.event("probe", f"{fam} still limited; next probe in "
                                          f"{int(self.opts.probe_interval_s / 60)} min")
            if ready:
                self.ledger.clear_paused(fam)
                models = [m for m in set(STAGE_MODEL.values()) if family_of(m) == fam]
                self.ledger.unpause_family_jobs(models, {j['id'] for j in self.inflight.values()})
                self.n.event("resume", f"{fam} limit lifted; resuming {self.ledger.remaining()} remaining jobs",
                             toast=True)

    # ------------------------------------------------------------ main loop
    def run(self) -> int:
        self.p.ensure()
        self.recover()
        self._pids: list = []
        rounds_before = self._finished_rounds()
        self.inflight: dict[Future, object] = {}
        inflight = self.inflight
        self.n.event("start", f"harness run started; {self.ledger.remaining()} jobs remaining")
        if self.opts.keep_awake:
            _keep_awake(True)
        try:
            return self._loop(rounds_before)
        finally:
            _keep_awake(False)

    def _loop(self, rounds_before) -> int:
        inflight = self.inflight
        with ThreadPoolExecutor(max_workers=self.opts.concurrency) as pool:
            while True:
                self._check_resume()
                paused = self.ledger.paused_families()
                free = self.opts.concurrency - len(inflight)
                if free > 0 and (self.opts.max_jobs is None or self.started < self.opts.max_jobs):
                    for job in self.ledger.claimable(paused, family_of, free):
                        if self.ledger.mark_running(job["id"]):
                            job = self.ledger.one("SELECT * FROM jobs WHERE id=?", (job["id"],))
                            inflight[pool.submit(self._work, job)] = job
                            self.started += 1
                while self._pids:
                    jid, pid = self._pids.pop()
                    self.ledger.set_pid(jid, pid)
                if not inflight:
                    if self.ledger.remaining() == 0:
                        break
                    if not self.ledger.paused_families() and not self._any_claimable_soon():
                        self.n.event("stuck", "jobs remain but none can run (failed dependencies?)")
                        break
                    time.sleep(self._idle_sleep())
                    continue
                done, _ = wait(list(inflight), timeout=2.0, return_when=FIRST_COMPLETED)
                for fut in done:
                    job = inflight.pop(fut)
                    self._handle(job, fut)
                self._announce_rounds(rounds_before)
        self._announce_rounds(rounds_before)
        counts = self.ledger.counts()
        self.n.event("finish", f"harness idle; counts={counts}", toast=True)
        return 0 if counts.get("failed", 0) == 0 else 1

    def _handle(self, job, fut: Future):
        try:
            res, meta = fut.result()
        except Exception as e:  # a bug in our own code: count as a real failure
            res, meta = CallResult("failure", error=f"harness exception: {e!r}"), None
        if res.kind == "ok" and meta is not None:
            self.ledger.mark_done(job["id"], output_path=stages.output_path(self.p, job), tokens_in=res.tokens_in,
                                  tokens_out=res.tokens_out, cost=res.cost_usd, duration=res.duration_s,
                                  family=family_of(job["model"]))
        elif res.kind == "limit":
            self._on_limit(job, res)
        elif res.kind == "transient":
            hits = self.ledger.one("SELECT transient_hits FROM jobs WHERE id=?", (job["id"],))["transient_hits"]
            backoff = min(600, 30 * (2 ** hits))
            n = self.ledger.mark_transient(job["id"], res.error, backoff)
            self.n.event("transient", f"{job['id']}: {res.error[:160]} (retry in {backoff}s)")
            if n >= MAX_TRANSIENT:
                self.ledger.mark_failure(job["id"], "too many transient errors: " + res.error, 1)
        else:
            status = self.ledger.mark_failure(job["id"], res.error, MAX_REAL_FAILURES)
            self.n.event("failure", f"{job['id']} ({status}): {res.error[:300]}")

    def _idle_sleep(self) -> float:
        now = time.time()
        waits = [5.0]
        for fam in self.ledger.paused_families():
            lim = self.ledger.get_limit(fam)
            t = lim["resume_at"] if lim["resume_at"] is not None else lim["next_probe"]
            if t:
                waits.append(max(0.5, t - now))
        nb = self.ledger.one("SELECT MIN(not_before) t FROM jobs WHERE status='pending' AND not_before>?", (now,))
        if nb and nb["t"]:
            waits.append(max(0.5, nb["t"] - now))
        return min(60.0, min(waits))

    def _any_claimable_soon(self) -> bool:
        if self.ledger.claimable(set(), family_of, 1):
            return True
        nb = self.ledger.one("SELECT COUNT(*) c FROM jobs WHERE status='pending' AND not_before>?", (time.time(),))
        return nb["c"] > 0

    # ------------------------------------------------------------ rounds
    def _finished_rounds(self) -> set[str]:
        rows = self.ledger.q(
            "SELECT r.round, SUM(CASE WHEN j.status='done' THEN 1 ELSE 0 END) d, COUNT(*) n "
            "FROM round_jobs r JOIN jobs j ON j.id=r.job_id GROUP BY r.round")
        return {r["round"] for r in rows if r["d"] == r["n"]}

    def _announce_rounds(self, before: set[str]):
        now_done = self._finished_rounds()
        for r in sorted(now_done - before):
            self.n.event("round_done", f"round {r}: every job is done; ready for the accept/reject decision",
                         toast=True)
        before |= now_done
