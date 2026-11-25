## Verdict

**Hedgehog Concept (working hypothesis):** Linewright makes professional subtitle files pass a broadcaster's delivery spec the first time, and earns its living per renewing seat.

**Weakest flywheel link:** "Fewer QC rejections → studios renew and add seats." Only two anecdotes support it, and your renewal number doesn't separate studios from individuals.

**Top three stop-doing items:** (1) the creator web app ("Linewright Lite"); (2) the Linux port; (3) selling auto-align as the reason to buy.

**Most urgent brutal fact:** Renewals have fallen four quarters in a row (64→52%). They have gone past your modeled 58% floor. Lantern's free auto-align, the top reason individuals buy, reaches stable release this winter.

**Numbers that would change this answer:** renewal split into studio seats and individual plans, net studio seat change, and verified QC-rejection data.

**Confidence:** moderate. The verdict rests on your own notes. If studio seats are leaking as fast as individual plans, the Hedgehog Concept is wrong.

Greatness potential: 28/100

---

*Run notes: autonomous mode. This session has no memory, past chats, or web search. There is no prior baseline, and competitor and market claims were not researched. The dossier is the only evidence. Inferences are marked `[ASSUMPTION]`.*

## 1. The great version in one paragraph

When Linewright is great, it is the tool a studio points to when a broadcaster asks how it knows every file will pass. Each studio sets a broadcaster's rules once in a shared style profile. Every freelancer working for that studio delivers files that pass QC the first time. The studio renews without thinking about it and adds seats as it grows. Freelancers who learned Linewright on studio jobs keep their own licenses because the update plan carries a living library of current delivery specs. Free tools can't match that library, because it is built and maintained by someone who has done the job. Auto-align is just expected, the same as in every tool. Linewright wins on compliance and on a fast keyboard-first editor. The business no longer depends on one person working 50-hour weeks. A second person can ship builds and handle support, and the founder spends most of their time on the spec engine.

## 2. The Hedgehog Concept

**Sentence:** *Linewright makes professional subtitle files pass a broadcaster's delivery spec the first time, and earns its living per renewing seat.*

| Circle | Candidates considered | Kept | Ruled out, and why |
|---|---|---|---|
| **Best in the world at** | Auto-align; keyboard-only timing editor; low price vs. enterprise; delivery-spec compliance plus shared style profiles | **Delivery-spec compliance for professional subtitle work**, with a fast keyboard editor as the craft layer | Auto-align: speech-model alignment is becoming free (Lantern) and will be parity. Creator captioning: a mass market with a different customer and a web stack, where an 11-year pro subtitler has no edge `[ASSUMPTION: platform auto-captions already crowd it; not researched]`. Enterprise workflow: the cloud platform owns it. |
| **Economic engine** | Profit per license sold; per studio account; per renewing seat | **Profit per renewing seat** (studio seats and individual update plans) | Per license sold rewards a one-time sale. That is exactly the segment shrinking (Q3 −23% YoY) and the one most exposed to Lantern. |
| **Passion** | Professional subtitling craft; building a business; reaching creators | **The craft and quality of professional subtitling.** You built the tool out of 11 years of frustration as a freelancer. `[ASSUMPTION: inferred from the founding story; the notes show no enthusiasm for the creator product, only pressure]` | Creator growth is Marisol's passion, not evidence of yours. |

**Denominator:** profit per renewing seat. Studio seats ($99/yr, low support load) weigh most. Individual update plans count if they renew because of specs, not because of alignment.

**Why the bet is uncomfortable (a good sign):** individuals bring in about 70% of revenue ($97.3k new + $50.3k renewals). Studios bring in about 30% ($63.8k). The Hedgehog Concept builds around the smaller segment. It does not abandon individuals: QC against delivery specs was already the #2 purchase reason for them (41%). It is the bridge between the two segments.

