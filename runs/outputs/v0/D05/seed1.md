# Tessel: Good to Great

## Verdict (one screen)

**Call:** Tessel has a working core and two real assets: a newsletter that caregivers actually open, and a discharge-desk referral that families ask for by name. It is not yet a product that families keep using or pay for. The next 90 days are fit work aimed at one narrow thing. They are not a time to expand.

**Hedgehog Concept (working hypothesis):** *Tessel is the quiet supply chain behind an aging parent's care. From the day the parent comes home from the hospital, it makes sure medicines and appointments never lapse, with the fewest possible phone calls for the one person holding it together.*

**Weakest flywheel link:** families who set up a circle stop using it. Only 7 of 41 circles are weekly active, and one of those is almost certainly the founder's own family. Only 3 circles pay.

**Top three stop-doing items:**
1. Stop building toward the employer checklist: SSO, admin dashboard, anonymized reporting and a human-staffed concierge.
2. Stop planning a native Android app or an Android hire. Give non-iPhone family members SMS and web access instead.
3. Stop making the roadmap depend on pharmacy data access, whether that's the Monday email export or the chain aggregator. Compute refill due dates without it.

**Most urgent brutal fact:** the application says the biggest risk is pharmacy access. The evidence says the biggest risk is that families stop using Tessel after setup. "I'd pay anything" has so far turned into 3 subscribers, about $21 a month.

**Missing numbers that would change this answer:**
- Week-4 and week-8 circle retention by acquisition source: discharge card, newsletter, forum, friends and colleagues.
- How many of the 41 circles came from the social worker.
- Whether the founder's family circle is counted in the 7.
- Churn of the 3 paying subscribers.
- Whether the HR pilot would be paid, and at what price.
- Any signal on the aggregator decision.

Greatness potential: 9/100

---

> **Evidence basis.** This run had no memory, past chats or web search. It is built only on the founder's accelerator application, taken as true as of the application week. Competitor, market, pricing and legal points that the dossier doesn't contain are marked `[ASSUMPTION]`.

---

## 1. The great version in one paragraph

When a parent leaves the hospital after a stroke, fall or cardiac event, the discharge social worker hands the family a Tessel card. That is already true at several hospitals, not one. Within a day, the primary caregiver (usually one exhausted daughter) has a circle set up from a photo of the discharge medication list. Her brother on Android and her aunt with a flip phone take part by text and never install anything. Tessel knows when each prescription will run out from the fill date and days' supply. It reminds the right person a week ahead and tracks the refill through requested, ready and picked up. Live pharmacy data makes this better where it exists, but the feature works without it. Nobody finds out on a Sunday night that the blood thinner has run out. Families keep their circle well past the 90-day post-discharge window and pay per circle, because Tessel replaced the group chat, the fridge whiteboard and most of the phone calls. *The Caregiver's Ledger* turns those families' stories into the next month's referrals. None of this depends on the founder loading a spreadsheet on Mondays.

## 2. The Hedgehog Concept

**Sentence:** *Tessel is the quiet supply chain behind an aging parent's care. From the day the parent comes home from the hospital, it makes sure medicines and appointments never lapse, with the fewest possible phone calls for the one person holding it together.*

| Circle | Candidates considered | Kept | Explicitly *not* best at |
|---|---|---|---|
| **Best in the world at** | (a) medication supply logistics for families; (b) the discharge-to-home transition; (c) a trusted voice for family caregivers (the newsletter); (d) general family care coordination | **(a) inside (b)**: never-lapse medication and appointment logistics, starting at discharge. (c) is the distribution engine. | Employer benefits administration; human care navigation and concierge; clinical care management; a general caregiver social network; cross-platform feature parity |
| **Economic / resource engine** | Revenue per paying user; employer PEPM; newsletter sponsorship per subscriber; revenue per discharge referral | **Revenue per care circle still active at day 90.** The circle is the unit of value. One payer covers a whole family, and the other members are free invitees who make the circle stick. Acquisition cost stays near zero through discharge referrals and the newsletter. | Revenue per account. 318 accounts is a vanity number. |
| **Deep passion** | Founder: father's stroke, two lapsed prescriptions, nine years in logistics ("a supply-chain problem with love in it"). Aunt: retired nurse, clinical reviewer. Social worker: hands out cards unprompted. | All three point at the post-discharge medication scramble. | Enterprise sales. Nothing in the dossier suggests the founder wants to run an HR-benefits business. |

