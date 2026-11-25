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
Assumed roster: about 60 cases (A 28, B 9, C about 4, D 12, E 7), split into about 37 dev and 16 held-out. 3 seeds.

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


## Track E: already-great controls (added 2026-11-23 at the user's request)
**Why:** every other track rewards prescribing change. Track E tests whether the skill recognizes a subject that is already great and holds back. It also gives Track B a control group: without companies that stayed great, a generic decline register would "flag" decline everywhere, and we couldn't tell foresight from boilerplate.

**Cases:**
- **E01–E05:** real good-to-great companies dated well after their transition, at a point where greatness then lasted 10 or more years with no How-the-Mighty-Fall decline. Candidates (to be verified): Nucor, Abbott, Walgreens, Gillette and Kimberly-Clark, each around the 1990s.
- **E06:** a synthetic subject that is great and stays great.
- **E07:** a synthetic subject that is great but quietly drifting into decline stage 1 or 2 (hubris, or pursuing more without discipline).

**Answer key:** `already_great: true`. The key gives the hedgehog the subject already lives by; the restraint decision (what *not* to change and which temptations to refuse); the expected decline watch-points (E07, plus the real cases where relevant); and `waive_checks: ["stop_doing_5"]`.

**Scoring:**
- **New judge dimension D9 (restraint):** 5 means it recognizes greatness with evidence, keeps the existing hedgehog, gives a few recommendations that preserve what works, and names specific warning signs. 1 means it overhauls or pivots the proven core, or is complacent with no warnings.
- **D2:** reinterpreted for these cases as the restraint decision.
- **D9 elsewhere:** null for all other tracks.
- **Greatness potential:** Track E is reported separately, not in the AUROC (which measures future greatness from a pre-transition date). The sustained real cases should score high.

**Prediction for v0:** it will over-prescribe. Gate 1 has no "already great" path, the skill's opening principle demands narrowing, and Gate 6 asks for at least five stop-doing items.

**Cost:** about 7 more cases, so about $17 more per improvement round and about $80–130 over the whole run.

## Phase 1 complete (2026-11-23)
**58 cases:**

| Track | Cases | Notes |
|---|---|---|
| A | 28 | 11 great, 11 comparison, 6 unsustained |
| B | 9 | fallen great companies |
| C | 2 | Stryker vs U.S. Surgical; 31 of 32 candidates rejected, see `data/track_c_criteria.md` |
| D | 12 | synthetic, in the mix you specified |
| E | 7 | 5 real already-great companies plus 2 synthetic |

**Splits:** 42 dev, 16 held-out (stratified; same-company and matched-pair cases kept in the same split). The held-out set has no singleton case types (the Track C pair, the Gate 0/1 fails, the drifting E07), because the loop needs those signals in dev. Final results for those behaviors will come from dev, which is a limitation.

**Contamination probe:** 44 of 44 real-company dossiers were identified by name (80–97% confidence); 14 of 14 synthetic ones were called fictional. So "recognizable vs not" is the same split as "real vs synthetic", and the two can't be separated in the report. A second, per-output measure is also tracked: the judge flags any output that names the real company or uses hindsight (`recognized_subject_by_name`, `hindsight_leak`).

**Build cost:** the 8 research agents used about 1.85M tokens. The probes cost $1.16 API-equivalent.

## Baseline round (awaiting OK)
v0 on dev, 42 cases × 3 seeds:
- **Calls:** 252 (126 skill runs + 126 judge calls).
- **Tokens:** about 4.8M.
- **Cost:** about $76 API-equivalent.
- **Time:** about 3 hours of call time at concurrency 2, plus limit pauses.

**Revised whole-run estimate with 58 cases:**
- **Each improvement round:** about $110.
- **Likely total (about 5 rounds):** about $700.
- **Worst case (8 rounds):** about $1,030.

**Next:** I'll show you 6 baseline outputs with their judge scores for calibration. If calibration changes the rubric, the baseline gets re-judged, which costs about $32.

## Changes decided 2026-11-24 (user)
1. **No human calibration.** The user judged that the model is better placed than they are to compare outputs with the answer keys. It's replaced by an automated judge check (`scripts/judge_validity.py`) with two parts:
   - **Consistency:** 12 unmodified outputs are judged a second time, and should agree with their first judgment within 1 point.
   - **Validity:** good outputs are deliberately damaged, and the judge must mark down the dimension each kind of damage targets:

     | Damage | Judge must mark down |
     |---|---|
     | Swap in another case's output | D1–D3 |
     | Delete the stop-doing list | D2 |
     | Insert untagged invented metrics | D7 |
     | Delete the verdict | D8 |
     | Tell an already-great subject to exit its core | D9 |

   If the judge misses one of these, the rubric gets fixed before round 1.
2. **The skill may depart from Collins.** It can change its fundamental principles where the evidence shows an obvious improvement, not just tune how it applies Collins. Track A and C answer keys still encode Collins's view, so a principle that departs from Collins can lose points there while helping on Tracks B, D and E. Every decision reports per-track deltas, so this stays visible.
3. **Derived figures.** A figure computed from dossier numbers is acceptable when it's visibly marked as derived or approximate. Computing a metric the dossier says is *missing* is still a D7 fault (judge). The regex `[ASSUMPTION]` check couldn't tell the two apart (it passed only 36–59 of 126 v0 outputs, mostly on honest derived numbers), so it's now reported only and left out of the composite.

## Decisions I need from you
1. **Edit evaluation.** I recommend that each round test one candidate (up to 3 edits bundled), accepted or rejected as a whole. When a bundle fails but one edit looks promising, the next round re-tests that edit alone. Testing every edit separately costs about 3×.
2. **Approve the next batch.** Build the full roster (Phase 1 proper) and run about 50 contamination probes (about $1). After that, the baseline round: 222 calls, about $67. I'll show you 6 baseline outputs alongside their judge scores for calibration before round 1.
3. **Contamination.** I recommend keeping the Track A dossiers strategically faithful and reporting recognizable and non-recognizable cases separately (as planned), rather than blurring them until they're useless.
