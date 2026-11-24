"""Run the skill under test headlessly on cases, through the harness ledger.

  python run_skill.py --version v0 --cases dryrun --seeds 1        # enqueue run+judge, then run them
  python run_skill.py --version v0 --cases A01 --seeds 3 --no-judge

This is a convenience wrapper. It enqueues jobs and then calls `python -m harness run`, so the
pause/resume rules, logging (tokens, time, skill version) and idempotency all apply.
The skill model is claude-opus-5-5, run with: --safe-mode --strict-mcp-config --tools "" (no web, memory
or any other tool), the SKILL.md as the system prompt, and the dossier as the only input.
"""
from __future__ import annotations

import argparse
import sys

from harness.__main__ import main as harness_main


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default="v0")
    ap.add_argument("--cases", required=True)
    ap.add_argument("--seeds", type=int, default=3)
    ap.add_argument("--round", default=None)
    ap.add_argument("--no-judge", action="store_true")
    ap.add_argument("--concurrency", type=int, default=2)
    a = ap.parse_args()
    stages = "run" if a.no_judge else "run,judge"
    args = ["enqueue", "--version", a.version, "--cases", a.cases, "--seeds", str(a.seeds), "--stages", stages]
    if a.round:
        args += ["--round", a.round]
    harness_main(args)
    return harness_main(["run", "--concurrency", str(a.concurrency)])


if __name__ == "__main__":
    sys.exit(main())