**Denominator:** revenue per care circle active at day 90 `[ASSUMPTION: hypothesis, untested]`.

**Tests the candidate passes:**
- *Does it explain past wins?* Yes. It explains the social worker referrals ("ask for it by name"), the founder's family using it daily, the excitement about refill sync, and the "fewer phone calls, not another app" insight.
- *Does it rule things out?* Yes. It rules out the employer pivot, native Android, the concierge, and new features that don't prevent a lapse or a call.
- *Is it uncomfortable to commit to?* Yes. It turns down Graham's money for now and demotes the feature users said they'd "pay anything" for from the foundation to an accelerator.

**What would confirm it (by the 90-day re-check):**
1. Discharge-referred circles retain to week 8 at a meaningfully higher rate than newsletter, forum or friend circles.
2. The discharge channel works at a second unit or hospital with no founder present at the desk.
3. At least some circles pay at day 30 or later on computed refill reminders alone, with no live pharmacy data.

If all three fail, the intersection isn't real and the run loops back to Gate 4.

## 3. The flywheel

```
   ┌──────────────────────────────────────────────────────────┐
   │                                                          ▼
 6. More discharge                                 1. Family gets a Tessel card
    teams refer                                       at discharge (+ newsletter
    (proof + kit)                                     readers start circles)
   ▲                                                          │
   │                                                          ▼
 5. Stories & "zero lapses"                       2. Primary caregiver sets up circle
    proof → newsletter,                              in week 1; family joins by
    social-worker kit                                SMS/web, no install needed
   ▲                                                          │
   │                                                          ▼
 4. Circle still active at day 90  ◄──────────  3. Right-time reminders: refill due,
    → caregiver pays per circle                    ready, who's covering → no lapses,
    (THE DENOMINATOR)                              fewer phone calls
```

**Weakest link:** 2 → 3 → 4, activation and retention. Only 17% of circles are weekly active (7 of 41), and only 7% pay (3 of 41). Every other link has at least one real data point behind it: the card at discharge, the newsletter's open rate, families asking by name.

**Current push (next one or two turns):**
1. Make link 3 work with no pharmacy data. Compute refill due dates from fill date, quantity and dose, let the caregiver mark refills as requested, ready and picked up, and send SMS to family members who don't have the app.
2. Make link 1 repeatable. Turn the one social worker's habit into a kit that a second and third discharge team can use.

**Doom-loop check:** **warning signs are present.** Question 7 of the application plus Graham's pitch lists four directions at once: chain integration, Android, a hire, and an employer pivot. Two of those are "big program to jump-start momentum" moves: an enterprise pilot that requires a staffed concierge, and a hire paid for out of runway. There is also one case of reaction without understanding: an interview quote ("I'd pay anything") is driving the roadmap while actual conversion is 3 of 41 circles. None of these has been acted on yet, and this plan is designed to keep it that way.

## 4. The bus

