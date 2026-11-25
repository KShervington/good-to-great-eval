# Linewright: Good to Great run

## Verdict

**Hedgehog Concept (working hypothesis):** *Linewright is the tool professional subtitlers and studios use to make a file pass the broadcaster's spec the first time. Studios pay for it per seat, every year.*

**Weakest flywheel link:** the proof step, "files pass QC first time." It rests on two unverified quotes from studio managers. Nobody measures first-pass QC rates, so renewals and new-studio sales both depend on anecdotes.

**Top three stop-doing items:**
1. Don't build Linewright Lite. Decline the creator product kindly and in writing.
2. Stop leading with auto-align. Keep it at parity with the free tools and compete on spec compliance.
3. Shelve the Linux port.

**Most urgent brutal fact:** about **70% of revenue** ($147.6k of $211.4k) comes from individual buyers. Their #1 reason to buy is auto-align (69%), and the free tool everyone learns on ships auto-align in its stable release **this winter**. Renewals have already fallen four quarters in a row, from 64% to 52%, which is below the 58% floor the founder modeled. Same-quarter new licenses are down 23%.

**Missing numbers that would change the answer:**
- Renewal rate **split by segment**: studio vs. individual.
- **Why** individuals churned: the price rise, Lantern, or leaving the trade.
- Measured QC rejection rates at even 3–5 studios.
- How much of the 19.5% revenue growth came from price and how much from volume.
- How many individual buyers also work for studio customers.

If studio renewals are weak too, the Hedgehog Concept is wrong and this run must loop back to Gate 5.

Greatness potential: 25/100

> *Autonomous run.* This session had no web search, memory, or past chats, so there was no prior baseline and no competitor or market research. Everything below comes from the founder's Q3 Year 0 notes. Inferences are marked `[ASSUMPTION]`.

---

## 1. The great version in one paragraph

In its great version, Linewright is the professional standard for spec-compliant subtitles. When a studio takes on a broadcaster or streamer, the first step is to load that client's Linewright spec profile. Every freelancer's file is checked against it before delivery, and the studio can show a measured drop in QC rejections. Revenue is mostly recurring studio seats that renew at high rates. Individual freelancers still buy licenses, but now as the way into the professional standard, not as the main engine. Auto-alignment is table stakes, no better and no worse than the free tools. The moat is the maintained spec library plus a timing editor built by someone who spent 11 years getting files rejected. The product runs on a cadence that doesn't depend on one person working 50-hour weeks. Support is mostly self-service, a second person can ship a release, and the spec library is maintained by a process, not from one person's memory.

## 2. The Hedgehog Concept

**Sentence:** *Make professional subtitle files pass the broadcaster's spec the first time, sold to studios as an annual per-seat standard.*

| Circle | Candidates considered | Kept | Ruled out (and why) |
|---|---|---|---|
| **Best in the world at** | Auto-alignment; keyboard-first timing editor; spec/QC checking; cheap captions; workflow management | **Encoding delivery specs and checking against them, inside a professional timing editor** | Auto-align: a free open-source tool is about to match it. Creator captions: platform tools and well-funded apps own that market `[ASSUMPTION, not researched]`. Workflow: the cloud platform is "very strong" there. Linux: no advantage. |
| **Economic engine (denominator)** | Profit per license sold; per active user; per spec profile; **per recurring professional seat** | **Recurring revenue per professional seat** (studio seats first) | Per license sold: one-time revenue that is shrinking and exposed to free tools. Per spec profile: a useful leading indicator, but not yet tied to revenue. |
| **Passion** | Subtitling craft; building tools; helping creators | **The professional subtitling craft:** timing, reading speed, files that pass `[ASSUMPTION, inferred from 11 years in the trade and why the founder built the product]` | Creator captioning is Marisol's passion, not the founder's. Nothing in the notes shows excitement about it beyond fear of missing out. |

**Tests:**
- **Explains past wins?** Yes. Studios renew because of the spec checker and shared style profiles, not auto-align. 41% of individuals cite QC checks. Auto-align explains individual *acquisition*, which is why that segment is exposed.
- **Rules things out?** Yes: Lite, Linux, workflow features, and auto-align as the headline.
- **Uncomfortable?** Yes. It demotes the feature 69% of buyers cite, and it turns down 2,310 waitlist signups and an old colleague.

