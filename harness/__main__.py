"""python -m harness <command>

  run       run every pending job in the ledger, pausing and resuming on usage limits
  enqueue   add jobs for a skill version x cases x seeds x stages (idempotent)
  status    progress per round and stage, pause state, tokens, estimated finish
  estimate  token and limit-reset estimate for the jobs that are not done yet
"""
from __future__ import annotations

import argparse
import json
import sys
import time

from .config import JUDGE_MODEL, PROBE_MODEL, SKILL_MODEL, WINDOW_HOURS, paths_from_env
from .ledger import Ledger


def cmd_run(a) -> int:
    from .claude_cli import ClaudeBackend, FakeBackend
    from .lock import AlreadyRunning, InstanceLock
    from .notify import Notifier
    from .scheduler import RunOptions, Scheduler

    p = paths_from_env(a.root)
    p.ensure()
    notifier = Notifier(p.events, toast=not a.no_toast)
    try:
        with InstanceLock(p.lock):
            if a.backend == "fake":
                backend = FakeBackend(p.cwd_sandbox, delay=a.fake_delay, limit_after=a.simulate_limit_after,
                                      reset_seconds=a.simulate_reset_seconds, limit_family=a.simulate_limit_family,
                                      give_reset=not a.simulate_no_reset_time,
                                      call_log=p.state / "fake_calls.log")
            else:
                if a.simulate_limit_after is not None:
                    print("--simulate-limit-after needs --backend fake", file=sys.stderr)
                    return 2
                backend = ClaudeBackend(p.cwd_sandbox)
            opts = RunOptions(concurrency=a.concurrency, resume_buffer_s=a.resume_buffer,
                              probe_interval_s=a.probe_interval, max_jobs=a.max_jobs)
            return Scheduler(p, backend, notifier, opts).run()
    except AlreadyRunning:
        print("harness is already running (lock held); nothing to do")
        return 0


def _case_ids(p, sel: str) -> list[str]:
    from .stages import load_cases
    cases = load_cases(p)
    if sel in ("dev", "heldout"):
        return [c for c, v in cases.items() if v.get("split") == sel]
    if sel == "dryrun":
        return [c for c, v in cases.items() if v.get("dry_run")]
    if sel == "all":
        return list(cases)
    ids = [s.strip() for s in sel.split(",") if s.strip()]
    missing = [i for i in ids if i not in cases]
    if missing:
        raise SystemExit(f"unknown cases: {missing}")
    return ids


def cmd_enqueue(a) -> int:
    from .ledger import job_id
    p = paths_from_env(a.root)
    led = Ledger(p.ledger)
    cases = _case_ids(p, a.cases)
    from .stages import load_cases
    allc = load_cases(p)
    held = [c for c in cases if allc[c].get("split") == "heldout"]
    if held and not a.final_eval:
        raise SystemExit(f"refusing to enqueue held-out cases {held} without --final-eval (Phase 4 only)")
    stages_ = [s.strip() for s in a.stages.split(",")]
    if a.round:
        led.add_round(a.round, a.version, a.compare_to, a.cases)
    n0 = led.one("SELECT COUNT(*) c FROM jobs")["c"]
    versions = [a.version] + ([a.compare_to] if a.compare_to else [])
    for c in cases:
        if "probe" in stages_:
            for s in range(1, a.seeds + 1):
                led.add_job(version="-", case_id=c, seed=s, stage="probe", model=PROBE_MODEL, round_name=a.round)
        for v in versions:
            for s in range(1, a.seeds + 1):
                if "run" in stages_ or "judge" in stages_ or "pairwise" in stages_:
                    led.add_job(version=v, case_id=c, seed=s, stage="run", model=SKILL_MODEL, round_name=a.round)
                if "judge" in stages_:
                    led.add_job(version=v, case_id=c, seed=s, stage="judge", model=JUDGE_MODEL,
                                depends_on=[job_id(v, c, s, "run")], round_name=a.round)
        if "pairwise" in stages_ and a.compare_to:
            for s in range(1, a.seeds + 1):
                led.add_job(version=a.version, other_version=a.compare_to, case_id=c, seed=s, stage="pairwise",
                            model=JUDGE_MODEL, round_name=a.round,
                            depends_on=[job_id(a.version, c, s, "run"), job_id(a.compare_to, c, s, "run")])
    n1 = led.one("SELECT COUNT(*) c FROM jobs")["c"]
    print(f"enqueued {n1 - n0} new jobs ({n1} total in ledger)")
    return 0


def _fmt_t(ts):
    return time.strftime("%Y-%m-%d %H:%M", time.localtime(ts)) if ts else "-"


