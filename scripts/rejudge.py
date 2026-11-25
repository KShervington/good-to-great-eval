"""Re-queue existing judge jobs after a rubric or scoring-rule change.

The old judgment files are moved (not deleted) to runs/judgments_archive/<tag>/<version>/<case>/, and the ledger
rows are reset to pending and moved to the front of the queue. Skill outputs are untouched.

  python scripts/rejudge.py --version v0 --tracks B --tag b-not-already-great
  python scripts/rejudge.py --version v0 --tracks all --tag rubric-v2
"""
from __future__ import annotations

import argparse
import json
import shutil
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", required=True)
    ap.add_argument("--tracks", required=True, help="comma-separated track letters, or 'all'")
    ap.add_argument("--tag", required=True)
    a = ap.parse_args()

    cases = json.loads((ROOT / "data" / "cases.json").read_text(encoding="utf-8"))["cases"]
    tracks = None if a.tracks == "all" else set(a.tracks.split(","))
    ids = {c["id"] for c in cases if c["split"] == "dev" and (tracks is None or c["track"] in tracks)}

    db = sqlite3.connect(ROOT / "state" / "ledger.db", timeout=30)
    rows = db.execute("SELECT id, case_id, seed, status FROM jobs WHERE stage='judge' AND version=?",
                      (a.version,)).fetchall()
    rows = [r for r in rows if r[1] in ids]
    running = [r[0] for r in rows if r[3] == "running"]
    if running:
        raise SystemExit(f"refusing: {len(running)} of these judge jobs are running right now")
    moved = 0
    for jid, cid, seed, _ in rows:
        src = ROOT / "runs" / "judgments" / a.version / cid / f"seed{seed}.json"
        if src.exists():
            dst = ROOT / "runs" / "judgments_archive" / a.tag / a.version / cid / src.name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            moved += 1
        for extra in src.parent.glob(f"seed{seed}.*"):
            extra.unlink()
    db.executemany("UPDATE jobs SET status='pending', pid=NULL, not_before=0, attempts=0, transient_hits=0, "
                   "created_at=created_at-172800 WHERE id=?", [(r[0],) for r in rows])
    db.commit()
    print(f"reset {len(rows)} judge jobs for {a.version} ({a.tracks}); archived {moved} judgments under tag {a.tag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