**Confirmation tests (working hypothesis until these hold):**
- Studio-only renewal rate ≥ 85–90% `[ASSUMPTION threshold]`.
- Measured first-pass QC improvement at 5 or more studios.
- Retained individuals cite QC and specs more than auto-align.
- New studios trace back to freelancers who already use Linewright.

## 3. The flywheel

```
 (1) Encode each broadcaster's delivery spec precisely
        │      (maintained spec library + shared profiles)
        ▼
 (2) Files pass QC the first time  ◄── WEAKEST LINK: unmeasured
        │
        ▼
 (3) Studios standardize on Linewright: more seats, annual renewal
        │      → RECURRING REVENUE PER PROFESSIONAL SEAT
        ▼
 (4) Freelancers learn it as "the pro standard" and carry it
        │      to other studios; some buy individual licenses
        ▼
 (5) More studios adopt → more spec profiles requested
        │
        ▼
 (6) Recurring revenue funds spec curation, support and dev capacity
        │
        └──────────────► back to (1)
```

**Current push (next two turns):**
1. **Turn anecdote into proof (link 2):** ship per-studio QC reporting with first-pass rate and rejection reasons, alongside SSO and the admin console.
2. **Free the founder's time to spin link 1:** cut install and licensing tickets at the source, so spec work and studio features stop losing out to support.

**Doom-loop check: high risk, not yet entered.**
- *Four directions circling* (Lite, studio push, Linux, backlog): direction-hopping.
- *Lite as a six-month jump-start* to catch a "wave": a big program meant to create momentum.
- *Reaction without understanding:* the price rise was explained away and the Q3 drop blamed on summer, without segment data.
- *Flywheel stalled:* the last two releases were bug fixes.

Committing to Lite now would turn the risk into an actual doom loop.

## 4. The bus

| Person / commitment | Call | Note |
|---|---|---|
| Founder | **Keep, move seat** | Move from support desk and bug fixer to spec/product owner. The 30 tickets a week are the wrong use of the only person with 11 years of craft knowledge. |
| Mac contractor | **Keep, widen seat** | Best candidate to become the second person who can ship a release, which reduces the single-person risk `[ASSUMPTION: competent and available for more days]`. |
| Accountant | **Keep** | Already gives the most Hedgehog-aligned advice. Make them the monthly red-flag reviewer (see Gate 2). |
| Two studio managers quoting QC gains | **Keep, design partners** | Recruit them to define and validate the QC report. Their numbers become the proof. |
| Three studios asking for SSO | **Keep, design partners** | First customers for the studio pack and for testing tier pricing. |
| Forum regulars | **Keep** | The early-warning system. They flagged Lantern first. |
| Lisbon translator | **Keep, thank now** | Send a lifetime license and a public credit. Possible future seat for localization or community `[ASSUMPTION]`. |
| Marisol, as Lite partner | **Off this bus** | Not a judgment of her or her agency. Creator captioning is outside this endeavor. Keep the friendship. |
| Linux port | **Off** | 46 forum requests, no link to the Hedgehog Concept. |
| 140-item backlog | **Move seat** | It's a pile, not a plan. Triage it against "does this improve first-pass QC or studio retention?" |
| **Missing:** part-time support/ops | **Fill first** | After the licensing fixes, someone handles what's left. |
| **Missing:** second release-capable developer | **Fill within 12 months** | The product dies if the founder is out for a month. |
| **Missing:** spec-library curator | **Fill as the library grows** | Could be a working freelance subtitler, part time. |
| **Missing:** studio account person | **Defer** | Hire only after the QC report exists to sell with. When in doubt, don't hire. |

## 5. Stop-doing list

