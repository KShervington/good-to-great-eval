"""Automated judge check (replaces human calibration).

Two tests on the Fable judge, using real v0 baseline outputs:

1. Consistency (test-retest): 12 unmodified outputs are judged a second time. The judge should agree with
   itself within 1 point on nearly every dimension.
2. Validity (perturbation): copies of good outputs are deliberately damaged in one specific way. The judge
   must notice and mark down the dimension that the damage targets:
     swap         - an output from a different case is graded against this case's key -> D1/D2/D3 drop
     no_stop      - the stop-doing list (and the verdict's stop-doing lines) removed -> D2 drops
     fabricate    - precise, untagged metrics that aren't in the dossier inserted   -> D7 drops
     no_verdict   - the one-screen verdict removed                                   -> D8 drops
     overprescribe- (Track E) the verdict told to exit and pivot the proven core       -> D9 drops

  python scripts/judge_validity.py make      # write the damaged outputs and add judge jobs to the ledger
  python -m harness run                      # run them (31 judge calls)
  python scripts/judge_validity.py report    # pass/fail per test
"""
from __future__ import annotations

import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from harness.config import JUDGE_MODEL  # noqa: E402
from harness.ledger import Ledger  # noqa: E402

ROUND = "judge-validity"
OUT = ROOT / "runs" / "outputs"
JUD = ROOT / "runs" / "judgments"
SPEC = ROOT / "runs" / "judge_validity_spec.json"


def judged(cid, seed, version="v0"):
    p = JUD / version / cid / f"seed{seed}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def score_of(j, d):
    v = (j or {}).get(d) or {}
    return v.get("score")


def dev_cases():
    return [c for c in json.loads((ROOT / "data" / "cases.json").read_text(encoding="utf-8"))["cases"]
            if c["split"] == "dev"]


def split_sections(md: str):
    """Return (verdict_part, rest), where the verdict is everything before the first numbered/major section."""
    m = re.search(r"^#{2,3}\s*(?:1[.)]|.*great version)", md, re.I | re.M)
    if not m:
        m = re.search(r"^---\s*$", md, re.M)
    return (md[:m.start()], md[m.start():]) if m else ("", md)


def remove_stop_doing(md: str) -> str:
    lines = md.splitlines()
    out, skip_level = [], None
    for line in lines:
        h = re.match(r"^(#{1,6})\s+(.*)", line)
        if h and skip_level is not None and len(h.group(1)) <= skip_level:
            skip_level = None
        if h and re.search(r"stop[- ]doing", h.group(2), re.I):
            skip_level = len(h.group(1))
            out.append(line)
            out.append("")
            out.append("(No stop-doing items.)")
            continue
        if skip_level is not None:
            continue
        out.append(line)
    md2 = "\n".join(out)
    # verdict: drop each stop-doing label line and the list items that belong to it
    verdict, rest = split_sections(md2)
    kept, dropping, label_is_item = [], False, False
    for line in verdict.splitlines():
        if re.search(r"stop[- ]doing", line, re.I):
            dropping, label_is_item = True, bool(re.match(r"^\s*[-*]", line))
            continue
        if dropping:
            child = (re.match(r"^\s{2,}\S", line) if label_is_item
                     else re.match(r"^\s*(?:[-*]|\d+[.)])\s", line))
            if child:
                continue
            dropping = False
        kept.append(line)
    return "\n".join(kept) + ("\n" if kept else "") + rest


FAKE_METRICS = ("Key numbers: revenue growth of 23.7% a year, operating margin of 17.9%, customer retention "
                "of 91.3% and return on capital of 14.6%. Market share is 27.4% and rising.")


def fabricate(md: str) -> str:
    verdict, rest = split_sections(md)
    lines = verdict.splitlines()
    insert_at = next((i for i, l in enumerate(lines) if re.search(r"greatness potential", l, re.I)), len(lines))
    lines.insert(insert_at, "\n" + FAKE_METRICS + "\n")
    rest = re.sub(r"(?im)^(#{1,6}\s+.*scorecard.*)$", r"\1\n\n" + FAKE_METRICS, rest, count=1)
    return "\n".join(lines) + rest


def no_verdict(md: str) -> str:
    verdict, rest = split_sections(md)
    title = verdict.splitlines()[0] if verdict.strip().startswith("#") else ""
    return (title + "\n\n" if title else "") + rest


OVERPRESCRIBE = ("**Verdict:** This subject is only good, and its current model has run its course. Exit the "
                 "core business within 18 months, pivot to a new market, replace the leadership team and adopt a "
                 "new Hedgehog Concept built around the new market.\n\n**Top stop-doing item:** stop operating the "
                 "core business as it is run today.\n\n")


def overprescribe(md: str) -> str:
    verdict, rest = split_sections(md)
    lines = verdict.splitlines()
    first = 1 if lines and lines[0].startswith("#") else 0
    return "\n".join(lines[:first]) + "\n\n" + OVERPRESCRIBE + "\n".join(lines[first:]) + rest


