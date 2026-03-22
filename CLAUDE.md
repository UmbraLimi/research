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

`Minimum-Project/` is a fully-equipped project template with the complete conversation lifecycle infrastructure already in place: 10 r-* skills, 10 helper scripts, permissions, conv counter, and all standard project files (CLAUDE.md, PLAN.md, DECISIONS.md, etc.). It mirrors the infrastructure in `prod-helpers/` but with generic placeholders ready for customization.

### Setup steps

```bash
cp -r Minimum-Project My-New-Project
cd My-New-Project
claude
```

Then inside Claude Code:

1. **Set prefix** — Edit `PROJECT.yaml` with a 3-letter code (e.g., `MNP`). Register it in `/PROJECTS.yaml` at repo root.
2. **Fill out PURPOSE.md** — Describe goals, context, constraints. See the Section Library in `Minimum-Project/README.md` for project-type-specific sections.
3. **Run `/init`** — Customizes CLAUDE.md, DECISIONS.md categories, and skill topic tables from your PURPOSE.md.
4. **Create PLAN.md** — CC will offer, or build your own skeleton.
5. **Commit setup** — Run `/r-commit` so the repo is clean.
6. **Delete README.md** — It's setup instructions, not project documentation.

From this point on, start every conversation with `/r-start` and end with `/r-end`.

### What the template provides

| Component | Count | Purpose |
|-----------|-------|---------|
| `.claude/skills/r-*` | 10 | Full conversation lifecycle (start, end, resume, eos, learn-decide, dump, update-plan, docs, save-state, commit) |
| `.claude/scripts/` | 10 | Shell helpers for `!` backtick pre-computation in skills |
| `.claude/settings.local.json` | 1 | Permissions for all skills, scripts, and git operations |
| Root project files | 8 | CLAUDE.md, PLAN.md, DECISIONS.md, DOC-DECISIONS.md, COMPLETED_PLAN.md, CONV-COUNTER, CONV-FLOWCHART.md, PROJECT.yaml |

### Prerequisite

The `/r-start` and `/r-end` skills pull/push to sync the conv counter across machines. Projects inside this repo already have a remote. Standalone projects need `git remote add origin <url>` before `/r-start` will work.
