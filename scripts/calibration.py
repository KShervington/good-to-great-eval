"""Judge calibration: you score 6 outputs, then we compare against the judge.

  python scripts/calibration.py make [--ids A03:2,B01:1,...]   # build calibration/ from v0 baseline outputs
  python scripts/calibration.py compare                        # after you fill calibration/your_scores.csv

`make` picks 6 outputs across tracks (one each from A-great, A-comparison/unsustained, B, D, E, plus
one more that spreads the judge's scores), unless --ids is given. For each it writes
calibration/sheet_N.md with the dossier, the answer key and the analysis. The judge's scores go to
calibration/judge_scores.md. Score blind first, then open that file. The target is agreement within
1 point on most dimensions.
"""
from __future__ import annotations

import argparse
import csv
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "calibration"
DIMS = ["D1", "D2", "D3", "D5", "D7", "D8", "D9"]
DIM_NAMES = {
    "D1": "Hedgehog matches the key", "D2": "Stop-doing includes the real decision",
    "D3": "Brutal facts include the key's fact", "D5": "Decline risk flagged (N/A if no decline in key)",
    "D7": "Calibration and honesty", "D8": "One-screen verdict", "D9": "Restraint (already-great cases only)",
}


def judged(version="v0"):
    cases = {c["id"]: c for c in json.loads((ROOT / "data" / "cases.json").read_text(encoding="utf-8"))["cases"]}
    out = []
    for f in sorted((ROOT / "runs" / "judgments" / version).rglob("seed*.json")):
        if f.name.endswith(".meta.json"):
            continue
        cid, seed = f.parent.name, int(f.stem.replace("seed", ""))
        if cases.get(cid, {}).get("split") != "dev":
            continue
        j = json.loads(f.read_text(encoding="utf-8"))
        scores = {d: (j.get(d) or {}).get("score") for d in DIMS}
        if cases[cid]["track"] != "E":
            scores["D9"] = None  # restraint is scored on Track E only
        out.append({"case": cid, "seed": seed, "track": cases[cid]["track"], "group": cases[cid]["group"],
                    "scores": scores, "why": {d: (j.get(d) or {}).get("why") for d in DIMS}})
    return out


def pick(rows, rng):
    buckets = [
        lambda r: r["track"] == "A" and r["group"] == "great",
        lambda r: r["track"] == "A" and r["group"] in ("comparison", "unsustained"),
        lambda r: r["track"] == "B",
        lambda r: r["track"] == "D",
        lambda r: r["track"] == "E",
    ]
    chosen = []
    for b in buckets:
        cand = [r for r in rows if b(r) and r["case"] not in {c["case"] for c in chosen}]
        if cand:
            # prefer outputs where the judge was not uniformly 5s, so calibration sees the low end too
            cand.sort(key=lambda r: sum(v for v in r["scores"].values() if v) / max(1, sum(1 for v in r["scores"].values() if v)))
            chosen.append(cand[0] if rng.random() < 0.6 else rng.choice(cand))
    rest = [r for r in rows if r["case"] not in {c["case"] for c in chosen}]
    if rest:
        rest.sort(key=lambda r: min(v for v in r["scores"].values() if v) if any(r["scores"].values()) else 9)
        chosen.append(rest[0])
    return chosen[:6]


def cmd_make(a):
    rows = judged()
    if a.ids:
        want = {tuple(x.split(":")) for x in a.ids.split(",")}
        chosen = [r for r in rows if (r["case"], str(r["seed"])) in want]
    else:
        chosen = pick(rows, random.Random(11))
    OUT.mkdir(exist_ok=True)
    judge_lines = ["# Judge scores (open AFTER you've scored)\n"]
    with open(OUT / "your_scores.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["sheet", "case", "seed", *DIMS, "comments"])
        for i, r in enumerate(chosen, 1):
            w.writerow([i, r["case"], r["seed"], *["" for _ in DIMS], ""])
    for i, r in enumerate(chosen, 1):
        cid, seed = r["case"], r["seed"]
        dossier = (ROOT / "data" / "dossiers" / f"{cid}.md").read_text(encoding="utf-8")
        key = json.loads((ROOT / "data" / "answer_keys" / f"{cid}.json").read_text(encoding="utf-8"))
        analysis = (ROOT / "runs" / "outputs" / "v0" / cid / f"seed{seed}.md").read_text(encoding="utf-8")
        applicable = [d for d in DIMS if r["scores"].get(d) is not None]
        sheet = [
            f"# Calibration sheet {i}: case {cid}, seed {seed} (Track {r['track']}, {r['group']})\n",
            "Score each dimension 1–5 in `your_scores.csv`, using the anchors in `prompts/judge_rubric.md`. "
            "Leave a cell empty if the dimension is N/A.\n",
            f"Dimensions the judge treated as applicable here: {', '.join(applicable)}\n",
            "\n## Answer key (the analyst never saw this)\n\n```json\n" + json.dumps(key, indent=2, ensure_ascii=False) + "\n```\n",
            "\n## Dossier (the analyst's only input)\n\n" + dossier,
            "\n\n---\n\n## The analysis being graded\n\n" + analysis,
        ]
        (OUT / f"sheet_{i}.md").write_text("\n".join(sheet), encoding="utf-8")
        judge_lines.append(f"\n## Sheet {i}: {cid} seed {seed}\n\n| Dim | Judge | Why |\n|---|---|---|")
        for d in DIMS:
            judge_lines.append(f"| {d} {DIM_NAMES[d]} | {r['scores'].get(d) if r['scores'].get(d) is not None else 'N/A'} | "
                               f"{(r['why'].get(d) or '').replace('|', '/')} |")
    (OUT / "judge_scores.md").write_text("\n".join(judge_lines) + "\n", encoding="utf-8")
    (OUT / "chosen.json").write_text(json.dumps(chosen, indent=1), encoding="utf-8")
    print("wrote", [f"sheet_{i}.md ({r['case']} s{r['seed']})" for i, r in enumerate(chosen, 1)])


def cmd_compare(a):
    chosen = json.loads((OUT / "chosen.json").read_text(encoding="utf-8"))
    by = {(r["case"], int(r["seed"])): r for r in chosen}
    agree, total, rows = {d: 0 for d in DIMS}, {d: 0 for d in DIMS}, []
    with open(OUT / "your_scores.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            r = by[(row["case"], int(row["seed"]))]
            for d in DIMS:
                mine, judge = row.get(d, "").strip(), r["scores"].get(d)
                if not mine or judge is None:
                    continue
                total[d] += 1
                diff = int(mine) - int(judge)
                agree[d] += abs(diff) <= 1
                rows.append((row["sheet"], row["case"], d, int(mine), judge, diff))
    print("dim  within-1  n   (you - judge on each sheet)")
    for d in DIMS:
        if total[d]:
            diffs = [x[5] for x in rows if x[2] == d]
            print(f"{d}   {agree[d]}/{total[d]}      {diffs}")
    n_ok = sum(1 for d in DIMS if total[d] and agree[d] / total[d] >= 0.8)
    n_dims = sum(1 for d in DIMS if total[d])
    print(f"\ndimensions with >=80% agreement within 1 point: {n_ok}/{n_dims}")
    big = [x for x in rows if abs(x[5]) >= 2]
    if big:
        print("disagreements of 2+ points (rubric candidates):")
        for x in big:
            print(f"  sheet {x[0]} {x[1]} {x[2]}: you {x[3]}, judge {x[4]}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("make")
    m.add_argument("--ids")
    m.set_defaults(fn=cmd_make)
    c = sub.add_parser("compare")
    c.set_defaults(fn=cmd_compare)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
