"""Interrupt-and-resume test. Spends no tokens (fake backend).

What it does:
  1. Builds a sandbox with the 3 dry-run cases and two skill versions.
  2. Enqueues a full round: 3 cases x 3 seeds x (run + judge) for v0 and v1, plus pairwise v1 vs v0
     = 18 runs + 18 judges + 9 pairwise = 45 jobs.
  3. Starts `python -m harness run` with a simulated Opus usage limit after 6 calls (reset in 4 s).
  4. Waits until the limit has paused and resumed, then kills the harness hard in the middle of the round,
     while jobs are in flight.
  5. Checks that a second copy refuses to start while the first holds the lock (before the kill).
  6. Restarts the harness (no simulated limit) and lets it finish.
  7. Asserts: every job done exactly once, one output file per job, no job started after it was done,
     the pause/resume was logged, and Fable (judge) jobs kept running while Opus was paused.

Run:  python tests/test_resume.py
"""
from __future__ import annotations

import json
import shutil
import sqlite3
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
SANDBOX = PROJECT / "tests" / "_sandbox_resume"
PY = sys.executable


def harness(*args, wait=True, **kw):
    cmd = [PY, "-m", "harness", "--root", str(SANDBOX), *args]
    if wait:
        return subprocess.run(cmd, cwd=PROJECT, capture_output=True, text=True, timeout=600, **kw)
    return subprocess.Popen(cmd, cwd=PROJECT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, **kw)


def db():
    con = sqlite3.connect(str(SANDBOX / "state" / "ledger.db"), timeout=30)
    con.row_factory = sqlite3.Row
    return con


def setup():
    if SANDBOX.exists():
        shutil.rmtree(SANDBOX)
    (SANDBOX / "data").mkdir(parents=True)
    shutil.copytree(PROJECT / "data" / "dossiers", SANDBOX / "data" / "dossiers")
    shutil.copytree(PROJECT / "data" / "answer_keys", SANDBOX / "data" / "answer_keys")
    (SANDBOX / "data" / "probes").mkdir()
    cases = json.loads((PROJECT / "data" / "cases.json").read_text(encoding="utf-8"))
    cases["cases"] = [c for c in cases["cases"] if c.get("dry_run")]
    (SANDBOX / "data" / "cases.json").write_text(json.dumps(cases), encoding="utf-8")
    for v in ("v0", "v1"):
        d = SANDBOX / "skill_versions" / v
        d.mkdir(parents=True)
        shutil.copy(PROJECT / "skill_versions" / "v0" / "SKILL.md", d / "SKILL.md")
    (SANDBOX / "skill_versions" / "v1" / "SKILL.md").open("a").write("\n<!-- v1 test edit -->\n")


