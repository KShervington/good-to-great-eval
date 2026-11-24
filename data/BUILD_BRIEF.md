# Build brief for dossier writers

You are writing evaluation cases for a skill that runs a subject through Jim Collins's Good to Great framework. A separate model will read ONLY the dossier (never the answer key) and produce a strategy analysis. A judge then compares that analysis with the answer key.

Study the worked examples before writing:
- `data/dossiers/A01.md` + `data/answer_keys/A01.json` (Track A, great company)
- `data/dossiers/A02.md` + `data/answer_keys/A02.json` (Track A, direct comparison company)
- `data/dossiers/D01.md` + `data/answer_keys/D01.json` (Track D, synthetic)

## Dossier rules (`data/dossiers/<ID>.md`)
1. **Point in time.** State the "as of" point in relative terms (for example "Year 0", "early in Year 0") with no calendar year. Include ONLY what was known or knowable on that date. Nothing that happened later: no later results, no later product names, no later CEOs.
2. **Anonymize.** Replace every company, person, brand and place name with an invented one, or with a role such as "Rival P" or "the new CEO". Blur any detail that gives the company away but isn't strategically important (exact founding year, the founder's hometown, famous slogans). Keep anything that carries strategic meaning, even if it's distinctive. Don't gut the dossier to defeat recognition: a separate probe measures recognizability.
3. **Facts, not guesses.** Every figure must come from a source you list. If you can't confirm a figure, leave it out and list it under "## What is not in this dossier". Prefer relative or qualitative statements over invented precision. Never invent numbers for real companies.
4. **Neutral voice.** Don't hint at what the right strategy is, and don't editorialize ("unfortunately", "wisely"). Present the internal debates as debates.
5. **Shape.** Same sections as A01: Overview, Financial position, Market position, Leadership, Strategy and known problems, What is not in this dossier. About 450–900 words.
6. Plain markdown, UTF-8.

## Answer-key rules (`data/answer_keys/<ID>.json`)
Use the same fields as A01/A02, plus the track-specific fields below. Required for every case:
`case_id, track, group, real_identity (null for synthetic), aliases (names a probe might answer with), as_of_year (null for synthetic), transition_year, expected_gate_fail (null, 0 or 1), greatness_label, later_history, notes`, and a `collins` block (real companies) or equivalent `reference_*` fields (synthetic): `hedgehog`, `hedgehog_key_points`, `stop_doing`, `stop_doing_key_points`, `leader_type`, `brutal_facts`.

`greatness_label` means: 1 if the subject, from the dossier's date, went on to become (or, for E, stay) great for 10+ years; 0 if not; null if unclear.

**Track-specific fields:**
- **Track A, unsustained comparisons:** `group: "unsustained"`. The `collins` block says what Collins said went wrong after the short-term rise.
- **Track B (decline tests):** `group: "fallen"`, `already_great: true`. Add `decline_mechanism` (one paragraph), `decline_risks_expected` (list of short phrases, each mapped to a How the Mighty Fall stage), and `decline_stage_at_dossier_date`.
- **Track E (already great):** `group: "already_great"`, `already_great: true`, `waive_checks: ["stop_doing_5"]`. The `collins` (or `reference_`) hedgehog is the one the subject *already* lives by. `stop_doing` = the restraint decision: what NOT to change, and which tempting moves to refuse. Add `decline_risks_expected` (an empty list if it stayed great).
- **Track D (synthetic):** add a `planted` block with `brutal_fact`, `brutal_fact_key_points`, `distraction`, `distraction_key_points`, `missing_metric` and `missing_metric_key_points` (see D01).

## Sources (`data/sources_parts/<your-part>.md`)
For each case, list the sources used: title, publisher, URL, and which facts came from it. Flag anything you couldn't verify. Record dates you had to choose (the transition year, the dossier date) and the evidence for them. Use Collins's books as the authority for the answer key (paraphrase, never quote more than a few words). Use independent sources (company histories, encyclopedias, newspaper archives, annual reports) for the dossier facts.

## Don'ts
- Don't touch files outside your assigned IDs and your sources part.
- Don't write quotations from Collins of 15 words or more anywhere.
- Don't edit `data/cases.json`. Return your manifest in your final report instead.

## Your final report (keep it short)
1. A JSON array, one object per case: `{"id","track","group","as_of_year","real_identity","transition_year"}`.
2. Facts or dates you were not able to verify, and what you did about them.
3. Any candidate you rejected, with the reason.
