# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

<!-- CUSTOMIZE: Replace this section with your project description after /init -->
<!-- /init will rewrite this from PURPOSE.md -->

New research project. See `PURPOSE.md` for goals and context.

## Project Status

Not started. Fill out `PURPOSE.md` and run `/init`.

## Critical Rule: Ask Before Deciding

Do NOT make structural, architectural, or format decisions autonomously. When facing a choice that isn't clearly dictated by existing patterns or explicit instructions, stop and present the options with trade-offs. Let the user decide. This applies to: file formats, naming conventions, directory structure, which patterns to adopt, whether to simplify or preserve complexity, and any other fork in approach.

## Skills: Preserve `!` Backtick Determinism

Pre-computed context (`!` backticks in SKILL.md) is a core feature of this project's skills. It guarantees determinism — the skill author controls what data Claude sees, not Claude's runtime decisions. Do NOT replace `!` backtick commands with tool-based alternatives unless the user explicitly approves. When a `!` backtick command hits a permission issue, fix the permission or the command — don't remove the pre-computation.

## Fix Proposals: Simple vs Durable

When proposing fixes, present the **simplest** option but also supply the **most durable/bulletproof** option(s). Never act on the simplest fix without user approval — especially in early-stage work where patterns are still forming and short-term expedience can lock in fragile conventions. If in doubt about which direction to take, ask.

## Documentation Structure

```
docs/
├── sessions/          # Conv logs (learnings, decisions, dev transcripts)
│   └── YYYY-MM/       # Organized by month
├── requirements/      # What needs to be built/done (user stories, RFCs)
│   ├── user-stories.md (or user-stories/ dir if split by role)
│   └── rfcs/          # Numbered change requests (RFC-001/, RFC-002/, ...)
├── reference/         # External tools, APIs, services (their docs, our notes)
├── as-designed/       # Pre-build: specs, formats, plans for things not yet built
├── as-built/          # Post-build: how implemented systems actually work
└── guides/            # How-to procedures for specific workflows
```

Lifecycle: requirements → as-designed → build → as-built. Folders created as needed, never pre-created empty.

**Key project files:**

| File | Purpose | Updated By |
|------|---------|-----------|
| `PLAN.md` | Current & pending work (forward-looking only) | `/r-update-plan` |
| `COMPLETED_PLAN.md` | Archive of completed phases (terse) | `/r-update-plan` |
| `DECISIONS.md` | Cumulative decision record | `/r-learn-decide` |
| `DOC-DECISIONS.md` | Repo workflow conventions & deferred enhancements | `/r-learn-decide` |
| `PURPOSE.md` | Project goals, context, constraints | Manual |
| `RESUME-STATE.md` | Cross-session continuity (created as needed) | `/r-save-state` |
| `CONV-COUNTER` | Persistent conversation counter (synced via git) | `/r-start` |

## Decision Tracking

Decisions are recorded in `DECISIONS.md` under project-specific categories. Each entry includes date and one-line summary.

<!-- CUSTOMIZE: Update the categories in DECISIONS.md to match your project -->

## Slash Commands

**Project-level (`r-*`):**

| Command | Purpose |
|---------|---------|
| `/r-start` | **Start conversation** — check repo clean, pull, increment conv counter, push, transfer pending tasks, resume |
| `/r-end` | **End conversation** — run end-of-conv sequence, save state, commit, push, cleanup |
| `/r-eos` | End-of-conv sequence (runs learn-decide, dump, update-plan, docs) |
| `/r-learn-decide` | Capture learnings and decisions to conv files |
| `/r-dump` | Create development conv log |
| `/r-update-plan` | Update PLAN.md with current progress |
| `/r-docs` | Update all project documentation |
| `/r-save-state` | Save work state to RESUME-STATE.md |
| `/r-commit` | Stage and commit this folder only (includes Conv + Machine) |
| `/r-resume` | Load PLAN.md and show where you left off |

**Parent-level (`par-*`)** — also available:

| Command | Purpose |
|---------|---------|
| `/repo-commit` | Stage and commit all changes in repo |
| `/par-pare` | Optimize CLAUDE.md by offloading content |

## TodoWrite Discipline

Any unresolved issue, opportunity, question, or implied action item must be added to TodoWrite immediately. This includes:
- Pre-existing errors found during checks
- Ideas spotted while reading code
- User messages containing signal words: "should", "might", "could", "need to", "do later", "soon", "eventually"

**The user decides priority, not the assistant.** TodoWrite items carry forward via `/r-save-state` → RESUME-STATE.md. Silently skipping items means they're lost in conversation noise.

## Multi-Session Blocks

For blocks too large for one session, create `CURRENT-BLOCK-PLAN.md` at project root with:
- Per-item checkboxes
- Key files table
- Progress summary updated each session

Each session reads the file first, works through unchecked items, updates progress. Deleted when block completes. PLAN.md is too high-level for item tracking; RESUME-STATE.md is session-specific and gets deleted on resume — this fills the gap.

## Conversation Workflow

Always start with `/r-start` and end with `/r-end`. This is the only workflow:

```
/r-start → work → /r-end → exit
```

`/r-end` automatically saves pending TodoWrite items to `RESUME-STATE.md`. `/r-start` automatically transfers them back to TodoWrite on the next conversation. No manual state management needed.

| Skill | Does | Syncs git? |
|-------|------|-----------|
| `/r-start` | check repo clean, pull, increment conv, push, transfer RESUME-STATE.md → TodoWrite, resume | Yes (pull + push) |
| `/r-end` | end-of-conv sequence, save state (TodoWrite → RESUME-STATE.md), commit, push, cleanup | Yes (push) |
| `/r-resume` | read RESUME-STATE.md + PLAN.md, show context | No |

Conv docs go to `docs/sessions/YYYY-MM/`.
