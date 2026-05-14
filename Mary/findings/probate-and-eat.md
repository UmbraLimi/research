# Ontario Probate and Estate Administration Tax (EAT)

**Topic:** Whether Mary's estate requires a Certificate of Appointment of Estate Trustee ("probate"), how the Estate Administration Tax is calculated on what is included in the probate value, and what changes when the bank decides probate is/isn't required.

**Why this matters for Daughter (Q4, Q5, Q6 of `Background.md`):** Daughter has notified Mary's bank of the death and is waiting on the bank's decision about whether probate will be required. This findings file explains what the bank's decision will mean, what assets become subject to EAT if probate is required, and the downstream filing and timing consequences.

**Cross-reference:** This file assumes the *Pecore* analysis in `findings/jtwros-treatment.md`. If that analysis lands on resulting trust (likely on current facts), the joint accounts and investments fall back into the estate and become part of the probate base — significantly changing the EAT calculation. Read the two files together.

---

## Entry 1 — What probate is in Ontario, and when it is required

**Captured:** 2026-05-14
**Source:** Government of Ontario, "Apply for probate of an estate"
**URL:** https://www.ontario.ca/page/apply-probate-estate
**Date page last updated:** 2025-09-11
**Source quality:** Primary (official Government of Ontario page). Current.

### Verbatim definition

> "Probate is a procedure to ask the court to either:
> - give a person the authority to act as the estate trustee of an estate
> - confirm the authority of a person named as the estate trustee in the deceased's will and
> - formally approve that the deceased's will is their valid last will."

In Ontario, the documents produced are:
- **Certificate of Appointment of Estate Trustee** — for estates valued over $150,000
- **Small Estate Certificate** — for estates valued at $150,000 or less

Both are colloquially called "probate."

### When probate is required (per the same Ontario page)

> "Probate is not always required in order to administer an estate. The type of assets in the estate usually determine whether an estate should be probated. If the deceased owned real property or assets held by a financial institution, the estate normally must be probated."

> "A person may apply for probate if:
> - the deceased person died without a will
> - the deceased's will does not name an estate trustee
> - a financial institution wants proof of a person's legal authority to receive the money or investments of the deceased
> - the estate's assets include real property which does not pass to another person by right of survivorship
> - the deceased's real property must be sold ...
> - there is a dispute about who should be the estate trustee
> - there is a dispute or potential dispute about the validity of the will
> - some beneficiaries named in the will are not able to provide legal consent"

**Why it matters for Daughter:**

- The will exists and names Daughter as estate trustee, so probate isn't *automatically* required on that ground.
- Mary owned no real property (per `Background.md`).
- The triggering question for Mary's situation is the third bullet: **"a financial institution wants proof of a person's legal authority to receive the money or investments of the deceased."** This is what the bank is deciding right now.
- A latent fourth trigger is on the horizon: if Brother disputes the *Pecore* treatment of the joint accounts (per `findings/jtwros-treatment.md`), bullets 6–7 ("dispute about who should be the estate trustee" / "dispute about validity") could activate even though they don't apply today.

---

## Entry 2 — Ontario Estate Administration Tax: rate, calculation, and what is included

**Captured:** 2026-05-14
**Source:** Government of Ontario, "Estate Administration Tax"
**URL:** https://www.ontario.ca/page/estate-administration-tax
**Date page last updated:** 2026-01-02 (current)
**Source quality:** Primary (official Government of Ontario page).

### The rate (post-2020 regime — applies to Mary)

> "If you apply for an estate certificate on or after January 1, 2020:
> - You do not need to pay Estate Administration Tax if the value of the estate is $50,000 or less. However, you must still file an Estate Information Return within 180 calendar days after the estate certificate has been issued.
> - For estates valued over $50,000, the Estate Administration Tax will be calculated as $15 for every $1,000 (or part thereof) of the value of the estate.
> - The estate value is rounded up to the nearest thousand."

### Worked example from the Ontario page

> "for an estate valued at $240,000, the tax would be calculated as follows:
> - $0 per $1,000 for the first $50,000 of the estate
> - $15 per $1,000 for the remaining $190,000 of the estate
> - $240,000 − $50,000 = $190,000
> - $190,000 ÷ $1,000 = $190
> - $190 × $15 = $2,850"

