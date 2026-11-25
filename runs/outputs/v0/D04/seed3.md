# Linewright: Good to Great

## One-screen verdict

**Hedgehog Concept (working hypothesis):** *Linewright is the keyboard-first timing editor that makes every professional subtitle file pass the client's delivery spec the first time, paid for as renewing seats, with studios first.*

**Weakest link in the flywheel:** turning delivered value into renewals. The combined renewal rate fell 64% → 58% → 55% → 52% over four quarters. It went below your own 58% model and is still falling. You can't currently tell whether studios or individuals are the ones leaving.

**Top three stop-doing items:**
1. Stop pursuing Linewright Lite, the creator product. Say no to Marisol, kindly.
2. Stop selling Linewright on auto-align. It becomes free this winter.
3. Stop answering install and licensing tickets by hand. Fix the cause.

**Most urgent brutal fact:** 69% of surveyed buyers bought mainly for auto-align. Lantern Subs, which is free and is the tool everyone learns on, has had auto-align in its nightly builds since April and ships it in stable "this winter", which is next quarter. The renewal decline past your model started in the same quarter. That timing is a correlation, not proof.

**Missing numbers that would change this answer:**
- Renewal rate split into studio seats and individual update plans.
- Studio seat count and studio revenue a year ago.
- Before-and-after QC rejection data from at least three studios.
- The reasons lapsed renewers give for leaving.

If studios renew no better than individuals, the Hedgehog Concept is wrong and Gate 5 has to be re-run.

**Decision on the four options:** No to the creator product. No to Linux. Yes to the studio push, but in sequence: data and proof first, then admin and reporting, and the sales hire last. Clear only the part of the backlog that serves the Hedgehog Concept.

Greatness potential: 30/100

> **Evidence note.** This run was autonomous, with no tools. I couldn't search memory or past chats, so there is no prior baseline. I couldn't do web research, so every competitor and market claim comes from the dossier. I asked no questions. Every inference is marked `[ASSUMPTION]` for you to correct.

---

## 1. The great version in one paragraph

Great Linewright is the tool a broadcaster's QC desk is glad to see on a delivery. Studios set a broadcaster's or streamer's rules once, in a shared style profile with a spec-checker preset. Every freelancer on the job then produces a file that passes the first time, and the studio can see that in a per-studio report. Auto-align is table stakes and simply works, probably on the same open speech models everyone else uses. Linewright's edge is everything around it: spec compliance, a keyboard-first editor built by a working subtitler, and the shared rules layer. Most revenue is renewing seats, and studio seats renew in the 90s. The founder spends their week on the spec library and the editor, not on licensing tickets. Releases, support and the spec library would keep running if the founder took a month off.

## 2. The Hedgehog Concept

**Sentence:** *The keyboard-first timing editor that makes every professional subtitle file pass the client's delivery spec the first time, paid for as renewing seats, studio first.*

| Circle | Candidates considered | Verdict |
|---|---|---|
| **Best in the world at** | Auto-align | **No.** Free speech models are commoditizing it, so you can't win an accuracy race against them. |
| | Keyboard-first pro timing editor | **Partly.** It's a real strength (37% of buyers cite it), but on its own it's "good". Lantern is free and familiar. |
| | **Spec compliance across a team: encode the client's rules once, and every file passes** | **Yes, in a narrow world:** studios and freelancers delivering to broadcasters and streamers. Studios name it as their reason to buy, and 41% of individuals cite QC checks. The cloud platform is weak on the editor, and Lantern has no shared rules layer `[ASSUMPTION]`. |
| | Creator captioning | **No.** No advantage, and the core feature there is the one being commoditized. |
| | Linux | **No.** That's parity, not excellence. |
| **Economic engine denominator** | Profit per license (one-time) | Weak. It doesn't compound. |
| | Revenue per studio | Too lumpy. The biggest studio is 11.5% of studio revenue. |
| | **Recurring revenue per renewing seat** | **Chosen.** A studio seat pays $99 a year and renews without you chasing it. An individual update plan pays $49 a year. Recurring revenue is $114.1k, 54% of the total. |
| **Passion** | The craft of professional subtitling | 11 years as a freelancer, and you built the tool you wished you had `[ASSUMPTION: this is what you care about, not creator content]`. The forum regulars and the Lisbon translator suggest the pro community shares it. |

