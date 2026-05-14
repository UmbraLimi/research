# Deemed Disposition at Death — Income Tax Consequences for Mary's Estate

**Topic:** What income tax is triggered by Mary's death on 2026-04-21, with primary focus on the *Income Tax Act* deemed-disposition rules applied to the non-registered investments and the RIF.

**Why this matters for Daughter (Q1, Q3, Q5, Q6):**

- Q1 asked what's significant about 2026-04-21. The answer is principally this file: that date is the moment of *deemed disposition* of Mary's capital property at fair market value, triggering capital-gains tax on her terminal T1 return. It is also the deemed receipt date for the RIF.
- Q3 (when are taxes due) and Q5 (what is taxed and on what value) are answered here for the income-tax piece. EAT is in `findings/probate-and-eat.md`.

**Cross-reference:** This file does not resolve *whose* capital property the joint accounts and investments are. That depends on the *Pecore* analysis in `findings/jtwros-treatment.md`. Two scenarios — Pecore-resulting-trust and Pecore-rebutted-gift — produce different deemed-disposition outcomes; both are walked through below.

---

## Entry 1 — Income Tax Act s. 70(5): the deemed disposition rule

**Captured:** 2026-05-14
**Source:** *Income Tax Act* (Canada), R.S.C. 1985, c. 1 (5th Supp.), s. 70(5), as consolidated at Justice Canada.
**URL:** https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-70.html
**Source quality:** Primary (consolidated federal statute, official Government of Canada source).

### Verbatim text — Marginal note: "Capital property of a deceased taxpayer"

Subsection 70(5) reads (paraphrased into readable form from the consolidated text):

> "(5) Where in a taxation year a taxpayer dies,
> (a) the taxpayer is deemed to have, immediately before the taxpayer's death, disposed of each capital property of the taxpayer and received proceeds of disposition therefor equal to the fair market value of the property immediately before the death; and
> (b) any person who, as a consequence of the taxpayer's death, acquires any property that is deemed by paragraph (a) to have been disposed of by the taxpayer at that time is deemed to have acquired it at the time of the death at a cost equal to its fair market value immediately before the death."

