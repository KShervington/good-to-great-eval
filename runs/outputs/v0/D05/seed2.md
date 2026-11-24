# Tessel: Good to Great

## One-screen verdict

**Tessel isn't great yet, and it isn't fully good either.** The trust and attention around it are good: a 2,140-reader newsletter with a 52% open rate, and a discharge social worker whose families ask for the app by name. The product hasn't yet shown that families keep using it. Six outside families use it in a given week. The plan below narrows Tessel to the moment where its pull is strongest, and defers the two big distractions until the product holds families.

- **Hedgehog Concept (working hypothesis):** *Tessel is the medication-and-refill backstop for families from the day a parent comes home from the hospital, handed to them by the people they already trust.*
- **Denominator:** profit per retained care circle.
- **Weakest flywheel link:** going from set-up to weekly reliance. 41 of 318 accounts (13%) ever form a circle. 7 of those 41 circles are active weekly, and one of the seven is the founder's own family.
- **Top three stop-doing items:**
  1. Building the employer pilot spec: SSO, admin dashboard, reporting, and a staffed concierge.
  2. Building a native Android app now. Use text-message reminders for non-iPhone relatives instead.
  3. Making the chain-pharmacy integration the plan's centerpiece. "Don't run out" needs a run-out date, not live pharmacy status.
- **Most urgent brutal fact:** about 6 families outside the founder's own use Tessel weekly, and 3 pay, roughly $21 a month. The accelerator's planned use of funds (chain integration, Android, a hire) doesn't target that.
- **Missing numbers that would change the answer:**
  - Week-1, week-4 and week-8 retention split by source (discharge card, newsletter, forum, friends).
  - How many circles use refill sync, and whether they retain or pay better.
  - Who the 3 payers are.
  - What the HR head would pay for an app-only pilot with no human concierge.
  - The aggregator's decision.
  - The legal basis for the weekly pharmacy export.

`Greatness potential: 9/100`

> *Evidence basis:* There was no search, memory or past-chat access in this session. No prior run exists to use as a baseline, and the competitive and regulatory points are general knowledge, flagged as unverified. The run was autonomous: there were no evidence-batch questions, and every inference is marked `[ASSUMPTION]`.

---

## 1. The great version in one paragraph

Great Tessel is the thing a discharge social worker, case manager or pharmacist hands to a family when a parent goes home from the hospital. The family trusts it because the hand-off comes from someone they trust. Within ten minutes of getting home, the primary caregiver has photographed the pill bottles. Tessel knows each run-out date and nudges the refill request days before the Sunday-night crisis. The brother and the aunt get text reminders without installing anything. The app mostly disappears: families get fewer phone calls, not another screen. Circles stay because a lapse never happens, and they pay because the absence of lapses is worth far more than $6.99. Their stories feed *The Caregiver's Ledger*, which brings in the next referrer. Chain-pharmacy data, Android and employer sales all come later, as accelerators of a loop that is already turning. They are not rescue plans.

## 2. The Hedgehog Concept

**Sentence:** *Tessel is the medication-and-refill backstop for families from the day a parent comes home from the hospital, handed to them by the people they already trust.*

| Circle | Candidates considered | Kept | Ruled out, and why |
|---|---|---|---|
| **Best in the world at** | (a) a general family care-coordination app; (b) pharmacy-data integration; (c) an employer caregiving benefit with a concierge; (d) medication and refill continuity after discharge; (e) writing for exhausted primary caregivers | **(d)**, with (e) as the channel | (a) The category is crowded, and several entrants have shut down or been absorbed `[ASSUMPTION: general knowledge, unverified]`. (b) Tessel doesn't control the data pipe. (c) Funded, services-heavy players already sell this `[ASSUMPTION: unverified]`, and a solo founder can't staff a concierge. |
| **What drives the engine** | revenue per paying circle; revenue per employee per month (employer); circles activated per discharge referral; profit per retained circle | **Profit per retained care circle** | Per employee per month is a different product and a different buyer. Activation per referral is an input to the denominator, not the denominator itself. |
| **Deep passion** | the founder's father and the two lapsed prescriptions; logistics ("a supply-chain problem with love in it"); the weekly newsletter; the aunt's clinical care; the social worker's patients | **No family lets a medication lapse, and the exhausted primary caregiver gets fewer calls** | — |

**Why this denominator:** Acquisition through trusted referrers and the newsletter costs almost nothing in cash. Tessel's economics therefore depend almost entirely on how long a circle stays and pays.

