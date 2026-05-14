# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

This is not a software project. It is a **research and documentation workspace** to help Daughter (executor) administer the estate of her late mother Mary (d. 2026-04-21) under Ontario, Canada law.

The user collaborating with you is acting on Daughter's behalf. The work product is a documented, dated, source-cited trail of findings that Daughter can use to make decisions and reconcile conflicting advice she is receiving from her financial advisor and tax accountant.

**Source of truth for facts:** `Background.md` in this directory. Re-read it whenever you need the situation context — it is the canonical statement of who/what/when. As new facts emerge through Q&A, append them to `Background.md` (or ask the user to) rather than scattering them across files.

## Jurisdiction and scope

- **Province:** Ontario, Canada
- **Country tax authority:** Canada Revenue Agency (CRA)
- **Relevant regimes** likely in scope: Ontario Estate Administration Tax (EAT, formerly "probate fees"), CRA deemed-disposition on death, terminal T1 return, T3 estate return, RRIF rollover/beneficiary rules, joint-ownership-with-right-of-survivorship (JTWROS) treatment under *Pecore v. Pecore* (2007 SCC 17) and successors.
- Do **not** apply rules from other provinces (BC, Alberta, Quebec) or other countries (US, UK) without explicitly flagging the jurisdiction mismatch.

## Critical disclaimer — embed in every substantive answer

Claude is **not** a lawyer, accountant, or licensed financial advisor. Findings here are research notes intended to:
1. Help Daughter understand the landscape and vocabulary
2. Surface questions she should put to a CRA agent, an Ontario estates lawyer, or a CPA
3. Triangulate where her financial advisor and tax accountant disagree

Anything that looks like advice must be framed as "what the [statute / CRA bulletin / case law] says" with a citation, not "what Daughter should do."

## Research workflow (per Background.md instructions)

1. **Consult external sources freely.** Prefer primary sources in this order: CRA web pages and Income Tax Folios, Ontario government estates pages, Ontario statutes (e.g., *Succession Law Reform Act*, *Estate Administration Tax Act, 1998*), reported case law. Treat blog posts, law-firm marketing pages, and Reddit threads as leads to verify against primary sources, not as authority.
2. **Capture as you go.** When you find a material snippet, create or append to a markdown file in `findings/` (create the folder on first use). Each entry must include:
   - Timestamp: `YYYY-MM-DD HH:MM` (use today's date from system context; today is 2026-05-14)
   - Source URL and the source's own publication/last-revised date if visible
   - Verbatim quote of the relevant passage (kept short — fair-use snippet)
   - Your plain-language paraphrase
   - **Why it matters** for one of Daughter's six questions in `Background.md`
   - Confidence note (e.g., "primary source, current as of 2026" vs "secondary, may be stale")
3. **One file per topic, not per session.** E.g., `findings/probate-and-eat.md`, `findings/deemed-disposition.md`, `findings/jtwros-treatment.md`, `findings/rrif-beneficiary.md`, `findings/terminal-t1.md`, `findings/distribution-timing.md`. Append chronologically inside each file so the audit trail is preserved.
4. **Ask when unsure.** Background.md explicitly says to ask. Don't guess at Daughter's situation (e.g., whether an investment was registered or non-registered, whether the joint account was JTWROS or tenants-in-common, whether the will names an alternate executor). If a fact you need isn't in Background.md, ask — then the user (or you, with permission) appends the answer to Background.md.

## What goes where

| File | Purpose |
|------|---------|
| `Background.md` | Facts about Mary, Daughter, the estate. Append-only as new facts emerge. |
| `CLAUDE.md` | This file — how Claude should approach the project. |
| `findings/<topic>.md` | Dated, cited research snippets per topic. |
| `questions-open.md` | Questions raised that need an answer from Daughter, the bank, CRA, the lawyer, or the accountant. Mark resolved with date + where the answer landed. |
| `summary.md` | Eventual plain-language consolidated answer to Daughter's six numbered questions, with citations back to `findings/`. Build this last, after the findings exist. |

Do **not** create a `docs/` folder, `PLAN.md`, `DECISIONS.md`, or the `r-*` skill scaffolding from the parent monorepo template unless the user asks — they are overkill for this project's nature.

## Specific landmines to watch for

- **The April 21, 2026 date** (Question 1): under CRA rules, death triggers a deemed disposition of capital property at FMV. For JTWROS assets, the *Pecore* framework distinguishes true beneficial joint ownership from a resulting trust — outcome is fact-specific. Do not assume "joint = automatically Daughter's, no tax." Flag this as the central legal/tax question.
- **Probate vs. no probate** (Question 4): in Ontario, EAT is owed on the value of assets that pass through the estate. Assets passing by survivorship or by named beneficiary (the RRIF) generally bypass the estate for EAT purposes — but the bank's probate requirement is a separate question from CRA tax treatment. Keep these two threads clearly distinguished.
- **"When can Daughter disperse funds"** (Question 2): the executor's year, clearance certificates from CRA (form TX19), and personal liability of the executor for unpaid tax are the relevant concepts. Distributing too early exposes Daughter personally.
- **Conflicting advice** (financial advisor vs tax accountant): when you encounter this, do not pick a side. Document both positions, identify the specific factual or legal point they diverge on, and frame it as a question for the CRA / lawyer.

## Sensitivity

This concerns a recent death in the user's family. Keep tone matter-of-fact and respectful. Avoid euphemisms ("passed on," "lost") and avoid clinical coldness — "Mary's death on 2026-04-21" is fine.

## Repo context

This folder lives inside `/Users/jamesfraser/MyResearch/`, a monorepo of unrelated research projects. The parent `CLAUDE.md` documents repo-wide conventions (slash commands, Minimum-Project template, docs/ structure) — most of those do not apply here, but `/repo-commit` and `/par-*` commands are still available if you want to commit work or capture session notes.