| Person / commitment | Current seat | Call | Note |
|---|---|---|---|
| Founder | Everything: code, design decisions, data loading, newsletter, sales, support, plus 10 h/wk contract work and their own caregiving | **Keep, but change seats** | Off: hand-loading pharmacy data. On: retention, the discharge channel, the newsletter. The founder is also a caregiver, so burnout is a structural risk, not a personality flaw. |
| UX designer friend (weekends) | Ad hoc help | **Keep; give a defined seat** | Owns first-week onboarding and the discharge-card-to-circle flow. |
| Aunt (retired nurse) | Clinical review | **Keep; formalize** | Owns sign-off on the days'-supply and refill-due logic and any clinical wording. Veto power on clinical matters. `[ASSUMPTION: willing]` |
| Stroke-unit social worker | Hands out cards | **Keep; move to champion / design partner** | Co-design the discharge kit, then ask for introductions to two or three peers. |
| Family-owned pharmacy's pharmacist | Emails a weekly refill export | **Keep the relationship; stop the export flow pending counsel** | A valuable design partner, but see brutal fact #5. |
| Graham Fairley | Pushing the strategy toward employers | **Move seat: advisor on a future channel** | His view is credible, so keep him close, with a written trigger for revisiting (see Risk Register). He should not set direction now. |
| HR head (manufacturer, ~1,800 employees) | Conditional pilot "next spring" | **Wrong seat now** | Reply with one low-build offer: sponsored family codes, with no SSO, dashboard or concierge. If they insist on all four conditions, decline warmly and keep the door open. |
| Founder's family (brother, aunt, father) | Daily users | **Keep, but exclude from metrics** | They are the best test circle and the worst evidence of traction. |
| Contract analytics work (10 h/wk, $1,900/mo) | Runway support | **Keep** | It roughly doubles runway. Don't drop it to "go all in" before retention is proven. |
| Planned part-time developer (for Android) | Not yet hired | **Off (for now)** | When in doubt, don't hire. At an assumed ~$3,000/mo `[ASSUMPTION]`, runway falls from ~17 to ~8 months, spent on parity work. |
| **Missing:** technical co-builder | — | **Missing** | Fill only after the week-8 retention signal. Scope it to the flywheel, not to Android. |
| **Missing:** privacy / health-data counsel | — | **Missing (urgent)** | The lawyer who drafted the privacy policy may be able to cover this. |
| **Missing:** 2–5 more discharge champions | — | **Missing** | This is the channel's repeatability test. |

## 5. Stop-doing list

1. **Stop building the employer checklist** (SSO, admin dashboard, anonymized reporting, staffed concierge). A human concierge is a staffing business, and a solo founder can't run one.
2. **Stop planning native Android now.** About a third of the waitlist is on Android, but family members don't need an app to receive "Dad's refill is due Thursday, can you pick it up?" Use SMS and a web link.
3. **Stop letting pharmacy data access gate the roadmap.** Refill *due* can be computed. Refill *ready* can come from the caregiver tapping a status or forwarding the pharmacy's own "ready" text. The aggregator becomes an accelerator, not a dependency.
4. **Stop hand-loading the Monday export** until counsel confirms the data flow is permitted. Then replace it with something that doesn't need the founder.
5. **Stop reporting accounts (318) as traction.** Report circles active at weeks 4 and 8, excluding the founder's family and friendly cohorts, and report paying circles.
6. **Stop adding features that don't prevent a lapse or a phone call.** Every build ticket answers one question: which call does this remove?
7. **Stop treating friendly-cohort enthusiasm as demand.** Support-group friends and former colleagues are great testers. They are not market evidence.
8. **Stop pricing per person** `[ASSUMPTION: current pricing basis unclear]`. Price per circle, and test a higher price on new circles.

## 6. Brutal facts and the faith statement

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | Families stop using it. | 41 circles → 7 weekly active (17%). One is likely the founder's own family, leaving about 6 external `[ASSUMPTION]`. | **Critical** | Founder |
| 2 | Willingness to pay is unproven. | 3 subscribers at $6.99, about $21/mo, against "I'd pay anything". No subscriber has yet reached 90 days, because the paid tier is 6 weeks old. | **Critical** | Founder |
| 3 | At this price, a solo founder needs hundreds of paying circles to survive. | Net burn is $4,300 − $1,900 = $2,400/mo. At ~$5.94 net per subscriber after an assumed 15% store fee `[ASSUMPTION]`, covering net burn takes ~404 paying circles and covering full costs takes ~724. | High | Founder |
| 4 | The most-wanted feature doesn't exist at scale. | Refill sync covers one pharmacy through a weekly manual export, so "ready" status can be up to 7 days stale. Chain access has been "under review" since August, and Tessel has no control over the outcome. | High | Founder |
| 5 | The pharmacy export may create legal exposure. | A pharmacy emailing prescription data to an app developer probably needs patient authorization or a formal agreement. Consumer health apps may also face breach-notification and state health-privacy rules. `[ASSUMPTION: needs counsel; this is not legal advice]` If it's wrong, it could also sink the aggregator application. | High | Founder + counsel |
| 6 | The founder is the whole bus. | Every seat, plus contract work, plus the Sunday newsletter, plus caregiving for their own father. | High | Founder |
| 7 | The evidence comes from friendly sources. | First users came from a support group and former colleagues. 26 interviews stated preferences rather than showing behavior. | Medium | Founder |
| 8 | A circle is only as connected as its least-connected member. | About a third of the waitlist is on Android. An Android sibling can't join an iOS-only circle today. | Medium | Founder + UX friend |
| 9 | The category is crowded, and users say they don't want another app. | Family coordination and medication-reminder apps already exist `[ASSUMPTION: not researched in this session]`. The founder's own learning: "Caregivers don't want another app." | Medium | Founder |
| 10 | The employer pivot is tempting because the consumer numbers are weak. | One 1,800-person employer at $3–5 PEPM comes to $5,400–$9,000/mo if billed across all employees `[ASSUMPTION about pricing basis]`, versus $21/mo today. That gap is exactly why the decision needs a trigger rather than a mood. | Medium | Founder + Graham |

