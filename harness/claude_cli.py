"""Calling `claude -p` and classifying what comes back.

Every call returns a CallResult with kind:
  ok         - success; text and usage are set
  limit      - a Max-plan usage/session limit; reset_at is set when the CLI gave a time
  transient  - network, overload or 5xx; retried without counting toward the cap
  failure    - anything else; counts toward the retry cap of 3
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    ZoneInfo = None  # type: ignore

CREATE_NO_WINDOW = 0x08000000 if os.name == "nt" else 0


@dataclass
class CallResult:
    kind: str
    text: str = ""
    tokens_in: int = 0
    tokens_out: int = 0
    cost_usd: float = 0.0
    duration_s: float = 0.0
    reset_at: float | None = None
    error: str = ""
    raw: dict = field(default_factory=dict)
    models_used: dict = field(default_factory=dict)


# ---------------------------------------------------------------- classification

LIMIT_PATTERNS = [
    r"usage limit",
    r"limit reached",
    r"hit your (?:\w+ )?limit",
    r"(?:session|weekly|daily|5-hour|five-hour|opus|fable) limit",
    r"out of (?:extra )?usage",
    r"limit will reset",
    r"resets? (?:at|on|in)?\s*\d",
    r"claude ai usage limit",
]
TRANSIENT_PATTERNS = [
    r"overloaded",
    r"\b5\d\d\b",
    r"econnreset",
    r"etimedout",
    r"econnrefused",
    r"enotfound",
    r"socket hang up",
    r"fetch failed",
    r"network",
    r"connection (?:error|reset|refused)",
    r"service unavailable",
    r"internal server error",
    r"bad gateway",
    r"gateway timeout",
    r"api_error",
]


def classify(text: str, api_status: int | None = None) -> str:
    t = text.lower()
    if any(re.search(p, t) for p in LIMIT_PATTERNS):
        return "limit"
    if api_status == 429:
        # A 429 with no limit wording is treated as a short rate limit: transient.
        return "transient"
    if api_status is not None and 500 <= api_status < 600:
        return "transient"
    if any(re.search(p, t) for p in TRANSIENT_PATTERNS):
        return "transient"
    return "failure"


_MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


def parse_reset(text: str, now: datetime | None = None) -> float | None:
    """Return the reset time as a unix timestamp, or None if the message gives none.

    Handles the formats the CLI has used: `...limit reached|1736272800`, ISO timestamps,
    `resets 3pm (Europe/London)`, `resets at 3:30pm`, `resets Nov 24, 3pm`, `resets in 2h 15m`.
    """
    # unix epoch after a pipe or 'reset' word
    m = re.search(r"\|(\d{10})\b", text) or re.search(r"reset\w*\D{0,20}(\d{10})\b", text, re.I)
    if m:
        return float(m.group(1))
    m = re.search(r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2})?(?:\.\d+)?(?:Z|[+-]\d{2}:?\d{2})?)", text)
    if m:
        s = m.group(1).replace("Z", "+00:00")
        try:
            dt = datetime.fromisoformat(s)
            if dt.tzinfo is None:
                dt = dt.astimezone()
            return dt.timestamp()
        except ValueError:
            pass
    m = re.search(r"resets? in\s+(?:(\d+)\s*h\w*)?\s*(?:(\d+)\s*m\w*)?", text, re.I)
    if m and (m.group(1) or m.group(2)):
        return time.time() + int(m.group(1) or 0) * 3600 + int(m.group(2) or 0) * 60
    m = re.search(
        r"resets?\s+(?:at\s+|on\s+)?(?:([A-Za-z]{3})[a-z]*\.?\s+(\d{1,2}),?\s+(?:at\s+)?)?"
        r"(\d{1,2})(?::(\d{2}))?\s*(am|pm)\b\s*(?:\(([^)]+)\))?",
        text, re.I)
    if m:
        mon, day, hh, mm, ampm, tzname = m.groups()
        tz = None
        if tzname and ZoneInfo is not None:
            try:
                tz = ZoneInfo(tzname.strip())
            except Exception:
                tz = None
        base = now or (datetime.now(tz) if tz else datetime.now().astimezone())
        if tz is not None:
            base = base.astimezone(tz)
        hour = int(hh) % 12 + (12 if ampm.lower() == "pm" else 0)
        cand = base.replace(hour=hour, minute=int(mm or 0), second=0, microsecond=0)
        if mon and day and mon.lower()[:3] in _MONTHS:
            cand = cand.replace(month=_MONTHS[mon.lower()[:3]], day=int(day))
            if cand < base - timedelta(days=1):
                cand = cand.replace(year=cand.year + 1)
        elif cand <= base:
            cand += timedelta(days=1)
        return cand.timestamp()
    return None


# ---------------------------------------------------------------- real backend

class ClaudeBackend:
    def __init__(self, cwd: Path):
        self.exe = shutil.which("claude") or "claude"
        self.cwd = cwd

    def build_cmd(self, model: str, system_prompt_file: Path, effort: str | None) -> list[str]:
        cmd = [
            self.exe, "-p",
            "--model", model,
            "--safe-mode",                 # no CLAUDE.md, skills, plugins, hooks, MCP, memory
            "--strict-mcp-config",         # and no MCP servers at all
            "--tools", "",                 # no tools: no web, no files, no shell
            "--disable-slash-commands",
            "--no-session-persistence",
            "--output-format", "json",
            "--system-prompt-file", str(system_prompt_file),
        ]
        if effort:
            cmd += ["--effort", effort]
        return cmd

    def call(self, *, model: str, system_prompt_file: Path, user_text: str, effort: str | None,
             timeout_s: int, on_pid=None, job_tag: str = "") -> CallResult:
        cmd = self.build_cmd(model, system_prompt_file, effort)
        t0 = time.time()
        env = dict(os.environ)
        env.pop("ANTHROPIC_API_KEY", None)  # always use the Max-plan login, never a stray API key
        try:
            proc = subprocess.Popen(
                cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                cwd=str(self.cwd), env=env, creationflags=CREATE_NO_WINDOW,
                encoding="utf-8", errors="replace",
            )
        except OSError as e:
            return CallResult("failure", error=f"could not start claude: {e}")
        if on_pid:
            on_pid(proc.pid)
        try:
            out, err = proc.communicate(user_text, timeout=timeout_s)
        except subprocess.TimeoutExpired:
            _kill_tree(proc.pid)
            proc.communicate()
            return CallResult("failure", error=f"timeout after {timeout_s}s", duration_s=time.time() - t0)
        return interpret(out, err, proc.returncode, model, time.time() - t0)

    def probe(self, model: str) -> CallResult:
        """One tiny call to see whether a limit has lifted."""
        sp = self.cwd.parent / "probe_system.txt"
        sp.write_text("Reply with exactly: OK", encoding="utf-8")
        return self.call(model=model, system_prompt_file=sp, user_text="ping", effort="low", timeout_s=300)


def interpret(out: str, err: str, rc: int, model: str, duration: float) -> CallResult:
    data = None
    try:
        data = json.loads(out.strip().splitlines()[-1]) if out.strip() else None
    except (json.JSONDecodeError, IndexError):
        data = None
    if data is None:
        msg = (err or "") + "\n" + (out or "")
        kind = classify(msg)
        return CallResult(kind, error=msg.strip()[-2000:], duration_s=duration,
                          reset_at=parse_reset(msg) if kind == "limit" else None)
    usage = data.get("usage") or {}
    tin = int(usage.get("input_tokens", 0)) + int(usage.get("cache_creation_input_tokens", 0)) + int(
        usage.get("cache_read_input_tokens", 0))
    tout = int(usage.get("output_tokens", 0))
    res = CallResult("ok", text=data.get("result") or "", tokens_in=tin, tokens_out=tout,
                     cost_usd=float(data.get("total_cost_usd") or 0), duration_s=duration, raw=data,
                     models_used=data.get("modelUsage") or {})
    if data.get("is_error") or data.get("subtype") not in (None, "success") or rc != 0:
        msg = f"{data.get('result') or ''} {err or ''}"
        status = data.get("api_error_status")
        res.kind = classify(msg, int(status) if isinstance(status, (int, str)) and str(status).isdigit() else None)
        res.error = msg.strip()[-2000:] or f"exit {rc}, subtype {data.get('subtype')}"
        if res.kind == "limit":
            res.reset_at = parse_reset(msg)
        return res
    # Guard against a silent model substitution: the requested model must have produced the output.
    mu = res.models_used.get(model)
    if not mu or int(mu.get("outputTokens", 0)) == 0:
        res.kind = "failure"
        res.error = f"requested {model} but modelUsage was {list(res.models_used)}"
    if res.kind == "ok" and not res.text.strip():
        res.kind = "failure"
        res.error = "empty result text"
    return res


def _kill_tree(pid: int):
    if os.name == "nt":
        subprocess.run(["taskkill", "/PID", str(pid), "/T", "/F"], capture_output=True,
                       creationflags=CREATE_NO_WINDOW)
    else:  # pragma: no cover
        try:
            os.kill(pid, 9)
        except OSError:
            pass


def kill_stale(pid: int) -> bool:
    """Kill a leftover claude process from a run that died, if it is still alive."""
    if os.name != "nt" or not pid:
        return False
    r = subprocess.run(["tasklist", "/FI", f"PID eq {pid}", "/FO", "CSV", "/NH"], capture_output=True, text=True,
                       creationflags=CREATE_NO_WINDOW)
    line = r.stdout.strip().lower()
    if line.startswith('"claude') or line.startswith('"node'):
        _kill_tree(pid)
        return True
    return False


# ---------------------------------------------------------------- fake backend (tests)

class FakeBackend:
    """Stand-in for `claude -p` used by the resume test. Spends no tokens.

    After `limit_after` successful calls (counted per process) every call for the limited
    family returns a CLI-style usage-limit message until the fake reset time passes.
    """

    def __init__(self, cwd: Path, *, delay: float = 0.3, limit_after: int | None = None,
                 reset_seconds: float = 5, limit_family: str = "opus", give_reset: bool = True,
                 call_log: Path | None = None):
        self.cwd = cwd
        self.delay = delay
        self.limit_after = limit_after
        self.reset_seconds = reset_seconds
        self.limit_family = limit_family
        self.give_reset = give_reset
        self.call_log = call_log
        self._ok_calls = 0
        self._limit_until: float | None = None
        self._lock = threading.Lock()

    def _family(self, model: str) -> str:
        return "fable" if "fable" in model else "opus"

    def call(self, *, model, system_prompt_file, user_text, effort, timeout_s, on_pid=None,
             job_tag: str = "") -> CallResult:
        fam = self._family(model)
        with self._lock:
            now = time.time()
            limited = False
            if self.limit_after is not None and (self.limit_family in (fam, "any")):
                if self._limit_until is None and self._ok_calls >= self.limit_after:
                    self._limit_until = now + self.reset_seconds
                if self._limit_until is not None and now < self._limit_until:
                    limited = True
            if not limited:
                self._ok_calls += 1
            if self.call_log:
                with open(self.call_log, "a", encoding="utf-8") as f:
                    f.write(f"{time.time():.3f}\t{os.getpid()}\t{job_tag}\t{'LIMIT' if limited else 'START'}\n")
        if limited:
            if self.give_reset:
                msg = f"Claude AI usage limit reached|{int(self._limit_until) + 1}"
            else:
                msg = "You've hit your session limit."
            return CallResult("limit", error=msg, reset_at=parse_reset(msg))
        time.sleep(self.delay)
        text = _fake_text(user_text, job_tag)
        if self.call_log:
            with open(self.call_log, "a", encoding="utf-8") as f:
                f.write(f"{time.time():.3f}\t{os.getpid()}\t{job_tag}\tEND\n")
        return CallResult("ok", text=text, tokens_in=1000, tokens_out=500, cost_usd=0.0, duration_s=self.delay,
                          models_used={model: {"outputTokens": 500}})

    def probe(self, model: str) -> CallResult:
        fam = self._family(model)
        if self._limit_until and time.time() < self._limit_until and self.limit_family in (fam, "any"):
            return CallResult("limit", error="still limited")
        return CallResult("ok", text="OK")


def _fake_text(user_text: str, tag: str) -> str:
    if "JUDGE" in user_text or "PAIRWISE" in user_text:
        return json.dumps({"fake": True, "tag": tag, "scores": {}, "winner": "tie"})
    return f"# Fake output\n\njob: {tag}\n\nGreatness potential: 50/100\n"