**The unit math, plainly:**
- At $6.99 a month, minus an assumed 15% store fee `[ASSUMPTION]`, each paying circle nets about $5.94.
- Covering the $2,400 monthly net burn takes about 404 paying circles.
- Replacing the contract work, so the founder can work on Tessel full time, takes about 725.
- Tessel has 3 today.

**Tests of the concept:**

| Test | Result |
|---|---|
| Explains past wins? | Yes. The discharge card, the excitement about refills in interviews, the founder's own two lapses, and the newsletter's pull all fit. |
| Rules things out? | Yes. It rules out the employer concierge, native Android now, generic care-log features, and the broad "all aging-parent families" positioning. |
| Uncomfortable to commit to? | Yes. It defers the most money-looking opportunity (Graham's) and narrows the audience. |

**Confirmation tests (90–180 days):**
- Discharge-referred circles retain clearly better at week 8 than circles from other sources.
- At least 3 discharge-referred circles pay.
- A second discharge referrer, unprompted by the first, starts handing out cards.

**Runner-up concept:** if discharge circles *don't* retain better, the real hedgehog may be media-led: *"the trusted Sunday companion for the exhausted primary caregiver,"* with the app as a feature of the newsletter. The source-cohort numbers decide between the two.

## 3. The flywheel

```
 ┌─► 1. A trusted referrer (discharge social worker, pharmacist,
 │      Sunday newsletter) hands Tessel to a family at the crisis moment
 │                     │
 │                     ▼
 │   2. Primary caregiver sets up meds in minutes (photo of label
 │      → run-out date) and adds relatives by text, no install needed
 │                     │   ◄── WEAKEST LINK (13% form a circle; ~6 outside circles weekly-active)
 │                     ▼
 │   3. Run-out nudges arrive days early: no lapses, fewer phone calls
 │                     │
 │                     ▼
 │   4. Circle stays and pays → PROFIT PER RETAINED CIRCLE
 │                     │
 │                     ▼
 │   5. "No lapse" stories and simple outcome data feed the newsletter
 │      and give referrers proof
 │                     │
 │                     ▼
 └── 6. More referrers recommend Tessel by name
```

**Current push (the next two turns):**
1. **Rebuild the first 48 hours for discharge-referred families.** Give each card a unique code, offer a set-up call, have meds entered and relatives invited by text before the first refill is due.
2. **Make run-out prediction work without any pharmacy.** Use the fill date, quantity and refills from the label, entered by hand first and scanned later. The rules for this get the aunt's review. Pharmacy readiness becomes a bonus, not a dependency.

**Doom-loop check:**

| Sign | Present? |
|---|---|
| New direction after new direction | **Yes, in the plan.** The use of funds lists three directions (chain integration, Android, a hire), and section 8 floats a fourth (employer). |
| A big program as savior | **Yes.** "Finish chain integration once access comes through" treats an outside approval as the thing that unlocks momentum. |
| Reaction without understanding | **Risk.** Graham's pitch and the HR head's wish list could set the roadmap before retention data exists. |
| Inconsistency | Not yet. The Sunday newsletter is a model of consistency. |

## 4. The bus

| Person / commitment | Call | Note |
|---|---|---|
| Founder | **Keep, move seat** | Currently CEO, sole iOS developer, Monday data loader, newsletter writer and support. Point the founder's best hours at the biggest opportunity (discharge channel and retention), not the biggest problem (waiting on the aggregator, Android). |
| Aunt (retired nurse) | **Keep, formalize** | Clinical reviewer. Give her a written review checklist for anything touching doses, run-out logic or wording. |
| UX friend (weekends) | **Keep** | Point the weekend hours at the first-48-hours flow. Clarify expectations, whether equity or thanks, before the work grows `[ASSUMPTION: currently informal]`. |
| Stroke-unit social worker | **Keep, the most valuable external seat** | Make her a design partner. Confirm her hospital's policy allows the referral so she's protected `[ASSUMPTION: not yet checked]`. |
| Family-pharmacy pharmacist | **Keep, move seat** | Move from data source to pharmacy advisor. That person can validate the run-out logic and the refill-request timing. |
| Graham Fairley | **Move seat** | Move from strategist to advisor for a later channel. His employer-market knowledge is real and useful *after* Tessel holds families. Thank him and give him a specific revisit trigger. |
| Three HR heads | **Off the bus for now** | A warm "not yet." Offer them the newsletter and a revisit date. |
| Contract analytics work (10 hrs/week) | **Keep** | It roughly halves the burn and buys about 17 months of runway. |
| Pharmacy-data aggregator | **Not on the bus; a dependency** | Follow up once a month. Don't plan around it. |
| Part-time developer | **Don't hire yet** | When in doubt, don't hire. At an assumed ~$3,000 a month `[ASSUMPTION]`, runway falls from about 17 months to under 8. |
| **Missing seats** | — | (1) Privacy and health-data counsel, now. (2) A second discharge referrer at another unit or hospital. (3) An engineer, only after the Gate 1 condition passes. |

## 5. Stop-doing list

1. **Stop building toward the employer pilot spec** (SSO, admin dashboard, anonymized reporting, staffed concierge). Revisit trigger: the Gate 1 condition passes *and* an employer will pay for an app-only pilot.
2. **Stop the native Android build.** Send text-message and email reminders to relatives without iPhones. That fits the founder's own finding that caregivers want fewer calls, not another app.
3. **Stop making chain-pharmacy integration the plan's centerpiece.** Keep the application alive with one follow-up a month.
4. **Stop adding general care-log features** (calendar polish, new note types) that don't serve medication and refill continuity after discharge.
5. **Stop hiring** until retention is proven.
6. **Stop reporting accounts created, star ratings and competition wins as traction.** Report weekly active circles, excluding the founder's own, by source.
7. **Stop expanding the hand-loaded pharmacy export** beyond its current scope until its consent and data-handling basis is confirmed in writing.
8. **Stop entering pitch competitions** for the next 6 months. A story win isn't a market win.

## 6. Brutal facts and the faith statement

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | The product doesn't yet hold families. | 318 accounts → 41 circles (13%) → 7 weekly active (17% of circles, 2.2% of accounts). One of the 7 is the founder's own. | **Critical** | Founder |
| 2 | Enthusiasm isn't payment. | 3 subscribers in 6 weeks (~$21/month), against "I'd pay anything." About 725 paying circles are needed to go full time. | **High** | Founder |
| 3 | The most-loved feature barely exists. | Refill sync covers one pharmacy through a manual weekly email the founder loads. "Ready" status is at best a weekly snapshot. The aggregator application has been under review since August. | **High** | Founder |
| 4 | Possible compliance exposure. | Tessel stores medication lists and wound photos and receives patient refill data by email. The basis for each disclosure and the consumer-health-data rules that apply aren't stated `[ASSUMPTION: not confirmed in writing]`. If this is wrong, it can hurt the pharmacist who is helping. | **High if wrong** | Founder + lawyer |
| 5 | Early signals come from friendly channels. | First users came from the support group and former colleagues. 4.9 stars rests on 11 ratings. | Medium | Founder |
| 6 | The employer opportunity is conditional and is a different business. | The HR head said "would pilot *if*" Tessel had four enterprise features, one of them a staffed human. The PEPM ($3–5) and 1-in-5 figures come secondhand from someone who places benefits. One 1,800-person employer at $3–5 PEPM would be $5,400–9,000/month, which is exactly why it's tempting. | High (as a distraction) | Founder |
| 7 | One-person bus. | Development, data loading, newsletter, support and contract work all run through one person. Nothing works if the founder is out for two weeks. | Medium–High | Founder |
| 8 | A third of the waitlist can't use the app. | Android share of the waitlist. | Medium | Founder |
| 9 | The category has a graveyard. | Family care-coordination apps have come and gone `[ASSUMPTION: general knowledge, unverified]`. | Medium | — |

Good news that is also a fact: runway is about **17 months** ($41,000 ÷ $2,400 net monthly burn). There is time to prove retention without a pivot.

**Truth climate.**
- **The charisma risk is the story.** "My father's stroke, a supply-chain problem with love in it" wins rooms and a $10,000 prize. It can also stand in for weak numbers.
- **Where the risk is named.** The application names an outside gate (pharmacy access) as the biggest risk and says "everything else I can build." The risks the founder controls, activation and retention, aren't named.
- **Red-flag mechanism:** a Monday metrics line that can't be fudged. It shows weekly active circles excluding the founder's own, by source, with week-8 retention.

**Faith statement:** *Families in the worst week of their lives already ask for Tessel by name, and the person building it has lived the lapse and knows logistics. If Tessel earns weekly reliance from discharged families, everything else can be built.*

## 7. Core ideology and BHAG

**Core values**
1. Never let a dose lapse. Reliability beats features.
2. Fewer calls, not more screens.
3. No clinical claim without clinical review. Tessel never gives medical advice.
4. The family's health data is theirs: minimal, protected, never sold.

**Core purpose:** No family should discover on a Sunday night that the medicine ran out.

**BHAG (kept to one line because the horizon is early-stage):** By 2040, no family brings a parent home from a U.S. hospital without a medication backstop.

**Clock-building mechanisms** (so Tessel works without the founder):
- A written clinical-review checklist.
- A data-handling runbook, starting with the pharmacy export.
- Automated weekly metrics.
- A referrer kit (card, code, one-page explainer) that a new social worker can use without the founder present.
- Guest contributors for the newsletter.

## 8. Scorecard

All 12-month targets below are proposed by this run `[ASSUMPTION]`. They are not benchmarks.

| Output | Current | 12-month target | BHAG trajectory |
|---|---|---|---|
| Weekly active circles, excluding the founder's own | ~6 (7 including the founder's) | 100, with week-8 retention of new circles ≥ 40% | Thousands of circles, most started at discharge |
| Paying retained circles (profit per retained circle) | 3 (~$21/month gross) | 150 (~$890/month net) as proof of willingness to pay; ~405 covers burn | Self-funding without contract work, then a second payer (hospital or employer) on a proven product |
| Active discharge referrers / referred-family activation | 1 referrer; activation unknown | 5 referring units or pharmacies; ≥ 50% of referred families enter meds within 48 hours | A standard part of discharge |

