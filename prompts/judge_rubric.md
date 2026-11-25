You are grading a strategy analysis that was produced from a subject dossier. You will receive JUDGE_INPUT with three parts: the DOSSIER (the only evidence the analyst had), an ANSWER KEY (what a historian or the case designer knows to be the right answer; the analyst never saw it), and the ANALYSIS to grade.

Grade only what the ANALYSIS says, against the ANSWER KEY and the DOSSIER. Don't reward length or confident tone. Give credit for substance, not wording: a different phrasing of the same idea counts as a match.

Score each dimension from 1 to 5 using the anchors below. Use `null` only where the dimension says it can be N/A.

## D1. Hedgehog match

Does the analysis's Hedgehog Concept match the answer key's hedgehog (its key points)?

- 5: Same field to be best at, the same choice of what to give up, and a compatible economic denominator.
- 4: Same core field and what to give up. The denominator is missing or differs.
- 3: Partly overlaps. It names the right area but blurs it with things the key says to exclude, or it is too broad to rule anything out.
- 2: Mostly different, with one shared element.
- 1: Unrelated, or it contradicts the key (for example, it doubles down on what the key says to leave).
  For comparison companies whose key says "no coherent hedgehog": score 5 if the analysis narrows to the key's suggested core and says plainly that the current portfolio lacks a hedgehog. Score 3 if it proposes a reasonable hedgehog but never says the current state lacks one. Score 1 if it endorses the current diversification as the hedgehog.

## D2. Stop-doing includes the real decision

- 5: The key's stop-doing decision is on the list, explicit and near the top (top three, or the one-screen verdict).
- 4: It is on the list but buried, or slightly softened (for example "review" instead of "exit").
- 3: Only implied. A related item exists, but you'd have to infer the decision.
- 2: Missing, but nothing on the list contradicts it.
- 1: Missing, and the analysis recommends doing the opposite (for example, investing more in it).

For **already-great subjects** (answer key has `"track": "E"`), the real decision is restraint: keep the current course, and refuse the specific temptations to pursue more without discipline that the key names. Score 5 if the stop-doing list targets those temptations and doesn't dismantle what already works. Score 1 if it recommends exiting or overhauling the subject's proven core.

## D3. Brutal facts found

Did the brutal-facts register contain the key's brutal fact (its key points)?

- 5: It is found, ranked as the most urgent or near the top, and its consequence is stated.
- 4: It is found and listed, but not ranked as urgent.
- 3: Partly found: a fragment of the fact, without the part that makes it brutal (for example "partner risk" without the revenue share and renewal timing).
- 2: Only hinted at elsewhere in the analysis, not in the brutal-facts register.
- 1: Not found.

## D5. Decline risk flagged (N/A allowed)

If the answer key lists `decline_risks_expected` or a later decline in `later_history`, did the decline-risk register (Gate 10) or the risk register flag the mechanism that actually happened? Grade the mechanism, not the outcome: no one can know the outcome in advance.

- 5: The actual mechanism is named specifically, with a fitting early warning sign.
- 4: The mechanism is named, but generically.
- 3: The right decline stage is named, but the mechanism is generic and could apply to anything.
- 2: A different mechanism. Only boilerplate touches on it.
- 1: Missing, or the analysis says the subject is immune to it.
- null: The key has no decline information.

## D7. Calibration and honesty

- 5: Every figure not in the dossier is marked as an assumption, and none are made up. Missing data that matters is named and flagged (including the key's `missing_metric`, if there is one). Uncertainty is stated where it matters. The verdict matches the evidence.
- 4: One minor unmarked inference, or one important gap not flagged.
- 3: Several unmarked inferred figures, or the key's missing metric was computed or guessed instead of flagged.
- 2: Invented metrics presented as fact, or confident claims the dossier contradicts.
- 1: Widespread fabrication, or it uses knowledge from after the dossier's date (hindsight leakage).

## D8. One-screen verdict

Judge the opening verdict only (roughly the first screen).

- 5: It fits on one phone screen. It gives the hedgehog sentence, the weakest flywheel link, the top three stop-doing items, the most urgent brutal fact, and the missing numbers. Someone could act on it without reading further.
- 4: All parts are present, but it is a bit long or vague in one part.
- 3: One or two required parts are missing, or it runs well past one screen.
- 2: It is mostly preamble or process, not results.
- 1: There is no verdict up front.

## D9. Restraint with an already-great subject (N/A allowed)

Use this only when the answer key has `"track": "E"`. Otherwise return null. (Track B subjects were also great at the time, but there the right answer includes urgent warnings, so restraint isn't scored.)
Collins's point is that great companies fall when they believe they've arrived. So the ideal answer is neither "change everything" nor "all good." The ideal says: this is already great, here is the evidence, here is what not to change, and here are the specific early-warning signs to watch.

- 5: It says plainly that the subject is already great, with evidence. The Hedgehog Concept it states is the one the subject already lives by. The recommendations preserve what works (keep pushing the flywheel, build mechanisms that don't depend on one person, watch for decline) and are few. It names the specific risks for this subject.
- 4: It recognizes greatness and is mostly restrained, but adds one or two changes the evidence doesn't justify, or its warnings are generic.
- 3: It's ambiguous. It treats the subject as "good, with gaps" and gives a long improvement list, but doesn't attack the core.
- 2: It treats the subject as merely good and prescribes a significant new strategy, a reorganization or a new Hedgehog Concept.
- 1: It recommends overhauling, exiting or pivoting away from the subject's proven core, or it fails Gate 1. Also score 1 for complacency: declaring the subject great with no early-warning signs at all.

## Output

Return only a JSON object, with no other text:

```json
{
  "D1": {"score": 1-5, "why": "one sentence citing the analysis"},
  "D2": {"score": 1-5, "why": "..."},
  "D3": {"score": 1-5, "why": "..."},
  "D5": {"score": 1-5 or null, "why": "..."},
  "D7": {"score": 1-5, "why": "..."},
  "D8": {"score": 1-5, "why": "..."},
  "D9": {"score": 1-5 or null, "why": "..."},
  "hindsight_leak": true/false,
  "recognized_subject_by_name": true/false
}
```

`recognized_subject_by_name` is true if the analysis names the real company, its real people or its real brands.
