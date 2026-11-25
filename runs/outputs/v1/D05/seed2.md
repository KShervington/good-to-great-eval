# Good to Great: Tessel

## Verdict

**Not yet good. The run stops at Gate 1, a gentle FAIL.**
Tessel goes after a real and painful problem, and the founder is unusually well suited to it. The product does not yet work without the founder's own hands and network. Of 41 care circles, 7 are weekly active, and one of those is the founder's family. The headline feature, refill sync, depends on one pharmacy's weekly email, which the founder loads by hand.

- **Hedgehog Concept:** not drafted. Anything built on it now would rest on unproven ground.
- **Weakest link:** circles started by strangers that keep coming back every week.
- **Hold until good:** the employer pilot build list, a full Android app, and hiring.
- **Most urgent brutal fact:** retention outside the founder's own circle is unproven, and roughly 17 months of runway are left.
- **Numbers that would change this:** where the 7 active circles and 3 payers came from, week-8 retention by channel, and how many active circles actually use refill sync.

`Greatness potential: 7/100`

---

## Gate 0: Fit (PASS)

**Subject card**

| Field | Value |
|---|---|
| Name | Tessel |
| Type | Product / app (consumer mobile, iOS) |
| Steward | The founder (solo) |
| Time horizon | Years. Family caregiving is a long-running problem, and the founder has committed 14 months and $38k so far. |
| Current stage | Live 4 months, pre-seed, applying to an accelerator |
| Rearrangeable resources | Founder time (minus 10 hrs/week of contract work), ~$41k savings, a volunteer UX designer, a retired-nurse clinical reviewer, the newsletter, one pharmacy relationship, a social-worker referral channel |
| Measurable | Yes: circles, weekly activity, retention, paid conversion, refills tracked |

It is an ongoing endeavor with a clear steward and countable outcomes, so the framework applies.

---

## Gate 1: Baseline (FAIL: not yet good)

### Baseline sheet

| Measure | Value | Honest reading |
|---|---|---|
| Accounts | 318 | Roughly one circle for every eight accounts. Many accounts never became part of a working circle. |
| Care circles | 41 | The real unit of value. Small. |
| Weekly active circles | 7 (17% of circles) | At least one is the founder's own family. [ASSUMPTION] Several of the others likely trace to the support group or former colleagues. |
| Paid subscribers | 3 × $6.99 ≈ **$21 MRR** | Contrast this with "I'd pay anything." Stated willingness to pay hasn't turned into payment yet. Where the 3 came from is unknown. |
| App Store rating | 4.9 (11 ratings) | The sample is too small to mean much, and [ASSUMPTION] it is probably skewed toward the founder's network. |
| User interviews | 26 | Good discipline, and a real asset. |
| Newsletter | 2,140 subscribers, 52% open rate | **Tessel's strongest asset with strangers.** That is roughly 1,100 readers a week, against 318 app accounts. Newsletter-to-circle conversion is unknown. |
| Refill sync | 1 pharmacy, weekly email export, loaded by hand | The defining feature runs on the founder's personal effort. With a weekly feed, the "ready at pharmacy" status can be up to a week stale, so even the one working version doesn't yet deliver the promise. |
| Chain pharmacy access | Aggregator application "under review" since August | The key dependency sits in a third party's queue. |
| Android | None. About 1/3 of the waitlist is on Android. | This may block circles from forming, since siblings use mixed devices. [ASSUMPTION, unmeasured] |
| Distribution signal | A stroke-unit social worker hands out Tessel cards, and families ask for it by name | A promising channel at the moment of greatest need. The conversion count is unknown. |
| Runway | ~$41k ÷ (~$4,300 costs − $1,900 contract income) ≈ **~17 months** | Computed from the dossier, before any accelerator money. |

### Draft definition of great (product framing: category-defining, durable usage)

1. **Superior performance:** families coordinating on Tessel miss fewer refills and doses, and need fewer coordination calls, than families using group chats and whiteboards. A possible measure is lapsed prescriptions per circle-month.
2. **Distinctive impact:** discharge planners and caregivers treat it as the default. If it disappeared, families would feel the hole immediately.
3. **Lasting endurance:** it works without the founder loading data, beyond the founder's own network, and beyond any single pharmacy.

### Scorecard outputs (the baseline for every future run)

1. **Weekly active circles from outside the founder's personal network.** Current: unknown, at most 6.
2. **Week-8 retention of new circles, by acquisition channel.** Current: unmeasured.
3. **Paying circles from outside the network.** Current: unknown, at most 3 (about $21 MRR in total).

### State: not yet good

The dossier matches the skill's description of "not yet good" almost point for point. Early users came from the founder's own circle, retention outside that circle is unproven, and the key feature is operated by hand. Gates 2–10 would be built on that foundation, so the run stops here. This is not a verdict on the founder or the idea. The founder-problem fit, the interview discipline and the newsletter are real strengths. The **product** has simply not yet shown that it works on its own.

---

## What "good" would look like

Families who have never met the founder find Tessel, form a full circle, keep using it every week, and some of them pay. Meanwhile the refill feature runs without anyone touching a spreadsheet.

### Milestones that would prove it (target about 6 months; thresholds are judgment calls, [ASSUMPTION])

| # | Milestone | Proves |
|---|---|---|
| **M1** | **25+ weekly active circles from outside the personal network**, with **≥35% of new circles still weekly active at week 8** | The core works for strangers |
| **M2** | **The refill feature updates without the founder's hands**, either through aggregator access or a version that needs no permission (see below), and its effect on retention is measured | The key feature is a product, not a service |
| **M3** | **15+ paying circles from outside the network that stay through at least two billing cycles** | The value is real enough to pay for |

