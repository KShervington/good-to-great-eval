"""Validate every case and (re)build data/cases.json with dev/held-out splits.

  python scripts/build_manifest.py            # validate + write cases.json
  python scripts/build_manifest.py --check    # validate only

Split rules:
- About 70/30 dev/held-out within each track, stratified by group.
- Cases about the same real company (for example Circuit City in Track A and Track B) form one cluster
  and always land in the same split. So do Track A matched pairs (great + comparison).
- The 3 dry-run cases (A01, A02, D01) are forced into dev, because their results were already viewed.
- Splits are deterministic (fixed seed) and are not changed once written, unless --resplit is given.
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REQUIRED = ["case_id", "track", "group", "real_identity", "expected_gate_fail", "greatness_label"]
DRY_RUN = {"A01", "A02", "D01"}
HELDOUT_FRACTION = 0.30


def norm_name(s: str | None) -> str | None:
    if not s:
        return None
    s = s.lower()
    s = re.sub(r"\b(corporation|corp|company|co|inc|laboratories|labs|stores|department|the)\b", "", s)
    return re.sub(r"[^a-z]", "", s) or None


def validate(case_id: str, key: dict, dossier: str) -> list[str]:
    problems = []
    for f in REQUIRED:
        if f not in key:
            problems.append(f"missing field {f}")
    if key.get("case_id") != case_id:
        problems.append(f"case_id {key.get('case_id')} != file name")
    words = len(dossier.split())
    if words < 350 or words > 1300:
        problems.append(f"dossier length {words} words")
    years = sorted(set(re.findall(r"\b(1[89]\d\d|20[0-3]\d)\b", dossier)))
    if years:
        problems.append(f"dossier contains calendar years {years[:6]}")
    for alias in key.get("aliases") or []:
        if len(alias) >= 4 and re.search(rf"\b{re.escape(alias)}\b", dossier, re.I):
            problems.append(f"dossier contains real name/alias '{alias}'")
    t = key.get("track")
    if t == "B":
        for f in ("decline_mechanism", "decline_risks_expected"):
            if f not in key:
                problems.append(f"Track B missing {f}")
    if t == "E":
        if not key.get("already_great"):
            problems.append("Track E missing already_great: true")
        if "stop_doing_5" not in (key.get("waive_checks") or []):
            problems.append("Track E should waive stop_doing_5")
    if t == "D" and "planted" not in key:
        problems.append("Track D missing planted block")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--resplit", action="store_true")
    a = ap.parse_args()

    old = {}
    if (DATA / "cases.json").exists():
        old = {c["id"]: c for c in json.loads((DATA / "cases.json").read_text(encoding="utf-8"))["cases"]}

    keys, bad = {}, 0
    for kp in sorted((DATA / "answer_keys").glob("*.json")):
        cid = kp.stem
        try:
            key = json.loads(kp.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"{cid}: INVALID JSON {e}")
            bad += 1
            continue
        dp = DATA / "dossiers" / f"{cid}.md"
        if not dp.exists():
            print(f"{cid}: no dossier")
            bad += 1
            continue
        probs = validate(cid, key, dp.read_text(encoding="utf-8"))
        if probs:
            bad += 1
            print(f"{cid}: " + "; ".join(probs))
        keys[cid] = key
    orphan = [p.stem for p in (DATA / "dossiers").glob("*.md") if p.stem not in keys]
    for o in orphan:
        print(f"{o}: dossier without answer key")
        bad += 1
    print(f"\n{len(keys)} cases, {bad} with problems")
    if a.check:
        return 1 if bad else 0

    # ---- clusters: same real company, or Track A matched pair
    parent = {c: c for c in keys}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        parent[find(x)] = find(y)

    by_name = defaultdict(list)
    for cid, k in keys.items():
        n = norm_name(k.get("real_identity"))
        if n:
            by_name[n].append(cid)
    for ids in by_name.values():
        for x in ids[1:]:
            union(ids[0], x)
    for cid, k in keys.items():
        if k.get("track") in ("A", "C") and k.get("group") == "comparison":
            m = re.match(r"([AC])(\d+)", cid)
            partner = f"{m.group(1)}{int(m.group(2)) - 1:02d}"
            if partner in keys:
                union(cid, partner)
    clusters = defaultdict(list)
    for cid in keys:
        clusters[find(cid)].append(cid)

    # ---- assign splits
    split = {}
    if not a.resplit:
        for cid in keys:
            if cid in old and old[cid].get("split") in ("dev", "heldout") and not old[cid].get("provisional"):
                split[cid] = old[cid]["split"]
    rng = random.Random(20261123)
    todo = [cl for cl in clusters.values() if not any(c in split for c in cl)]
    rng.shuffle(todo)
    # stratify: per (track, group), aim for HELDOUT_FRACTION held out
    target = defaultdict(float)
    for cid, k in keys.items():
        target[(k["track"], k["group"])] += HELDOUT_FRACTION
    held = defaultdict(float)
    for cid in split:
        if split[cid] == "heldout":
            held[(keys[cid]["track"], keys[cid]["group"])] += 1
    for cl in todo:
        if any(c in DRY_RUN for c in cl):
            for c in cl:
                split[c] = "dev"
            continue
        strata = [(keys[c]["track"], keys[c]["group"]) for c in cl]
        need = sum(target[s] - held[s] for s in strata) / len(strata)
        to_held = need >= 0.5
        for c in cl:
            split[c] = "heldout" if to_held else "dev"
            if to_held:
                held[(keys[c]["track"], keys[c]["group"])] += 1

    cases = []
    for cid in sorted(keys, key=lambda x: (x[0], int(re.sub(r"\D", "", x)))):
        k = keys[cid]
        prev = old.get(cid, {})
        cases.append({
            "id": cid, "track": k["track"], "group": k["group"], "dossier": f"data/dossiers/{cid}.md",
            "split": split[cid], "recognizable": prev.get("recognizable", False if k.get("real_identity") is None else None),
            "dry_run": cid in DRY_RUN, "cluster": find(cid),
        })
    (DATA / "cases.json").write_text(json.dumps({"cases": cases}, indent=1), encoding="utf-8")

    tally = defaultdict(lambda: [0, 0])
    for c in cases:
        tally[(c["track"], c["group"])][0 if c["split"] == "dev" else 1] += 1
    print("\ntrack/group            dev  heldout")
    for (t, g), (d, h) in sorted(tally.items()):
        print(f"  {t} {g:<24} {d:>3}  {h:>3}")
    print(f"  total                     {sum(v[0] for v in tally.values()):>3}  {sum(v[1] for v in tally.values()):>3}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