1. **Building Linewright Lite or any creator-captioning product.** It takes six months of the only developer's time while Lantern ships. The rough math: 2,310 free signups × 10% conversion × $96/yr × 70% after revenue share ≈ **$15.5k/yr** `[ASSUMPTION: all three rates]`. About ten average studios (≈164 seats × $99) bring in **$16.2k/yr** with far higher retention and no new product.
2. **Leading marketing with auto-align.** Keep it at parity. Lead with "passes the spec."
3. **The Linux port.**
4. **Answering install and licensing tickets by hand without fixing the cause.**
5. **Working the backlog top to bottom.** Close anything that doesn't serve the Hedgehog Concept.
6. **Building enterprise workflow features** (project management, vendor routing) to compete with the cloud platform.
7. **Further price moves on individuals** until churn reasons are known.
8. **Explaining away a metric without segment data.** "Summer is slow" doesn't explain a 23% drop against the *same* quarter last year.
9. **Hiring a salesperson before per-studio proof exists.** This is deferred, not ruled out.

## 6. Brutal facts and the faith statement

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | The #1 reason individuals buy is about to be free | Auto-align cited by 69%. Lantern nightlies have it since April, stable release "this winter" | **Critical** | Founder |
| 2 | Renewals are falling, not settling | 64% → 58% → 55% → 52%. The model predicted a 58% floor | **High** | Founder + accountant |
| 3 | New individual sales are declining year over year | Q3: 161 vs. 209 (−23%), same season | **High** | Founder |
| 4 | Revenue is concentrated in the exposed segment | Individual = $97.3k + $50.3k = **70%** of revenue | **High** | Founder |
| 5 | The business depends on one person | 50 h/week, one week off this year, everything runs through the founder | **High** | Founder |
| 6 | Product momentum has stalled | Two bug-fix releases, 140-item backlog | Med-High | Founder |
| 7 | The support load is self-inflicted | ~30 tickets a week, mostly install and licensing | Medium | Founder + Mac contractor |
| 8 | The studio value claim is unverified | Two anecdotes saying rejections fell "by more than half" | Medium | Founder |
| 9 | The waitlist isn't evidence of demand | 2,310 free signups from one 400k-follower post, no price tested. The "50x market" figure comes from a partner's pitch deck | Medium (decision risk) | Founder |
| 10 | The cash buffer is thin | $88k ≈ 7 months of costs plus pay (~$151k/yr). Studio revenue alone ($63.8k) doesn't cover the founder's pay | Medium | Founder + accountant |
| 11 | Studio pricing may be too low | $99/seat/yr vs. the cloud platform's $480/seat/yr. SSO and admin are usually paid-tier features `[ASSUMPTION]` | Opportunity | Founder |

**Truth climate and charisma check.** No team is suppressing bad news. The founder is doing it alone, through comfortable explanations ("always going to cost some renewals," "summer is always slow"). The strongest outside pressure comes from charisma, not data: Marisol's "you'll regret not catching the wave." There is no red-flag mechanism yet.

**Faith statement:** *Free tools will learn to align audio. They won't learn every broadcaster's rulebook, and the person who spent eleven years getting files rejected knows those rules better than anyone.*

## 7. Core ideology and BHAG

**Core purpose:** every subtitle a viewer reads is timed right and readable, and the subtitler who made it doesn't waste a day on rejections.

**Core values:**
1. Frame-accurate craft over "good enough."
2. Respect the subtitler's time: keyboard first, no busywork.
3. Files that pass, every time.
4. Fair pricing for professionals.

**BHAG (one line, since this is a product):** *By Year 15, broadcasters and streamers point their vendors to Linewright's spec profiles as the reference implementation of their own delivery rules.*

## 8. Scorecard

| Output | Current (end of Q3, Year 0) | 12-month target | BHAG trajectory |
|---|---|---|---|
| **Studio recurring revenue** | $63.8k TTM; 39 studios, 638 seats | ~$90k (≈50 studios / ~850 seats, plus SSO-tier uplift) `[ASSUMPTION]` | Studio recurring revenue becomes the majority of total revenue |
| **Renewal rate, split by segment** | 52% blended; split unknown | Studio ≥ 90%; individual stabilized at ≥ 55%; reported separately every month `[ASSUMPTION targets]` | Studio ≥ 95% and individual renewals tied to studio work |
| **First-pass QC acceptance for Linewright-checked files** | Unmeasured (two anecdotes) | Measured at ≥ 10 studios with a published baseline | The published reference number broadcasters cite |

