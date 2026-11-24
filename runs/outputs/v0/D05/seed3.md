# Tessel: Good to Great

## Verdict

**Overall:** Tessel is *early-good*, not yet good. It has a real founder insight, a working iOS app, a strong newsletter and one promising referral channel. All of that sits on a core promise that almost none of its users actually receive. The way forward is to narrow to one promise. It is not more features, and it is not a pivot.

**Hedgehog Concept (working hypothesis):** *Tessel makes sure a family caring for an aging parent at home never runs out of a medication, starting the day that parent comes home from the hospital.*

**Weakest flywheel link: account → circle → retained circle.**
- Only 41 of 318 accounts formed a care circle (13%).
- Only 7 of those 41 circles are weekly active (17%).
- The likely cause is twofold. "Never run out" works only for customers of one pharmacy. And a circle breaks when a sibling uses Android. `[ASSUMPTION]`

**Top three stop-doing items:**
1. **Stop waiting on the pharmacy-data aggregator.** Don't treat chain-pharmacy API access as the gate for refill sync. Ship a version that works with any pharmacy now.
2. **Stop building toward the employer pilot spec.** That means no staffed care concierge, no SSO and no admin dashboard.
3. **Freeze general care-coordination features.** If a feature doesn't keep meds stocked or cut phone calls, it waits.

**Most urgent brutal fact:** The feature users say they'd "pay anything" for runs for exactly one pharmacy, on a Monday email you load by hand. Access to every other pharmacy has sat "under review" with a third party since August. The risk you named as your biggest is one you can't act on, so the plan has to stop depending on it.

**Missing numbers that would change this answer:**
1. How many of the 41 circles were still active at week 8, and whether the 7 active circles are the ones with refill sync.
2. How many circle invites went unaccepted because the invitee uses Android.
3. Whether the 1,800-employee manufacturer would *pay* for a pilot of the existing app without a concierge.
4. How many discharge cards were handed out, and how many circles they produced.

**This week (application deadline):** rewrite application answers 7 and 11 around this plan. Draft text is in §9.

Greatness potential: 12/100

---

**How this run was done.** This was run in autonomous mode. No memory, past chats or web search were available, so there is:
- no prior run to use as a baseline,
- no competitor or market research,
- no check on the pharmacy-data landscape.

The founder's accelerator application is the only evidence. Every inference is marked `[ASSUMPTION]`. The vocabulary is the **product / app** column: leader = founder/product owner; engine = revenue or retention per X; great = category-defining, durable usage.

---

## 1. The great version in one paragraph

Five years out, Tessel is the card a hospital social worker hands a family at discharge, and the reason that family's parent never misses a dose for lack of pills.

The primary caregiver, usually one exhausted daughter, photographs the pill bottles once. From then on Tessel knows:
- what's on hand,
- when each refill is due,
- which sibling is picking it up,
- and, wherever data exists, whether it's ready.

Siblings don't need the app; they get a text at the right moment. Most weeks the family barely opens Tessel, and that's the point: fewer phone calls and no Sunday-night surprises.

It's paid for by whoever values that continuity most: families, employers, or the hospitals sending patients home. It runs on automated data pipelines and a small team, not on the founder loading a spreadsheet every Monday. It isn't the biggest caregiving app. It's the one that never lets the pills run out.

## 2. The Hedgehog Concept

**Sentence (working hypothesis):** *Tessel makes sure a family caring for an aging parent at home never runs out of a medication, starting the day that parent comes home from the hospital.*

