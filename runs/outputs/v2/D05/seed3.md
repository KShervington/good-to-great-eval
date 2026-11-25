# Tessel: Good to Great run

**Verdict: not yet good. The run stopped at Gate 1, a gentle FAIL.**

- **Hedgehog Concept:** none drafted. The core product hasn't yet worked without the founder, so there is nothing to narrow.
- **Weakest link:** refill sync. It's the feature users want most, and today it is one pharmacist's Monday email that the founder loads by hand. Almost no user can get it.
- **Pause:** (1) the employer build (SSO, admin dashboard, reporting, staffed concierge); (2) Android; (3) hiring a developer.
- **Most urgent brutal fact:** only 7 of 41 care circles are active weekly. One of those 7 is the founder's own family, and the earliest users came from his support group and former colleagues.
- **Numbers that would change this:** week-8 retention of circles that came from *outside* the founder's network (newsletter, forum, discharge cards), broken out by source.
- **Confidence:** medium-high on calling it "not yet good." The call rests entirely on the self-reported figures in the accelerator application.

`Greatness potential: 8/100`

---

## Why the run stopped here

The skill puts a subject in "not yet good" when its core doesn't yet work without the steward's personal effort, network or manual workarounds. Tessel meets all three conditions:

1. **Network.** The first users came from the founder's Wednesday support group and his old colleagues. The best-retained circle is his own family's.
2. **Manual workaround.** Refill sync, the feature with the strongest pull, depends on a weekly email export from one family-owned pharmacy, which the founder imports himself.
3. **Retention unproven outside the circle.** 7 of 41 circles (17%) are active weekly. The dossier doesn't say how many of the 7 came from strangers, and at most 6 can be someone other than the founder's family.

Running Gates 2–10 on this would mean writing a Hedgehog Concept and a flywheel on sand. What follows is the baseline, what "good" would look like, and the shortest path to proving it.

This is not a judgment on the founder or on the idea. He shipped a working iOS app by teaching himself Swift, built a newsletter with real reach, and found a discharge channel where families ask for Tessel by name. Those are real assets. They just aren't yet evidence that the *product* works on its own.

---

## Gate 0: Fit (PASS)

| Field | Value |
|---|---|
| **Name** | Tessel |
| **Type** | Product / app (consumer mobile, iOS), solo founder |
| **Steward** | The founder (former logistics analyst, 9 years) |
| **Supporting cast** | Aunt (retired nurse, clinical review), UX designer friend (weekends), discharge social worker (informal channel), Graham Fairley (prospective advisor, employer channel) |
| **Time horizon** | Multi-year. Caregiving for an aging parent typically lasts years `[ASSUMPTION]` |
| **Current stage** | Live 4 months; paid tier 6 weeks old; pre-seed accelerator application due this week |
| **Measurable?** | Yes: circles, weekly activity, paid subscriptions, refills tracked |

Tessel is an ongoing endeavor with a clear steward, rearrangeable resources and measurable outcomes, so the framework can work on it.

---

## Gate 1: Baseline (FAIL: not yet good)

### Evidence sheet

| Signal | Number | What it proves | What it doesn't prove |
|---|---|---|---|
| App shipped and rated | Live 4 months; 4.9★ from 11 ratings | The founder can build and ship; early users like it | 11 ratings is too few to mean anything about the market |
| Founder's family | Daily use | It solves the founder's own problem | n = 1, and the user is also the builder |
| **Newsletter** | **2,140 subscribers, 52% average open rate** | **The founder can earn caregivers' attention well beyond his own network. This is the strongest "good" signal in the dossier.** | That newsletter readers become retained app users |
| Discharge channel | A social worker hands out Tessel cards; families "ask for it by name" | There is pull at the moment of greatest need | Volume, conversion, or retention of these families (none reported) |
| Interviews | 26 | Real insight (e.g. "fewer phone calls," "one exhausted daughter") | Willingness to pay. "I'd pay anything" is a stated preference |
| Funnel | 318 accounts → 41 circles → 7 weekly active | Some circles stick | That the product retains strangers. Only ~13% of accounts formed a circle and ~2% of accounts are in a weekly active circle |
| Paid | 3 subscribers in 6 weeks at $6.99/month (~$21 MRR) | Someone pays | That anyone outside the network pays. Source unknown |
| Refill sync | 1 pharmacy, manual weekly import | Families light up when it works | That it works at all without the founder's hands |
| Prize | $10,000 | Judges liked the pitch | Anything about users |