## 9. Next 90 days (to end of Q4, Year 0)

| # | Action | Owner | Pushes link |
|---|---|---|---|
| 1 | **Split the numbers (weeks 1–2).** Renewal rate by segment and cohort. Send a two-question survey to lapsed individuals: why they left, and whether they now use something else. Decompose the TTM growth into price and volume. | Founder + accountant | Red-flag mechanism; confirms Gate 5 |
| 2 | **Kill the ticket load.** Self-service license reset, an offline-activation fix, installer clean-up, and FAQ macros. Target fewer than 12 tickets a week. If the load stays above that, bring in part-time support. | Founder; Mac contractor for the Mac installer | Frees capacity for (1) |
| 3 | **Ship studio pack v1:** SSO, admin console, and a simple per-studio QC report (first-pass rate and top rejection reasons). Build it with the three SSO studios and the two QC-quoting managers. Price SSO as a higher tier. | Founder | (2) proof → (3) retention and the denominator |
| 4 | **Reposition before Lantern ships.** Website, onboarding, and renewal emails lead with "passes the spec." Auto-align becomes a supporting feature. Explore letting individuals receive a studio's shared spec profile. | Founder | (4) freelancers as the pro standard |
| 5 | **Close the open loops kindly.** Decline Lite to Marisol in writing, as a choice about focus, not a judgment of her. Send the Lisbon translator a lifetime license and a public thank-you. Triage the backlog against the Hedgehog test. | Founder | Removes doom-loop pull |

## 10. Re-check

I can't schedule anything in this session. I'd suggest one scheduled task about **90 days out (end of Q4, Year 0)**. It would re-score the three scorecard rows with real figures, especially the segment-split renewal rate, and re-run Gates 1, 5 and 8. If the studio renewal rate is under ~85%, that review should reopen the Hedgehog Concept.

## 11. Risk register

| Source | Risk | Condition to clear / warning sign |
|---|---|---|
| Gate 2 (CONDITIONAL) | Leader is a single point of failure and rationalizes metrics | Clears when a second person can ship a release and a monthly segment-split review with the accountant has happened 3 times |
| Gate 3 (CONDITIONAL) | Missing seats (support/ops, second developer); founder at 50 h/week | Clears when tickets are under 12/week or a support person is in place, and a contractor has shipped one release |
| Gate 4 (CONDITIONAL) | No red-flag mechanism; facts are explained away | Clears when the first monthly segment-split report exists and churn-reason survey results are in |
| Gate 5 (CONDITIONAL) | Hedgehog Concept unconfirmed; studio retention and QC value unproven | Clears when studio renewal ≥ 85–90% and measured QC improvement at ≥ 5 studios |
| Gate 10 · Hubris | Treating two quotes as proof; "studios love us" | Warning sign: QC claims in marketing without data |
| Gate 10 · Undisciplined more | Lite, Linux, workflow features, a second product | Warning sign: any roadmap item not traceable to first-pass QC or studio retention |
| Gate 10 · Denial | "Summer," "it'll settle at 58%" | Warning sign: any metric explained away twice in a row |
| Gate 10 · Grasping | Lantern ships, individual sales drop, then a panic pivot, deep discounts, or a rushed Lite | Warning sign: "emergency" launch talk or price cuts before the churn data is in |
| Gate 10 · Capitulation | Founder burnout leads to selling or shutting down | Warning signs: under 2 weeks off a year, hours over 50, release cadence only bug fixes |

The four CONDITIONAL verdicts share **two root problems**: (a) all capacity and continuity sit with one person, and (b) segment-level data is missing, so the blended numbers hide which engine is failing.

## 12. Gate log