**Truth climate:** the founder works alone, so nobody pushes back. The founding story is moving and award-winning, and that is the charisma risk here: the story can run ahead of the numbers, in the founder's own head as much as with funders. **Red-flag mechanism:** a weekly dashboard of circles active at weeks 4 and 8 by source, with the founder's family and friendly cohorts excluded. Any circle that goes quiet for 14 days gets a blameless "what happened?" call.

**Faith statement:** *Families will always need someone to make sure Dad's pills don't run out, and Tessel has the founder who lived it, a channel that puts it in families' hands at the exact moment of need, and 2,140 caregivers who open its letter every Sunday.*

## 7. Core ideology and the BHAG

**Core purpose:** no family should have to hold a parent's care together with a group chat, a whiteboard and panicked phone calls.

**Core values:**
1. Fewer phone calls, not more screens.
2. The exhausted primary caregiver comes first.
3. Never guess about anything clinical. A nurse checks it.
4. A family's health data is held in trust.

**BHAG (10–20 years):** *Tessel is in the discharge packet at most US hospitals* `[ASSUMPTION: US market]`*, and families who use it essentially never have a preventable medication lapse.*

## 8. Scorecard

All targets are `[ASSUMPTION]`, to be reset at the 90-day re-check once real baselines exist.

| Output | Current | 12-month target | BHAG trajectory |
|---|---|---|---|
| **Circles active at week 8** (external only) | Unknown. Proxy: ~6 weekly active external circles | 150 | Tens of thousands of families per year, the default after discharge |
| **Paying circles retained past day 90** | 0 eligible yet (3 paying, tier is 6 weeks old) | 400, which covers net burn | Self-funding growth, with an employer channel optional rather than required |
| **Active discharge referral sources** (units or hospitals referring monthly) | 1 | 10 | Most US discharge teams |

Track one supporting number alongside these: refill lapses reported per active circle. It should trend toward zero.

## 9. Next 90 days

| # | Action | Owner | Flywheel link |
|---|---|---|---|
| 1 | **This week:** rewrite application questions 7 and 11. The biggest risk is retention and willingness to pay, not pharmacy access. The funds go to the discharge channel, computed refill reminders and SMS participation, not Android or enterprise. Show the honest funnel. | Founder | Whole loop |
| 2 | **Weeks 1–6:** ship "refill due without the pharmacy": days' supply computed from fill date and quantity, a requested/ready/picked-up status, and SMS and web participation for family members without the app. Try reading the fill date and quantity from the pill-bottle photos families already take. | Founder (build), UX friend (flow), aunt (clinical sign-off) | 2 → 3 |
| 3 | **Weeks 1–4:** have counsel review the pharmacy export and Tessel's health-data obligations. Pause the hand-loading until the flow is confirmed as permitted. | Founder + privacy lawyer | Protects 3 and the aggregator path |
| 4 | **Weeks 2–12:** turn the discharge card into a kit (card with QR, a one-page script for social workers, first-week onboarding) and get it into 2–3 more units through the social worker's peers. Tag every circle by source. | Founder + social worker | 6 → 1 |
| 5 | **Weekly, ongoing:** retention dashboard by source, a call to every quiet circle, and a test of per-circle pricing at a higher price point on new circles. Add one newsletter call to action per issue ("set up a circle before the next appointment"). Reply to the HR head with the sponsored-codes offer. | Founder | 4 → 5 |