### Where the funnel leaks

```
318 accounts ──(13%)──▶ 41 circles ──(17%)──▶ 7 weekly active ──▶ 3 paying
                                               └─ 1 of the 7 is the founder's family
```

The biggest leak is account to circle: 277 accounts never formed or joined a care circle. The dossier doesn't say whether these are people who browsed and left, or people who joined a circle someone else created. If it's the second, the leak is smaller than it looks. **This number is missing and matters.** `[ASSUMPTION: most of the 277 are non-converting sign-ups]`

### Draft definition of great (to revisit once Tessel is good)

1. **Superior performance.** Tessel families miss measurably fewer refills and doses, and make fewer coordination calls, than they did before Tessel.
2. **Distinctive impact.** Discharge planners and caregivers recommend it unprompted. If it vanished, families would fall back to group chats and lapsed prescriptions.
3. **Lasting endurance.** It works without the founder importing data, writing every recruitment message, or knowing the users personally.

### Candidate scorecard outputs

- **A. Weekly active circles from outside the founder's network, still active at week 8** (by source cohort)
- **B. Refills caught before running out**, per active circle per month (needs instrumentation)
- **C. Paying circles from outside the network**, with 3-month paid retention

---

## What "good" looks like: three milestones

Tessel is *good* when it does its core job for strangers, without the founder's hands in the loop, and some of those strangers pay. All thresholds below are `[ASSUMPTION]`, set as reasonable proof points for a pre-seed consumer health app. Adjust them if the accelerator or comparable apps suggest different bars.

| # | Milestone | Proof threshold `[ASSUMPTION]` | Current |
|---|---|---|---|
| **M1** | **Strangers stay** | ≥20 weekly active circles from non-network sources, and ≥35% of a month's new non-network circles still active at week 8 | Unknown; at most 6 |
| **M2** | **The core runs without the founder's hands** | The feature that keeps circles active is delivered entirely by software, with zero weekly manual data imports in the retention path. Two ways to get there: automated refill data from at least one source, *or* proof that log + reminders + predicted refill dates retain on their own | 0 automated sources; 1 manual |
| **M3** | **Strangers pay** | ≥15 paying circles from non-network sources, with ≥60% still paying after 3 months | 3 paying, source unknown |

When all three hold, re-run this skill from Gate 1. Gates 2–10 will then have real material to work on.

---

## Brutal facts found while baselining

This is not a full Gate 4. These are the facts that drove the Gate 1 call or that can't wait.

| Fact | Evidence | Severity | Owner |
|---|---|---|---|
| Retention is the real biggest risk, not pharmacy access. The application says the opposite. | 7 of 41 circles weekly active; Q11 names pharmacy access as the biggest risk | **High** | Founder |
| The most exciting feature is out of reach for nearly every user. Interview enthusiasm for refill sync is enthusiasm for something most of them can't use. | One pharmacy, near the founder's father's house | **High** | Founder |
| "Ready at the pharmacy" status can be up to 7 days stale. | Exports arrive weekly on Mondays | **High.** A wrong "ready" or "not ready" on a blood thinner is the exact failure Tessel exists to prevent | Founder + aunt |
| The manual pharmacy data flow may carry privacy or legal exposure. A pharmacy emailing patients' refill data to a third-party app could require patient authorizations or a formal agreement, depending on how it's set up. | Weekly email export from pharmacist to founder | **High until checked** `[ASSUMPTION: US health-privacy rules apply]`. It may also matter to the aggregator's review | Founder + the lawyer who drafted the privacy policy |
| The aggregator is a gatekeeper with no deadline. | Second application under review since August | High | Founder |
| The part of the business that works without the founder's personal network today is the newsletter, not the app. | 2,140 subscribers at 52% open vs. 7 weekly active circles | Medium. It's an asset, but don't confuse it with product traction | Founder |
| The founder is every role: builder, data loader, writer, recruiter. | Team = 1 plus weekend help | Medium | Founder |
| Runway is about 17 months as things stand, and roughly 6–8 months if he hires a developer. | $41,000 ÷ ($4,300 − $1,900 = $2,400/month net burn). A part-time developer at $2,500–4,000/month `[ASSUMPTION]` brings it to about 6–8 months | Medium now; High if he hires | Founder |

