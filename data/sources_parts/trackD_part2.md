# Sources and design notes: Track D part 2 (D08-D12) and Track E synthetic (E06, E07)

All seven cases are fictional. No external sources were used, and no real company, person, brand or place is depicted. Every figure was invented for the case and checked for internal consistency (totals, shares, weighted averages). Dates are relative only ("Year 0"); `as_of_year` and `transition_year` are null for all seven.

Shared design rules applied to the D cases:
- The brutal fact is never stated and its consequence is never spelled out. It emerges only by combining two or more details placed in different parts of the document, usually next to a plausible competing explanation.
- The distraction has a credible advocate, real evidence and something the subject wants (money, headcount, a promotion, a story funders like).
- The missing metric is one an analyst would want and could be tempted to compute from partial numbers. The key states which computation counts as making it up.
- Forms vary, and each dossier includes irrelevant but realistic detail.

---

## D08: Eastbank Housing Defense Collaborative (nonprofit, civil legal aid, ~$3.4M budget)
- **Form:** annual grant report to a foundation, plus the program officer's site-visit notes.
- **Brutal fact (selection effect plus shrinking coverage):** pieces are (1) the Q2 screening protocol in "Program changes", written as a quality improvement; (2) the results table (cases 1,688 to 1,274; win rate 81% to 93%); (3) county filings 6,152 to 7,486, which appear only in the program officer's notes. Coverage falls from about 27% to about 17%. The report's own explanation (two vacancies) is plausible but too small to explain it. The advice desk's outcomes are untracked, which hides where the screened-out tenants end up.
- **Distraction:** Homeownership Pathways ($735K, 18% indirect, which would close the deficit), advocated by the bank-executive treasurer, with 41% survey interest. Secondary: doubling the policy unit.
- **Missing metric:** cost per full-representation case. Expenses are reported only by functional class, so total / cases (~$2,700) is the tempting fabrication.
- **Irrelevant detail:** bar award, Room 2B renovation, elevator outage, case-management migration.
- **Label rationale (1):** Level 5-leaning ED, real distinctive capability, county partner happy; the problem is fixable once confronted.