def main() -> int:
    setup()
    r = harness("enqueue", "--round", "test-r1", "--version", "v1", "--compare-to", "v0", "--cases", "dryrun",
                "--seeds", "3", "--stages", "run,judge,pairwise")
    print(r.stdout.strip())
    assert "45" in r.stdout, r.stdout + r.stderr

    # --- first run: simulated limit, then a hard kill mid-round
    proc = harness("run", "--backend", "fake", "--simulate-limit-after", "6", "--simulate-reset-seconds", "4",
                   "--resume-buffer", "1", "--fake-delay", "0.6", "--concurrency", "2", "--no-toast", wait=False)
    killed_running = []
    deadline = time.time() + 120
    events = SANDBOX / "state" / "events.log"
    second_copy_checked = False
    while time.time() < deadline:
        time.sleep(0.3)
        log = events.read_text(encoding="utf-8") if events.exists() else ""
        if "\tpause\t" in log and not second_copy_checked:
            r2 = harness("run", "--backend", "fake", "--no-toast")
            assert "already running" in r2.stdout, "second copy should refuse to run: " + r2.stdout + r2.stderr
            second_copy_checked = True
            print("lock check: second copy refused to start while the first was running")
        if "\tresume\t" in log:
            con = db()
            done = con.execute("SELECT COUNT(*) FROM jobs WHERE status='done'").fetchone()[0]
            running = [x[0] for x in con.execute("SELECT id FROM jobs WHERE status='running'")]
            con.close()
            if running and 15 <= done <= 35:
                proc.kill()  # TerminateProcess: no cleanup runs, like a crash or a closed window
                proc.wait()
                killed_running = running
                print(f"killed harness mid-round: {done} done, in flight: {running}")
                break
    else:
        proc.kill()
        out = proc.stdout.read() if proc.stdout else ""
        raise AssertionError("never reached the kill point\n" + out)
    assert second_copy_checked, "lock check did not run"

    con = db()
    stale = [x[0] for x in con.execute("SELECT id FROM jobs WHERE status='running'")]
    con.close()
    assert stale, "expected stale running rows after the kill"
    print(f"stale running rows after kill: {len(stale)}")

    # --- second run: resume from the ledger and finish
    r = harness("run", "--backend", "fake", "--fake-delay", "0.1", "--concurrency", "2", "--no-toast")
    print(r.stdout[-1500:])
    assert r.returncode == 0, r.stdout + r.stderr

    # --- checks
    con = db()
    rows = [dict(x) for x in con.execute("SELECT * FROM jobs")]
    statuses = defaultdict(int)
    for x in rows:
        statuses[x["status"]] += 1
    assert statuses == {"done": 45}, f"not all done: {dict(statuses)}"

    outputs = [p for p in (SANDBOX / "runs").rglob("*") if p.is_file() and not p.name.endswith(".meta.json")]
    assert len(outputs) == 45, f"expected 45 output files, found {len(outputs)}"
    for x in rows:
        meta = json.loads(Path(x["output_path"] + ".meta.json").read_text(encoding="utf-8"))
        assert meta["job_id"] == x["id"], (meta["job_id"], x["id"])

    # No job was started after it was done, and every call's END maps to a single saved output.
    calls = defaultdict(list)
    for line in (SANDBOX / "state" / "fake_calls.log").read_text(encoding="utf-8").splitlines():
        ts, pid, tag, what = line.split("\t")
        calls[tag].append((float(ts), what))
    finished_at = {x["id"]: x["finished_at"] for x in rows}
    for jid, evs in calls.items():
        starts_after_done = [t for t, w in evs if w == "START" and t > finished_at[jid] + 0.01]
        assert not starts_after_done, f"{jid} was started again after it was done"
    ends = {jid: sum(1 for _, w in evs if w == "END") for jid, evs in calls.items()}
    duplicated = {j: n for j, n in ends.items() if n > 1}
    # A completed call can only be repeated if the kill landed between its END and the ledger update,
    # i.e. it was one of the jobs in flight at the kill. Anything else is a duplicate.
    bad = {j: n for j, n in duplicated.items() if j not in killed_running or n > 2}
    assert not bad, f"duplicated jobs: {bad}"
    lost = [x["id"] for x in rows if ends.get(x["id"], 0) == 0]
    assert not lost, f"jobs marked done with no completed call: {lost}"

    limits = sum(x["limit_hits"] for x in rows)
    attempts = sum(x["attempts"] for x in rows)
    assert limits >= 1, "the simulated limit never fired"
    assert attempts == 0, "limits must not count as failures"

    # Fable jobs kept running while Opus was paused
    p = con.execute("SELECT start, end FROM pauses WHERE family='opus' ORDER BY id LIMIT 1").fetchone()
    fable_during = con.execute(
        "SELECT COUNT(*) FROM jobs WHERE model LIKE '%fable%' AND finished_at BETWEEN ? AND ?", (p[0], p[1])
    ).fetchone()[0]
    assert fable_during >= 1, "Fable jobs should keep running while only Opus is limited"
    log = (SANDBOX / "state" / "events.log").read_text(encoding="utf-8")
    assert "\tpause\t" in log and "\tresume\t" in log and "\trecover\t" in log and "\tround_done\t" in log
    con.close()

    print("\nPASS")
    print(f"  45/45 jobs done, 45 output files, 0 lost, 0 duplicated")
    print(f"  simulated limit hits: {limits}; real-failure attempts: {attempts}")
    print(f"  jobs in flight at the kill (re-run after restart): {len(killed_running)}")
    print(f"  Fable jobs finished while Opus was paused: {fable_during}")
    print(f"  calls whose result was recomputed after the kill: {sorted(duplicated)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