## 10. Re-check

**Offer:** set up a scheduled task for about 90 days out (late February). It would:
- re-score the scorecard with real numbers;
- re-run Gate 1 (is it now good?), Gate 5 (did the three confirmation tests pass?) and Gate 8 (has activation and retention stopped being the weakest link?).

This session has no tools, so the task can't be created here. Without the re-check, nobody finds out whether these verdicts were right.

## 11. Risk register

| Source | Risk / open condition | What turns it into a PASS, or the early warning sign |
|---|---|---|
| Gate 1 (CONDITIONAL) | "Good" rests on the newsletter and a handful of circles. Product retention is unproven. | ≥20 external circles active at week 8, with paying circles retained past day 30. |
| Gate 3 (CONDITIONAL) | The founder fills every seat. Counsel and co-builder seats are empty. | Counsel engaged; manual data loading off the founder; a scoped co-builder lined up once the retention signal arrives. |
| Gate 5 (CONDITIONAL) | The engine circle is unproven: 3 subscribers, no day-90 data. | Discharge-referred circles out-retain other sources; a second hospital refers without the founder present. |
| Gate 8 (CONDITIONAL) | The loop closes on paper, but links 2→3→4 have almost no evidence. | Week-8 retention by source trends up across two consecutive monthly cohorts. |
| Employer pivot | Pivoting early turns Tessel into a services and enterprise business run by one person. | **Revisit trigger:** about 100 paying day-90 circles, *or* an employer willing to pay for sponsored codes with no concierge or SSO build. |
| Runway | ~17 months at $2,400/mo net burn, and ~8 months if a developer is hired early. | Warning sign: any hire before the week-8 retention signal. |
| Decline 1: Hubris | The prize, an accelerator acceptance and "asked for by name" get mistaken for traction. | Warning: pitch decks lead with the story, not week-8 retention. |
| Decline 2: Undisciplined more | Android, enterprise, chain integration and concierge pursued at once. | Warning: more than two major build tracks open, or tickets with no "phone call removed" rationale. |
| Decline 3: Denial of risk | Pharmacy access stays "the" risk while retention and compliance are ignored. | Warning: the retention dashboard goes unreviewed for 2 weeks, or quiet circles go uncalled. |
| Decline 4: Grasping for salvation | At ~6 months of runway, a jump into a concierge-heavy enterprise pilot or a big hire. | Warning: a decision justified by "this will fix everything." |
| Decline 5: Capitulation | A founder who is also a caregiver burns out and returns to full-time analytics. | Warning: a skipped Sunday newsletter, or contract hours creeping above 10 a week. |

## 12. Gate log

| Gate | Verdict | One line |
|---|---|---|
| 0 Fit | PASS | Ongoing product with a steward, resources, a multi-year horizon and measurable outcomes. |
| 1 Baseline | CONDITIONAL | Working core and two real assets. Retention and payment unproven. |
| 2 Level 5 Leadership | PASS | Ambition is clearly for the cause. Gap: looks out the window (pharmacy access) rather than in the mirror (retention). |
| 3 First Who | CONDITIONAL | No misaligned person in a key seat, but the founder is the whole bus and key seats are missing. |
| 4 Brutal Facts | PASS | Facts surfaced. They reinforce Gate 1's condition rather than contradicting it. |
| 5 Hedgehog | CONDITIONAL | Plausible intersection at post-discharge medication logistics. Engine untested. |
| 6 Discipline | PASS | Eight-item stop-doing list and a clear framework. |
| 7 Technology | PASS | Pharmacy API demoted to accelerator. Computed refills and SMS promoted. |
| 8 Flywheel | CONDITIONAL | The loop closes. The activation-to-retention link is unproven. |
| 9 Built to Last | PASS | Ideology and BHAG drafted. Mechanisms designed but not yet built. |
| 10 How the Mighty Fall | PASS | All five stages mapped, with warning signs. |