| Gate | Verdict | One line |
|---|---|---|
| 0 Fit | PASS | Ongoing product with a steward, resources, a multi-year horizon, and measurable outcomes |
| 1 Baseline | PASS | Clearly good: $211k TTM (+19.5%), profitable, pays the founder. Leading indicators are weakening |
| 2 Level 5 Leadership | CONDITIONAL | Humble and craft-driven, but no successor and a habit of explaining numbers away |
| 3 First Who | CONDITIONAL | No misaligned seats, but key seats are missing and the founder is overloaded |
| 4 Brutal Facts | CONDITIONAL | Facts surfaced and none contradict Gate 1, but there's no red-flag mechanism yet |
| 5 Hedgehog | CONDITIONAL | A real intersection (spec compliance × studio seats × craft), but studio retention is unverified |
| 6 Discipline | PASS | Nine stop-doing items, disciplines and boundaries defined |
| 7 Technology | PASS | Auto-align is parity, spec tech accelerates, Linux and the web app are dropped |
| 8 Flywheel | PASS | The loop closes. Doom-loop risk is high if Lite proceeds |
| 9 Built to Last | PASS | Ideology, one-line BHAG, mechanisms listed |
| 10 Mighty Fall | PASS | Decline register built. Stages 2 and 3 are already showing early signs |

Count from the table: **7 PASS, 4 CONDITIONAL, 0 FAIL** (11 gates). That's fewer than half CONDITIONAL, but all four share the two root problems above.

---

## Appendix: gate artifacts not shown above

**Gate 0: Subject card.**
- Name: Linewright.
- Type: product (desktop app, Windows and Mac).
- Leader/steward: the solo founder.
- Horizon: years (fourth year on sale).
- Stage: profitable, growth slowing, and a free competitor is adding the headline feature.

**Gate 1: Baseline sheet.**
- *Evidence of good:* $211.4k TTM revenue, up from $176.9k. Costs about $31k. Founder paid about $120k. $88k cash. About 3,400 licenses sold. 39 studios with 638 seats (average ~16; the largest, 74 seats, is ~12% of seats and ~$7.3k/yr). TTM new licenses ≈ 750 at list price `[ASSUMPTION: no discounts]`. Recurring revenue (studio plus renewals) = $114.1k, or 54%.
- *Great means* (product: category-defining, durable usage):
  - Superior performance: the go-to pro tool for spec-compliant subtitles, with high studio retention.
  - Distinctive impact: if Linewright vanished, studios' QC rejections would rise and no free or cloud tool would fill the gap.
  - Endurance: survives the founder's absence and Lantern's free auto-align.
- *Caveat:* the 19.5% growth is a lagging figure, partly from the price rise. Same-quarter sales and renewals are both falling.

**Gate 2: Leadership read.**
- *Strengths:* deep craft credibility, frugal (cash retained), listens to customers (survey, studio calls), credits others (the Lisbon translator).
- *Gaps:* explains away bad numbers; does every role; no successor; indecision across four options.
- *Behavior change:* each month, write the numbers before the explanations and walk through them with the accountant.

**Gate 6: Disciplines and framework.**
- *Non-negotiables:* a monthly release with at least one spec-checker or studio improvement; spec-profile updates shipped within an agreed window after a broadcaster changes rules `[ASSUMPTION: e.g., 14 days]`; a monthly segment-split metrics review.
- *Framework:* contractors and future hires work freely within one test: does this improve first-pass QC or studio retention?
- *Bureaucracy check:* the licensing friction is a system defect being absorbed by hand, not a people problem.

**Gate 7: Tech triage.**

| Technology | Call |
|---|---|
| Spec checker / shared style profiles | **Accelerates** |
| SSO, admin console, per-studio reporting | **Accelerates** |
| Auto-alignment (speech models) | **Parity**: keep up, don't compete on it |
| Licensing / activation system, code signing | **Parity**: fix so it stops generating tickets |
| Linux port | **Irrelevant**: drop |
| Web app for creators | **Irrelevant here**: hype-driven, drop |

*Pioneer opportunities:*
1. Use speech models for **QC**, not alignment: flag text/audio mismatches and spec violations before delivery.
2. **Spec-as-code**: machine-readable, versioned broadcaster profiles that studios share and freelancers receive.

**Gate 9: Clock-building mechanisms.**
- Documented spec-library process with change log.
- Automated build and release a second person can run.
- Self-service licensing and support runbooks.
- Codebase access and documentation for the contractor.
- Source-code escrow offered to studios, which also addresses their single-founder worry `[ASSUMPTION]`.