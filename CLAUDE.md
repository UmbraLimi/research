# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a research workspace containing multiple projects in pre-development phases. Each project has its own CLAUDE.md with project-specific guidance.

**Why a single repo?** Research and planning projects change infrequently and don't warrant individual GitHub repos. This monorepo provides a single backup point while keeping projects organized in subfolders.

```
MyResearch/
├── .claude/commands/     # Parent-level slash commands (/par-*)
├── Alpha-Peer/           # Main research project (see Alpha-Peer/CLAUDE.md)
└── Minimum-Project/      # Template for new projects
```

## Working with Projects

**Launch Claude Code from the project folder, not MyResearch root:**
```bash
cd Alpha-Peer && claude
```

This ensures project-specific `.claude/commands/` are available.

## Git Commit Workflow

Two commit options available from any subfolder:

| Command | Scope | Use when |
|---------|-------|----------|
| `/repo-commit` | All changes in repo | Committing work across multiple projects |
| `/r-commit` | Current folder only | Committing just this project's changes |

Both commands are available from any project folder.

## Slash Commands

Commands are split between two locations:

**Parent-level (`.claude/commands/`)** - Available in all subfolders:
| Command | Purpose |
|---------|---------|
| `/par-resume` | Analyze PLAN.md and resume work |
| `/par-update` | Update PLAN.md with progress |
| `/par-end-session` | End session (learnings, prompts, optional commit) |
| `/repo-commit` | Stage and commit all changes |
| `/par-learnings` | Document session learnings |
| `/par-prompts` | Save session prompts |
| `/par-timestamp` | Get current date/time |
| `/par-pare` | Optimize CLAUDE.md by moving content to OFFLOAD.md |

**Project-level** - See each project's CLAUDE.md for `/r-*` commands.

## Standard Documentation Structure

All projects in this repo follow this docs/ folder convention. Folders are created as needed, never pre-created empty.

```
docs/
├── sessions/       # Conv/session logs (universal, all projects)
│   └── YYYY-MM/
├── requirements/   # What needs to be built/done (user stories, RFCs)
│   └── rfcs/       # Numbered change requests: RFC-001/, RFC-002/, ...
├── reference/      # External tools, APIs, services
├── as-designed/    # Pre-build: specs, formats, plans (how things SHOULD work)
├── as-built/       # Post-build: how implemented systems actually work
└── guides/         # How-to procedures for specific workflows
```

**Lifecycle:** requirements → as-designed → build → as-built

**Root-level docs** (per project, not in docs/):
- `PLAN.md` — current & pending work
- `COMPLETED_PLAN.md` — archive of finished phases
- `DECISIONS.md` — project-domain decisions
- `DOC-DECISIONS.md` — repo workflow & documentation conventions
- `PURPOSE.md` — project goals, context, constraints

**Decision routing:** Project/technical decisions → `DECISIONS.md`. Workflow/documentation conventions → `DOC-DECISIONS.md`.

## Creating New Projects

Copy the `Minimum-Project/` template:
```bash
cp -r Minimum-Project My-New-Project
cd My-New-Project
# Update CLAUDE.md and PLAN.md for your project
```