**Count:** 7 PASS, 4 CONDITIONAL, 0 FAIL. That is fewer than half CONDITIONAL, but all four share two root problems: **(1) no evidence yet that families outside the founder's circle keep using Tessel and pay for it, and (2) the founder is the only person on the bus.**

---

## Appendix: gate workings

**Gate 0, subject card.**
- **Name:** Tessel, including the app, *The Caregiver's Ledger* and the discharge-card channel.
- **Type:** product/app (consumer mobile).
- **Steward:** the solo founder.
- **Horizon:** years.
- **Stage:** 14 months building, 4 months live, applying to a pre-seed accelerator.

**Gate 1, baseline sheet.**

*Evidence of good:*
- Live iOS app, 4.9 stars from 11 ratings.
- Used daily by the founder's family.
- Funnel: 2,140 newsletter subscribers (52% open rate) → 318 accounts → 41 circles → 7 weekly active → 3 paid.
- Unprompted referral at discharge, with families asking for it by name.
- $10k pitch-competition prize.
- Basic security review and a privacy policy already done.

*Definition of great:*
1. **Superior performance:** circles retain well past day 90, with near-zero medication lapses.
2. **Distinctive impact:** discharge teams and families would feel the hole if it disappeared.
3. **Endurance:** it runs without the founder loading data or carrying the channel personally.

*Scorecard outputs:* see section 8.

**Gate 2, leadership read.**
- *Strengths:* resolve (taught themselves Swift, put in $38k of savings). Credits others (colleagues "incredibly generous", the aunt, the social worker). Ambition aimed at the cause, not status.
- *Gap:* frames the biggest risk as external ("everything else I can build"). Nothing would survive the founder's absence yet.
- *One behavior change:* open every weekly review with the retention number, before anything about pharmacy access.

**Gate 6, framework.**
- *Boundary:* build only what removes a lapse or a phone call for the primary caregiver, starting at discharge.
- *Freedom inside it:* the UX friend owns onboarding design; the aunt holds the clinical veto.
- *Non-negotiables:* the Sunday newsletter (this fanatical consistency already exists), a weekly retention review, a day-7 check-in with every new circle, clinical sign-off before anything clinical ships, and no health data outside a flow counsel has approved.
- *Bureaucracy check:* there is almost no bureaucracy. The Monday export is a crutch standing in for missing data access, not a rule.

**Gate 7, tech triage.**

| Technology | Class | Note |
|---|---|---|
| Push reminders | Accelerates | Core of "the app disappears into a reminder." |
| Computed refill-due (days' supply) | Accelerates | **Build now.** Removes the dependency on pharmacy data. |
| SMS / web participation for family | Accelerates | Covers Android and "no another app." |
| Pill-bottle photo → fill date and quantity | Accelerates (**pioneer**) | Uses behavior families already show. Must be caregiver-confirmed and nurse-reviewed. |
| Discharge-list photo → pre-filled circle | Accelerates (**pioneer**) | Makes week-one setup nearly effortless. |
| Pharmacy aggregator API | Accelerates *later* | Take it if access arrives. Don't wait for it. |
| Shared calendar, photo notes | Parity | Keep; don't extend. |
| Native Android | Parity, later | Revisit after the retention signal. |
| Manual weekly email export | Drop | Doesn't scale; compliance question. |
| SSO, admin dashboard, anonymized reporting | Irrelevant now | Flag: adoption driven by fear of "leaving money on the table." |
| Human concierge chat | Irrelevant | A services business, not technology. |

**Gate 9, mechanisms (clocks, not time-telling).**
- Computed refill logic that needs no founder input.
- A source-tagged retention dashboard.
- A clinical-review checklist owned by the aunt.
- A discharge kit that social workers use without the founder.
- A newsletter backlog and a guest-contributor pipeline.
- A written first-week onboarding playbook.