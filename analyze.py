"""Round decisions and reports.

  python analyze.py decide --round r1 --candidate v1 --baseline v0
  python analyze.py summary --version v0 [--split dev]

`decide` refuses to run unless every job in the round is `done` in the ledger (round integrity).
It accepts the candidate only if ALL of these hold:
  1. the mean composite improves, and the 95% bootstrap CI of the paired difference excludes 0
     (paired by case x seed; resampled by case cluster, 10,000 draws);
  2. no judge dimension's mean drops by more than 0.3 (on the 1-5 scale);
  3. the skill is at most 20% longer than the original v0 (in words);
  4. the overfitting scan finds no company names, case-specific names or answer-key facts in the skill.
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sqlite3
import statistics
import sys
from collections import defaultdict
from pathlib import Path

import score

ROOT = Path(__file__).resolve().parent
MAX_DIM_DROP = 0.3
MAX_GROWTH = 0.20
N_BOOT = 10_000


def load_cases(split: str | None):
    cases = json.loads((ROOT / "data" / "cases.json").read_text(encoding="utf-8"))["cases"]
    return [c for c in cases if split is None or c.get("split") == split]


def records(version: str, cases, seeds=3) -> dict[tuple[str, int], dict]:
    out = {}
    for c in cases:
        for s in range(1, seeds + 1):
            r = score.case_record(ROOT, version, c, s)
            if r and any(isinstance(r.get(d), (int, float)) for d in score.JUDGE_DIMS):
                r["composite"] = score.composite(r)
                r["cluster"] = c.get("cluster", c["id"])
                out[(c["id"], s)] = r
    return out


def round_complete(round_name: str) -> tuple[bool, dict]:
    con = sqlite3.connect(str(ROOT / "state" / "ledger.db"))
    rows = con.execute(
        "SELECT j.status, COUNT(*) FROM round_jobs r JOIN jobs j ON j.id=r.job_id WHERE r.round=? GROUP BY j.status",
        (round_name,)).fetchall()
    con.close()
    counts = dict(rows)
    return bool(counts) and set(counts) == {"done"}, counts


def bootstrap_ci(diffs_by_cluster: dict[str, list[float]], n=N_BOOT, seed=7) -> tuple[float, float, float]:
    clusters = list(diffs_by_cluster)
    rng = random.Random(seed)
    all_d = [d for v in diffs_by_cluster.values() for d in v]
    means = []
    for _ in range(n):
        sample = [d for _ in clusters for d in diffs_by_cluster[rng.choice(clusters)]]
        means.append(sum(sample) / len(sample))
    means.sort()
    return statistics.mean(all_d), means[int(0.025 * n)], means[int(0.975 * n) - 1]


def skill_words(version: str) -> int:
    return len((ROOT / "skill_versions" / version / "SKILL.md").read_text(encoding="utf-8").split())


def overfit_scan(version: str) -> list[str]:
    """Names and answer-key specifics that must never appear in the skill."""
    skill = (ROOT / "skill_versions" / version / "SKILL.md").read_text(encoding="utf-8")
    base = (ROOT / "skill_versions" / "v0" / "SKILL.md").read_text(encoding="utf-8")
    hits = []
    for kp in (ROOT / "data" / "answer_keys").glob("*.json"):
        key = json.loads(kp.read_text(encoding="utf-8"))
        for n in [key.get("real_identity"), *(key.get("aliases") or [])]:
            if n and len(n) >= 4 and re.search(rf"\b{re.escape(n)}\b", skill, re.I) and not re.search(
                    rf"\b{re.escape(n)}\b", base, re.I):
                hits.append(f"real name '{n}' ({kp.stem})")
    # invented proper nouns from dossiers (company, brand and person names) that weren't in v0
    for dp in (ROOT / "data" / "dossiers").glob("*.md"):
        for tok in set(re.findall(r"\b[A-Z][a-z]+(?:[A-Z][a-z]+|-[A-Z][a-z]+)+\b", dp.read_text(encoding="utf-8"))):
            if tok in skill and tok not in base:
                hits.append(f"dossier name '{tok}' ({dp.stem})")
    return sorted(set(hits))


def overfit_soft(version: str) -> list[str]:
    """For manual review: capitalized words new to this skill version that also appear in a dossier."""
    skill = (ROOT / "skill_versions" / version / "SKILL.md").read_text(encoding="utf-8")
    base_words = set(re.findall(r"[a-z]+", (ROOT / "skill_versions" / "v0" / "SKILL.md").read_text(
        encoding="utf-8").lower()))
    new = {t for t in re.findall(r"[A-Z][a-zA-Z]{3,}", skill) if t.lower() not in base_words}
    out = []
    for dp in (ROOT / "data" / "dossiers").glob("*.md"):
        txt = dp.read_text(encoding="utf-8")
        out += [f"{t} ({dp.stem})" for t in new if re.search(rf"{t}", txt)]
    return sorted(set(out))


def dim_means(recs: dict) -> dict[str, float | None]:
    out = {}
    for d in score.JUDGE_DIMS:
        vals = [r[d] for r in recs.values() if isinstance(r.get(d), (int, float))]
        out[d] = statistics.mean(vals) if vals else None
    return out


def pairwise_summary(candidate: str, baseline: str) -> dict:
    base = ROOT / "runs" / "pairwise" / f"{candidate}__vs__{baseline}"
    tally = defaultdict(lambda: defaultdict(int))
    for f in base.rglob("seed*.json"):
        if f.name.endswith(".meta.json"):
            continue
        j = json.loads(f.read_text(encoding="utf-8"))
        cand_is_1 = j.get("_analysis_1_is") == candidate
        for dim, v in j.items():
            if dim.startswith("_") or dim == "why":
                continue
            v = str(v)
            who = "tie" if v in ("tie", "na") else ("candidate" if (v == "1") == cand_is_1 else "baseline")
            tally[dim][who if v != "na" else "na"] += 1
    return {k: dict(v) for k, v in tally.items()}


def cmd_decide(a) -> int:
    ok, counts = round_complete(a.round)
    if not ok:
        print(f"REFUSED: round {a.round} is not complete. Job counts: {counts}")
        return 2
    cases = load_cases("dev")
    rc, rb = records(a.candidate, cases), records(a.baseline, cases)
    common = sorted(set(rc) & set(rb))
    if not common:
        print("REFUSED: no paired results")
        return 2
    diffs = defaultdict(list)
    for k in common:
        diffs[rc[k]["cluster"]].append(rc[k]["composite"] - rb[k]["composite"])
    mean_d, lo, hi = bootstrap_ci(diffs)
    mc, mb = dim_means({k: rc[k] for k in common}), dim_means({k: rb[k] for k in common})
    drops = {d: round(mb[d] - mc[d], 3) for d in mc if mc[d] is not None and mb[d] is not None}
    growth = skill_words(a.candidate) / skill_words("v0") - 1
    overfit = overfit_scan(a.candidate)
    checks = {
        "improves_beyond_noise": mean_d > 0 and lo > 0,
        "no_dimension_drop_gt_0.3": all(v <= MAX_DIM_DROP for v in drops.values()),
        "growth_le_20pct_vs_v0": growth <= MAX_GROWTH,
        "no_overfitting_content": not overfit,
    }
    decision = "ACCEPT" if all(checks.values()) else "REJECT"
    report = {
        "round": a.round, "candidate": a.candidate, "baseline": a.baseline, "decision": decision,
        "n_pairs": len(common), "n_clusters": len(diffs),
        "mean_composite": {"candidate": round(statistics.mean(rc[k]["composite"] for k in common), 2),
                           "baseline": round(statistics.mean(rb[k]["composite"] for k in common), 2)},
        "diff": {"mean": round(mean_d, 3), "ci95": [round(lo, 3), round(hi, 3)]},
        "dimension_means": {"candidate": mc, "baseline": mb}, "dimension_drops": drops,
        "skill_growth_vs_v0": round(growth, 3), "overfit_hits": overfit,
        "overfit_review_manually": overfit_soft(a.candidate), "checks": checks,
        "pairwise": pairwise_summary(a.candidate, a.baseline),
    }
    out = ROOT / "runs" / "decisions" / f"{a.round}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


def cmd_summary(a) -> int:
    cases = load_cases(a.split)
    recs = records(a.version, cases)
    by = defaultdict(list)
    for r in recs.values():
        rg = {True: "recognizable", False: "not recognizable"}.get(r.get("recognizable"), "untagged")
        by[(r["track"], rg)].append(r)
    print(f"version {a.version}, split {a.split}, {len(recs)} judged outputs")
    for (t, rg), rs in sorted(by.items()):
        comp = statistics.mean(r["composite"] for r in rs)
        dm = dim_means({i: r for i, r in enumerate(rs)})
        dims = "  ".join(f"{d}={v:.2f}" for d, v in dm.items() if v is not None)
        print(f"  {t} {rg:<17} n={len(rs):<3} composite={comp:6.2f}  {dims}")
    sl = [(r["gp"], r["label"]) for r in recs.values()
          if r["gp"] is not None and r["label"] in (0, 1) and r["track"] in ("A", "C", "D") and not r["already_great"]]
    print(f"  AUROC (greatness potential, tracks A/C/D): {score.auroc(sl)}")
    e = [r for r in recs.values() if r["already_great"] and r["track"] == "E"]
    if e:
        print(f"  Track E mean greatness potential: {statistics.mean(r['gp'] for r in e if r['gp'] is not None):.1f}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("decide")
    d.add_argument("--round", required=True)
    d.add_argument("--candidate", required=True)
    d.add_argument("--baseline", required=True)
    d.set_defaults(fn=cmd_decide)
    s = sub.add_parser("summary")
    s.add_argument("--version", default="v0")
    s.add_argument("--split", default="dev")
    s.set_defaults(fn=cmd_summary)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