**Faith statement:** The pain is real, recurring and expensive. The founder lived it, the people who see it at discharge are pushing families toward Tessel, and 2,140 caregivers open his letter every Sunday. If the product can keep strangers the way the letter does, Tessel has a real shot.

---

## The employer question (Graham's proposal)

This is the most attractive option on the table, so it gets a direct answer: **not now. Keep the door open, with a specific trigger for reopening it.**

**Why it's attractive.** At Graham's numbers, the 1,800-employee manufacturer alone would be worth about $64,800–$108,000 a year at $3–5 per employee per month. That's more than 250 times current MRR. The employer channel may well turn out to be the better business model.

**Why not now:**
- The pilot is conditional on **four builds**: an admin dashboard, SSO, anonymized usage reporting, and a care concierge staffed by a person. The concierge is a services business, and the person staffing it would be the founder.
- An HR buyer will judge the pilot on employee engagement. With today's retention, the pilot would likely produce data that kills the renewal and the reference.
- "Would pilot next spring if…" is interest, not a commitment.
- In Collins's terms, this is reaching for more before the core is good. It would also change *who the customer is*, and that belongs in a Gate 5 decision made after Tessel is good.

**A no-build test that uses the relationship:** ask the HR lead whether 10–20 employees who are caring for a parent would use the *current consumer app* free for 8 weeks. Tessel would get a fresh cohort from outside the founder's network, which feeds M1, and a first read on employer-sourced engagement, without building anything enterprise.

Graham is generous with his network. His frame is benefits sales, which is his expertise. That makes him worth keeping close as an advisor for the employer channel later, not someone who should set the roadmap now.

---

## Pause list (not a stop-doing list; that comes after Gate 5)

1. **The employer build:** SSO, admin dashboard, reporting, concierge.
2. **Android.** A third of the waitlist is real demand, but a second platform doubles the surface area before the first one is proven. Collect Android emails and tell those people when.
3. **Hiring a part-time developer.** It cuts runway by more than half before you know what to build.
4. **Treating aggregator approval as the plan.** Keep the application alive, but find a path that doesn't wait on it (see the 90-day plan).
5. **Expanding the manual pharmacy model to more pharmacies** until the legal question is answered and M1 shows whether refill data even drives retention.

---

## Scorecard

| Output | Current | 90-day target `[ASSUMPTION]` | 12-month target `[ASSUMPTION]` |
|---|---|---|---|
| A. Weekly active non-network circles at week 8 | Unknown (≤6) | Measured by source; ≥10 | ≥20 (M1), then growing |
| B. Refills caught before running out, per active circle per month | Not instrumented | Instrumented; baseline set | Rising, and reported to users |
| C. Paying non-network circles, 3-month paid retention | 3 paying, source unknown | ≥5 from non-network sources | ≥15 at ≥60% retention (M3) |
| M2 status: manual imports in the retention path | 1 per week | Decision made: which core retains | 0 |

The BHAG trajectory is not set. Gate 9 didn't run.

---

## Next 90 days

