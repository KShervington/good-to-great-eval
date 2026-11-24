# Plan: good-to-great-anything evaluation and improvement

## Status
- **Model access confirmed (2026-11-23).** `claude -p --model claude-opus-5-5` and `claude -p --model claude-fable-5-2` both answered, and `modelUsage` named the requested model in each case. The CLI prints an `unrecognized_model` warning for Fable 5.2 but serves it. The harness checks `modelUsage` on every call, so a silent switch to another model is recorded as a real failure.
- **Phase 1 dry run (3 cases):** A01 (great), A02 (its direct comparison) and D01 (synthetic startup). The dossiers, answer keys and sources are in `data/`.
- **Harness:** built and tested with simulated limits (`tests/test_resume.py`, `tests/test_limits.py`).

## Design decisions (say if you want any changed)
1. **Isolation of the skill run.** Each run uses `claude -p --model claude-opus-5-5 --safe-mode --strict-mcp-config --tools "" --disable-slash-commands --no-session-persistence --system-prompt-file <preamble + SKILL.md>`, with the dossier on stdin and an empty working directory. That means no tools, web, MCP, CLAUDE.md, memory or plugins. I checked: the model reports no tools and no memory.
2. **Fixed preamble (same for every version).** It tells the model the user is away, so autonomous mode applies; there are no tools; the dossier is the only evidence; output markdown only; and it must add the line `Greatness potential: NN/100`. I put that line in the harness, not in SKILL.md, so the baseline v0 can be scored for AUROC too. The improvement loop may not edit the preamble.
3. **Seeds** are independent samples. The CLI has no seed parameter.
4. **Effort settings:** skill run `high`, judge and pairwise `high`, contamination probe `low`. All are set explicitly, so a change in a default can't shift the results.
5. **Judge blinding.** The judge sees the dossier, the answer key (with real names removed) and the output. It never sees the skill version or the run metadata. Pairwise A/B order is randomized but fixed per job, so a re-run shows the same order.
6. **Score.** The composite score (0–100) is 80% the mean of the judge's 1–5 dimensions (D1, D2, D3, D5, D7, D8), rescaled, plus 20% deterministic checks (including D6, whether Gate 0/1 fails when it should). D4 (AUROC over greatness potential) is reported separately, because it's a property of the whole case set, not of one output. The "2% of max" stop rule therefore means 2 points.
7. **Contamination probe** uses Opus 5.5, the model under test, because what matters is whether *it* recognizes the case.
8. **Limit handling.** On a limit, in-flight jobs for that model are marked `paused_limit` but allowed to finish. If they succeed, their output is kept; if they hit the limit, they stay paused. The Opus and Fable limits are tracked separately: a limit on one model doesn't stop the other.
9. **Splits.** Track A cases go to dev or held-out as matched pairs (a great company and its comparison stay together). Companies that appear in both Track A and Track B (Circuit City, Fannie Mae, Wells Fargo) go to the same split in both tracks. `harness enqueue` refuses held-out cases unless given `--final-eval`.

## Open questions
See "Decisions I need from you" at the bottom.

## Dry-run results (1 seed, v0)
| Case | Group | Composite | Det. checks | Greatness potential | D1 | D2 | D3 | D5 | D7 | D8 | Probe guess |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A01 | great | 92.0 | 7/7 | 35 | 5 | 5 | 5 | n/a | 4 | 4 | Kimberly-Clark (97%) |
| A02 | comparison | 90.0 | 7/7 | 25 | 4 | 5 | 5 | 5 | 4 | 4 | Scott Paper (93%) |
| D01 | synthetic | 88.3 | 5/7 | 25 | 5 | 5 | 5 | 5 | 4 | 4 | FICTIONAL (85%) |

What it shows:
- **Contamination is real for Track A.** Opus 5.5 named both real companies with 93–97% confidence, despite the anonymization. The details that give them away (a tissue inventor with a lawyer CEO diagnosed with cancer; the two brothers who invented the paper towel) are also the strategically meaningful ones. I expect most Track A cases to be tagged `recognizable: true`, so the non-recognizable group will be mostly Tracks D and B.
- **There's little headroom on Track A.** v0 already scores 4–5 on hedgehog, stop-doing and brutal facts. The room to improve is in D7 (calibration), D8 (verdict length), the one-sentence hedgehog rule, and the synthetic traps.
- **The D01 traps worked as intended.** The skill found the buried 38%-of-revenue channel risk and put the dental pilot first on the stop-doing list. But it still *computed* a blended CAC and payback from figures the dossier said were missing (judge D7 = 4), and it wrote a two-sentence hedgehog (failed the deterministic check). However, the probe called D01 "textbook", so the remaining synthetic cases should bury their traps more subtly.
- **The deterministic checker** needed parser fixes on the first real outputs; those are done. The `[ASSUMPTION]` check also flags *derived* figures (for example "38% of ARR ≈ $0.9M"). I've left it strict for now. We'll settle it during judge calibration.

## Measured cost per call (dry run, API-equivalent list price)
| Stage | Model | Input tok | Output tok | $ / call | Time / call |
|---|---|---|---|---|---|
| Skill run | Opus 5.5 (high) | 7.7K | 15.6K | $0.35 | 157 s |
| Judge | Fable 5.2 (high) | 12.6K | 1.8K | $0.25 | 21 s |
| Pairwise | Fable 5.2 | ~21K (est.) | ~2.5K (est.) | ~$0.27 | ~30 s |
| Probe | Opus 5.5 (low) | 2.2K | 0.16K | $0.02 | 6 s |

## Total estimate
Assumed roster: about 53 cases (A 28, B 9, C about 4, D 12), split into about 37 dev and 16 held-out. 3 seeds.

| Block | Calls | Tokens | API-equivalent |
|---|---|---|---|
| Phase 1: remaining probes | ~50 | ~0.1M | ~$1 |
| Baseline round (v0 on dev): run + judge | 222 | ~4.2M | ~$67 |
| Each improvement round (one candidate of ≤3 edits): run + judge + pairwise | 333 | ~6.8M | ~$97 |
| Held-out final (v0 and final): run + judge + pairwise | 240 | ~5M | ~$71 |
| **Worst case: 8 rounds** | ~3,200 | ~65M (~17M output) | **~$920** |
| **Likely: plateau after ~5 rounds** | ~2,000 | ~45M | **~$630** |
| If each edit is tested separately (3 candidates per round) | ~8,300 | ~170M | ~$2,300 |

**Limit resets.** Anthropic doesn't publish Max 5x limits in tokens, so this part is a guess. If a 5-hour window allows roughly $20–40 of Opus/Fable-class usage, the likely run needs **about 16–32 limit resets**, and the worst case about 23–46. The weekly cap will probably bind before the 5-hour cap, so expect **about 1–2 weeks of calendar time**. Call time itself is only about 3.2 hours per round at concurrency 2. The harness logs exactly how many tokens were used before each limit, so after the first real limit I'll replace this guess with a measured figure.

## Decisions I need from you
1. **Edit evaluation.** I recommend that each round test one candidate (up to 3 edits bundled), accepted or rejected as a whole. When a bundle fails but one edit looks promising, the next round re-tests that edit alone. Testing every edit separately costs about 3×.
2. **Approve the next batch.** Build the full roster (Phase 1 proper) and run about 50 contamination probes (about $1). After that, the baseline round: 222 calls, about $67. I'll show you 6 baseline outputs alongside their judge scores for calibration before round 1.
3. **Contamination.** I recommend keeping the Track A dossiers strategically faithful and reporting recognizable and non-recognizable cases separately (as planned), rather than blurring them until they're useless.
