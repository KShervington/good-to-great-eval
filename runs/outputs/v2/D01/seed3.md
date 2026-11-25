# Tallypaw: Good to Great

## Verdict

**Tallypaw is good but not yet great, and its biggest threat is sitting under "housekeeping" in the board notes.**

- **Hedgehog Concept (working hypothesis):** Tallypaw is the best in the world at running the independent vet clinic's drug and supply shelf, whichever distributor the clinic buys from, and it grows by raising lifetime gross profit per independent clinic.
- **Weakest flywheel link:** new clinics come in through Maya's personal demos and through VetSource. VetSource is a partner that is now building a rival inventory tool.
- **Top three stop-doing:** (1) the dental build, (2) the corporate-chain pilots, (3) Maya running most demos.
- **Most urgent brutal fact:** VetSource-referred accounts are 38% of ARR (about $0.9M). Renewal is due in five months, and two emails have gone unanswered.
- **Missing numbers that would change this:** the VetSource contract terms (who owns those customers), CAC by channel, logo churn, and the size of the independent-clinic market.
- **Confidence:** moderate to low. The verdict rests on founder-reported figures and the CTO's churn analysis.

Greatness potential: 25/100

---

## 1. The great version in one paragraph

In three to five years, great Tallypaw is the default system for the pharmacy and supply shelf of independent vet clinics in every market it serves. Each clinic gets a monthly report showing money saved (fewer stockouts, less expired stock, better reorder timing) worth more than its subscription. Practice managers recruit other practice managers. The product works with several distributors, so a clinic never has to trust a supplier to tell it what to buy from that same supplier. No single channel brings in more than 25% of ARR. A demo playbook run by former practice managers replaces Maya as the sales engine, and reminders are a cheap, parity-level feature. The "second market" question is settled with numbers, not a conference LOI. If those numbers show that independent vet cannot reach venture scale alone, the honest outcome may be a great, capital-efficient company rather than a venture-scale one. That is a board conversation to have openly, not a reason to build a dental product.

## 2. The Hedgehog Concept

**Sentence:** *Tallypaw is the best in the world at running the independent vet clinic's drug and supply shelf, whichever distributor it buys from, and it grows by raising lifetime gross profit per independent clinic.*

