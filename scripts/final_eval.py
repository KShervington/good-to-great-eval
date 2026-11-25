"""Phase 4: score the held-out evaluation (v0 vs final) and draw the report charts.

Refuses to run until the 'final' round is complete. Writes runs/decisions/final.json
and report/*.png. Usage: python scripts/final_eval.py [--final v3]
"""
import argparse
import json
import random
import re
import sqlite3
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import analyze  # noqa: E402
import score  # noqa: E402

BLUE, ORANGE = "#2a78d6", "#eb6834"          # validated categorical slots 1-2 (light surface)
SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
DIMS = ["D1", "D2", "D3", "D5", "D7", "D8", "D9"]
DIM_NAMES = {"D1": "Hedgehog", "D2": "Stop-doing", "D3": "Brutal facts", "D5": "Decline register",
             "D7": "Honesty", "D8": "Verdict", "D9": "Restraint (E)"}


def group_of(r):
    if r["track"] == "E":
        return f"E {r['group']}".replace("_", " ")
    return r["track"]


def boot(diffs_by_cluster, n=10000, seed=7):
    cl = list(diffs_by_cluster)
    rng = random.Random(seed)
    means = []
    for _ in range(n):
        s = [d for _ in cl for d in diffs_by_cluster[rng.choice(cl)]]
        means.append(sum(s) / len(s))
    means.sort()
    allv = [d for v in diffs_by_cluster.values() for d in v]
    return statistics.mean(allv), means[int(0.025 * n)], means[int(0.975 * n) - 1], sum(m > 0 for m in means) / n


def ci_of_mean(recs, n=10000, seed=11):
    by = defaultdict(list)
    for r in recs:
        by[r["cluster"]].append(r["composite"])
    m, lo, hi, _ = boot(by, n, seed)
    return m, lo, hi


def mean(xs):
    xs = [x for x in xs if x is not None]
    return round(statistics.mean(xs), 3) if xs else None


def says_already_great(version, cid, seed):
    md = (ROOT / f"runs/outputs/{version}/{cid}/seed{seed}.md").read_text(encoding="utf-8")
    return bool(re.search(r"stewardship mode|already great", md[:2500], re.I))


def version_block(version, recs):
    rs = list(recs.values())
    out = {"n": len(rs), "composite": mean(r["composite"] for r in rs),
           "dims": {d: mean(r.get(d) for r in rs) for d in DIMS}}
    for key, fn in (("by_track", group_of),
                    ("by_recognizable", lambda r: {True: "recognizable", False: "not recognizable"}.get(r.get("recognizable"), "untagged"))):
        g = defaultdict(list)
        for r in rs:
            g[fn(r)].append(r)
        out[key] = {k: {"n": len(v), "composite": mean(x["composite"] for x in v),
                        "dims": {d: mean(x.get(d) for x in v) for d in DIMS}} for k, v in sorted(g.items())}
    checks = defaultdict(lambda: [0, 0])
    for r in rs:
        for k, v in r["checks"].items():
            if v is not None:
                checks[k][1] += 1
                checks[k][0] += bool(v)
    out["checks"] = {k: f"{a}/{b}" for k, (a, b) in checks.items()}
    d6 = [r for r in rs if r.get("D6") is not None]
    out["D6_correct"] = f"{sum(1 for r in d6 if r['D6'])}/{len(d6)}"
    out["D6_wrong"] = sorted(f"{r['case']}s{r['seed']}" for r in d6 if not r["D6"])
    sl = [(r["gp"], r["label"]) for r in rs
          if r["gp"] is not None and r["label"] in (0, 1) and r["track"] in ("A", "C", "D") and not r["already_great"]]
    out["auroc_ACD"] = score.auroc(sl)
    e = [r for r in rs if r["track"] == "E"]
    if e:
        out["trackE_says_already_great"] = f"{sum(says_already_great(version, r['case'], r['seed']) for r in e)}/{len(e)}"
        out["trackE_mean_gp"] = mean(r["gp"] for r in e)
    non_e = [r for r in rs if r["track"] != "E"]
    out["nonE_says_already_great"] = sorted(f"{r['case']}s{r['seed']}" for r in non_e
                                            if says_already_great(version, r["case"], r["seed"]))
    out["hindsight_leaks"] = sum(1 for r in rs if r.get("hindsight_leak"))
    return out