## D09: Larder Line (nonprofit, food rescue, ~$0.6M budget)
- **Form:** consultant's interview notes (ED, ops manager, board chair, treasurer, pantry partner).
- **Brutal fact (anchor donor's markdown app):** pieces are (1) the ED's gala anecdote that Freshway's app goes chainwide next year; (2) the ops manager's aside that Eastside stores have piloted it since spring; (3) the treasurer's table, where Eastside pounds per pickup fall 412 to 263 while other Freshway stores hold at 398 to 391; Freshway is 44% of all pounds. A competing explanation (Route 9 construction) is offered by the treasurer.
- **Distraction:** the Larder Kitchen café, championed by a respected restaurateur board chair, with a rent-free kitchen, a $150K grant invitation and a peer café's year-3 break-even. Secondary: backpack and composting add-ons.
- **Missing metric:** food actually reaching households (discard rate, unduplicated households). The tempting fabrication is pounds / 1.2 = meals, or cost per meal.
- **Irrelevant detail:** van transmission quote, Saturday no-shows, "more dairy, less bread".
- **Label rationale (0):** yes-to-everything founder, single-donor dependence, weak measurement.

## D10: Delivery Platform team, Brightwater Financial (team, internal engineering platform)
- **Form:** the team's own quarterly retro notes, with a short context paragraph.
- **Brutal fact (adoption is broad but shallow):** pieces are (1) adoption growth driven by new services (34 of 35); (2) the incident table (5 of 6 serious incidents, both Sev-1s, on legacy pipelines, 4 in Payments); (3) "what didn't go well" (rollback epic slipped a third time; Payments' stated migration condition); (4) the action items (rollback "carried over (3rd time)", OKR "80% of services").
- **Distraction:** Atlas developer portal: VP sponsor, two headcount, 58% survey pain, a peer company's halved onboarding, an excited team.
- **Missing metric:** change failure rate and restore time by pipeline. Deploys aren't split by pipeline, and legacy isn't instrumented. The tempting fabrication is 6/4,212, or apportioning deploys by the 64% service share.
- **Irrelevant detail:** bowling offsite, coffee machine, intern dashboard, secret-manager migration.
- **Label rationale (1):** Level 5 EM, strong execution and team; the fix is a reprioritization.

## D11: Heart Failure Transitions Program, St. Aldric (team, hospital clinical)
- **Form:** manager's annual memo to the VP of Nursing, with an accreditation-prep checklist and a budget attachment.
- **Brutal fact (benefit fades after the measured window):** pieces are (1) the protocol ending with a "graduation" call at day 30; (2) the 30-day table (15.9% vs 21.8%); (3) 90-day rates (32.7% vs 33.9%), buried in the pharmacist's accreditation checklist between fridge logs and label replacements; (4) the comparison group excludes decliners, unreachable patients and nursing-facility discharges (selection).
- **Distraction:** leading Hospital at Home: CMO request, published 19% cost study, board enthusiasm, 6 FTE and a director title for the manager.
- **Missing metric:** cost per readmission / net financial return. The tempting fabrication is (21.8% - 15.9%) x 1,146, about 68 "avoided", then $1.46M / 68 or times an assumed readmission cost.
- **Irrelevant detail:** donated scales, licensure, large-print handouts, penalty percentage.
- **Label rationale (0):** Level 3 manager pulled toward expansion; the core result is weaker than believed.

## D12: Bellmoor 250 (one-off artifact, expected Gate 0 FAIL)
- **Form:** ED's covering note explicitly requesting a full Good to Great review, plus two sets of steering-committee minutes.
- **Why it is tempting:** a chair devoted to the book, a $1.36M budget, 15 commissioners, nine subcommittees, 410 volunteers, numeric targets, a "legacy" theme and a councillor's idea for an annual festival.
- **Why it fails Gate 0:** a single ten-day event; the steward dissolves by charter about 90 days after the final audit; all staff are fixed-term; the horizon is 14 months. The expected answer is FAIL at Gate 0, with a suggested reframe (the town's ongoing heritage and events capacity, the oral-history archive, the producer's career) or a better method (project plan, pre-mortem, risk register, cash-flow plan).
- **Plants (for consistency; should not be reached):** brutal fact is the Calder Mills pledge (63% of sponsorship, $160K due April) combined with the parent's consolidation news and the retired sponsor contact; distraction is the $96K AR app; missing metric is a grounded attendance forecast (no baseline; do not derive from population or the workshop target).
- **Label:** null (greatness over 10+ years undefined for a one-off event).

## E06: Halvard Strings (Track E, already great and stays great; small company)
- **Form:** CFO's pre-read for the board strategy session, in the standard section shape.
- **Greatness evidence:** 14 years of growth ($11.2M to $46.8M), operating margin 24-29% in ten of eleven years, ~34% ROIC, professional share 9% to 31%, 78% three-year loyalty, held premium pricing.
- **Existing hedgehog:** professional violin-family strings through independent shops, validated by the Listening Room; it exited student and mass-market guitar strings fourteen years ago.
- **Temptation to refuse:** Halvard Six (guitar strings through a national chain): a 6x larger market, a real 2.3x corrosion-life lab result, 900-store placement, a credible advocate from consumer audio, and a "concentration risk" argument. It re-enters the business the company deliberately left, at half the gross margin, through a channel that conflicts with its shop strategy. Secondary: buying a student-string brand.
- **No decline signals planted.** Ordinary watch points (succession, shop consolidation, a mass-retail-minded commercial director) are present so a good answer can name specific warnings without inventing decline.
- **Leader:** Level 5 (credit to players, luck attribution, mechanisms and succession in place).

## E07: Calloway Reading Partners (Track E, already great but drifting into How the Mighty Fall stages 1-2; nonprofit)
- **Form:** board packet excerpts: CEO letter, program dashboard, four committee reports, decisions requested.
- **Greatness evidence:** two RCTs (0.31, 0.27 SD), 70% vs 39% benchmark, 12 years of renewals, 41-school waitlist, cost per student well below the sector median, 84% staff engagement, 22% of former tutors becoming teachers.
- **Drift signals, spread out and each framed as an achievement or routine decision:**
  - Stage 1: "cracked the code" and "proven in every setting" (CEO letter, finance committee); speaking engagements 6 to 23; the governance committee prizes his "visibility"; research director vacant 9 months, internal outcome study replaced by a dashboard; new-school decline labeled "ramp-up".
  - Stage 2: $40M grant tied to five states in 30 months plus three funder-nominated seats; One Million Readers; training cut from 30 to 18 hours (presented as a $410K saving); coaching ratio 1:12 to 1:19; tutor retention 81% to 68%; the founding COO replaced by a VP of Growth, with training merged into "Talent and Growth"; math pilot and parent app.
- **Design choice:** the all-school benchmark rate only slips 73% to 70%, which looks like noise; the decline is visible only in the split by school age (new schools 69% to 63% to 58%, older schools flat at 74%). The all-school figure is consistent with older schools carrying about 75-80% of students.
- **Label (0):** fictional later history has the effect diluting in new states and the first non-renewal.

## Dates chosen
All cases use relative dates only. No transition year applies (synthetic), so `transition_year` is null throughout. E06's narrowing decision is placed at Year -14 and E07's founding at Year -16 to give each more than ten years of record before the dossier date.