**Confirmation tests (each must pass to keep the hypothesis):**
1. When split out, studio seat renewal comes in clearly above individual renewal. `[ASSUMPTION threshold: ≥85%]` If studio seats renew at roughly 52% as well, return to this gate.
2. Three to five studios supply before/after QC rejection data showing a material drop. `[ASSUMPTION: ≥40%]`
3. Individual users who rely on spec presets renew at a higher rate than those who don't.
4. Studio renewals hold steady through the quarter after Lantern's stable release ships auto-align.

## 3. The flywheel

```
  ┌─► 1. Encode more broadcaster / streamer delivery specs as presets
  │          │   (founder's 11 years of spec knowledge)
  │          ▼
  │   2. Studios set one shared style profile → freelancer files
  │      pass QC the first time (fewer rejections)
  │          │
  │          ▼
  │   3. Studios renew and add seats  ── profit per renewing seat ↑
  │          │
  │          ▼
  │   4. Freelancers who learned Linewright on studio jobs buy and renew
  │      individual plans for the living spec library
  │          │
  │          ▼
  │   5. Cash plus rejection data fund spec coverage and free the
  │      founder from support (the second seat)
  └──────────┘
```

**Weakest link:** 2→3. Only two studio managers' unverified "more than half" claims support it, and the renewal metric can't show whether studios are holding. Link 4 is also `[ASSUMPTION]`: nothing in the dossier shows studio exposure turning into individual purchases.

**Current push (next one or two turns):**
1. **Measure the loop.** Split renewals by segment and cohort, and get before/after rejection numbers from studios.
2. **Turn link 2→3 into product.** Build SSO, an admin console, and a per-studio QC report that shows the studio its rejection rate. The report is both the value and the proof.

**Doom-loop check: early signs are present.**
- *Four directions under consideration at once* (creator product, studio push, Linux, backlog). This is the start of chasing a new direction each time.
- *A big program to jump-start momentum:* a six-month web app for a different market, proposed just as the core shows strain.
- *Reaction without understanding:* the January price rise was modeled, but the miss against the model has been explained away, not investigated.
- *Drift:* the last two releases were bug fixes, and the backlog has 140 untriaged items.

None of these is fatal yet. The creator product is the one that would tip the business into the doom loop.

## 4. The bus

| Person / commitment | Call | Reasoning |
|---|---|---|
| **You (founder)** | **Keep, move seat** | You are in the support seat (30 tickets a week, mostly install and licensing) and the bug-fix seat. Your highest-value seat is spec engine plus studio product. |
| **Mac contractor** | **Keep, consider expanding** | The likeliest candidate to become the second person who can ship a full release. |
| **Accountant** | **Keep** | Right seat, and the clearest strategic read in the dossier ("the only part that compounds"). |
| **Lisbon translator** | **Keep, bring closer** | She translated the whole UI unpaid. Thank her properly (a lifetime license plus payment or a gift `[ASSUMPTION]`) and ask if she'd maintain the localization. This is a model for community contributors. |
| **Forum regulars** | **Keep** | Your early-warning system on Lantern. Ask them directly what would make them stop renewing. |
| **Marisol (as Lite partner)** | **Off this bus** | She's a capable operator, but her agency's interest (creator reach, revenue share) points away from this Hedgehog Concept. Keep the friendship and decline the build. This is a statement about fit for this endeavor, not about her. |
| **Linux requests (46)** | **Off** | A commitment that would eat capacity with no link to the denominator. |
| **140-item backlog** | **Move seat** | Triage it against the Hedgehog Concept. Close anything outside it, publicly and kindly. |
| **Missing: part-time support/ops person** | **Missing (first hire)** | Takes the install and licensing load and becomes the start of "works without the founder." |
| **Missing: studio-facing role** | **Missing (later)** | Hold off on the salesperson. When in doubt, don't hire. Revisit once the QC report and renewal split prove the studio loop. If you do hire, look for someone with studio QC or ops background, not a generalist seller. |

