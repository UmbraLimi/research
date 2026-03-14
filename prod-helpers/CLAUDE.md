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

**Parent-level (`par-*`)** — also available:

| Command | Purpose |
|---------|---------|
| `/par-resume` | Load PLAN.md and show where you left off |
| `/repo-commit` | Stage and commit all changes in repo |
| `/par-pare` | Optimize CLAUDE.md by offloading content |

## Session Documentation

Use `/r-eos` for full end-of-session wrap-up. Session docs go to `docs/sessions/YYYY-MM/`.