**Tests:**
- *Does it explain past wins?* Partly. It explains why studios buy and renew, and the QC share of individual purchases. It does **not** explain the biggest historical draw, auto-align at 69%. That gap is uncomfortable, and it's intentional.
- *Does it rule things out?* Yes: Lite, Linux, the auto-align accuracy race, and generic "more features".
- *Is it uncomfortable to commit to?* Yes. It walks away from a 2,310-person waitlist and a "50x market" pitch from a friend.

**What would confirm it:**
1. Studio-seat renewal is clearly above individual renewal: at least 85% against roughly 50% `[ASSUMPTION thresholds]`.
2. Three or more studios provide before-and-after rejection counts showing at least a 30% drop.
3. After Lantern's stable release ships auto-align, studio seats keep growing quarter over quarter.
4. Individuals who use the spec checker renew at a higher rate than those who don't. This needs opt-in telemetry or a survey question.

## 3. The flywheel

```
   ┌──► 1. Encode client delivery specs as shared presets (spec library)
   │              │
   │              ▼
   │    2. Files pass QC first time ─ fewer rejections, shown in per-studio reports
   │              │
   │              ▼
   │    3. Studios standardize on Linewright and add seats (incl. their freelancers)
   │              │
   │              ▼
   │    4. Freelancers learn it on studio jobs → buy individual licenses and renew
   │              │
   │              ▼
   │    5. Recurring revenue per renewing seat rises  ◄── DENOMINATOR
   │              │
   │              ▼
   └─── 6. Funds support help and a spec librarian → founder time back on specs and editor
```

**Weakest link: steps 2→3 and 3→5.** The proof that rejections fall is anecdotal ("by more than half", unverified). Renewal, where value turns into revenue, is at 52% and falling, and nobody has split it by segment.

**Current push, the next two turns:**
1. **Measure the loop.** Split renewal by segment, add an exit survey, and collect rejection data from studios.
2. **Free the founder.** Remove the licensing and install ticket load so time goes to steps 1 and 2.

**Doom-loop check: moderate risk.** Three signs are present:
- **A new direction:** a creator web app on a different platform, for a different buyer, at a different price.
- **A jump-start program:** a sales hire, admin console and SSO all at once, before proof that studios retain.
- **A reaction without understanding:** the January price rise was a lever pulled before anyone knew why renewals move.

None of these has been acted on yet. That is the good news.

## 4. The bus

| Person / commitment | Call | Note |
|---|---|---|
| **You (founder)** | **Keep, move seat** | Move from support desk and bug fixer to owner of the spec library and the editor. Today that seat gets almost none of your 50 hours. |
| Mac contractor | Keep, consider expanding | The only other person who touches code. Make them the documented backup for releases, to reduce bus-factor risk. |
| Accountant | Keep, extend the brief | Ask for monthly renewal by segment and cohort, not just books. They already see the compounding part clearly. |
| Lisbon translator | **Keep, formalize** | Send a lifetime license and public credit. Invite her to lead a community localization program. |
| Forum regulars | Keep as an early-warning system | They flagged Lantern before you did. |
| Marisol (as Lite partner) | **Off the bus for this endeavor** | She's a capable operator with a real audience. That audience simply isn't Linewright's customer. Keep the friendship, decline the deal. |
| Linux port | Off | 46 requests is about 1.4% of licensees. |
| 140-item backlog | Off, mostly | Triage to Hedgehog items. Close the rest publicly. |
| **Missing: support/licensing help** | First seat | Fix the root cause first. If tickets stay above 15 a week, add a part-time support contractor. |
| **Missing: spec librarian / studio success** | Second seat | Ideally an ex-QC person, part-time, who maintains presets and gathers rejection data. Hire this *before* a salesperson. |
| **Missing: backup developer** | Third seat | Even a few days a month, so releases don't depend on one person. |
| Part-time salesperson | Deferred | When in doubt, don't hire. Revisit after confirmation tests 1 and 2. |