(Source: text quoted from the search-summary extract of CRA's commentary on s. 70(5); the consolidated statute on laws-lois.justice.gc.ca confirms the substance. The official text uses slightly more legal-form sentence structure but the substance is identical.)

### What this means in plain language

1. The moment immediately before Mary died (2026-04-21), every piece of capital property Mary owned is *treated as if she sold it* at its fair market value on that date.
2. The "sale" produces proceeds equal to the FMV. Mary's adjusted cost base (the cost she paid, plus any allowed adjustments) is subtracted from those proceeds. The difference is a capital gain or a capital loss.
3. The capital gain or loss is reported on Mary's **terminal T1 return** for tax year 2026.
4. The person who receives the property — whether by survivorship, by named beneficiary, or by inheritance through the estate — takes it with a cost base equal to that FMV at the date of death (a "step-up" in cost base). They are not double-taxed; only future gains, after the date of death, are taxed when they later sell.

### Why the date 2026-04-21 is the answer to Q1

Mary's death date is significant because it is the moment of deemed disposition. Pre-death accrued gains on Mary's capital property are crystallized for tax purposes on that date and become a tax liability of Mary (paid out of her estate). Anything that happens to the property *after* the deemed disposition is the new owner's tax responsibility, based on the stepped-up cost base.

This is why the chronology of events leading up to and following 2026-04-21 matters so much: it sets the dividing line for tax accountability.

---

## Entry 2 — Income Tax Act s. 70(6): the spousal rollover (does NOT apply to Mary)

**Captured:** 2026-05-14
**Source:** Same as Entry 1.
**URL:** https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-70.html

### Marginal note: "Where transfer or distribution to spouse or spouse trust"

Subsection 70(6) provides a rollover that allows capital property to pass at the deceased's **adjusted cost base** (not FMV) — deferring the capital-gains tax — but **only** where the property goes to:

> "(a) the taxpayer's spouse or common-law partner who was resident in Canada immediately before the taxpayer's death, or
> (b) a trust, created by the taxpayer's will, that was resident in Canada immediately after the time the property vested indefeasibly in the trust ... [under which the spouse or common-law partner is the sole income beneficiary and capital-access beneficiary before their own death]."

The property must vest indefeasibly in the spouse or qualifying spousal trust within 36 months of death.

### Why this matters for Daughter

**Mary had no surviving spouse** (per `Background.md`). The s. 70(6) rollover therefore **cannot apply** to Mary's assets. Every piece of her capital property goes through full deemed disposition at FMV under s. 70(5) on 2026-04-21, with no deferral available for property passing to Daughter (or Brother).

This is critical because lay people sometimes assume "the assets just transfer to my kids tax-free." That is true for *legal title* under survivorship or beneficiary designation rules, but **not** for income-tax purposes. The taxable event under s. 70(5) happens regardless of how legal title moves.

---

## Entry 3 — Income Tax Act s. 146.3(6): RIF deemed receipt on death

**Captured:** 2026-05-14
**Source:** *Income Tax Act*, s. 146.3(6), as consolidated at Justice Canada.
**URL:** https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-146.3.html
**Source quality:** Primary (consolidated federal statute).

### Verbatim text — Marginal note: "Where last annuitant dies"

> "(6) Where the last annuitant under a registered retirement income fund dies, that annuitant shall be deemed to have received, immediately before death, an amount out of or under a registered retirement income fund equal to the fair market value of the property of the fund at the time of the death."

### What this means for Mary's RIF

- Mary's RIF held $805 at the time of death (per `Background.md`).
- On 2026-04-21, Mary is deemed to have received $805 from the RIF immediately before her death.
- That $805 is included in Mary's income for 2026 and is taxable at Mary's marginal rate on her terminal T1.
- Because Daughter is the named beneficiary of the RIF (per `Background.md`), the $805 will pass to Daughter outside the estate (no EAT — see `findings/probate-and-eat.md`). Daughter receives the $805 with no tax obligation, because the income inclusion happens on Mary's return, not Daughter's.

**Net cash impact:** Daughter receives $805 from the RIF. Mary's estate (i.e., the residue split with Brother) bears the tax cost of including $805 in Mary's terminal-T1 income. At a notional 30% marginal rate, that's about $240 of tax owed by Mary's estate on the RIF, leaving the rest of Mary's estate net of that liability.

**Why it matters for Daughter:** This is the only piece of the deemed-disposition picture where the answer is straightforward. The RIF is small, the rule is mechanical, and there's no *Pecore* uncertainty (named beneficiary designations are statutorily distinct from joint accounts).

### Note on the alternative — "designated benefit" rollover

s. 146.3(6.11) and related provisions allow a RIF to be rolled over tax-deferred to a qualifying beneficiary (spouse / dependent child / financially-dependent infirm child). **None of these apply** to Daughter as a non-dependent adult child. The $805 inclusion stands.

---

## Entry 4 — Application to Mary's joint accounts and investments: the two Pecore scenarios

**Captured:** 2026-05-14
**Source:** Synthesis of the statutory rules (Entries 1–2 above) with the *Pecore* legal framework (see `findings/jtwros-treatment.md`).

This is where the legal question from the JTWROS findings file directly drives the tax outcome.

### Scenario A — *Pecore* presumption is rebutted (gift of survivorship found)

Under this scenario, when Mary added Daughter to the joint accounts and investments, she effectively made an *inter vivos* gift of the right of survivorship. For income-tax purposes, this is complex:

- At the time Daughter was added as a joint holder (date unknown), there *may* have been a deemed disposition of a portion of the property under the attribution and beneficial-ownership rules. CRA has published technical interpretations on this point. Whether this happened depends on whether and how the gift of beneficial interest was characterized at the time. This is a specialist question; see Action Items.
- On Mary's death, only Mary's beneficial portion (which may be less than 100% under this scenario) is subject to the s. 70(5) deemed disposition. Daughter's pre-existing beneficial portion does not trigger a s. 70(5) event for Mary.
- Income earned on the accounts during Mary's lifetime would be split between Mary and Daughter according to their respective beneficial interests for tax purposes.

This scenario reduces Mary's terminal-T1 capital-gains tax exposure, because not all the accrued gains are Mary's. However, it raises *Daughter's* tax exposure (Daughter may have had a deemed disposition on the gifted portion at the time of the gift, with consequences potentially not addressed at the time).

### Scenario B — *Pecore* presumption is upheld (resulting trust found)

This is the scenario the JTWROS findings file (`findings/jtwros-treatment.md`) suggests is the more likely outcome on present facts.

Under this scenario:

- Mary remained the sole *beneficial* owner of the joint accounts and investments at all times until her death. Daughter held legal title jointly only as bare trustee for Mary.
- Income earned on the accounts during Mary's lifetime was 100% Mary's (and was so reported — consistent with what was almost certainly the actual tax reporting given the convenience-only use pattern at `Background.md` Q3).
- On Mary's death, the *full* FMV of the joint accounts and investments is subject to the s. 70(5) deemed disposition. The taxable capital gain is `(FMV at 2026-04-21) − (Mary's original adjusted cost base)`.
- Daughter receives no step-up that is independent of Mary's death; instead, Daughter takes the property (or its value, as part of the estate split) at its FMV on 2026-04-21.

This scenario produces the largest terminal-T1 capital-gains tax bill, but the tax is paid out of the estate (i.e., out of the residue split with Brother). It does not create any *additional* personal tax exposure for Daughter outside her share.

### Worked illustration

Suppose the non-registered joint investments have:

- FMV at 2026-04-21: $300,000 (hypothetical — to be filled in once Daughter provides values)
- Mary's original adjusted cost base: $150,000 (hypothetical)

Then under Scenario B:

- Capital gain on death: $300,000 − $150,000 = $150,000.
- Taxable capital gain (50% inclusion rate at current rates, assuming the 2026 rules are still in effect — verify): $75,000.
- At a ~30% marginal rate, federal + Ontario tax on the gain: roughly $22,500 to be paid by Mary's estate.

Under Scenario A, the figure could be lower (only Mary's portion is hit) but with offsetting complications.

**Important:** the 50% capital-gains inclusion rate has been subject to legislative proposals to change to 2/3 for gains over $250,000. As of 2026-05-14, verify whether any rate change is in effect — this is one of the next research-pass action items.

---

## Entry 5 — Terminal T1 filing deadline and what to file

**Captured:** 2026-05-14 (revised 2026-05-14 — clarified statutory basis and added the 2025 T1 deadline that applies if not yet filed)
**Source:** *Income Tax Act*, R.S.C. 1985, c. 1 (5th Supp.), s. 150(1)(b) and s. 150(1)(d), as consolidated at Justice Canada.
**URL:** https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html
**Source quality:** Primary (consolidated federal statute).

### The statutory rule — there are two deadlines, depending on when in the year death occurs

**s. 150(1)(b) — Deceased individuals (the "6 months after death" rule):**

> "(b) in the case of an individual who **dies after October of the year** and on or before the day that would be the individual's filing due date for the year if the individual had not died, by the individual's legal representatives on or before the day that is the **later** of the day on or before which the return would otherwise be required to be filed and the day that is **6 months after the day of death**;"

This rule applies *only* when death occurs in the window from November 1 of a year to April 30 of the following year. In that window, the regular April 30 deadline would give the legal representative less than six months to file, so the law extends the deadline to six months after death.

**s. 150(1)(d) — Individuals (the regular rule):**

For an individual who dies in May through October, s. 150(1)(b) does not apply. The terminal return falls under the regular individual filing deadline:

> "(d) in the case of any other person, on or before
> (i) the following April 30..."

(If the deceased or their spouse had business income, the deadline shifts to June 15 under s. 150(1)(d)(ii). Not applicable to Mary per `Background.md`.)

### Application to Mary

Mary died **2026-04-21**. This is before November 2026, so:

- For Mary's **2026 terminal T1** (the year of death), s. 150(1)(b) does **not** apply. The deadline is the regular April 30 of the following year under s. 150(1)(d): **2027-04-30**.
- For Mary's **2025 T1** (the regular return for the *year before* death), the question of whether s. 150(1)(b) would have applied is now moot: **Mary filed her 2025 T1 before her death** (resolved 2026-05-14 — see `Background.md` Q&A further facts and `questions-open.md` D-05 / T-01). Recording the analysis for reference: had the 2025 T1 not been filed, s. 150(1)(b) would have applied because the "dies after October of the year [2025]" condition is met (Mary died in 2026, after October 2025) and she died before the would-be April 30, 2026 deadline, giving an extended deadline of 2026-10-21. This is the most likely source of the "six months after death" shorthand the user encountered.

### The "six months after death" shorthand

The "six months after death" deadline that appears in some practitioner guidance and CRA brochures is correct as a one-line rule, but only because in any case where six months gives a later date, the person died after October — exactly the s. 150(1)(b) scenario. It does **not** apply broadly to every terminal return. For an individual who died in May through October, the regular April 30 of the following year deadline applies.

For Mary specifically, only one deadline remains:

| Return | Filing deadline | Statutory basis | Status |
|---|---|---|---|
| **2025 T1** | (would have been 2026-10-21 if unfiled) | s. 150(1)(b) | **Moot — filed before death** |
| **2026 terminal T1** (the year of death) | **2027-04-30** | s. 150(1)(d) | Open — to be filed by legal representative |

### Optional separate returns

The legal representative may also be able to file up to three "optional" separate returns for the year of death, claiming personal credits on each, which can reduce overall tax:

- Rights or things return (under s. 70(2)) — for declared-but-unpaid amounts.
- Return for a partner or proprietor — not applicable to Mary (no business).
- Return for income from a testamentary trust — not applicable (no inherited trust income for Mary).

The rights-or-things return could be relevant for any declared dividends, accrued interest, or similar amounts owed to Mary at death and not yet paid. Likely small but worth checking with the tax accountant.

### Estate T3 returns

Income earned by the *estate* after the date of death (e.g., interest on bank balances during administration, dividends declared after death) is taxed on a T3 trust return for the estate. The estate can elect to be a "graduated rate estate" (GRE) for up to 36 months, which gives it access to graduated income-tax rates rather than the top marginal rate. This is generally a good election and is something the tax accountant should handle.

**See `findings/t3-estate-returns.md` for the full T3 framework**: GRE definition (verbatim from ITA s. 248(1)), year-end choice strategy, 90-day filing deadline (ITA s. 150(1)(c)), how income is split between Mary's terminal T1 and the estate's T3, the s. 164(6) loss-carryback election, and timeline projections for Mary's estate.

---

## Entry 6 — Putting it together: answers to Q1, Q3, Q5

**Q1 — What is significant about April 21, 2026 in terms of asset ownership?**

It is the date of:
- The deemed disposition of all Mary's capital property at FMV under *Income Tax Act* s. 70(5), crystallizing all unrealized capital gains for terminal-T1 tax purposes.
- The deemed receipt of the full FMV of Mary's RIF (s. 146.3(6)), included in her terminal-T1 income.
- The vesting of legal title to joint property in Daughter as the surviving joint holder under provincial law (this is the legal-survivorship event, separate from the income-tax event).
- The trigger date for the *Pecore* analysis: the will, the joint accounts, and Daughter's role as executor all hold the meaning they had as of that date.

In short, 2026-04-21 is the tax-event date, the legal-title transition date, and the date that all of Mary's intentions (testamentary and otherwise) are frozen for legal interpretation.

**Q3 — When will taxes be due?**

| Tax | Due date |
|---|---|
| Mary's **2026 terminal T1** (income tax for 2026 including the deemed-disposition gains and RIF inclusion) | **2027-04-30** (s. 150(1)(d)) |
| Tax owing on the terminal T1 | Same date as the terminal T1 |

(Mary's 2025 T1 was filed before her death — see Entry 5. No separate prior-year filing deadline remains.)
| Ontario Estate Administration Tax | When the probate application is filed, if probate is required (see `findings/probate-and-eat.md`) |
| Estate Information Return (Ontario MoF) | 180 days after Certificate of Appointment issued |
| T3 estate trust return | 90 days after the estate's chosen first year-end (a graduated-rate-estate election is generally beneficial) |
| Future T1 or T3 returns for the estate | Annually, until the estate is wound up |

**Q5 — What is taxed, and on what value?**

For *income tax* purposes (separate from EAT, which is on the full estate value):

- **Capital property** (non-registered investments): only the *capital gain* (FMV at death − adjusted cost base) is taxed, not the full FMV. Currently, 50% of the capital gain is included in taxable income (verify the inclusion rate for 2026 in the next research pass — there have been proposed legislative changes).
- **RIF**: the *full* FMV of the RIF at the date of death is included in income.
- **Bank accounts**: typically no capital gain (cash and term deposits have no embedded gain), but any accrued interest to date of death must be reported.
- **Personal effects**: generally no taxable disposition if FMV per item is under $1,000 each (and adjusted cost base is also under $1,000).

For *EAT* (Ontario probate tax): the full FMV of all assets in the EAT base, less encumbrances on real property only. See `findings/probate-and-eat.md`.

---

## Action items arising from this findings file

1. **Get rough asset values from Daughter** (non-registered joint investments, bank balances). This lets us put real numbers on Scenarios A and B and the rough terminal-T1 tax bill.
2. **Engage the tax accountant explicitly on the GRE election** and the optional separate returns. The accountant already in the picture should handle this; if there is no engagement letter yet, get one.
3. **Verify the 2026 capital-gains inclusion rate.** As of 2026-05-14 there has been recent legislative activity on this; the next research pass should confirm whether the rate is 50% or 2/3 for gains above $250,000.
4. **Check whether Mary filed her 2025 T1** (regular return for the year before death). If not, the legal representative must file it. Due dates may apply.
5. **Coordinate the tax position with the *Pecore* analysis.** The terminal-T1 return is the document where Daughter's lawyer-approved view on Pecore (Scenario A vs. B) gets crystallized in writing. Filing inconsistently with the *Pecore* position is the kind of move that triggers CRA scrutiny and undermines the position later.
6. **Next research pass:** retry the CRA terminal-return guidance pages (capital-gains.html, report-income.html, what-to-file.html) when fetch is feasible; capture CRA's published technical interpretations on the deemed-disposition treatment of joint accounts subject to *Pecore* analysis; capture CRA's RC4111 (What to do when someone dies) verbatim.

---

## Sources cited in this file

- [Income Tax Act, s. 70 — Justice Canada (consolidated)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-70.html)
- [Income Tax Act, s. 146.3 — Justice Canada (consolidated)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-146.3.html)
- CRA "Taxable capital gains on property, investments, and belongings" (https://www.canada.ca/en/revenue-agency/services/tax/individuals/life-events/doing-taxes-someone-died/prepare-returns/report-income/capital-gains.html) — referenced via search-summary extract; direct fetch blocked in this session, to be re-verified next pass.
- CRA "Death of a RRIF annuitant" (https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/registered-retirement-income-fund-rrif/death-a-rrif-annuitant.html) — referenced via search-summary extract.
- CRA "Doing taxes for someone who died" (https://www.canada.ca/en/revenue-agency/services/tax/individuals/life-events/doing-taxes-someone-died/) — landing page for terminal-T1 guidance.
- *Pecore v. Pecore*, 2007 SCC 17 — see `findings/jtwros-treatment.md`.