## 5. Stop-doing list

1. **Stop considering Linewright Lite.** It needs six months of solo time in a different market with a different stack, right when Lantern ships. The waitlist shows interest, not willingness to pay. At an `[ASSUMPTION]` 5% waitlist-to-paid conversion, 2,310 signups is about 115 subscribers. At $8/month that is roughly $11k a year before Marisol's revenue share. The "50x market" figure comes from a deck written by someone who would share the revenue.
2. **Stop the Linux port.** 46 forum requests don't touch the denominator.
3. **Stop leading with auto-align.** Keep it at parity and keep improving it quietly, but stop marketing it as the reason to buy. Within months it will be the reason not to.
4. **Stop reporting renewal as one blended number.** It hides which business is leaking.
5. **Stop answering install and licensing tickets by hand.** Fix the causes (installer, self-service license recovery and transfer) and route the rest to the support hire.
6. **Stop shipping bug-fix-only releases from an untriaged backlog.** Every release moves the spec engine forward.
7. **Stop explaining year-over-year drops as seasonal.** Q3 vs. Q3 is already a same-season comparison.
8. **Don't cut price to fight Lantern.** You can't win a price war with free.

**Non-negotiable disciplines:**
- Every release ships at least one spec-checker or style-profile improvement.
- A monthly metrics review: renewal by segment and cohort, net studio seats, support tickets reaching the founder.
- Requested broadcaster specs become presets within a fixed window `[ASSUMPTION: 4 weeks]`.
- At least one full week off per quarter, as a test that the business can run without you.

**Freedom within a framework:** the contractor and the support hire act on their own within the release checklist and the support playbook. Any feature outside the Hedgehog Concept gets a default "no" until it passes the three-circle test. **Bureaucracy check:** none yet. You're solo, so the risk is too little process, not too much.

## 6. Brutal facts and faith statement

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | Renewal has declined four quarters in a row and hasn't settled where you modeled it. | 64→58→55→52%. Modeled floor was ~58%. | **High** | Founder |
| 2 | You can't tell which segment is leaking. | Renewal blends studio and individual. | **High** | Founder + accountant |
| 3 | The top reason individuals buy is about to be free. | Auto-align is cited by 69% of buyers. Lantern's nightly builds have it, and the stable release is due "this winter." | **High** | Founder |
| 4 | New individual sales are down year over year, and seasonality doesn't explain it. | Q3: 161 vs. 209 (−23%), same season. | **High** | Founder |
| 5 | The business is one tired person. | 50 hrs/week, one week off this year, 30 tickets/week, two bug-fix releases in a row, 140-item backlog. | **High** | Founder |
| 6 | The studio value claim is unverified. | Two anecdotes of "more than half" fewer rejections. | Medium | Founder |
| 7 | Customer insight is skewed toward individuals. | 214 survey responses, nearly all individual. Studio input comes only from calls. | Medium | Founder |
| 8 | The creator opportunity's evidence is weak and comes from an interested party. | Waitlist ≠ payment. The "50x" claim is from a partner's deck. | Medium (as a distraction) | Founder |

Revenue grew 19.5% ($176.9k → $211.4k), but the leading indicators (new licenses, renewals) are falling. The growth may partly reflect the January price rise `[ASSUMPTION: prior-year mix not in the dossier]`. This doesn't contradict Gate 1. Linewright is good. It does mean "good" is not stable.

**Truth climate:** you are honest in your notes, but twice you reach for a comforting story ("summer is always slow," "expected it to settle"). The missing red-flag mechanism is a split metric reviewed monthly.

**Faith statement:** Free tools can copy alignment, but they can't copy 11 years of knowing what makes a file pass a broadcaster's QC. Linewright will prevail by owning that.

## 7. Core ideology and the BHAG

**Core values:**
1. The file has to pass. Quality to spec *is* the product.
2. Built by people who've done the job.
3. Speed through craft (keyboard-first, no friction).
4. Fair dealing: honest pricing, a tool you own.