## 5. Stop-doing list

1. **Linewright Lite.** It would take six months of the only developer's time, during exactly the window when Lantern ships auto-align. Rough economics: 2,310 sign-ups × 10% conversion `[ASSUMPTION]` × $96 a year ≈ **$22k gross a year, before Marisol's share**. That's about 6% of the recurring base you'd be neglecting.
2. **Leading with auto-align** on the website, in onboarding and in release notes. Lead with "passes the spec first time".
3. **Handling install and licensing tickets one by one.** Build self-serve activation and deactivation, signed installers and a fix-it page.
4. **The Linux port.**
5. **Working the backlog first-in, first-out.** Only spec-checker, style-profile, editor-speed and studio-admin items survive triage.
6. **Explaining declines before measuring them.** "Summer is always slow" doesn't explain a 23% drop against the *same* summer last year.
7. **Further individual price increases** until you understand why renewals are falling.
8. **Bolting on enterprise workflow features** to fight the cloud platform. It's better at workflow and isn't after your customers.

## 6. Brutal facts and faith statement

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | The #1 reason for buying becomes free next quarter | 69% cite auto-align. Lantern nightlies have it since April, with stable "this winter". | **Critical** | Founder |
| 2 | Renewal is falling past your own model | 64→58→55→52%. The model said it would settle at 58%. | **Critical** | Founder + accountant |
| 3 | New individual units are down 23% year on year | Q3 161 against 209. Seasonality applies to both years. | High | Founder |
| 4 | Headline growth hides falling volume | Revenue +19.5% ($176.9k→$211.4k) includes the $39→$49 price rise, while units and renewal rate both fell. | High | Founder |
| 5 | The company is one person | 50 hours a week, one week off, bus factor of one, no successor. | High | Founder |
| 6 | The product has stalled | Last two releases were bug fixes. 140-item backlog. | High | Founder |
| 7 | Support load is self-inflicted | About 30 tickets a week, mostly install and licensing, roughly 5–8 hours a week `[ASSUMPTION]`. | Medium | Founder |
| 8 | The studio case is unverified | "More than half" fewer rejections is anecdote. The survey is almost all individuals. | Medium | Founder |
| 9 | Thin cushion | $88k cash ≈ 7 months of salary plus costs with zero revenue. | Medium | Founder |
| 10 | The creator signal is a waitlist, not revenue | 2,310 sign-ups from one post. "50x" comes from a pitch deck. | Medium | Founder |
| 11 | Studio concentration | The largest studio is 74 seats ≈ $7.3k, 11.5% of studio revenue. | Low | Founder |

**Truth climate.** There's no team to coerce, so the risk is self-persuasion. You anchored on your own 58% model, and outside charisma (Marisol's deck) fills the gap. Red-flag mechanisms to set up:
- a monthly one-page dashboard showing year-on-year and segment figures;
- a one-question exit survey on every lapsed renewal;
- the forum as a listening post on Lantern.

**Faith statement:** *Free auto-align raises the floor for everyone, but it doesn't guarantee a file passes a broadcaster's spec. The people who carry that risk will keep paying for a tool built by one of their own that makes rejection rare.*

## 7. Core ideology and BHAG

**Core purpose:** No subtitle gets rejected, and no subtitler has to fight their tool.

**Core values `[ASSUMPTION; confirm]`:**
1. The file passes: correctness beats feature count.
2. Built by subtitlers, for subtitlers: keyboard-first craft.
3. Honest pricing that customers can predict.
4. Treat users like colleagues: credit contributors, answer straight.

**BHAG (one line, given the scale of a solo product):** *Within 15 years, every major broadcaster and streamer delivery spec exists as a Linewright preset, and a Linewright pass report is accepted as QC evidence.*

**Clock-building mechanisms:**
- documented release process that the contractor can run;
- self-serve licensing;
- a spec library maintained by someone other than you;
- community localization program;
- monthly segment dashboard;
- at least three weeks a year when you are genuinely offline, which tests every mechanism above.