**Why it matters for Daughter:** EAT is a flat 1.5% rate on the value of the probated estate over $50,000. It is not a tax on income or capital gains — it is essentially a court fee tied to issuing the certificate. The full income-tax piece is separate and handled on Mary's terminal T1 (see `findings/jtwros-treatment.md` Entry 4 and the future `findings/terminal-t1.md`).

### Assets that ARE included in the EAT calculation

The Ontario page lists, verbatim:

> - "real estate in Ontario, less encumbrances"
> - "bank accounts (includes foreign banks)"
> - "investments (for example, stocks, bonds, trust units, options, mutual funds, TFSAs, RRSPs, RRIFs, part of the RESP that the deceased subscriber was entitled to, RDSPs for which the deceased was a beneficiary)"
> - "vehicles and vessels ..."
> - "**all property of the deceased that was held in another person's name**" *(emphasis added — see commentary below)*
> - "all other property, wherever situated, including: goods; intangible property; business interests; insurance, if proceeds are left to the estate"

**Critical for Mary's situation:** The phrase "all property of the deceased that was held in another person's name" is exactly the language that captures property subject to a *Pecore* resulting trust. If a court (or the parties acting reasonably in light of *Pecore*) determines that the joint accounts and investments were beneficially Mary's despite being legally held jointly with Daughter, those assets are **included** in the EAT base by this listed category — not excluded under the next list.

### Assets that are NOT included in the EAT calculation

> - "assets that the deceased had before death but not at the time of death, such as insurance that will be paid to a named beneficiary"
> - "**assets where there is joint ownership that automatically become assets of the other owner(s)**" *(emphasis added)*
> - "real estate outside of Ontario"
> - "CPP Death Benefit"
> - "**RPPs, RRSPs, RRIFs and TFSAs with a beneficiary designation or beneficiary declaration**" *(emphasis added)*
> - "RDSPs to which the deceased subscribed to but was not a beneficiary"

**Why it matters for Daughter (and the Pecore intersection):**

- The exclusion for "assets where there is joint ownership that automatically become assets of the other owner(s)" is the *legal-title* survivorship exclusion. It applies cleanly only when the joint asset truly belongs beneficially to the survivor. If *Pecore* analysis finds a resulting trust, the asset legally passes to Daughter but beneficially belongs to the estate — and the EAT page's "property held in another person's name" inclusion (above) sweeps it in.
- The **RIF of $805** is excluded from the EAT base because Daughter is the named beneficiary. This is straightforward.
- The Ministry of Finance does not, on this page, address how a *Pecore* resulting trust interacts with the EAT inclusion/exclusion lists. In practice, this is a question for an Ontario estates lawyer — see Action Items below.

### Two scenario calculations for Mary

Joint accounts + non-registered investments total approximately **CAD $480,000** (D-02 confirmed 2026-05-14).

**Scenario A — Pecore presumption is rebutted (joint assets pass to Daughter, are excluded from EAT):**

- EAT base ≈ $0 (the $805 RIF passes by named beneficiary; no real estate; no other assets identified)
- **EAT ≈ $0**
- Probate may not even be required, depending on the BMO's decision (open question B-01)

**Scenario B — Pecore presumption stands (joint assets fall back into estate via resulting trust):**