| # | Action | Owner | Pushes toward |
|---|---|---|---|
| 1 | **This week: revise the accelerator application.** Name retention as the biggest risk and show the funnel honestly. Redirect use of funds from Android and a developer hire to "prove strangers stay." Accelerators tend to trust founders who already know their weak number. | Founder | Credibility; runway |
| 2 | **Weeks 1–2: instrument and listen.** Tag every circle by source (network, newsletter, forum, discharge card, employer test). Track weekly activity at weeks 1, 4 and 8. Count refills caught. Call 15 of the 34 inactive circles and ask what they used instead. Find out whether the "account → circle" leak is people leaving or people joining existing circles. | Founder | M1, Scorecard B |
| 3 | **Weeks 2–10: run two stranger cohorts.** (a) Ask the social worker how many cards she has handed out, and ask for an introduction to one more discharge unit. (b) Invite newsletter subscribers in batches, with onboarding built around "one reminder at the right time, fewer phone calls." Compare week-8 retention by source. | Founder; designer friend on onboarding; social worker as partner | M1, M3 |
| 4 | **Weeks 1–6: get refill value without the gatekeeper, and close the legal question.** Ship **predicted refill-due dates** from fill date plus days' supply, entered once by the caregiver. That half of refill sync needs no pharmacy data. Test whether it retains as well as full "ready" status does. In parallel, ask the lawyer to review the weekly-export arrangement. Have the aunt review the reminder logic for clinical safety, and label "ready" status with its as-of date. | Founder; aunt; lawyer | M2; safety risk |
| 5 | **Week 2: give Graham a specific "not yet."** Thank him, name the reopening trigger (M1 hit), and propose the no-build 10–20 employee test above. | Founder | M1 cohort; keeps channel open |

---

## Re-check

Offer: a scheduled re-check about 90 days from the application deadline. It would re-score the scorecard with real cohort numbers, re-run Gate 1 against M1–M3, and, if Gate 1 passes, run Gates 5 and 8 for the first time. This session can't create the scheduled task, so ask for it to be set up when you're back.

Bring these numbers to the re-check:
1. Week-8 retention by source cohort.
2. How many of the 7 weekly active circles came from outside the founder's network.
3. Whether the 277 accounts with no circle left or joined existing circles.
4. Refills caught per circle.
5. Where the 3 paying subscribers came from.

---

## Risk register

No CONDITIONAL verdicts were issued, because the run ended at Gate 1. Gate 10 didn't run either, so these are early warning signs, not a full decline analysis.

| Risk | Early warning sign | Trigger for action |
|---|---|---|
| **Pursuing more before good** (the employer build, Android, a hire) | Engineering time on SSO, dashboards or a second platform | Any of these starts before M1 is met |
| **Gatekeeper dependency** (pharmacy aggregator) | No decision 6 months after the second application `[ASSUMPTION threshold]` | Commit fully to the predicted-due-date path and drop "ready" status from the pitch |
| **Manual data flow: legal and safety exposure** | Lawyer flags it, or a family acts on a stale "ready" status | Stop or restructure the export immediately |
| **Runway compression** | Monthly net burn above $2,400, or contract work dropped | Re-plan when runway falls below 9 months `[ASSUMPTION]` |
| **Single-person dependency** | The newsletter skips a Sunday; imports slip | Write down which tasks only the founder can do, and automate or hand off one |
| **Founder-as-user bias** | Roadmap decisions justified by "what we needed for Dad" | Require evidence from a non-network cohort for any new feature |
| **Wrong unit of measure** | "Circles" stay low while single primary caregivers stay active | If solo caregivers retain better than groups, re-test the core idea that this is a *shared* app |

---

## Gate log

| Gate | Verdict |
|---|---|
| 0 Fit | PASS |
| 1 Baseline | FAIL (not yet good) |
| 2 Level 5 Leadership | Not run |
| 3 First Who | Not run |
| 4 Brutal Facts | Not run (facts surfaced during Gate 1 are listed above) |
| 5 Hedgehog | Not run |
| 6 Discipline | Not run |
| 7 Technology | Not run |
| 8 Flywheel | Not run |
| 9 Built to Last | Not run |
| 10 Mighty Fall | Not run (early warning signs are in the risk register) |

**Tally:** 1 PASS, 1 FAIL, 0 CONDITIONAL, 9 not run.

**Method:** autonomous mode, so no evidence questions were asked. This session had no memory or past-chat search, so no earlier run was available as a baseline, and no web research, so the employer-benefit market and its competitors are unverified. The dossier (the founder's accelerator application) is the only evidence.