## 8. Scorecard

| Output | Current (end of Q3, Year 0) | 12-month target | BHAG trajectory |
|---|---|---|---|
| **Studio seats on subscription** | 638 seats, 39 studios | 850 `[ASSUMPTION]` | Thousands of seats across most studios delivering to major broadcasters |
| **Renewal rate, split by segment** | 52% combined (Q3); split unknown | Studio ≥90%, individual ≥55%, combined up two quarters in a row `[ASSUMPTION]` | Studio ≥95% |
| **Recurring revenue (studio + update plans)** | $114.1k, 54% of revenue | ≥$140k and ≥60% of revenue `[ASSUMPTION]` | >80% of revenue |

## 9. Next 90 days

| # | Action | Owner | Flywheel step |
|---|---|---|---|
| 1 | Split renewal by segment and quarterly cohort for the last 4 quarters. Add a one-question exit survey to every lapsed renewal. Start a monthly dashboard. | Founder + accountant | Measures 3→5 |
| 2 | Kill the licensing and install ticket load with self-serve activation and deactivation, signed installers and a troubleshooting page. Target fewer than 15 tickets a week. If that's missed, add a part-time support contractor. | Founder | Frees time for step 6 |
| 3 | Interview 5 studios, including the 74-seat studio and the two that cited rejection cuts. Collect before-and-after rejection counts. Ship a basic per-studio QC report. Scope SSO for the three requesters, with a go/no-go at day 90. | Founder | Proves step 2, feeds step 3 |
| 4 | Get ahead of Lantern's stable release. Bring auto-align to parity, adopting an open speech model if that's cheaper than competing. Rewrite the site and onboarding around "passes the spec first time" before winter. | Founder (+ Mac contractor for builds) | Protects 4→5 |
| 5 | Close the open loops. Decline Lite and Linux publicly and kindly. Send the Lisbon translator a lifetime license and credit, and open community localization. Have the contractor run one release end to end. Take one real week off. | Founder | Steps 6 and 1, endurance |

## 10. Re-check

Would you like a scheduled task set up for about 90 days out, at the end of Q4 Year 0 or start of Q1 Year 1? It would re-score the scorecard with real numbers and re-run Gates 1, 5 and 8. Lantern's stable release should have shipped by then, which makes it the real test of the Hedgehog Concept.

## 11. Risk register

| Source | Risk / condition | Evidence that clears it |
|---|---|---|
| Gate 2 (CONDITIONAL) | Single point of failure. Bad news is explained by outside causes before it's measured. | Contractor ships a release solo. The quarterly notes lead with year-on-year and segment numbers. |
| Gate 3 (CONDITIONAL) | Founder capacity is the whole bus. Missing seats. | Tickets under 15 a week. A spec librarian or studio-success seat is filled or scoped with a budget. |
| Gate 4 (CONDITIONAL) | Renewal split and churn reasons unknown. | Segment table plus at least 30 exit-survey responses. |
| Gate 5 (CONDITIONAL) | The Hedgehog Concept depends on studios retaining better. | Confirmation tests 1 and 2 met. |
| Gate 8 (CONDITIONAL) | The proof link (2→3) is anecdotal. | Rejection data from at least three studios, and per-studio reports live. |
| Decline 1: Hubris | "Revenue is up 19.5%" while units and renewal fall. | Warning sign: quarterly notes cite only total revenue. |
| Decline 2: Undisciplined more | Lite, Linux, or sales + console + SSO all at once. | Warning sign: more than 20% of founder time spent outside the Hedgehog Concept. |
| Decline 3: Denial of risk | Lantern ships and renewals keep sliding while they're blamed on price or summer. | Warning sign: no segment data by day 30. Combined renewal below 50%. |
| Decline 4: Grasping for salvation | A crisis bet on Lite, a lifetime-deal fire sale, or a big price cut. | Warning sign: a launch planned to "fix the numbers". |
| Decline 5: Capitulation | Burnout, then maintenance mode or a distressed sale. | Warning signs: a third bug-fix-only release, zero weeks off, cash below 4 months of costs. |

## 12. Gate log