If none of these is in sight by around month 9, with about 8 months of runway left, the founder will need to decide whether to narrow, pause, or change course.

---

## How the pending decisions look against those milestones

These are not Gate 5 or Gate 6 verdicts, because those gates weren't run. They only show which moves serve the path to "good."

- **Refill sync and the aggregator.** "Refill sync" combines two things. *Due for refill* can be computed from the fill date and the days' supply, which needs no pharmacy access. *Ready at the pharmacy* needs integration. The founder can ship the first part now, measure whether it alone keeps circles active, and stop letting a third party's queue set the pace. If due-date reminders retain circles, aggregator access becomes an upgrade rather than a lifeline.
- **Graham's employer pivot: hold, and keep the relationship warm.** The pilot is conditional ("next spring, *if*") and comes with four requirements: an admin dashboard, single sign-on, anonymized reporting, and a **human-staffed concierge**. Meeting them would turn a solo-built consumer app into a staffed B2B service for a buyer who isn't the user, before the user product has shown it retains. It also cuts against the founder's own best insight: caregivers want *fewer* phone calls, and the app should disappear into the right reminder. Changing direction to jump-start momentum before the core works is an early doom-loop pattern. The employer channel may turn out to be the right economic engine, but that is a Gate 5 question for later. One cheap move does serve M1: ask the HR head whether interested employees could try Tessel now, at no cost and without the enterprise features. Graham's figures ($3–5 per employee per month, about 1 in 5 employees caregiving) could not be verified in this run.
- **Android.** First find out *why* 318 accounts produced 41 circles. If circles stall because invited family members are on Android, a lighter path for secondary members, such as SMS or web, may solve it more cheaply than a second native app. [ASSUMPTION; this needs invite-acceptance data.]
- **Part-time developer.** Hold until M1 shows that what's being built is worth scaling.
- **Accelerator money.** The application currently asks for funds for an integration that is blocked, a second platform, and a hire. Tying the use of funds to M1–M3 would be more honest to the evidence and probably more persuasive.

---

## Brutal facts surfaced at baseline (not the full Gate 4)

| Fact | Evidence | Severity |
|---|---|---|
| Retention beyond the founder's circle is unproven | 7 of 41 circles weekly active; early users came from the support group and colleagues | High |
| The defining feature is hand-operated and stale | One pharmacy, a weekly email, loaded manually | High |
| The named "biggest risk" isn't the biggest one | Pharmacy access matters, but retention is the larger risk and the one more within the founder's control | High |
| Stated demand ≠ paid demand | "I'd pay anything" vs 3 subscribers | Medium |
| The founder is the single point of failure | Solo, 10 hrs/week of contract work, a weekly newsletter, manual data loading | Medium |
| Runway is finite | About 17 months at the current net burn | Medium |

**Why it's worth continuing:** the problem is real, the founder lived it, about a thousand strangers read the founder's writing every Sunday, and families on a stroke unit already ask for Tessel by name.

---

## Next 90 days (owner: the founder unless noted)

1. **Tag every circle by source** (personal network / newsletter / forum / social worker / other) and build week-1, week-4 and week-8 retention for each source. Do this in the first two weeks, because every other decision depends on it.
2. **Ship due-date refill reminders that need no permission:** fill date plus days' supply gives a due date, which triggers a nudge to the whole circle. Compare retention for circles that use it against those that don't. *Clinical wording reviewed by the aunt.*
3. **Turn the two stranger channels into measured funnels:** a tracked link in every newsletter issue, and a code on the social worker's cards. Ask the social worker whether she would introduce Tessel to one or two peers on other units.
4. **Diagnose why 318 accounts became 41 circles:** measure invite-acceptance rates and the share of invitees on Android, and interview five circles that went inactive. *The UX designer friend handles onboarding fixes.*
5. **Park the employer build list:** send Graham and the HR head a short note proposing to revisit once M1 is met, and ask whether employees could join a free trial now.

---

## Re-check

Would you like a scheduled re-run around **22 February 2027**? It would re-score the three scorecard numbers with real data and re-run Gate 1. If Tessel then clears "good," the run continues through Gates 2–10, starting with the Hedgehog Concept, where the employer-versus-consumer question belongs. Scheduling isn't available in this session, so set it up when the tools are.

---

## Risk register

| Risk | Early warning sign |
|---|---|
| Retention stays confined to the founder's network | Stranger-sourced circles go quiet within 2–4 weeks |
| Single-pharmacy, hand-loaded dependency | A missed Monday load, or the pharmacist leaves or stops sending |
| Aggregator gatekeeper | Still "under review" at the 90-day re-check |
| A new direction before the core works (early doom-loop) | Roadmap time going to the dashboard, SSO or concierge before M1 |
| Circles failing to complete because of device mix | Low invite acceptance, concentrated among Android invitees |
| Founder capacity and runway | The newsletter skips a week, or runway falls below about 10 months with no milestone met |
| Health-data obligations (wound photos, medications, any employer reporting) | Anonymized reporting requested before the lawyer has confirmed which rules apply |

---

## Gate log

| Gate | Verdict |
|---|---|
| 0: Fit | PASS |
| 1: Baseline | FAIL (not yet good) |
| 2–10 | Not run, because of the Gate 1 fail |

Tally from the table: 1 PASS, 1 FAIL, 9 not run.

Evidence note: no memory, past-chat or web search was available. This run rests solely on the accelerator application, so market figures and benchmarks were not verified. The greatness score reflects a typical pre-seed consumer app with 7 weekly active circles, offset by strong founder-problem fit and an engaged newsletter audience.