## 9. Next 90 days

| # | Action | Owner | Flywheel push |
|---|---|---|---|
| 1 | **This week:** rewrite the accelerator use of funds around the Hedgehog (discharge channel, first 48 hours, run-out prediction, text reminders). Report weekly active circles excluding the founder's own, list Android and employer as gated, and send Graham and the HR heads a warm "not yet, here's the trigger" note. | Founder | Stops the doom loop |
| 2 | **Weeks 1–2:** instrument cohorts by source and retention, then interview at least 10 of the 34 circles that went quiet. Ask why they went quiet, not what features they want. | Founder | Links 2→3 |
| 3 | **Weeks 2–8:** ship the run-out date from the label (manual entry first, then on-device scan) and text or email reminders for non-app relatives. | Founder + aunt (review) + UX friend + pharmacist (validation) | Links 2→3 |
| 4 | **Weeks 2–12:** run a structured discharge pilot with the social worker: coded cards and a 48-hour set-up call. After confirming her hospital's policy, ask for one introduction to a second discharge team. | Founder + social worker | Links 1, 6 |
| 5 | **Weeks 1–4:** get the lawyer's written view on the pharmacy-export basis, the email transport, and the consumer health-data rules that apply. Fix whatever it finds before adding any pharmacy. | Founder + lawyer | Protects the whole loop |

