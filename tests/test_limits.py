"""Unit tests for limit classification and reset-time parsing, plus the probe path (no reset time given).

Run:  python tests/test_limits.py
"""
from __future__ import annotations

import shutil
import sqlite3
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT))

from harness.claude_cli import classify, interpret, parse_reset  # noqa: E402


def test_classify():
    assert classify("Claude AI usage limit reached|1736272800") == "limit"
    assert classify("You've hit your limit · resets 5pm (America/Los_Angeles)") == "limit"
    assert classify("5-hour limit reached ∙ resets 3am") == "limit"
    assert classify("You've reached your weekly limit. Your limit will reset on Nov 26") == "limit"
    assert classify("API Error: 529 {\"type\":\"overloaded_error\"}") == "transient"
    assert classify("API Error: 500 Internal server error") == "transient"
    assert classify("fetch failed: ECONNRESET") == "transient"
    assert classify("Error: something unexpected", 429) == "transient"
    assert classify("Invalid model name") == "failure"
    assert classify("Error: prompt is too long") == "failure"


def test_parse_reset():
    assert parse_reset("Claude AI usage limit reached|1736272800") == 1736272800.0
    ts = parse_reset("limit; try again at 2026-11-24T03:00:00Z")
    assert ts == datetime.fromisoformat("2026-11-24T03:00:00+00:00").timestamp()
    now = datetime.fromisoformat("2026-11-23T14:10:00-08:00")
    ts = parse_reset("You've hit your limit · resets 5pm (America/Los_Angeles)", now=now)
    assert datetime.fromtimestamp(ts).astimezone(now.tzinfo).hour == 17
    ts = parse_reset("resets 1am (America/Los_Angeles)", now=now)  # tomorrow, not 13 hours ago
    assert ts > now.timestamp()
    t0 = time.time()
    ts = parse_reset("resets in 2h 15m")
    assert abs(ts - (t0 + 8100)) < 5
    assert parse_reset("You've hit your session limit.") is None


def test_interpret_json_limit():
    out = ('{"type":"result","subtype":"success","is_error":true,"result":"Claude AI usage limit reached|1736272800",'
           '"usage":{},"modelUsage":{}}')
    r = interpret(out, "", 1, "claude-opus-5-5", 1.0)
    assert r.kind == "limit" and r.reset_at == 1736272800.0
    ok = ('{"type":"result","subtype":"success","is_error":false,"result":"hi","total_cost_usd":0.01,'
          '"usage":{"input_tokens":5,"output_tokens":3},"modelUsage":{"claude-opus-5-5":{"outputTokens":3}}}')
    assert interpret(ok, "", 0, "claude-opus-5-5", 1.0).kind == "ok"
    # silent model substitution is a real failure
    assert interpret(ok, "", 0, "claude-fable-5-2", 1.0).kind == "failure"


def test_probe_path():
    """No reset time in the message: the harness must probe, then resume when the probe succeeds."""
    sb = PROJECT / "tests" / "_sandbox_probe"
    if sb.exists():
        shutil.rmtree(sb)
    src = PROJECT / "tests" / "_sandbox_resume"
    assert src.exists(), "run tests/test_resume.py first (it builds the sandbox data)"
    shutil.copytree(src / "data", sb / "data")
    shutil.copytree(src / "skill_versions", sb / "skill_versions")
    run = lambda *a: subprocess.run([sys.executable, "-m", "harness", "--root", str(sb), *a], cwd=PROJECT,
                                    capture_output=True, text=True, timeout=300)
    run("enqueue", "--round", "probe-r", "--version", "v0", "--cases", "dryrun", "--seeds", "2",
        "--stages", "run,judge")
    r = run("run", "--backend", "fake", "--simulate-limit-after", "3", "--simulate-reset-seconds", "3",
            "--simulate-no-reset-time", "--probe-interval", "2", "--fake-delay", "0.1", "--no-toast")
    assert r.returncode == 0, r.stdout + r.stderr
    log = (sb / "state" / "events.log").read_text(encoding="utf-8")
    assert "probing every" in log and "\tresume\t" in log, log
    con = sqlite3.connect(str(sb / "state" / "ledger.db"))
    assert con.execute("SELECT COUNT(*) FROM jobs WHERE status!='done'").fetchone()[0] == 0
    con.close()


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"ok  {name}")
    print("PASS")