**Core purpose:** Let subtitlers spend their time on the craft, not on rework and rejections.

**BHAG (one line, given the solo, small-scale context):** Within 15 years, "delivered through Linewright" is what broadcasters and studios accept as proof that a subtitle file meets spec.

**Clock-building mechanisms:**
- A written release process the contractor can run end to end on both platforms.
- A support playbook and self-service licensing.
- A spec-preset pipeline that studios and community members can contribute to, reviewed against a checklist.
- A monthly metrics review that doesn't depend on your judgment to raise red flags.

## 8. Scorecard

| Output | Current | 12-month target | BHAG trajectory |
|---|---|---|---|
| **Studio recurring revenue / seats** | $63.8k · 638 seats · 39 studios | `[ASSUMPTION]` ~$85k · ~850 seats | Becomes the majority of revenue. Every major broadcaster spec is available as a preset. |
| **Renewal rate, by segment** | 52% blended. **Split unknown.** | Split measured within 30 days. Decline stopped. `[ASSUMPTION]` studio seats ≥90%, individual ≥50% after Lantern ships | Renewal driven by the spec library, holding regardless of free alignment tools |
| **Verified QC-rejection reduction at studios** | Two unverified anecdotes ("more than half") | Before/after data from ≥5 studios, built into the per-studio QC report | Rejection data becomes Linewright's proof to broadcasters |

*Watched input (not scored):* tickets reaching the founder each week. Currently ~30, target <10.

## 9. Next 90 days

| # | Action | Owner | Flywheel link |
|---|---|---|---|
| 1 | **Weeks 1–2:** Split renewals by segment and by cohort (before vs. after the January price change). Pull net studio seat change for the year. Decision rule: if studio renewal is close to individual renewal, re-run Gate 5 before building anything. | Founder + accountant | Measures 2→3 |
| 2 | Fix the top three install and licensing ticket causes. Hire a part-time support/ops person `[ASSUMPTION: affordable from ~$60k annual surplus after founder pay plus $88k cash]`. Take a full week off in the quarter to test whether the business runs without you. | Founder | 5→1 (frees founder) |
| 3 | Ship SSO, an admin console, and a **per-studio QC report**. Collect before/after rejection data from 3–5 studios, starting with the two that made the claim and the three that asked for SSO. | Founder; Mac contractor for builds | 2→3 |
| 4 | Reposition before Lantern's stable release. Lead the site and messaging with "passes spec first time." Present the individual update plan as access to the current spec library. Keep auto-align at parity and leave the price alone. | Founder | 1→4 |
| 5 | Decline Lite warmly and clearly. Send the Lisbon translator a proper thank-you. Close out-of-scope backlog items, including Linux, with a public note. | Founder | Protects the loop |

## 10. Re-check

