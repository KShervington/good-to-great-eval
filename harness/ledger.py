"""SQLite job ledger. One row per unit of work: version x case x seed x stage.

Only the scheduler's main thread writes to the ledger; worker threads only run
subprocesses and write output files. That keeps SQLite single-writer.
"""
from __future__ import annotations

import json
import sqlite3
import time
from pathlib import Path
from typing import Iterable

SCHEMA = """
CREATE TABLE IF NOT EXISTS jobs (
    id            TEXT PRIMARY KEY,
    version       TEXT NOT NULL,
    other_version TEXT,
    case_id       TEXT NOT NULL,
    seed          INTEGER NOT NULL,
    stage         TEXT NOT NULL,        -- run | judge | pairwise | probe
    model         TEXT NOT NULL,
    status        TEXT NOT NULL DEFAULT 'pending',  -- pending|running|done|failed|paused_limit
    attempts      INTEGER NOT NULL DEFAULT 0,       -- real failures only
    limit_hits    INTEGER NOT NULL DEFAULT 0,
    transient_hits INTEGER NOT NULL DEFAULT 0,
    executions    INTEGER NOT NULL DEFAULT 0,       -- times a call was started
    depends_on    TEXT NOT NULL DEFAULT '[]',
    not_before    REAL NOT NULL DEFAULT 0,
    pid           INTEGER,
    created_at    REAL NOT NULL,
    started_at    REAL,
    finished_at   REAL,
    tokens_in     INTEGER NOT NULL DEFAULT 0,
    tokens_out    INTEGER NOT NULL DEFAULT 0,
    cost_usd      REAL NOT NULL DEFAULT 0,
    duration_s    REAL,
    output_path   TEXT,
    error         TEXT
);
CREATE INDEX IF NOT EXISTS jobs_status ON jobs(status);
CREATE TABLE IF NOT EXISTS round_jobs (
    round  TEXT NOT NULL,
    job_id TEXT NOT NULL,
    PRIMARY KEY (round, job_id)
);
CREATE TABLE IF NOT EXISTS rounds (
    round      TEXT PRIMARY KEY,
    candidate  TEXT,
    baseline   TEXT,
    split      TEXT,
    created_at REAL,
    decided_at REAL,
    decision   TEXT
);
CREATE TABLE IF NOT EXISTS limits (
    family       TEXT PRIMARY KEY,     -- opus | fable
    paused       INTEGER NOT NULL DEFAULT 0,
    paused_since REAL,
    resume_at    REAL,                 -- parsed reset + buffer; NULL when unknown
    next_probe   REAL,                 -- used when no reset time was given
    reason       TEXT
);
CREATE TABLE IF NOT EXISTS pauses (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    family  TEXT NOT NULL,
    start   REAL NOT NULL,
    end     REAL,
    reason  TEXT
);
CREATE TABLE IF NOT EXISTS usage (
    ts         REAL NOT NULL,
    family     TEXT NOT NULL,
    tokens_in  INTEGER NOT NULL,
    tokens_out INTEGER NOT NULL,
    cost_usd   REAL NOT NULL
);
"""


def job_id(version: str, case_id: str, seed: int, stage: str, other: str | None = None) -> str:
    base = f"{version}|{case_id}|s{seed}|{stage}"
    return f"{base}|vs:{other}" if other else base