## 10. Re-check

When you're back, a re-check about 90 days out can be scheduled. It would re-score the scorecard with real cohort numbers and re-run Gates 1, 5 and 8, especially the test of discharge-led versus newsletter-led. Without that loop, nobody learns whether these verdicts were right.

## 11. Risk register

| Source | Risk | Condition, or early warning sign | Evidence that clears it |
|---|---|---|---|
| Gate 1 (CONDITIONAL) | The app isn't yet "good"; only its trust and attention are. | Weekly active circles excluding the founder's own stay at or below 10. | ≥ 20 outside weekly active circles and week-8 retention ≥ 40%, held for two consecutive months |
| Gate 5 (CONDITIONAL) | The Hedgehog is unproven. | Discharge cohorts retain no better than other sources. | ≥ 15 discharge-referred circles; ≥ 50% enter meds within 48 hours; week-8 active rate above other sources; ≥ 3 paying; a second referrer |
| Gate 8 (CONDITIONAL) | Links 2→3 and 4 are unproven; the plan shows doom-loop signs. | The use of funds still lists four directions. | A rewritten plan, plus one observed full turn: referral → active → paying → newsletter story → new referral |
| Gate 4 | Compliance exposure on health and pharmacy data | No written legal view by week 4 | A written basis plus fixes |
| Gate 2/3 | One-person bus | A missed Monday load or a missed newsletter | Automated metrics, runbooks, a referrer kit |
| Decline 1: Hubris | Treating the prize, 4.9 stars and "asked for by name" as proof | Pitch deck metrics that differ from the Monday metrics line | The same numbers everywhere |
| Decline 2: Undisciplined more | Android, employer, chain integration and a hire all at once | More than one new surface shipped in a quarter | The stop-doing list held for two quarters |
| Decline 3: Denial of risk | Calling pharmacy access *the* risk while retention slides | Retention not reviewed weekly | Retention is the first line of every update |
| Decline 4: Grasping for salvation | Taking the employer pilot or a big integration to rescue flat numbers | "If we just land X" language | Revisit triggers decided in advance, not under pressure |
| Decline 5: Capitulation | Runway hits about 6 months with no proof, then an exit or shutdown | Runway < 9 months and Gate 1 still CONDITIONAL | Decide at month 9: double down, switch to the newsletter-led concept, or pursue the employer channel deliberately |