def cmd_make():
    rng = random.Random(42)
    cases = dev_cases()
    by_id = {c["id"]: c for c in cases}
    spec = []

    def add(kind, cid, seed, content, target_dims, expect, source=None):
        version = f"cal-{kind}"
        p = OUT / version / cid / f"seed{seed}.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        spec.append({"kind": kind, "version": version, "case": cid, "seed": seed, "source": source or f"{cid}:s{seed}",
                     "target": target_dims, "expect": expect})

    def src(cid, seed):
        return (OUT / "v0" / cid / f"seed{seed}.md").read_text(encoding="utf-8")

    # 1. consistency: 12 unmodified outputs (seed 2), spread across tracks
    pool = [c["id"] for c in cases]
    rng.shuffle(pool)
    picked, seen_tracks = [], {}
    for cid in pool:
        t = by_id[cid]["track"]
        if seen_tracks.get(t, 0) < 3 and judged(cid, 2):
            picked.append(cid)
            seen_tracks[t] = seen_tracks.get(t, 0) + 1
        if len(picked) == 12:
            break
    for cid in picked:
        add("retest", cid, 2, src(cid, 2), ["all"], "within 1 of original")

    # 2. swap: A great outputs graded against another A great case's key
    greats = [c["id"] for c in cases if c["track"] == "A" and c["group"] == "great"]
    rng.shuffle(greats)
    for a, b in list(zip(greats[0::2], greats[1::2]))[:4]:
        add("swap", b, 1, src(a, 1), ["D1", "D2", "D3"], "each <= 2", source=f"{a}:s1 graded as {b}")

    # 3-5. targeted damage on outputs that scored well on the target dimension
    def good_on(dim, minimum, k, track=None):
        out = [c["id"] for c in cases if (track is None or c["track"] == track)
               and (score_of(judged(c["id"], 1), dim) or 0) >= minimum]
        rng.shuffle(out)
        return out[:k]

    for cid in good_on("D2", 5, 4):
        add("no_stop", cid, 1, remove_stop_doing(src(cid, 1)), ["D2"], "<= 3")
    for cid in good_on("D7", 4, 4):
        add("fabricate", cid, 1, fabricate(src(cid, 1)), ["D7"], "drops by >= 1 and <= 3")
    for cid in good_on("D8", 4, 4):
        add("no_verdict", cid, 1, no_verdict(src(cid, 1)), ["D8"], "<= 2")
    for cid in good_on("D9", 3, 3, track="E"):
        add("overprescribe", cid, 1, overprescribe(src(cid, 1)), ["D9"], "<= 2")

    led = Ledger(ROOT / "state" / "ledger.db")
    for s in spec:
        led.add_job(version=s["version"], case_id=s["case"], seed=s["seed"], stage="judge", model=JUDGE_MODEL,
                    round_name=ROUND)
    SPEC.write_text(json.dumps(spec, indent=1), encoding="utf-8")
    kinds = {}
    for s in spec:
        kinds[s["kind"]] = kinds.get(s["kind"], 0) + 1
    print(f"queued {len(spec)} judge jobs in round '{ROUND}': {kinds}")


def cmd_report():
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    results, retest_diffs = {}, []
    for s in spec:
        new = judged(s["case"], s["seed"], s["version"])
        if new is None:
            print(f"missing judgment for {s['version']} {s['case']}")
            continue
        orig_case = s["source"].split(":")[0]
        orig = judged(orig_case if s["kind"] != "swap" else s["case"], s["seed"])
        ok, detail = None, ""
        if s["kind"] == "retest":
            diffs = [abs(score_of(new, d) - score_of(orig, d)) for d in ("D1", "D2", "D3", "D5", "D7", "D8", "D9")
                     if score_of(new, d) is not None and score_of(orig, d) is not None]
            retest_diffs += diffs
            ok = all(x <= 1 for x in diffs)
            detail = f"abs diffs {diffs}"
        elif s["kind"] == "swap":
            vals = {d: score_of(new, d) for d in s["target"]}
            ok = all(v is not None and v <= 2 for v in vals.values())
            detail = str(vals)
        elif s["kind"] == "fabricate":
            o, n = score_of(orig, "D7"), score_of(new, "D7")
            ok = n is not None and o is not None and o - n >= 1 and n <= 3
            detail = f"D7 {o} -> {n}"
        else:
            d = s["target"][0]
            o, n = score_of(orig, d), score_of(new, d)
            limit = 3 if s["kind"] == "no_stop" else 2
            ok = n is not None and n <= limit
            detail = f"{d} {o} -> {n}"
        results.setdefault(s["kind"], []).append((s["case"], ok, detail))
    print("Judge check")
    for kind, rows in results.items():
        passed = sum(1 for r in rows if r[1])
        print(f"\n{kind}: {passed}/{len(rows)} pass")
        for r in rows:
            print(f"  {'ok  ' if r[1] else 'MISS'} {r[0]}: {r[2]}")
    if retest_diffs:
        within1 = sum(1 for x in retest_diffs if x <= 1) / len(retest_diffs)
        exact = sum(1 for x in retest_diffs if x == 0) / len(retest_diffs)
        print(f"\nretest: {len(retest_diffs)} dimension scores; identical {exact:.0%}, within 1 point {within1:.0%}")


if __name__ == "__main__":
    {"make": cmd_make, "report": cmd_report}[sys.argv[1]]()