- EAT base ≈ $480,000
- Calculation: ($480,000 − $50,000) ÷ $1,000 = 430; 430 × $15 = **$6,450**
- Probate almost certainly required (the joint assets are beneficially Mary's, the will needs to be administered, and the assets need to be re-collected into the estate for distribution per the will)

**Spread between Scenarios A and B in EAT terms: $6,450** — meaningful but not the dominant financial concern. The dominant financial concern is the capital-gains tax on the deemed disposition (see `findings/deemed-disposition.md` Entry 4), which could be in the range of ~$33,000 to ~$55,000 depending on Mary's adjusted cost base in the investments.

**Bottom line for EAT:** the actual EAT bill if probate is required is in the **single-digit thousands**, not the headline-grabbing range. EAT is the easier part of the tax exposure to plan around; the terminal-T1 capital-gains tax is the larger number.

### Non-deductible expenses

> "The following expenses, debts and payments cannot be deducted to reduce the total value of the estate:
> - funeral expenses
> - lawyer's fee
> - loans and interest payments
> - debt owed on a vehicle
> - credit card debts
> - real estate commissions
> - unregistered loans
> - line of credit"

(Mortgages and other registered encumbrances on real property can be deducted from the value of the real property, but Mary owned no real property, so this doesn't apply.)

---

## Entry 3 — Process and timing if probate is required

**Captured:** 2026-05-14
**Source:** Government of Ontario, "Apply for probate of an estate" (same URL as Entry 1).
**Source quality:** Primary.

### Documents required

> "Application (Form 74A)
> Affidavit of Service (Form 74B) or Lawyer's Certificate of Service (Form 74B.1)
> Affidavits, as required (the evidence that is required by legislation and the court rules ... for an application with a will, one of the following affidavits must be completed and it must attach the deceased's original will:
> Form 74D, an Affidavit of Execution of Will or Codicil
> or Form 74E, an Affidavit of Condition of Will or Codicil if the will was altered or marked in some way
> or Form 74F, an Affidavit attesting to the handwriting and signature of a holograph will for a holograph (handwritten) will
> Draft Certificate of Appointment of Estate Trustee (Form 74C)"

### Bond

A bond is generally required if (a) the deceased died without a will, (b) the applicant was not named as estate trustee, or (c) the applicant is not resident in Ontario / Canada / a Commonwealth country. **For Mary, none of these triggers apply** — Daughter is named as trustee in the will and is an Ontario resident. So no bond is expected to be required.

### Processing time

> "Applications are typically processed within 15 business days. It may take longer if:
> - you do not file all necessary documents or provide all necessary evidence and information
> - if the material filed raises an issue that requires a judge to make a decision."

### After the certificate is issued: Estate Information Return

> "Within 180 calendar days of receiving a certificate, you must file an Estate Information Return, which lists the value of the deceased's assets at the time of death with the Ministry of Finance."

**Why it matters for Daughter (Q3 and Q6):** Once a certificate is issued (if it is), Daughter has 180 days to file the Estate Information Return — a deadline separate from any income-tax filing. Penalties: "Estate representatives who do not file an Estate Information Return as required, or who make false or misleading statements on the return, may be fined at least $1,000 and up to twice the tax payable by the estate, imprisoned up to two years, or both."

---

## Entry 4 — What it means when the bank decides probate is / is not required

**Captured:** 2026-05-14 (revised 2026-05-14 — added probate-scope distinction and BMO context after user question on whether the bank's decision affects only the bank's funds or all of Mary's assets)
**Source:** Synthesis of Ontario page (Entry 1) + general estates-practice understanding. Marked as researcher's note pending Daughter's lawyer's input.

### BMO context for Mary

BMO holds approximately **$10,000** across Mary's chequing and savings accounts (per `Background.md`). BMO is currently deliberating whether to require a Certificate of Appointment before releasing those funds. The basis for that deliberation is not yet known and is worth asking BMO directly — see `questions-open.md` B-01 and B-05.

In practice, Ontario banks apply their own internal thresholds. Each major Canadian bank has a "small-balance" exception under which they will release funds to the estate trustee without requiring probate, typically capped somewhere between $25,000 and $100,000 (varies by institution and is subject to change). Above that threshold, the bank will require either:

- a Certificate of Appointment of Estate Trustee, or
- a Small Estate Certificate (if the estate qualifies, i.e., ≤$150,000), or
- an indemnity / risk-acceptance form from the heirs.

For accounts held **jointly with right of survivorship**, banks normally do *not* require probate at all — the funds are released to the surviving joint holder on production of a death certificate. The fact that BMO is deliberating despite the accounts being described as joint may mean one of: (i) the accounts are not, on BMO's records, set up with right of survivorship; (ii) some portion of the $10k is in Mary's sole name; (iii) BMO has an internal policy of requiring probate when any estate involvement is flagged; (iv) BMO is aware of *Pecore* and wants the protection of a court order before releasing. The lawyer's letter to BMO should ask for the basis.

### The scope of "probate" — what the bank's decision actually affects

This is a frequent point of confusion. **The bank's decision about whether to require probate is bank-scoped — it is about the bank's $10k specifically, and is the bank's institutional decision about what *it* needs before releasing *its* funds.**

**But the Certificate of Appointment itself, if Daughter ends up applying for one, is a single estate-wide document.** The Certificate is not asset-specific. Once issued, it authorizes Daughter as Estate Trustee to deal with *every* asset that is in Mary's estate. There is only one probate per estate; the Certificate is the single court authorization.

Three institutions are deciding (or not deciding) on probate separately:

1. **BMO** — about $10k of bank funds. Currently deliberating.
2. **The brokerage** holding the $480k joint investments — has not been asked. For assets held jointly with right of survivorship, brokerages typically do *not* require probate; they transfer legal title to the surviving joint holder on a death certificate.
3. **The RIF custodian** (whoever holds the $805 RIF) — not relevant; named-beneficiary designations bypass probate entirely.

The three institutions do not coordinate. One institution's decision does not bind the others. A "yes probate" decision from BMO does not force the brokerage to require it, and a "no probate" from any one of them doesn't release Daughter from any other institution's requirements.

**What probate does NOT do:**

- It does not bring assets into the estate that were not already there. Joint-with-survivorship assets still pass to the surviving joint holder outside the estate, regardless of whether a Certificate is obtained. Named-beneficiary RIFs still go to the named beneficiary directly.
- It does not force a particular *Pecore* characterization. Probate is a court authorization to act; the underlying beneficial-ownership question is separate.

### The procedural reach of the bank's small-dollar decision

Even though BMO's $10k is small, BMO's decision has outsized procedural consequences if it requires probate. An Application for Certificate of Appointment (Form 74A) requires a **sworn statement of estate value** — i.e., Daughter must declare on a court document what she is treating as estate property and what she is treating as outside the estate.

For Mary's situation, this is exactly where the **Path A vs Path B mechanism choice** (see `Background.md` Daughter's distribution intent paragraph) gets locked in on a sworn document:

- **If Daughter declares Path A** (the $480k joint investments are hers by survivorship, not estate property): estate value on Form 74A ≈ $10k + jewellery, under the $50k EAT threshold, EAT = $0. But the sworn statement positions Daughter as taking the joint investments outside the estate — committing to Path A. Brother would then receive his half via a personal gift from Daughter, with the documentation friction noted in `Background.md`.
- **If Daughter declares Path B** (the $480k joint investments are estate property under *Pecore*): estate value on Form 74A ≈ $10k + $480k + jewellery ≈ $490k, EAT ≈ $6,600. The investments flow through the estate per the will. Cleanest filings and documentation, aligned with the *Pecore*-tracking analysis in `findings/jtwros-treatment.md`.

If BMO does *not* require probate, Daughter avoids the forced sworn-statement step. The path choice still has to be made for tax-filing purposes (terminal T1, T3, Estate Information Return if a Certificate is ever obtained for some other reason), but it does not have to be locked in via a probate application.

This is why a $10k bank-deliberation is procedurally significant even though the dollar amount is small.

### Bank decides "no probate needed"

- Bank releases the chequing/savings balance to Daughter directly (either because the accounts were truly joint and pass by survivorship outside the estate, or because the bank's internal threshold isn't triggered).
- **No Certificate of Appointment is issued.**
- **No EAT is payable.**
- **No Estate Information Return is required.**
- However: this does *not* resolve the *Pecore* question between Daughter and Brother. The bank's internal decision is administrative, not judicial. If Brother later contests the *Pecore* treatment, the assets would still need to be accounted for as part of the residue, even though they were released to Daughter directly.

### Bank decides "probate required"

- Daughter must apply to the Superior Court of Justice for a Certificate of Appointment of Estate Trustee (or a Small Estate Certificate if value ≤ $150,000).
- EAT is owed on the value of the probated estate over $50,000 at the $15/$1,000 rate.
- Within 180 days of certificate issue, an Estate Information Return must be filed.
- The application requires identifying the estate's assets with sufficient particularity that the *Pecore* question becomes harder to ignore — Daughter as applicant signs a sworn document about what's in the estate, and Brother (as a beneficiary entitled to share of the residue) must be served with the application before it is filed.
- **Service on Brother is the moment the *Pecore* question becomes practically unavoidable.** Brother gets a copy of the application identifying what assets Daughter is treating as the estate's vs. what assets Daughter is treating as personally hers by survivorship. If those allocations don't match Brother's understanding, the dispute crystallizes here.

**Why it matters for Daughter (Q4):** A "no probate" decision from the bank is *not* a release from the *Pecore* analysis — it just delays the moment of confrontation. A "yes probate" decision forces the *Pecore* allocation to be made explicitly on a sworn application that Brother will see.

---

## Entry 5 — Estate Information Return obligations

**Captured:** 2026-05-14
**Source:** Government of Ontario, "Estate Administration Tax" page (same URL as Entry 2).

> "Beginning January 1, 2020, an estate representative must file an Estate Information Return with the Ministry of Finance within 180 calendar days after the estate certificate has been issued."

The return identifies the value of each estate asset at date of death.

> "Records and books of account in support of all entries on the Estate Information Return must be kept at the estate representative's principal place of business or residence for four years."

The Ministry of Finance has reassessment powers within four years of the tax becoming due, and longer in cases of misrepresentation. (See "Assessments" section of the page.)

**Why it matters for Daughter:** Daughter's signature on the Estate Information Return is itself a sworn statement about which assets were in the estate. If the *Pecore* question is unresolved and Daughter signs that the joint accounts/investments were not in the estate, and a court later determines otherwise, the Ministry has up to four years to reassess and the penalties are significant.

---

## Summary — answers to Daughter's questions Q4 and Q5 from `Background.md`

**Q4: What happens when the bank decides on probate (yes and no)?**

- *No probate:* bank releases Mary's bank balances directly to Daughter. No EAT. No Estate Information Return. But the *Pecore* question (per `jtwros-treatment.md`) is unresolved and may surface later when Brother realizes the residue is much smaller than he expected.
- *Yes probate:* Daughter applies to the Superior Court of Justice using Forms 74A/74B/74D/74C. EAT is owed at $15/$1,000 on the probated value over $50,000. Within 180 days of the Certificate issuing, an Estate Information Return must be filed. Brother is served with the application before filing — making the *Pecore* allocation explicit and visible.

**Q5: What exactly in the estate is subject to taxation? Is it the full asset value or some portion of it?**

- For **EAT (Ontario probate tax)**: the *full* value of all assets included in the EAT base, less encumbrances on real property only. There is no "step-up" — full FMV at date of death. The $50,000 threshold means no tax until the estate exceeds that figure.
- For **income tax (CRA terminal T1)**: only the *accrued capital gains* (and other income items like RIF inclusion) are taxable — not the full asset value. See `findings/jtwros-treatment.md` Entry 4 and the future `findings/terminal-t1.md`.
- For the joint accounts and investments specifically: whether they are in the EAT base or excluded depends on the *Pecore* analysis. The two outcomes diverge by a factor of ($X − $50,000) × 0.015 in EAT terms (Scenario A vs. B above).

---

## Action items arising from this findings file

1. **Get rough asset values.** Daughter to provide approximate totals for: chequing balance, savings balance, non-registered investments (jointly held). This lets us put real numbers on Scenarios A vs B.
2. **Find out the bank's small-balance threshold** for the specific bank (Mary's bank). This is what's determining whether probate is needed.
3. **Identify the bank.** Different Canadian banks have different probate thresholds and different stances on *Pecore* indemnities; we cannot research the specific bank's policy without knowing which one.
4. **Connect this to the Pecore analysis.** Before signing any sworn document (the probate application Form 74A or the Estate Information Return), Daughter should have the *Pecore* allocation reviewed by an Ontario estates lawyer.
5. **Next research pass:** capture the actual statute (Estate Administration Tax Act, 1998, SO 1998, c 34, Sch) text verbatim from a non-CanLII source if possible, and confirm whether there is any published Ontario MoF guidance or case law specifically on how *Pecore* resulting-trust property is treated for EAT purposes.

---

## Sources cited in this file

- [Estate Administration Tax — Government of Ontario](https://www.ontario.ca/page/estate-administration-tax) — last updated 2026-01-02
- [Apply for probate of an estate — Government of Ontario](https://www.ontario.ca/page/apply-probate-estate) — last updated 2025-09-11
- [Administering estates — Government of Ontario](https://www.ontario.ca/page/administering-estates) — last updated 2024-03-05
- [Estate Administration Tax Act, 1998, SO 1998, c 34, Sch](https://www.ontario.ca/laws/statute/98e34) — Ontario consolidated statute (fetched but not yet quoted verbatim in this file; action item for next pass)
- *Pecore v. Pecore*, 2007 SCC 17 — see `findings/jtwros-treatment.md` for full citation