def cmd_status(a) -> int:
    p = paths_from_env(a.root)
    if not p.ledger.exists():
        print("no ledger yet")
        return 0
    led = Ledger(p.ledger)
    now = time.time()
    print("== Progress by round and stage")
    rows = led.q(
        "SELECT r.round, j.stage, j.status, COUNT(*) c FROM round_jobs r JOIN jobs j ON j.id=r.job_id "
        "GROUP BY r.round, j.stage, j.status ORDER BY r.round, j.stage")
    table: dict = {}
    for r in rows:
        table.setdefault((r["round"], r["stage"]), {})[r["status"]] = r["c"]
    for (rnd, stage), st in table.items():
        total = sum(st.values())
        print(f"  {rnd:<14} {stage:<9} {st.get('done', 0):>4}/{total:<4} done  "
              + "  ".join(f"{k}={v}" for k, v in sorted(st.items()) if k != "done"))
    counts = led.counts()
    remaining = led.remaining()
    print(f"\n== Jobs: {sum(counts.values())} total, {remaining} remaining  {counts}")
    print("\n== Pause state")
    lims = led.q("SELECT * FROM limits")
    if not any(l["paused"] for l in lims):
        print("  not paused")
    for l in lims:
        if l["paused"]:
            when = l["resume_at"] or l["next_probe"]
            how = "expected resume" if l["resume_at"] else "next probe"
            print(f"  {l['family']}: PAUSED since {_fmt_t(l['paused_since'])}; {how} {_fmt_t(when)}"
                  f"  ({l['reason'][:80] if l['reason'] else ''})")
    pz = led.one("SELECT COUNT(*) n, SUM(COALESCE(end, ?) - start) s FROM pauses", (now,))
    print(f"  pauses so far: {pz['n']}, total paused time {((pz['s'] or 0) / 3600):.1f} h")
    print("\n== Tokens")
    tot = led.one("SELECT SUM(tokens_in) i, SUM(tokens_out) o, SUM(cost_usd) c FROM jobs WHERE status='done'")
    print(f"  all done jobs: in {tot['i'] or 0:,}  out {tot['o'] or 0:,}  (API-equivalent ${tot['c'] or 0:,.2f})")
    for fam in ("opus", "fable"):
        w = led.one("SELECT SUM(tokens_in) i, SUM(tokens_out) o, SUM(cost_usd) c FROM usage WHERE family=? AND ts>?",
                    (fam, now - WINDOW_HOURS * 3600))
        print(f"  {fam} last {WINDOW_HOURS}h: in {w['i'] or 0:,}  out {w['o'] or 0:,}  (${w['c'] or 0:,.2f})")
    print("\n== Estimated finish")
    avg = {r["stage"]: r["d"] for r in led.q(
        "SELECT stage, AVG(duration_s) d FROM jobs WHERE status='done' AND duration_s>0 GROUP BY stage")}
    rem = led.q("SELECT stage, COUNT(*) c FROM jobs WHERE status IN ('pending','running','paused_limit') GROUP BY stage")
    if not rem:
        print("  nothing left to run")
    else:
        secs = sum(r["c"] * (avg.get(r["stage"]) or 300) for r in rem) / max(1, a.concurrency)
        print(f"  ~{secs / 3600:.1f} h of call time at concurrency {a.concurrency}, plus any limit pauses"
              f"  -> earliest {_fmt_t(now + secs)}")
    return 0


def cmd_estimate(a) -> int:
    """Estimate tokens for jobs not yet done, using measured averages where we have them."""
    p = paths_from_env(a.root)
    led = Ledger(p.ledger)
    measured = {r["stage"]: (r["i"], r["o"], r["c"], r["n"]) for r in led.q(
        "SELECT stage, AVG(tokens_in) i, AVG(tokens_out) o, AVG(cost_usd) c, COUNT(*) n FROM jobs "
        "WHERE status='done' AND tokens_out>0 GROUP BY stage")}
    defaults = {"run": (9000, 12000, 0.27), "judge": (16000, 3000, 0.25), "pairwise": (26000, 3000, 0.33),
                "probe": (2000, 200, 0.012)}
    rem = led.q("SELECT stage, COUNT(*) c FROM jobs WHERE status!='done' GROUP BY stage")
    ti = to = usd = 0
    for r in rem:
        i, o, c = (measured[r["stage"]][:3] if r["stage"] in measured else defaults[r["stage"]])
        ti += i * r["c"]; to += o * r["c"]; usd += c * r["c"]
        src = f"measured over {measured[r['stage']][3]} jobs" if r["stage"] in measured else "assumed"
        print(f"  {r['stage']:<9} {r['c']:>5} jobs x ({i:,.0f} in + {o:,.0f} out) [{src}]")
    print(f"  total: {ti:,.0f} input + {to:,.0f} output tokens; API-equivalent ${usd:,.2f}")
    if a.window_usd:
        print(f"  at ~${a.window_usd:.0f} per 5-hour Max window: ~{usd / a.window_usd:.1f} windows")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="python -m harness")
    ap.add_argument("--root", help="alternate project root (tests use a sandbox)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run")
    r.add_argument("--concurrency", type=int, default=2)
    r.add_argument("--backend", choices=["claude", "fake"], default="claude")
    r.add_argument("--simulate-limit-after", type=int, default=None,
                   help="fake backend: hit a usage limit after N successful calls")
    r.add_argument("--simulate-reset-seconds", type=float, default=5)
    r.add_argument("--simulate-limit-family", choices=["opus", "fable", "any"], default="opus")
    r.add_argument("--simulate-no-reset-time", action="store_true")
    r.add_argument("--fake-delay", type=float, default=0.3)
    r.add_argument("--resume-buffer", type=float, default=120, help="seconds to wait past the reset time")
    r.add_argument("--probe-interval", type=float, default=1200, help="seconds between probes when no reset time")
    r.add_argument("--max-jobs", type=int, default=None)
    r.add_argument("--no-toast", action="store_true")
    r.set_defaults(fn=cmd_run)

    e = sub.add_parser("enqueue")
    e.add_argument("--round")
    e.add_argument("--version", default="v0")
    e.add_argument("--compare-to")
    e.add_argument("--cases", required=True, help="dev | heldout | dryrun | all | comma-separated ids")
    e.add_argument("--seeds", type=int, default=3)
    e.add_argument("--stages", default="run,judge")
    e.add_argument("--final-eval", action="store_true", help="allow held-out cases (Phase 4 only)")
    e.set_defaults(fn=cmd_enqueue)

    s = sub.add_parser("status")
    s.add_argument("--concurrency", type=int, default=2)
    s.set_defaults(fn=cmd_status)

    es = sub.add_parser("estimate")
    es.add_argument("--window-usd", type=float, default=None)
    es.set_defaults(fn=cmd_estimate)

    a = ap.parse_args(argv)
    if getattr(a, "root", None) is None:
        a.root = None
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