def pauses():
    con = sqlite3.connect(str(ROOT / "state" / "ledger.db"))
    rows = con.execute("SELECT family, start, end, reason FROM pauses ORDER BY start").fetchall()
    con.close()
    spans = sorted((s, e) for _, s, e, _ in rows if e)
    merged = []
    for s, e in spans:
        if merged and s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return {"events": [{"family": f, "start": s, "end": e, "hours": round((e - s) / 3600, 2) if e else None,
                        "reason": re.sub(r"\s*\[claude-code.*$", "", reason or "")} for f, s, e, reason in rows],
            "wall_clock_paused_h": round(sum(e - s for s, e in merged) / 3600, 2)}


def style(ax):
    ax.set_facecolor(SURFACE)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=INK2, length=0)
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def charts(dev, final_v, ho, dev_cis, ho_cis, outdir):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    outdir.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "text.color": INK,
                         "axes.labelcolor": INK2, "figure.facecolor": SURFACE})

    # 1. Composite by round: dev rounds, then held-out.
    fig, ax = plt.subplots(figsize=(8.2, 3.6))
    style(ax)
    ax.grid(axis="x", visible=False)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    pts = [("r0 baseline\nv0 (dev)", *dev_cis["v0"], BLUE, "baseline"),
           ("r1\nv1 (dev)", *dev_cis["v1"], ORANGE, "accepted"),
           ("r2\nv2 (dev)", *dev_cis["v2"], ORANGE, "rejected"),
           ("held-out\nv0", *ho_cis["v0"], BLUE, ""),
           (f"held-out\n{final_v} (final)", *ho_cis[final_v], ORANGE, "")]
    xs = [0, 1, 2, 3.6, 4.6]
    for x, (lab, m, lo, hi, c, note) in zip(xs, pts):
        ax.plot([x, x], [lo, hi], color=c, linewidth=2, solid_capstyle="round")
        face = SURFACE if note == "rejected" else c
        ax.plot(x, m, "o", markersize=9, markerfacecolor=face, markeredgecolor=c, markeredgewidth=2)
        ax.annotate(f"{m:.1f}" + (f"\n{note}" if note in ("accepted", "rejected") else ""), (x, hi),
                    xytext=(0, 6), textcoords="offset points", ha="center", va="bottom", fontsize=9, color=INK2)
    ax.axvline(2.8, color=GRID, linewidth=1)
    ax.set_xticks(xs, [p[0] for p in pts], fontsize=9)
    lo_all = min(p[2] for p in pts)
    ax.set_ylim(max(0, lo_all - 3), 100)
    ax.set_ylabel("Composite score (0-100)")
    ax.set_title("Composite by round, with clustered 95% CIs (open marker = rejected)",
                 loc="left", fontsize=11, color=INK)
    fig.tight_layout()
    fig.savefig(outdir / "composite_by_round.png", dpi=160)
    plt.close(fig)

    # 2/3. Held-out v0 vs final: per dimension and per track (dumbbell dots, shared scale per chart).
    for name, items, fmt, xlab in (
            ("heldout_dimensions.png",
             [(DIM_NAMES[d], ho["v0"]["dims"][d], ho[final_v]["dims"][d]) for d in DIMS
              if ho["v0"]["dims"][d] is not None],
             "{:.2f}", "Judge score (1-5)"),
            ("heldout_tracks.png",
             [(f"{k} (n={ho['v0']['by_track'][k]['n']})", ho["v0"]["by_track"][k]["composite"],
               ho[final_v]["by_track"].get(k, {}).get("composite")) for k in ho["v0"]["by_track"]],
             "{:.1f}", "Composite (0-100)")):
        items = [i for i in items if i[2] is not None]
        fig, ax = plt.subplots(figsize=(7.4, 0.5 * len(items) + 1.3))
        style(ax)
        for y, (lab, a, b) in enumerate(reversed(items)):
            ax.plot([a, b], [y, y], color=GRID, linewidth=3, solid_capstyle="round", zorder=1)
            ax.plot(a, y, "o", color=BLUE, markersize=8, zorder=2, markeredgecolor=SURFACE, markeredgewidth=2)
            ax.plot(b, y, "o", color=ORANGE, markersize=8, zorder=3, markeredgecolor=SURFACE, markeredgewidth=2)
            ax.annotate(("+" if b - a >= 0 else "") + fmt.format(b - a).replace("-", "−"), (max(a, b), y),
                        xytext=(8, 0), textcoords="offset points", va="center", fontsize=8.5, color=INK2)
        ax.set_yticks(range(len(items)), [i[0] for i in reversed(items)])
        ax.set_xlabel(xlab)
        lo = min(min(a, b) for _, a, b in items)
        hi = max(max(a, b) for _, a, b in items)
        pad = (hi - lo) * 0.25 + 0.05
        right = hi + pad * 1.6
        if "dim" in name:
            right = min(right, 5.2)
        ax.set_xlim(lo - pad, right)
        ax.plot([], [], "o", color=BLUE, label="v0 (original)")
        ax.plot([], [], "o", color=ORANGE, label=f"{final_v} (final)")
        ax.legend(loc="lower right", frameon=False, fontsize=9, ncol=2, bbox_to_anchor=(1, 1.0))
        ax.set_title("Held-out: " + ("by dimension" if "dim" in name else "by track"), loc="left",
                     fontsize=11, color=INK, pad=18)
        fig.tight_layout()
        fig.savefig(outdir / name, dpi=160)
        plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--final", default="v3")
    a = ap.parse_args()
    ok, counts = analyze.round_complete("final")
    if not ok:
        print(f"REFUSED: final round not complete: {counts}")
        return 2
    dev_cases, ho_cases = analyze.load_cases("dev"), analyze.load_cases("heldout")
    dev = {v: analyze.records(v, dev_cases) for v in ("v0", "v1", "v2")}
    ho = {v: analyze.records(v, ho_cases) for v in ("v0", a.final)}
    common = sorted(set(ho["v0"]) & set(ho[a.final]))
    diffs = defaultdict(list)
    for k in common:
        diffs[ho[a.final][k]["cluster"]].append(ho[a.final][k]["composite"] - ho["v0"][k]["composite"])
    m, lo, hi, p = boot(diffs)
    cl_means = {c: statistics.mean(v) for c, v in diffs.items()}
    result = {
        "final_version": a.final, "n_pairs": len(common), "n_clusters": len(diffs),
        "diff": {"mean": round(m, 3), "ci95": [round(lo, 3), round(hi, 3)], "p_final_gt_v0": round(p, 4),
                 "clusters_better": sum(v > 0 for v in cl_means.values()),
                 "clusters_worse": sum(v < 0 for v in cl_means.values())},
        "heldout": {v: version_block(v, ho[v]) for v in ho},
        "dev": {v: version_block(v, dev[v]) for v in dev},
        "pairwise_heldout": analyze.pairwise_summary(a.final, "v0"),
        "skill_words": {v: analyze.skill_words(v) for v in ("v0", "v1", "v2", a.final)},
        "pauses": pauses(),
    }
    case_diffs = defaultdict(list)
    for k in common:
        case_diffs[k[0]].append(ho[a.final][k]["composite"] - ho["v0"][k]["composite"])
    result["heldout_case_diffs"] = {c: round(statistics.mean(v), 2) for c, v in sorted(case_diffs.items())}
    out = ROOT / "runs" / "decisions" / "final.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    dev_cis = {v: ci_of_mean(list(dev[v].values())) for v in dev}
    ho_cis = {v: ci_of_mean(list(ho[v].values())) for v in ho}
    result["ci_of_means"] = {"dev": dev_cis, "heldout": ho_cis}
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    charts(dev, a.final, result["heldout"], dev_cis, ho_cis, ROOT / "report")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