| Circle | Candidates considered | What survives | What it is *not* best at |
|---|---|---|---|
| **Best in world** | (a) All-in-one care coordination; (b) medication continuity across a family circle; (c) caregiver content and community; (d) employer caregiving benefit; (e) the post-discharge handoff | **(b) + (e):** medication *supply* continuity (on hand, due, who's picking up, ready) across several family members, from discharge onward. This is a logistics problem, and the founder spent nine years as a logistics analyst and lived through two lapses. | General calendars and care journals (a crowded space, so parity at best `[ASSUMPTION: no competitor scan done]`); human care navigation; enterprise HR software; clinical advice. The newsletter is a distribution engine, not the product core. |
| **Economic / resource engine** | Consumer subscription per circle ($6.99); employer per-employee-per-month (Graham's $3–5); hospital or discharge partnership; newsletter sponsorship | **Gross margin per retained care circle** (active at 90 days). *Who pays is still open.* | Revenue that doesn't come from a retained circle: one-off sponsorships, or pilots that require services Tessel doesn't offer. |
| **Passion** | Founder: the exhausted primary caregiver; the lapsed prescriptions. Aunt: clinical safety. Social worker: families at discharge. Brother: daily user. | **Taking the logistics weight off the one person carrying it.** | Building software for its own sake, or enterprise sales for its own sake. |

**Why the denominator is the retained circle, not the account.** Value is created per family-per-parent, and it only exists once the family has stuck with it. 318 accounts produced 7 units of real value. Counting accounts hides that.

**Tests:**
- **Does it explain past wins?** Yes:
  - refill sync gets the most excitement in interviews;
  - the lapses are the founding story;
  - the social worker's discharge card is the strongest pull signal;
  - "caregivers want fewer phone calls, not another app" points at reminders and supply, not more screens.
- **Does it rule things out?** Yes: the concierge, enterprise features, new journal and calendar features, and generic "caregiving platform" ambitions.
- **Is it uncomfortable?** Yes:
  - It demotes half the current app to supporting cast.
  - It turns down the most tangible revenue conversation, the employer pilot, as currently specified.
  - It makes pharmacy access a design problem you own rather than a permission you await.

**Evidence that would confirm it (90-day tests):**
1. Circles using the pharmacy-independent refill countdown retain at **at least 2×** the rate of circles that don't.
2. At least 10 circles form from discharge referrals, and they retain better than newsletter-sourced circles.
3. Some payer, whether a family at a higher tier, an employer or a hospital, pays for "never run out" *without* a concierge attached.

If none of these hold, the passion and the insight are real, but this is not the hedgehog. Revisit Gate 5.

## 3. The flywheel

```
        ┌──────────────────────────────────────────────────────────┐
        ▼                                                          │
 1. A family arrives at the moment of need                         │
    (discharge card from a social worker; Sunday newsletter)       │
        │                                                          │
        ▼                                                          │
 2. The primary caregiver sets up meds in minutes (bottle photos)  │
    and pulls in siblings, with or without the app (SMS)           │
        │                                                          │
        ▼                                                          │
 3. Tessel keeps every med stocked: countdown, who's picking up,   │
    ready status from any source                                   │
        │                                                          │
        ▼                                                          │
 4. No lapses and fewer calls, so the circle stays active          │
    ══ RETAINED CARE CIRCLE (the denominator) ══                   │
        │                                                          │
        ▼                                                          │
 5. Someone pays per retained circle (family / employer / hospital)│
    and Tessel gathers outcome data and family stories             │
        │                                                          │
        ▼                                                          │
 6. Proof and stories feed the newsletter and give social workers  │
    and pharmacists a reason to refer ─────────────────────────────┘
```

**Weakest links:**
- **2→4:** 13% of accounts form a circle, and 17% of circles stay weekly active.
- **3:** the core promise is undelivered outside one pharmacy.
- **5:** the payer is unproven, with 3 subscribers bringing in about $21/month.

**Current push (the next two turns):**
1. **Make step 3 real for every pharmacy.** Ship a refill countdown that needs no pharmacy data:
   - fill date and quantity from a bottle photo, giving days of supply;
   - a named pickup person;
   - a "ready" tap, or a forwarded pharmacy text or email.

   Families already photograph pill bottles in Tessel, so this formalizes behavior that exists. The aggregator API becomes an upgrade, not a prerequisite.
2. **Unblock step 2 for mixed-phone families.** Let a sibling join a circle by SMS or web link before committing to a native Android build.

**Doom-loop check:**

| Doom-loop sign | Present? | Evidence |
|---|---|---|
| Waiting for a big event to jump-start momentum | **Yes** | Aggregator approval, accelerator money, an employer pilot "next spring": three external rescues and no internal push. |
| New direction after new direction | **Emerging** | The accelerator plan has three unconnected uses of money, plus a possible B2B pivot. |
| Reacting without understanding | **Watch** | "Possibly hire a part-time developer" with no stated bottleneck. The Android need is real but undiagnosed. |
| Inconsistency | **No** | The Sunday newsletter and daily family use are strongly consistent. |

## 4. The bus

| Person / commitment | Call | Seat in the great version | Note |
|---|---|---|---|
| **Founder** | Keep | Product owner, builder, voice of *The Caregiver's Ledger* | Also a caregiver: watch capacity (see §11). |
| **Aunt (retired nurse)** | Keep, **formalize the seat** | Clinical safety owner: signs off every medication-related release | Medication reminders carry harm potential. A volunteer reviewer should become a named role with a checklist. |
| **UX designer friend (weekends)** | Keep, **move seat** | From general design to the *biggest leak*: setup, invites and first-week activation | Put the best people on the biggest opportunity. |
| **Stroke-unit social worker** | Keep, **formalize** | First channel partner: trackable cards, plus introductions to peers | Families "ask for it by name." This is the strongest pull signal in the dossier. |
| **Independent pharmacist** | Keep, **expand seat** | Design partner for pharmacy workflow; introductions to nearby independent pharmacies | The only working refill data source today. |
| **Brother (daily user)** | Keep | Design partner; test circle for every release | |
| **Graham Fairley** | **Move seat** | From direction-setter to advisor on the *payer test* | See the note below the table. |
| **Contract analytics work (10 hrs/week, $1,900/month)** | Keep | Runway extender | Cuts burn from $4,300 to about $2,400/month, giving roughly 17 months of runway. Dropping it for speed is not worth it yet. |
| **Manual Monday refill load** | **Off** (as a manual task) | Replace with an automated import | It is a single point of failure that depends on the founder. |
| **Missing: Android / cross-platform developer** | Missing, **hire only after the SMS test** | Scoped contract, not open-ended "part-time help" | Hiring at an assumed ~$3k/month `[ASSUMPTION]` takes runway from about 17 to about 7.6 months. When in doubt, don't hire. |
| **Missing: pharmacy-data advisor** | Missing | Someone who knows how aggregators and pharmacy integrations actually get approved `[ASSUMPTION: such people are reachable via the pitch-competition or accelerator network]` | |
| **Missing: privacy / health-compliance advisor** | Missing before any employer or hospital deal | | Obligations may change when a business customer is involved `[ASSUMPTION; confirm with counsel]`. |
| **Missing: a second core person** | Missing (long-term) | Co-founder or first employee who could run the product without you | Endurance test (Gate 9). |

**Note on Graham.** He's probably right about the engine. Consumer willingness to pay looks weak, and his own figures work out to roughly $15–25 per caregiving employee per month: $3–5 per employee, with 1 in 5 employees caregiving. That is 2–3.5× the consumer price. But the pilot spec he relayed describes a different company: a staffed concierge plus enterprise software, for one conditional pilot. Use his network to test whether an employer will pay for *the core*. Don't let the spec drive the roadmap. His incentive and any compensation expectation are unknown `[ASSUMPTION]`; clarify both.

## 5. Stop-doing list

1. **Stop waiting on the aggregator.** Escalate once with a specific ask, then build as if it never comes.
2. **Stop building toward the employer pilot spec.** No concierge, SSO, admin dashboard or anonymized reporting suite. Answer the HR head with a slim, paid offer or a clear "not yet."
3. **Stop adding general coordination features.** Nothing new in the care log, calendar or photo notes unless it serves refill continuity or cuts calls.
4. **Stop leading with "318 accounts."** Report weekly active circles, circle formation rate and missed refills. Lead the application with the newsletter and the discharge channel, which are the honest strengths.
5. **Stop asking for single sign-ups.** Change every call to action, from the newsletter, the forum and the card, from "download Tessel" to "set up Mom's meds with your brother."
6. **Stop the open-ended "possibly hire."** Hire only against a diagnosed bottleneck, with a scope and an end date.
7. **Stop adding pharmacies by hand.** Automate the Monday import before taking on pharmacy number two.

## 6. Brutal facts and the faith statement

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | The most-wanted feature exists for one pharmacy, by a manual weekly email. The path to chains is gated by a third party that hasn't answered since August. | Application Q3, Q11 | **Critical** | Founder |
| 2 | The product mostly isn't used: 2.2% of accounts are in a weekly-active circle. | 318 → 41 → 7 | **Critical** | Founder |
| 3 | Willingness to pay is unproven. "I'd pay anything" is a stated preference, and those users mostly can't get refill sync. | 3 subscribers, about $21/month after six weeks | **High** | Founder |
| 4 | iOS-only probably breaks circles. If a third of family members use Android, only about 30% of three-person circles are all-iOS. | About a third of the waitlist is on Android; independence of phone choice is `[ASSUMPTION]` | **High** | Founder + future developer |
| 5 | Bus factor of one. The refill pipeline, releases and newsletter all run through one person who is also a caregiver. | Q10, Q3 | **High** | Founder |
| 6 | The accelerator plan has no answer if access never comes. Its first use of funds is contingent on a gatekeeper. | Q7 | **High** | Founder |
| 7 | The employer pivot as specified requires a staffed service business and enterprise software for one *conditional* pilot that is months away. | Q8 | Medium (as a distraction) | Founder + Graham |
| 8 | Early traction is network-assisted: the support group and former colleagues. Organic pull is unmeasured. | Q5 | Medium | Founder |
| 9 | Medication features carry safety and liability exposure. Clinical review is a volunteer. | Q10 | Medium | Aunt + founder |
| 10 | 4.9 stars is 11 ratings. | Q3 | Low | — |
| 11 | The competitive landscape is unexamined in this run. | No search available | Unknown | Founder (desk research in week 1) |

**Truth climate.** You are the truth climate, so the red-flag mechanism is a weekly dashboard you can't ignore: circles, retention, missed refills. The risk isn't charisma suppressing bad news. It's *kindness*: a support group, generous ex-colleagues, a prize and a loyal social worker form a warm cushion of encouraging feedback. Excitement in interviews isn't usage.

**Faith statement:** *Families will always need the pills not to run out. A logistics analyst who lived through two lapses is better placed than almost anyone to make that boringly reliable, and to get there without waiting for anyone's permission.*

## 7. Core ideology and BHAG

**Core values:**
1. **Never let it run out.** Reliability beats features.
2. **Fewer calls, not more screens.** Respect the caregiver's time; the best interaction is a well-timed text.
3. **Clinically careful.** Every medication feature is nurse-reviewed, and Tessel never gives medical advice.
4. **The parent's dignity and data come first.**
5. **Built with caregivers, not for them.**

**Core purpose:** *So families can care for the people who raised them without the logistics breaking them.*

**BHAG (20-year horizon, aspirational):** *A million families caring for a parent at home through Tessel, and among them, running out of a medication is practically unheard of. A Tessel card goes home with every family discharged to care for a parent.* `[ASSUMPTION: US market]`

## 8. Scorecard

| Output | Current | 12-month target | BHAG trajectory |
|---|---|---|---|
| **Weekly active care circles** | 7 | 100 `[ASSUMPTION]` | Roughly 1,000 by year 3, compounding through discharge and pharmacy channels toward 1M families |
| **Refill continuity:** % of tracked refills collected before supply runs out, across active circles | Not measured | Measured in every active circle; ≥97% `[ASSUMPTION]` | ~100%: "never" |
| **Paying circles (any payer) and proven payer** | 3 consumer subscribers (~$21/month); payer unknown | 40 paying circles, plus one completed paid partner test with an employer or discharge site | Revenue per retained circle covers the cost to serve and acquire it |

**Diagnostic, not scorecard:** the week-8 cohort retention of circles. This is the number that turns Gate 1 into a PASS.

## 9. Next 90 days

| # | Action | Owner | Pushes flywheel step | Done when |
|---|---|---|---|---|
| 0 | **This week:** rewrite application answers 7 and 11 (draft below). | Founder | All | Submitted |
| 1 | Ship a **pharmacy-independent refill countdown**: bottle photo gives fill date, quantity and days of supply; a named pickup person; a "ready" tap or forwarded pharmacy notice `[ASSUMPTION: feasibility of photo/notice capture]`. Escalate the aggregator once with a specific ask. | Founder; aunt (clinical sign-off); designer (flow) | 3 | Live by day 45; continuity tracked per circle |
| 2 | **App-optional siblings:** invite via SMS or web link. Measure circle completion before and after. Decide on a native Android build at day 90 based on that data. | Founder | 2 | Invite acceptance rate known; Android go/no-go made |
| 3 | **Make discharge a measured channel:** a unique link or code on the card; ask the social worker for two peer introductions; ask the pharmacist for two nearby independent pharmacies. Automate the Monday import first. | Founder + social worker + pharmacist | 1, 6 | ≥10 circles from discharge; import automated |
| 4 | **Run the payer test:** (a) offer families an annual "never run out" plan; (b) through Graham, offer the manufacturer a small *paid* pilot of the existing app with no concierge, or get a clear no. | Founder; Graham (advisor) | 5 | A yes or no from a real payer, with a price |
| 5 | **Instrument the truth:** a weekly dashboard of circle formation rate, week-8 retention, missed refills and source by channel. Report it in every update. | Founder | 4 | Gate 1 condition answered |

**Draft application text:**
- **Q7 (use of money):** "Make 'never run out' work for every family, with or without pharmacy APIs. Ship a refill countdown that works with any pharmacy, let non-iPhone siblings join by text, and turn our discharge-card channel into a repeatable pipeline. We'll hire an Android developer only if the text-invite data shows demand."
- **Q11 (biggest risk):** "Retention. Only 7 of 41 care circles are weekly active, and we think it's because refill sync works for one pharmacy and circles break across iPhone and Android. Both are fixable by us, and we have 90-day tests for each. Chain API access is an upgrade we're pursuing, not a dependency."

## 10. Re-check

This session has no tools, so I can't create the scheduled task myself. Here is the offer, made once: **set a re-check about 90 days from this run** to do three things:
- re-score the §8 scorecard with real numbers,
- re-run Gate 1 (did week-8 retention clear the bar?), Gate 5 (did any payer pay, and did countdown circles retain better?) and Gate 8 (did the loop turn?),
- log the verdict changes.

Without that loop, nobody learns whether these verdicts were right.

## 11. Risk register

**Open CONDITIONALs**

| Gate | Condition | Evidence that turns it into a PASS |
|---|---|---|
| 1 Baseline | "Good" is only in pockets (the newsletter, the founder's own circle, one referral channel). The app's core isn't yet proven good. | Week-8 circle retention ≥40% on recent cohorts, *or* ≥25 weekly active circles `[ASSUMPTION: thresholds]`. If retention is under ~15%, treat this run as a FAIL and do product-market-fit work first. |
| 5 Hedgehog | The economic circle is unproven: nobody has yet paid for "never run out" at scale. | One payer pays without a concierge attached; countdown circles retain ≥2× others. |
| 8 Flywheel | Step 5 (payment) doesn't yet close the loop. | Same as Gate 5. |
| 9 Built to Last | Bus factor of one; manual data pipeline. | Import automated and documented; a second person can ship a release. |

**Shared root causes:** two problems drive all four CONDITIONALs.
1. The core promise isn't delivered to most users.
2. Who pays is unknown.

Actions 1 and 4 in §9 attack them directly.

**Decline risks (Gate 10)**

| Stage | How Tessel could slide | Early warning sign |
|---|---|---|
| 1. Hubris | An accelerator acceptance, a prize or a viral post gets read as traction. | Updates cite accounts or awards, not active circles. |
| 2. Undisciplined pursuit of more | Building Android, enterprise features and a concierge at once. | Roadmap items that can't be traced to "never run out." |
| 3. Denial of risk | "Under review" treated as "coming soon"; missed-refill incidents and reminder bugs go unlogged. | No dated escalation; continuity isn't measured. |
| 4. Grasping for salvation | As runway shrinks, jumping to the employer pivot, a big hire or an "AI concierge." | A direction change within a quarter with no data behind it. |
| 5. Capitulation | Founder burnout: building, writing, contracting *and* caregiving. | The Sunday newsletter gets skipped; the weekly dashboard goes unreviewed. |

## 12. Gate log

| Gate | Verdict | One line |
|---|---|---|
| 0 Fit | PASS | Ongoing product, clear steward, multi-year horizon, measurable. |
| 1 Baseline | CONDITIONAL | Working core and real pull signals, but thin usage (7 active circles). |
| 2 Level 5 Leadership | PASS | Humble and resolute. Gap: the risk named is external, and the default answer is "build." |
| 3 First Who | PASS | No misaligned seats. Graham moves seat; four missing seats named. |
| 4 Brutal Facts | PASS | Facts confronted; consistent with the Gate 1 baseline. |
| 5 Hedgehog | CONDITIONAL | Strong best-at and passion; engine unproven. |
| 6 Discipline | PASS | Seven stop-doing items; the framework is set. |
| 7 Technology | PASS | API demoted to accelerator; SMS and photo capture are the pioneer bets. |
| 8 Flywheel | CONDITIONAL | Loop closes logically; the payment link is unproven. |
| 9 Built to Last | CONDITIONAL | Ideology set; bus factor of one. |
| 10 How the Mighty Fall | PASS | Five decline paths and their warning signs logged. |

**Count from the table:** 7 PASS, 4 CONDITIONAL, 0 FAIL across 11 gates. That is under half CONDITIONAL, and all four trace to the two root causes in §11.

---

## Appendix: gate artifacts not shown above

**Gate 0 – Subject card.**
- Name: Tessel.
- Type: product / app (solo-founder consumer mobile).
- Steward: the founder.
- Horizon: multi-year; about 17 months of personal runway at the current ~$2,400/month net burn.
- Stage: 14 months building; live on iOS for 4 months; paid tier 6 weeks old; applying to a pre-seed accelerator.

**Gate 1 – Baseline sheet.**

| Evidence of good | Figure |
|---|---|
| Daily use by the founder's own care circle | Yes |
| App Store rating | 4.9 (11 ratings) |
| Newsletter | 2,140 subscribers; ~52% open rate, about 1,100 opens per issue |
| Unprompted referral channel | Social worker at discharge; families ask by name |
| Competition prize | $10k |
| User interviews | 26 |

| Evidence of not-yet-good | Figure |
|---|---|
| Accounts that formed a circle | 13% |
| Circles weekly active | 17% |
| Paid subscribers | 3 (~$21/month) |
| Refill sync coverage | One pharmacy |

**Definition of great:**
- **Superior performance:** families using Tessel essentially never run out of a parent's medication.
- **Distinctive impact:** discharge teams and families would lose the one tool that keeps medication supply coordinated across siblings.
- **Lasting endurance:** it runs on automated data and a team, not one person's Mondays.

**Gate 2 – Leadership read.**
- **Strengths:**
  - Credits others freely: family, colleagues, the social worker.
  - Fierce resolve: $38k of savings invested, self-taught Swift, a newsletter every Sunday.
  - Ambition clearly aimed at the cause, not at status.
- **Gaps:**
  - The biggest risk named is outside your control ("everything else I can build"). That is a window-not-mirror pattern, and it frames non-build problems (activation, payer) as build problems.
  - Nothing survives your absence yet.
- **Behavior change:** every Monday, write one line naming the biggest risk *you* control and the metric that shows whether you moved it. As a self-audit: when retention is low, is your first question about the API or about the experience?

**Gate 7 – Tech triage.**

| Technology | Class | Note |
|---|---|---|
| Push reminders | **Accelerates** | The core of "disappear into a reminder." |
| Bottle-label photo capture to days of supply | **Accelerates (pioneer candidate)** | Builds on existing photo-note behavior `[ASSUMPTION: feasibility]` |
| SMS / web participation for non-app siblings | **Accelerates (pioneer candidate)** | Matches "caregivers don't want another app"; tests the Android blocker cheaply. |
| Parsing forwarded pharmacy "ready" notices | Accelerates | `[ASSUMPTION: notices are forwardable and consistent enough]` |
| Chain-pharmacy aggregator API | Accelerates *when available* | An upgrade, never a prerequisite. |
| Automated independent-pharmacy import | Accelerates | Replaces the manual Monday load. |
| Native Android app | Parity (required if the SMS test shows demand) | Decide at day 90. |
| Shared calendar, care log | Parity | Freeze. |
| SSO, admin dashboard, anonymized reporting | Irrelevant now | Revisit only with a paying employer. |
| "AI care concierge" | **Hype risk** | A tempting substitute for the human concierge request; it is outside the hedgehog. |

**Gate 6 – Framework and disciplines.**
- **Framework boundary:** anything that lowers the chance a family runs out, or cuts calls between siblings, is in. Everything else waits.
- **Freedom within it:**
  - The designer owns the activation flow.
  - The aunt holds a veto on clinical safety.
  - The social worker and pharmacist shape their own workflows.
- **Non-negotiables:**
  - the Sunday newsletter;
  - the Monday dashboard;
  - nurse sign-off on every medication release;
  - two calls a week with primary caregivers;
  - every feature traced to the hedgehog sentence.
- **Bureaucracy check:** there are no excess rules today. The risk runs the other way: an accelerator adding process before the core works.

**Gate 9 – Mechanisms (clock building).**
- Automated, documented refill import.
- A written release runbook.
- A clinical review checklist.
- A social-worker referral kit (cards, link, one-page explainer).
- A dashboard that reports itself.
- A newsletter with occasional guest caregiver voices, so the channel isn't one person's Sunday.

BHAG kept to one line, given the stage.