# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Productivity helpers: a collection of Claude Code skills and agents for managing a freelancer's personal knowledge system across three applications:

- **Dynalist** — tasks (fast entry, search, context visibility)
- **Obsidian** — project/event journaling, notes, credentials (JSON/YAML), URL archival
- **Joplin** — being retired; all content migrating to Dynalist (tasks) or Obsidian (everything else)

The project also handles: cross-app tagging, credential lookup via compiled programs, YouTube Shorts transcript/thumbnail archival, and data migration between the three apps.

Sister project: `Comm-Helpers/` (Slack, Email, Telegram summarization into Obsidian).

## Project Status

Pre-development / planning phase. No code written yet. See `PURPOSE.md` for goals and context.

## Critical Rule: Ask Before Deciding

Do NOT make structural, architectural, or format decisions autonomously. When facing a choice that isn't clearly dictated by existing patterns or explicit instructions, stop and present the options with trade-offs. Let the user decide. This applies to: file formats, naming conventions, directory structure, which patterns to adopt, whether to simplify or preserve complexity, and any other fork in approach.

## Skills: Preserve `!` Backtick Determinism

Pre-computed context (`!` backticks in SKILL.md) is a core feature of this project's skills. It guarantees determinism — the skill author controls what data Claude sees, not Claude's runtime decisions. Do NOT replace `!` backtick commands with tool-based alternatives unless the user explicitly approves. When a `!` backtick command hits a permission issue, fix the permission or the command — don't remove the pre-computation.

## Fix Proposals: Simple vs Durable

When proposing fixes, present the **simplest** option but also supply the **most durable/bulletproof** option(s). Never act on the simplest fix without user approval — especially in early-stage work where patterns are still forming and short-term expedience can lock in fragile conventions. If in doubt about which direction to take, ask.

## Key Design Principles

- **Agents must have guard rails** — agents should halt overtly when encountering situations not explicitly covered in their directives, rather than improvising
- **Shadow documentation** — every agent, skill, Python script, and bash script gets a companion doc capturing its state, rationale, usage, and history
- **Testability** — skills and agents must be testable under guardrail conditions and fail explicitly on unexpected inputs
- **Tag mapping** — a translation table (maintained outside Dynalist/Obsidian) will map tags across systems since a universal convention is impractical

## Documentation Structure

```
docs/
├── sessions/          # Session logs (learnings, decisions, dev transcripts, prompts)
│   └── YYYY-MM/       # Organized by month
├── reference/         # API and tool reference docs (populated during Phase 1)
│   ├── dynalist-api.md
│   ├── joplin-api.md
│   └── obsidian-cli.md
├── architecture/      # Design documents for cross-cutting concerns
│   ├── tag-mapping.md
│   ├── note-formats.md
│   └── agent-guardrails.md
├── vendors/           # External service notes (Whisper, etc.)
└── guides/            # How-to guides for specific workflows
```

**Key project files:**

| File | Purpose | Updated By |
|------|---------|-----------|
| `PLAN.md` | Current & pending work (forward-looking only) | `/r-update-plan` |
| `COMPLETED_PLAN.md` | Archive of completed phases (terse) | `/r-update-plan` |
| `DECISIONS.md` | Cumulative decision record | `/r-learn-decide` |
| `PLAYBOOK.md` | Repo workflow conventions & deferred enhancements | `/r-learn-decide` |
| `PURPOSE.md` | Project goals, context, constraints | Manual |
| `RESUME-STATE.md` | Cross-session continuity (created as needed) | `/r-save-state` |

## Decision Tracking

Decisions are recorded in `DECISIONS.md` under categories: Data Architecture, Tag System, Migration Strategy, Agent Design, Tooling & APIs. Each entry includes date and one-line summary.

## Slash Commands

**Project-level (`r-*`):**

| Command | Purpose |
|---------|---------|
| `/r-eos` | Full end-of-session sequence (runs all 4 below in order) |
| `/r-learn-decide` | Capture learnings and decisions to session files |
| `/r-dump` | Create development session transcript |
| `/r-update-plan` | Update PLAN.md with current progress |
| `/r-docs` | Update all project documentation |
| `/r-save-state` | Save work state to RESUME-STATE.md |
| `/r-commit` | Stage and commit this folder only |
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

## Session Documentation

Use `/r-eos` for full end-of-session wrap-up. Session docs go to `docs/sessions/YYYY-MM/`.
