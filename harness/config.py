"""Paths, model IDs and defaults. Every path can be re-rooted with --root (used by the tests)."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent

SKILL_MODEL = "claude-opus-5-5"
JUDGE_MODEL = "claude-fable-5-2"
PROBE_MODEL = "claude-opus-5-5"  # the contamination probe uses the model under test

MODEL_FAMILY = {SKILL_MODEL: "opus", JUDGE_MODEL: "fable"}

STAGE_MODEL = {
    "run": SKILL_MODEL,
    "judge": JUDGE_MODEL,
    "pairwise": JUDGE_MODEL,
    "probe": PROBE_MODEL,
}
STAGE_EFFORT = {"run": "high", "judge": "high", "pairwise": "high", "probe": "low"}
STAGE_TIMEOUT_S = {"run": 40 * 60, "judge": 30 * 60, "pairwise": 30 * 60, "probe": 10 * 60}

MAX_REAL_FAILURES = 3
MAX_TRANSIENT = 10
WINDOW_HOURS = 5  # Max plan session window, used for the rolling token count


@dataclass
class Paths:
    root: Path = PROJECT

    @property
    def state(self) -> Path:
        return self.root / "state"

    @property
    def ledger(self) -> Path:
        return self.state / "ledger.db"

    @property
    def events(self) -> Path:
        return self.state / "events.log"

    @property
    def lock(self) -> Path:
        return self.state / "harness.lock"

    @property
    def tmp(self) -> Path:
        return self.state / "tmp"

    @property
    def cwd_sandbox(self) -> Path:
        # Empty working directory for every claude call, so no project files are nearby.
        return self.state / "tmp" / "empty_cwd"

    @property
    def runs(self) -> Path:
        return self.root / "runs"

    @property
    def data(self) -> Path:
        return PROJECT / "data" if self.root == PROJECT else self.root / "data"

    @property
    def versions(self) -> Path:
        return PROJECT / "skill_versions" if self.root == PROJECT else self.root / "skill_versions"

    @property
    def prompts(self) -> Path:
        return PROJECT / "prompts"

    def ensure(self) -> None:
        for p in (self.state, self.tmp, self.cwd_sandbox, self.runs):
            p.mkdir(parents=True, exist_ok=True)


def paths_from_env(root: str | None = None) -> Paths:
    r = root or os.environ.get("HARNESS_ROOT")
    return Paths(Path(r).resolve()) if r else Paths()
