# Judge calibration: 6 baseline outputs

Score these six analyses yourself before opening the judge's scores, so you aren't anchored by them.

| Sheet | Case | What it is |
|---|---|---|
| [sheet_1.md](sheet_1.md) | A03, seed 1 | Track A, great company (just before its transition) |
| [sheet_2.md](sheet_2.md) | A25, seed 1 | Track A, unsustained company (just before its short-lived rise) |
| [sheet_3.md](sheet_3.md) | B05, seed 1 | Track B, great company that later fell (dated before the trouble) |
| [sheet_4.md](sheet_4.md) | C01, seed 1 | Track C, *Great by Choice* company (just before its transition) |
| [sheet_5.md](sheet_5.md) | D03, seed 1 | Track D, synthetic startup with planted traps |
| [sheet_6.md](sheet_6.md) | E06, seed 3 | Track E, synthetic subject that is already great (restraint test) |

Each sheet contains, in order: the answer key, the dossier (the analyst's only input), and the analysis.

**How to score:**
1. Use the 1–5 anchors in [../prompts/judge_rubric.md](../prompts/judge_rubric.md).
2. Fill in [your_scores.csv](your_scores.csv): one row per sheet, one column per dimension.
   - Leave D5 empty when the key has no decline information.
   - Leave D9 empty except on sheet 6.
   - The `comments` column is for anything the rubric gets wrong.
3. Then open [judge_scores.md](judge_scores.md) to see the judge's scores and reasons.
4. Tell me you're done. I'll run `python scripts/calibration.py compare` and adjust the rubric until we agree within 1 point on most dimensions. After that, the baseline will be re-judged.

**Dimensions:**
- D1: hedgehog matches the key
- D2: stop-doing list includes the real decision
- D3: brutal facts include the key's fact
- D5: decline risk flagged
- D7: calibration and honesty
- D8: one-screen verdict
- D9: restraint (Track E only)