class Ledger:
    def __init__(self, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.path = path
        self.db = sqlite3.connect(str(path), timeout=30, isolation_level=None)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.execute("PRAGMA synchronous=FULL")
        self.db.executescript(SCHEMA)

    # ---------- helpers ----------
    def tx(self):
        return _Tx(self.db)

    def q(self, sql: str, args: Iterable = ()) -> list[sqlite3.Row]:
        return list(self.db.execute(sql, tuple(args)))

    def one(self, sql: str, args: Iterable = ()):
        rows = self.q(sql, args)
        return rows[0] if rows else None

    # ---------- enqueue ----------
    def add_job(self, *, version, case_id, seed, stage, model, other_version=None,
                depends_on=(), round_name=None) -> str:
        jid = job_id(version, case_id, seed, stage, other_version)
        with self.tx():
            self.db.execute(
                "INSERT OR IGNORE INTO jobs(id,version,other_version,case_id,seed,stage,model,depends_on,created_at)"
                " VALUES (?,?,?,?,?,?,?,?,?)",
                (jid, version, other_version, case_id, seed, stage, model, json.dumps(list(depends_on)), time.time()),
            )
            if round_name:
                self.db.execute("INSERT OR IGNORE INTO round_jobs(round,job_id) VALUES (?,?)", (round_name, jid))
        return jid

    def add_round(self, name, candidate, baseline, split):
        with self.tx():
            self.db.execute(
                "INSERT OR IGNORE INTO rounds(round,candidate,baseline,split,created_at) VALUES (?,?,?,?,?)",
                (name, candidate, baseline, split, time.time()),
            )

    # ---------- start-up recovery ----------
    def stale_running(self) -> list[sqlite3.Row]:
        return self.q("SELECT * FROM jobs WHERE status='running'")

    def reset_stale(self, jid: str):
        self.db.execute("UPDATE jobs SET status='pending', pid=NULL WHERE id=? AND status='running'", (jid,))

    # ---------- claiming ----------
    def claimable(self, paused_families: set[str], family_of, limit: int) -> list[sqlite3.Row]:
        now = time.time()
        rows = self.q(
            "SELECT * FROM jobs WHERE status='pending' AND not_before<=? ORDER BY created_at, id", (now,)
        )
        out = []
        for r in rows:
            if family_of(r["model"]) in paused_families:
                continue
            deps = json.loads(r["depends_on"])
            if deps:
                done = self.one(
                    f"SELECT COUNT(*) c FROM jobs WHERE status='done' AND id IN ({','.join('?' * len(deps))})", deps
                )["c"]
                if done != len(deps):
                    continue
            out.append(r)
            if len(out) >= limit:
                break
        return out

    def mark_running(self, jid: str) -> bool:
        cur = self.db.execute(
            "UPDATE jobs SET status='running', started_at=?, executions=executions+1 WHERE id=? AND status='pending'",
            (time.time(), jid),
        )
        return cur.rowcount == 1

    def set_pid(self, jid: str, pid: int):
        self.db.execute("UPDATE jobs SET pid=? WHERE id=?", (pid, jid))

    def mark_done(self, jid: str, *, output_path, tokens_in, tokens_out, cost, duration, family):
        with self.tx():
            # A job counts as done only here, after its output file has been renamed into place.
            self.db.execute(
                "UPDATE jobs SET status='done', finished_at=?, output_path=?, tokens_in=?, tokens_out=?,"
                " cost_usd=?, duration_s=?, error=NULL, pid=NULL WHERE id=? AND status IN ('running','paused_limit')",
                (time.time(), str(output_path), tokens_in, tokens_out, cost, duration, jid),
            )
            self.db.execute(
                "INSERT INTO usage(ts,family,tokens_in,tokens_out,cost_usd) VALUES (?,?,?,?,?)",
                (time.time(), family, tokens_in, tokens_out, cost),
            )

    def mark_limit(self, jid: str, err: str):
        self.db.execute(
            "UPDATE jobs SET status='paused_limit', limit_hits=limit_hits+1, error=?, pid=NULL WHERE id=?",
            (err[:2000], jid),
        )

    def mark_transient(self, jid: str, err: str, backoff_s: float) -> int:
        self.db.execute(
            "UPDATE jobs SET status='pending', transient_hits=transient_hits+1, error=?, not_before=?, pid=NULL"
            " WHERE id=?",
            (err[:2000], time.time() + backoff_s, jid),
        )
        return self.one("SELECT transient_hits FROM jobs WHERE id=?", (jid,))["transient_hits"]

    def mark_failure(self, jid: str, err: str, max_attempts: int) -> str:
        row = self.one("SELECT attempts FROM jobs WHERE id=?", (jid,))
        attempts = row["attempts"] + 1
        status = "failed" if attempts >= max_attempts else "pending"
        self.db.execute(
            "UPDATE jobs SET status=?, attempts=?, error=?, pid=NULL WHERE id=?",
            (status, attempts, err[:2000], jid),
        )
        return status

    def pause_family_jobs(self, family_models: list[str]):
        if not family_models:
            return
        marks = ",".join("?" * len(family_models))
        self.db.execute(
            f"UPDATE jobs SET status='paused_limit' WHERE status='running' AND model IN ({marks})", family_models
        )

    def unpause_family_jobs(self, family_models: list[str], in_flight: set[str] = frozenset()):
        # Jobs whose call is still in flight stay paused_limit; their result decides their status.
        marks = ",".join("?" * len(family_models))
        rows = self.q(f"SELECT id FROM jobs WHERE status='paused_limit' AND model IN ({marks})", family_models)
        for r in rows:
            if r["id"] not in in_flight:
                self.db.execute("UPDATE jobs SET status='pending', not_before=0 WHERE id=?", (r["id"],))

    # ---------- limits ----------
    def get_limit(self, family: str):
        return self.one("SELECT * FROM limits WHERE family=?", (family,))

    def set_paused(self, family, resume_at, next_probe, reason):
        now = time.time()
        with self.tx():
            existing = self.get_limit(family)
            if existing and existing["paused"]:
                self.db.execute(
                    "UPDATE limits SET resume_at=?, next_probe=?, reason=? WHERE family=?",
                    (resume_at, next_probe, reason, family),
                )
                return False
            self.db.execute(
                "INSERT OR REPLACE INTO limits(family,paused,paused_since,resume_at,next_probe,reason)"
                " VALUES (?,1,?,?,?,?)",
                (family, now, resume_at, next_probe, reason),
            )
            self.db.execute("INSERT INTO pauses(family,start,reason) VALUES (?,?,?)", (family, now, reason))
            return True

    def clear_paused(self, family):
        now = time.time()
        with self.tx():
            self.db.execute("UPDATE limits SET paused=0, resume_at=NULL, next_probe=NULL WHERE family=?", (family,))
            self.db.execute("UPDATE pauses SET end=? WHERE family=? AND end IS NULL", (now, family))

    def paused_families(self) -> set[str]:
        return {r["family"] for r in self.q("SELECT family FROM limits WHERE paused=1")}

    # ---------- summaries ----------
    def counts(self) -> dict[str, int]:
        return {r["status"]: r["c"] for r in self.q("SELECT status, COUNT(*) c FROM jobs GROUP BY status")}

    def remaining(self) -> int:
        return self.one("SELECT COUNT(*) c FROM jobs WHERE status IN ('pending','running','paused_limit')")["c"]


class _Tx:
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.db.execute("BEGIN IMMEDIATE")

    def __exit__(self, exc_type, *_):
        self.db.execute("ROLLBACK" if exc_type else "COMMIT")