## 12. Gate log

| Gate | Verdict | One line |
|---|---|---|
| 0 Fit | PASS | An ongoing product with a steward, years of horizon, and measurable circles |
| 1 Baseline | CONDITIONAL | Trust and attention are good; product retention is unproven |
| 2 Level 5 | PASS | Ambition is aimed at the cause and the founder credits others. Gap: names outside risks, not the ones it controls |
| 3 First Who | PASS | No misaligned person in a key seat. Missing: counsel, a second referrer |
| 4 Brutal Facts | PASS | Facts confronted. Consistent with Gate 1, which already discounted the founder's own circle |
| 5 Hedgehog | CONDITIONAL | Post-discharge medication backstop; working hypothesis |
| 6 Discipline | PASS | 8-item stop-doing list; the Sunday newsletter proves consistency |
| 7 Technology | PASS | Label-to-run-out and text reminders accelerate; Android and SSO wait |
| 8 Flywheel | CONDITIONAL | Loop closes on paper; the set-up→reliance and payment links are unproven |
| 9 Built to Last | PASS | Values, purpose, one-line BHAG, mechanisms |
| 10 Mighty Fall | PASS | Five decline paths mapped with warning signs |

**Count from the table:** 8 PASS, 3 CONDITIONAL, 0 FAIL. The three CONDITIONALs share one root: strong demand signals at the top of the funnel, with no evidence yet that the product holds families week after week.

---

### Appendix: other gate artifacts

**Subject card:** Tessel. Product / app, consumer iOS. Steward: the solo founder. Horizon: years, with about 17 months of runway. Stage: 14 months building, 4 months live, applying to a pre-seed accelerator.

**Baseline sheet:**

| Strand | Evidence |
|---|---|
| Good | Daily use by the founder's family; a discharge referrer with pull; a 2,140-reader newsletter at 52% opens; 26 interviews; a working iOS core |
| Not yet good | Activation (13%), weekly reliance (~6 outside circles), payment (3) |

Draft definition of great:
- **Superior performance:** retention and no-lapse outcomes that beat general care apps.
- **Distinctive impact:** discharge teams would notice if it vanished.
- **Lasting endurance:** it runs on referrer kits and automated pipes, not on the founder's Mondays.

**Leadership read:**
- *Strengths:* resolve aimed at the cause, learning humility (the "fewer phone calls" insight), credit given to colleagues and the social worker.
- *Gap:* the risk is framed through the window (pharmacy access), not the mirror (activation and retention), and the founder is a single point of failure.
- *Behavior change:* open every weekly review with the one number the founder controls, weekly active circles excluding the founder's own, before any mention of the aggregator.

**Discipline framework:**
- *Freedom:* any feature that shortens set-up or prevents a lapse.
- *Boundary:* anything else goes to a parking lot reviewed quarterly.
- *Bureaucracy check:* the Monday manual load is a workaround for a missing pipe, not a rule. Retire it once there's a documented or automated path.
- *Fanatical consistency:* the Sunday newsletter, the Monday metrics line, clinical review on every dose-related change, and a 48-hour set-up call for every referred family.

**Technology triage:**

| Tech | Call |
|---|---|
| Push reminders; text/email reminders to relatives | Accelerate |
| Label → run-out date (on-device text recognition, family confirms, clinically reviewed rules) | Accelerate. **Pioneer candidate** |
| Coded discharge card or QR code that pre-starts a circle | Accelerate. **Pioneer candidate** |
| Aggregator pharmacy API | Accelerate *later*; not a dependency |
| iOS app, calendar, photo notes | Parity. Keep, but photo notes are privacy-sensitive |
| Manual emailed pharmacy export | Neutral. Needs a compliance fix |
| Native Android | Drop for now |
| SSO, admin dashboard | Irrelevant now |
| AI "concierge" chat | **Hype flag**. Don't build one to fill the HR head's staffed-human request |