| Circle | Candidates considered | Kept | Rejected, and why |
|---|---|---|---|
| **Best in the world at** | Appointment reminders; full practice-management suite; enterprise chain software; dental software; inventory for independent vets; distributor-neutral purchasing intelligence | Inventory for 1–4 vet independents, made **distributor-neutral** | Reminders are a commodity running on a rented SMS vendor. Full practice-management software is a crowded fight against incumbents `[ASSUMPTION]`. Chains: 0 of 2 pilots converted. Dental: Tallypaw is not "one of them" there, and dental supply chains differ `[ASSUMPTION]` |
| **Economic engine** | ARR per clinic; gross profit per clinic; **lifetime gross profit per independent clinic**; revenue per seat | **Lifetime gross profit per independent clinic** | Inventory clinics churn about half as often as reminder-only clinics. Inventory therefore roughly doubles customer lifetime, and lifetime value is the variable the business actually controls |
| **Deeply passionate about** | Independent clinics; how small clinics order drugs; venture scale; enterprise logos | Independent clinics and their supply shelf (Maya as a former practice manager, Jonah's inventory engine, CS staff who are former vet techs) | "Venture scale" and "real money upmarket" express growth anxiety, not passion for the work |

**Denominator:** lifetime gross profit per independent clinic, roughly (ACV × 78% GM) ÷ annual logo churn. Today that is about **$6,000 gross profit per clinic per year**. The churn input is unknown, so the lifetime figure cannot be computed yet.

**Why the "whichever distributor" clause matters:** VetSource's native tool will almost certainly optimize ordering inside VetSource's own catalog `[ASSUMPTION]`. A neutral tool is something a distributor cannot credibly build. If independents order from more than one supplier `[ASSUMPTION]`, neutrality is the moat.

**Confirmation tests** (this is a hypothesis, not a finding):
1. **Multi-sourcing:** what share of clinics order from two or more distributors? If it is under about 30% `[ASSUMPTION threshold]`, the neutrality clause adds little. Narrow back to "inventory for independents" and focus on depth.
2. **Measurable savings:** is the median annual dollar value saved per inventory clinic at least as large as the ACV ($7,700)? If it is far below, the referral step of the flywheel has no fuel.
3. **Market size:** are there at least about 10× the current clinic count (3,000+) reachable independent clinics in serviceable markets `[ASSUMPTION threshold]`? If not, the scale debate is real and belongs with the board.
4. **Direct-channel payback:** is CAC payback in the non-VetSource channels under about 18 months?

## 3. The flywheel

```
 ┌─► 1. Built by people who ran clinics
 │      (practice-manager-native product, ex-vet-tech CS)
 │          │
 │          ▼
 │   2. Inventory adoption (attach 71% → 85%)
 │          │
 │          ▼
 │   3. Measured savings per clinic
 │      (fewer stockouts, less expired stock, smarter reorders, across ANY distributor)
 │          │
 │          ▼
 │   4. Clinics stay and expand → LIFETIME GROSS PROFIT PER INDEPENDENT CLINIC ▲
 │          │
 │          ▼
 │   5. Practice managers refer practice managers
 │      (savings proof, case studies, reviews, the CS staff they name)
 │          │
 │          ▼
 │   6. More independent clinics at lower CAC → more cross-clinic ordering data
 │          │
 └──────────┘  data sharpens reorder suggestions; gross profit funds product + CS
```

The loop closes. Each turn makes the next clinic both cheaper to acquire and more valuable to keep.

**Weakest link: step 5 → 6.** Acquisition today runs on Maya's demos and VetSource's bundle, not on a referral engine the flywheel generates itself. Step 3 is the second-weakest link: nothing in the dossier shows that Tallypaw measures and shows clinics their savings, so referrals rest on enthusiasm rather than proof.

**Current push (next two turns):**
1. **Secure the base.** Resolve VetSource on the best terms available. In parallel, build a direct relationship with every VetSource-referred clinic.
2. **Make savings visible.** Ship a per-clinic savings report. Turn it into the referral mechanism and the core of the demo playbook, so Maya is no longer required to run the demo.

**Doom-loop check: early signs are present, but the full loop has not started.**
- Two new directions appeared in two board meetings: the chains (Head of Sales) and dental (Maya).
- The board's request for focus was deferred until "after the dental pilot."
- The risk to watch: if VetSource walks away, dental will look like salvation. That is the classic grasping move.
- No acquisitions or big-bang programs yet.

## 4. The bus

| Person / commitment | Call | Seat and reasoning |
|---|---|---|
| **Maya (CEO)** | **Keep, move seat** | Her credibility as a former practice manager is the company's best asset. Move it from running demos to (a) leading the VetSource negotiation and the distribution strategy, and (b) codifying her demo into a playbook. Her current seat makes her the sales bottleneck |
| **Jonah (CTO)** | **Keep** | Shows the strongest Level 5 signals in the dossier (he looks in the mirror first in post-mortems). Give him the savings report and the multi-distributor integration work, which is the heart of the Hedgehog |
| **Head of Sales** | **Wrong seat, possibly off** | His thesis (chains are "where the real money is") contradicts the Hedgehog, and 0 of 2 pilots converted. Offer a clear independent-clinic charter: channel attribution on the $1.1M, a repeatable demo playbook, and a referral program. If his conviction stays upmarket, part ways respectfully. He would be in the wrong role for *this* company, which says nothing about his ability |
| **CS (2 former vet techs)** | **Keep, put on the biggest opportunity** | Customers praise them by name. Point them at the ~118 VetSource-referred clinics `[ASSUMPTION: 38% of 310 at a uniform ACV]` to build direct relationships, not just tickets |
| **VetSource (partner)** | **Keep on the bus conditionally** | Renew if the terms are fair and allow neutrality. Either way, VetSource-referred ARR should fall below 30% within 12 months |
| **SMS vendor** | **Move seat** | Prices rose 30%, and the vendor supports a parity module. Renegotiate or replace |
| **Dental group owner (LOI)** | **Off the bus** | Decline graciously. The LOI is non-binding and outside the Hedgehog |
| **Board** | **Keep** | It asked the right question (fewer roadmap items). Treat it as an ally of focus |

**Missing seats:**
1. A **partnerships/channel lead** with vet-distribution experience, to run multi-distributor integrations and non-VetSource channels.
2. A **second seller who is a former practice manager**, to run the codified demo.
3. A **third CS hire** (former vet tech). Two people for 310 clinics is about 155 clinics each.
4. A **RevOps/finance analyst** to produce CAC by channel, churn, and savings data. Several decisions in this plan are blocked on numbers nobody currently owns.

## 5. Stop-doing list

1. **Stop the dental build.** Assign zero engineers and decline the pilot. Two engineers for six months is roughly 20% of engineering capacity `[ASSUMPTION: ~10 engineers of 23 staff]`, taken out during the five-month VetSource window.
2. **Stop the corporate-chain pilots.** End the sales motion, and add no chain-specific features (enterprise SSO, multi-region rollups).
3. **Stop Maya running most demos.** Hand them over gradually: at least 50% run by others within 90 days.
4. **Stop unattributed S&M spend.** No new trade show or campaign without channel tracking. The $1.1M cannot currently be judged.
5. **Stop investing in reminders beyond parity.** Keep the module working, reprice or switch the SMS vendor, and build no new reminder features.
6. **Stop building inventory features that only work inside the VetSource portal** `[ASSUMPTION: some current integration is VetSource-specific]`. New inventory work should be distributor-neutral by default.
7. **Stop treating the VetSource renewal as housekeeping.** It becomes the standing first agenda item at every board meeting until it is resolved.
8. **Don't expand the office at the March lease renewal** `[ASSUMPTION: no expansion plan stated]`. Hold or shrink space until the VetSource outcome is known, given 20 months of runway.

**Non-negotiable disciplines:**
- Every roadmap item must strengthen inventory for independents. The roadmap is capped at five items per quarter.
- Every new clinic gets a savings baseline at onboarding.
- Every S&M dollar is tagged to a channel.
- Blameless post-mortems (already Jonah's habit) extend to sales losses and churned clinics.

**Framework boundaries:**
- *Freedom inside:* how teams serve independent clinics, which features ship within the five-item cap, and how CS builds relationships.
- *Outside the framework, requiring a board vote:* any new market, any customer segment above four vets, any engineering allocation over 10% outside the Hedgehog, and any single channel exceeding 30% of ARR.

**Bureaucracy check:** no compensating bureaucracy appears in the dossier. The risk runs the other way: decisions move at Maya's speed with too little structure.

## 6. Brutal facts and the faith statement

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | The largest channel partner is becoming a competitor to the best module | VetSource announced "native inventory intelligence" last month; VetSource referrals are 38% of ARR (about $912K) | **Critical** | Maya |
| 2 | Renewal is due in about five months and VetSource is silent | Two unanswered emails. The dates also don't match: a four-year term signed three years ago would end in about 12 months, so the five-month date may be a notice deadline. **Check the contract** | **Critical** | Maya and counsel |
| 3 | Nobody knows who owns the VetSource-referred customers | The dossier doesn't say whether those clinics contract with Tallypaw or with VetSource, or whether non-solicit or data clauses apply | **Critical** | Maya and counsel |
| 4 | The existential risk sat under housekeeping while new markets got the presentations | Board notes structure | High (truth climate) | Board chair and Maya |
| 5 | The upmarket thesis has not worked | 0 of 2 chain pilots converted in 8 months | High | Head of Sales |
| 6 | The dental plan pulls engineers away during the most dangerous window | Non-binding LOI; the 4× market estimate is Maya's own and unverified; 2 engineers for 6 months | High | Maya |
| 7 | Growth depends on the founder | Maya "still runs most demos" | High | Maya and Head of Sales |
| 8 | Sales efficiency cannot be judged | $1.1M S&M with no channel breakdown. Net new ARR of about $0.9M gives roughly 0.8 net-new ARR per S&M dollar (blended, and it hides the VetSource subsidy) | High | Head of Sales |
| 9 | "Venture scale needs a second market" is a belief, not a calculation | Independent-clinic market size is not given; consolidation of clinics into corporate chains may be shrinking the segment `[ASSUMPTION: industry trend, not verified here]` | Medium-High | Maya and board |
| 10 | Expansion is modest | NRR is 104%, so there is little upsell beyond inventory | Medium | Jonah and CS |
| 11 | Reminder margins are eroding | SMS vendor prices up 30%; gross margin of 78% sits slightly below typical SaaS `[ASSUMPTION benchmark]` | Medium | Engineering lead |
| 12 | CS is stretched thin | 2 people for 310 clinics | Medium | Maya |

**Truth climate:** mixed. Strengths: Jonah's mirror behavior, the CTO's own churn analysis, and a board that pushes for focus. Weaknesses: Maya's speed and decisiveness, combined with founder charisma, appear to steer attention toward exciting new opportunities and away from the threat to the core. The red-flag mechanism needed: any channel above 30% of ARR, or any unanswered partner communication on a renewal, automatically goes to the top of the board agenda.

**Faith statement:** *No chain-focused vendor and no distributor selling its own shelf will understand the independent clinic's supply room the way we do, and clinics that run their inventory on Tallypaw stay.*

## 7. Core ideology and the BHAG

**Core purpose:** keep independent vet clinics independent by letting a small practice run its pharmacy and supplies as well as any chain.

**Core values:**
1. **Built by people who did the job.** Practice managers and vet techs shape the product and the customer relationship.
2. **The clinic's interest comes first.** That means distributor-neutral recommendations, always.
3. **Own the mistake first.** Jonah's post-mortem habit, made company-wide.
4. **Fewer things, done fully.**

**BHAG** (10–20 years): *Half of all independent vet clinics in the markets Tallypaw serves run their drug and supply shelf on Tallypaw, and each saves more than it pays.* `[ASSUMPTION: penetration target; requires market-size data to calibrate]`

**Clock-building mechanisms:**
- A codified demo playbook and a team of former practice managers who sell.
- A per-clinic savings report that sells the product without a founder in the room.
- A channel-concentration tripwire at 30%.
- A quarterly stop-doing review with the board.
- Blameless post-mortems for lost deals and churned clinics.
- CAC tracked by channel.

## 8. Scorecard

| Output | Current | 12-month target | BHAG trajectory |
|---|---|---|---|
| **Paying independent clinics** | 310 | 400 `[ASSUMPTION: matches last year's +90 with dental and chains cut and VetSource at risk]` | ~2× every 2–3 years until penetration data says otherwise `[ASSUMPTION]` |
| **Gross profit per clinic per year** (with inventory attach as the leading indicator) | ~$6,000 (ACV $7,700 × 78% GM); attach 71% | $6,600; attach 80%; NRR 108% `[ASSUMPTION targets]` | Lifetime gross profit per clinic at least 2× today, once churn is measured |
| **Largest single channel's share of ARR** | 38% (VetSource) | ≤30% | ≤20% within 24 months, ≤15% at steady state |

**Add as soon as measured:** annual logo churn, split into inventory and reminder-only clinics, and median dollars saved per inventory clinic.

## 9. Next 90 days

1. **Escalate VetSource above email** (owner: **Maya**, with a board member).
   - Within 2 weeks: arrange an in-person meeting with a VetSource executive.
   - Have counsel review the contract for customer ownership, data rights, non-solicit and termination clauses, and resolve the five-month vs. ~12-month date conflict.
   - Build "renew" and "no renew" scenarios with ARR at risk and runway impact.
   - Decide the walk-away terms before the meeting.
2. **Build a direct relationship with every VetSource-referred clinic** (owner: **CS lead**, with the two former vet techs). Hold a check-in and a savings review with each of the ~118 clinics, and move them to direct contracts at renewal wherever the contract allows.
3. **Ship the per-clinic savings report and scope a second-distributor integration** (owner: **Jonah**). Pull the two dental-assigned engineers onto this. It covers flywheel step 3 and the neutrality moat, and it tests Hedgehog confirmation tests 1 and 2.
4. **Formally close the off-Hedgehog bets** (owner: **Maya**, presenting to the board). Decline the dental pilot, end the chain pilots, and deliver a roadmap of five items or fewer within 30 days, which the board already asked for. Commission an estimate of the independent-clinic market (test 3).
5. **Fix sales measurement and remove the founder bottleneck** (owner: **Head of Sales**).
   - Tag channel attribution on the $1.1M, including CAC payback by channel.
   - Write the demo playbook, with at least 50% of demos run by someone other than Maya by day 90.
   - Launch a practice-manager referral program.
   - At day 90, Maya decides on his seat based on this charter.

*Also assigned, outside the five:* the engineering lead renegotiates or re-bids the SMS vendor within 60 days.

## 10. Re-check

A scheduled re-check about 90 days from now (**around 23 February 2027**) would land before the VetSource deadline. It would re-score the scorecard with real numbers (clinics, gross profit per clinic, channel share, and the newly measured churn and savings figures) and re-run Gates 1, 5 and 8 to see whether the Hedgehog's confirmation tests held. If you want it, ask once and it will be set up. No scheduling tool was available in this run.

## 11. Risk register

| Risk | Source | Early warning sign | Trigger and action |
|---|---|---|---|
| **Denial of risk: VetSource** (stage 3, the primary decline mechanism) | Gate 10 | No executive meeting within 2 weeks; VetSource demos its native tool to shared clinics; VetSource-referred new logos fall >30% quarter on quarter; churned clinics cite "the portal does it now" | No signed term sheet 60 days before the deadline → run the direct-migration plan and redirect S&M to direct channels |
| **Undisciplined pursuit of more: dental, chains, then "salvation"** (stages 2 and 4) | Gate 10 | Any engineer assigned outside independent vet; roadmap above 5 items; a new-market proposal following any VetSource setback | Allocation over 10% outside the Hedgehog → requires a board vote. If VetSource is lost, dental is explicitly **not** the response |
| Leadership speed outruns discipline | Gate 2 CONDITIONAL | Board requests deferred; decisions made without numbers | **Condition:** Maya delivers the ≤5-item roadmap and closes dental within 30 days, and Maya-run demos fall below 50% by day 90 → PASS |
| Head of Sales is misaligned | Gate 3 CONDITIONAL | Continued chain prospecting; no channel attribution by day 60 | **Condition:** an accepted independent-clinic charter plus delivered attribution data → PASS. Otherwise a respectful exit |
| Truth climate buries existential risk | Gate 4 CONDITIONAL | Partner, market or concentration risks appearing under housekeeping | **Condition:** a channel-concentration tripwire on every board agenda and a VetSource status in each meeting → PASS |
| Hedgehog not yet proven | Gate 5 CONDITIONAL | Low multi-sourcing; savings below ACV; small market | **Condition:** confirmation tests 1–4 come back positive → PASS. If test 1 fails, drop the neutrality clause |
| Discipline not yet installed | Gate 6 CONDITIONAL | Stop-doing items quietly resurface | **Condition:** a board-adopted stop-doing list and a quarterly review held at least once → PASS |
| Hubris (stage 1) | Gate 10 | "Vets love us because we were one of them" is used in place of data; NPS falls among clinics not sold by Maya | NPS below 45 in any acquisition cohort → investigate |
| Capitulation (stage 5) | Gate 10 | Runway below 12 months with no path to cover the VetSource ARR gap | Runway below 12 months → the board weighs bridge financing, cost reduction, or strategic options deliberately, not reactively |
| Reminder margin squeeze | Gate 4 / Gate 7 | Further SMS price rises; gross margin below 75% | Switch vendors or reprice reminders |

## 12. Gate log

*Method note: no memory, past-chat, or web-search access was available in this run. No earlier baseline was found, market and competitor research was not possible, and the dossier is the only evidence. Market claims are marked `[ASSUMPTION]`.*

| Gate | Verdict | One line |
|---|---|---|
| 0 Fit | PASS | An ongoing B2B business with a clear steward, people to rearrange, and measurable outcomes |
| 1 Baseline | PASS | Good, not yet great: +60% ARR, 104% NRR, 78% GM, inventory halves churn. All three tests of great are still unmet |
| 2 Level 5 Leadership | CONDITIONAL | Maya has strong domain resolve but speed tilts toward new markets. Jonah shows Level 5 traits |
| 3 First Who | CONDITIONAL | Head of Sales is pushing a strategy that contradicts the Hedgehog. Four seats are missing |
| 4 Brutal Facts | CONDITIONAL | Facts surfaced and they don't contradict Gate 1, but the truth climate filed the existential risk as housekeeping |
| 5 Hedgehog | CONDITIONAL | Distributor-neutral inventory for independents, per lifetime gross profit per clinic. Four confirmation tests pending |
| 6 Discipline | CONDITIONAL | Stop-doing list is clear but not yet adopted. The board's focus request is still deferred |
| 7 Technology | PASS | Inventory and data accelerate; reminders and SMS are parity; dental is irrelevant |
| 8 Flywheel | PASS | The loop closes. Weakest link is acquisition; early doom-loop signs noted |
| 9 Built to Last | PASS | Purpose, values, BHAG, and clock-building mechanisms defined |
| 10 Mighty Fall | CONDITIONAL | Stage 3 (VetSource denial) and stage 2 (dental and chains) are already active |

**Tally from the table:** 5 PASS, 6 CONDITIONAL, 0 FAIL, across 11 gates. **More than half the gates are CONDITIONAL.** They trace to two shared root problems:
1. **Attention is flowing to new markets instead of the threat to the core business.** This drives Gates 2, 3, 6 and 10, and the housekeeping placement in Gate 4.
2. **Key numbers are missing:** channel CAC, churn, contract terms, and market size. This drives Gate 5. Fixing either root moves most of the CONDITIONAL gates toward PASS.

---

### Supporting artifacts

**Subject card (Gate 0)**
- **Name:** Tallypaw
- **Type:** Business (B2B SaaS)
- **Steward:** Maya (CEO), with Jonah and the board
- **Horizon:** multi-year, with 20 months of runway at current burn
- **Stage:** post-Series A; $2.4M ARR, 310 clinics, 23 staff

**Baseline sheet (Gate 1)**
- ARR $1.5M → $2.4M (+60%).
- Clinics 220 → 310 (+41%).
- ARR per clinic about $6.8K → $7.7K (+13%, consistent with inventory upsell).
- NRR 104%, GM about 78%, NPS 61 (n = 138).
- Inventory attach 71% (about 220 clinics), with about half the logo churn of reminder-only clinics.

Tests of great:

| Test | Status | Why |
|---|---|---|
| Superior performance | Partial | Strong growth, modest NRR |
| Distinctive impact | Plausible but threatened | VetSource could fill the gap Tallypaw leaves |
| Endurance | Not yet | Founder-led sales and single-channel concentration |

**Leadership read (Gate 2)**
- **Maya's strengths:** domain credibility, resolve for independent clinics, and decisiveness.
- **Maya's gaps:**
  - Speed beats discipline: she deferred the board's focus request.
  - Her ambition is framed around "venture scale" rather than around the clinics.
  - The company would stall without her demos.
- **One concrete behavior change:** before discussing any new opportunity, put the VetSource status and the stop-doing list on the table first, and hand off half the demos within 90 days.
- **Jonah:** his "mirror" behavior is the template the rest of the company should copy.

**Tech triage (Gate 7)**

| Technology | Call |
|---|---|
| Inventory engine and reorder suggestions | Accelerates |
| Cross-clinic ordering benchmarks | Accelerates; **pioneer** candidate |
| Multi-distributor catalog normalization and integrations | Accelerates; **pioneer** candidate |
| ML demand forecasting | Accelerates if explainable. **Flag:** risk of a fear-driven "AI" rush in reaction to VetSource's announcement |
| VetSource portal integration | Parity; maintain during renewal |
| Reminders on the third-party SMS vendor | Parity; reprice or switch |
| CRM and channel attribution tooling | Parity, but urgently needed |
| Dental version, enterprise chain features | Irrelevant; drop |