I can set up a scheduled re-check for about 90 days out (end of Q4, Year 0, shortly after Lantern's stable release). It would re-score the scorecard with real numbers, including the renewal split, and re-run Gates 1, 5 and 8. Without that check, nobody will know whether this Hedgehog Concept was right.

## 11. Risk register

| Source | Risk | Condition / early warning | Evidence that clears it |
|---|---|---|---|
| Gate 2 (CONDITIONAL) | The founder is a single point of failure. | No one else can ship a release or run support. | A two-week founder absence with no customer-visible incident. |
| Gate 3 (CONDITIONAL) | The founder is in the wrong seat (support and bug fixing). | Tickets reaching the founder stay above ~10 a week. | Support hire in place and ticket causes fixed. |
| Gate 4 (CONDITIONAL) | The renewal decline is undiagnosed. | The metric is still blended. | Renewal split by segment and cohort, reviewed monthly. |
| Gate 5 (CONDITIONAL) | The Hedgehog Concept may be wrong if studios leak too. | Studio renewal close to 52%, or no rejection data. | Confirmation tests 1 and 2 pass. |
| Decline 1: Hubris | 19.5% revenue growth breeds "it'll settle" thinking. | Metric misses explained by stories, not data. | — |
| Decline 2: Undisciplined pursuit of more | Lite, Linux, enterprise features. | A second codebase or new market started. | — |
| Decline 3: Denial of risk | Lantern written off as "rough." | Renewals keep falling after Lantern's stable release with no response. | — |
| Decline 4: Grasping for salvation | A panic price cut, a sudden pivot to creators, or selling out to the cloud platform. | A new strategy proposed within one quarter of a bad number. | — |
| Decline 5: Capitulation | Founder burnout puts the product into maintenance mode. | Another year of bug-fix releases and under two weeks off. | — |

**Shared root problems:** all four CONDITIONALs trace back to two issues: **(a) everything depends on the founder's time**, and **(b) a blended renewal metric that hides what's happening.** Fixing those two clears most of the register. The business is currently drifting between decline stages 1 and 2, and the creator product is the stage-2 move.

## 12. Gate log

| Gate | Verdict | Note |
|---|---|---|
| 0 Fit | PASS | Ongoing product, a steward, 4 years in, measurable. |
| 1 Baseline | PASS | Good, not yet great. Profitable and growing, but endurance fails (solo founder). |
| 2 Level 5 Leadership | CONDITIONAL | Craft-driven, owns decisions, but the business can't survive the founder's absence. |
| 3 First Who | CONDITIONAL | No one misaligned, but the founder is in the wrong seat and the support seat is empty. |
| 4 Brutal Facts | CONDITIONAL | Facts confronted. Red-flag mechanism (split renewal) missing. |
| 5 Hedgehog | CONDITIONAL | Real intersection exists. Studio renewal and rejection data unverified. |
| 6 Discipline | PASS | Eight stop-doing items. Disciplines set. |
| 7 Technology | PASS | Alignment at parity. Spec engine is the accelerator. |
| 8 Flywheel | PASS | Loop closes. Weakest link 2→3 logged under Gate 5. |
| 9 Built to Last | PASS | One-line BHAG. Clock mechanisms listed. |
| 10 Mighty Fall | PASS | Drifting between stages 1–2. Warnings set. |

Tally from the table: 7 PASS, 4 CONDITIONAL, 0 FAIL (11 gates).

---

### Appendix: gate artifacts

**Subject card (Gate 0):** Linewright · Product (solo-founder desktop software, Windows and Mac) · Steward: the founder · Horizon: years (4 so far) · Stage: established and profitable, with leading indicators softening.

**Baseline sheet (Gate 1):**
- *Evidence of good:* $211.4k trailing-12-month revenue (+19.5%), ~$31k costs, founder paid ~$120k, ~$88k cash, 3,400 licenses sold, 39 studios / 638 seats, studios renewing.
- *Three tests of great:*
  - Superior performance: not yet.
  - Distinctive impact: plausible for studios (spec plus shared profiles), weak for individuals once alignment is free.
  - Endurance: fails (one person).

**Leadership read (Gate 2):**
- *Strengths:* deep domain credibility, honest self-notes, modeled the price change instead of guessing.
- *Gaps:* explains misses with stories, has spread attention across four options, and is the business's only operator.
- *One behavior change:* each month, read the split metrics before writing any interpretation of them.

**Tech triage (Gate 7):**

| Technology | Class |
|---|---|
| Spec-checker engine, shared style profiles, per-studio QC report, SSO / admin console | **Accelerates** |
| Speech-model auto-align; installer and licensing automation | **Parity** (licensing work has high leverage on founder time) |
| Linux port; creator web app | **Irrelevant here** (the web app is hype-driven by the waitlist) |

*Pioneer candidates:* (1) machine-readable delivery specs ("spec as code") that studios can share and audit; (2) QC-rejection analytics across studios.