| Gate | Verdict | One line |
|---|---|---|
| 0 Fit | PASS | Ongoing product, a steward, a multi-year horizon, measurable outcomes. |
| 1 Baseline | PASS | Good: $211.4k, profitable, paying the founder. Leading indicators are trending down. |
| 2 Level 5 | CONDITIONAL | Humble and resolute, but no succession and some rationalizing. |
| 3 First Who | CONDITIONAL | No misaligned key seat. Capacity and missing seats are the problem. |
| 4 Brutal Facts | CONDITIONAL | Facts confronted, consistent with Gate 1. Segment data missing. |
| 5 Hedgehog | CONDITIONAL | Real intersection at spec compliance and renewing seats. Pending confirmation. |
| 6 Discipline | PASS | Eight-item stop-doing list with clear boundaries. |
| 7 Technology | PASS | Auto-align moved to parity. Spec library is the pioneer bet. |
| 8 Flywheel | CONDITIONAL | The loop closes. The proof and renewal links are unmeasured. |
| 9 Built to Last | PASS | Purpose, values, one-line BHAG, mechanisms. |
| 10 Mighty Fall | PASS | Early stage-1 to stage-3 signs logged. |

**Count:** 6 PASS, 5 CONDITIONAL, 0 FAIL. That's 5 of 11, just under half. Two root problems cause all five conditionals:
1. **Every unit of capacity is the founder.**
2. **There is no segment-level evidence on who renews and why.**

Fix those two and most of the conditionals clear together.

---

## Appendix: Gate artifacts not covered above

**Gate 0, subject card.**
- Name: Linewright.
- Type: product (solo-founder desktop software).
- Steward: the founder.
- Horizon: years; it's in its fourth year on sale.
- Stage: profitable, founder-salaried, growth slowing in leading indicators.

**Gate 1, baseline.**
- *Evidence of good:* $211.4k trailing revenue (+19.5%); about $31k costs; $120k founder pay; about $60k retained; $88k cash; 3,400 licenses sold; 39 studios and 638 seats (consistent with $63.8k at $99 per seat); studios renewing.
- *Leading indicators, down:* Q3 new units −23% year on year; renewal down four quarters in a row; about 754 new individual licenses in the trailing 12 months `[ASSUMPTION: no discounting]`.
- *Great means:* (1) studio renewal and seat growth beat the market; (2) studios would face rejected deliveries without it; (3) it runs without the founder in the room.

**Gate 2, leadership read.**
- *Strengths:* honest, self-critical notes ("I can't verify that"); built from craft, not status; four years of steady effort.
- *Gaps:* you reach for an explanation (summer, the price rise) before reaching for a measurement, and the business can't run without you.
- *Self-audit questions:* Who could ship a release if you were ill for a month? Which number would you least like to look at right now?
- *One behavior change:* write the bad-news section of each quarterly note first, with year-on-year and segment figures, before any explanation.

**Gate 6, framework.**
- *Non-negotiable disciplines:* every release ships at least one spec, preset or editor-speed improvement; the monthly segment dashboard; an exit survey on every lapse; three or more offline weeks a year.
- *Freedom within the framework:* the contractor owns builds and releases; the translator community owns localization; any support help can issue refunds and license resets up to a set limit without asking.
- *Bureaucracy check:* none yet. The risk is the opposite, everything routing through you.

**Gate 7, technology triage.**

| Technology | Class |
|---|---|
| Spec-checker rules engine and presets | Accelerates |
| Shared style profiles | Accelerates |
| Per-studio QC reporting and admin console | Accelerates |
| SSO | Accelerates for larger studios (an enterprise checkbox) |
| Speech-model auto-align | Parity: keep up, consider adopting open models |
| Licensing and activation | Parity, but urgent |
| Code signing | Parity |
| Linux build | Irrelevant |
| Creator web app | Irrelevant |

*Flagged hype and fear:* the "creator wave" and the "50x" claim (hype); an auto-align accuracy race (fear).

*Pioneer bets:*
1. A versioned, machine-readable library of delivery specs.
2. A per-file "pass report" that studios forward with deliveries.