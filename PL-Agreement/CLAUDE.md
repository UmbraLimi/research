# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Folder Purpose

This folder is for examining and analyzing a legal agreement PDF related to PeerLoop development work. The goal is to:
- Assess the agreement for potential concerns
- Suggest changes to protect the developer's interests
- Explain the intent behind specific clauses
- Identify what may be missing that should be included

## Background Context

- **The Agreement**: A proposed written agreement from Brian's lawyer
- **Brian**: The client currently paying for development of the PeerLoop web application (formerly called Alpha Peer)
- **Current Status**: No written agreement exists yet; this document is intended to formalize the working relationship
- **Brian's Goals**: Ensure no hurdles to securing investors who may want ownership stake in the business and/or software being developed
- **Document Origin**: Crafted by Brian's lawyer from Brian's perspective

## My Role as Claude

When analyzing this agreement, I should:

1. **Identify Foreseeable Issues**: Flag provisions that could be problematic for the developer based on what IS included
2. **Identify Missing Protections**: Highlight what is NOT included that would typically safeguard and/or benefit a developer in this type of arrangement
3. **Explain Intent**: Help clarify what specific clauses likely mean and why the lawyer may have included them
4. **Suggest Changes**: Propose alternative language or additions that would better balance the agreement
5. **Provide Due Diligence Support**: Assist with "broad strokes" analysis while acknowledging this is not a substitute for legal counsel

## Important Disclaimers

- This analysis supports preliminary due diligence only
- The user does not currently have a lawyer but should consult one before signing
- My analysis should highlight areas requiring professional legal review

## Handling the Document

When working with the agreement PDF:
1. Use the Read tool to view PDF contents
2. Provide thorough analysis of terms and implications
3. Offer balanced perspective on what protects each party
4. Flag standard vs. unusual provisions

## Project Files and Relationships

This project maintains several interconnected files. **When updating any file, check whether related files need updates.**

| File | Purpose | Updates Trigger |
|------|---------|-----------------|
| `FACTS.md` | Living document of facts gathered across sessions (parties, timeline, payment terms, concerns) | When new information is learned about the parties, arrangement, or context |
| `REDLINES.md` | Detailed redline document with proposed changes, rationale, and negotiation guidance | When proposed changes are added, modified, or prioritized |
| `PROPOSED-CHANGES-YYYY-MM-DD-A.md` | Formal proposed revisions document for sharing with Client | When REDLINES.md changes are finalized for presentation |

### File Dependencies

```
FACTS.md (source of truth for context)
    ↓
REDLINES.md (analysis + proposed changes + negotiation strategy)
    ↓
PROPOSED-CHANGES-*.md (clean presentation version)
```

### Update Triggers

**When FACTS.md changes:**
- Review REDLINES.md - do any rationales or proposed changes need adjustment?
- Review PROPOSED-CHANGES - does the formal document reflect current understanding?

**When REDLINES.md changes:**
- Update PROPOSED-CHANGES to match (they should stay in sync)
- Consider if FACTS.md needs new information added

**When PROPOSED-CHANGES changes:**
- Ensure REDLINES.md has the same content (REDLINES is the working copy)
- Update summary statistics in both files

### Naming Convention

- `PROPOSED-CHANGES-YYYY-MM-DD-A.md` - Date indicates version, letter suffix (A, B, C) for same-day revisions
- When creating a new version, keep the previous version for history

## Session Continuity

Maintain `FACTS.md` as a living document of facts and pertinent information gathered across sessions. When new information is learned:
1. Update FACTS.md with the new information
2. Consult FACTS.md at the start of sessions to recall context
3. Keep information organized by category for easy reference
4. **Check if REDLINES.md or PROPOSED-CHANGES need updates based on new facts**

## Git Workflow

Two commit options:
- `/r-commit` - Commit only this project's changes
- `/repo-commit` - Commit all changes across the repo
