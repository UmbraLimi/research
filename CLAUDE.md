# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a research and planning repository for **Alpha Peer**, a web application in the pre-development phase. The project uses iterative research, documentation, and decision tracking to prepare for eventual handoff to implementation. There is no code to build, lint, or test.

## Repository Structure

```
MyResearch/
├── Alpha-Peer/           # Main project folder
│   ├── STRUCTURE.md      # Master guide for organization (check first!)
│   ├── Needs.md          # Evolving requirements for handoff
│   ├── client-docs/      # Client-provided materials (don't modify originals)
│   ├── research/         # Technology research (tech-NNN-*.md, comp-NNN-*.md)
│   ├── user-stories/     # Requirements (story-NNN-*.md)
│   ├── docs/sessions/    # Session logs by month (YYYY-MM/)
│   ├── prompts/          # Commands and prompt templates
│   ├── learnings/        # Knowledge capture (learning-NNN-*.md)
│   ├── decisions/        # Decision records (decision-NNN-*.md)
│   └── .claude/commands/ # Project-specific slash commands (r-*)
└── file_holding/         # Temporary staging for file processing
```

**Important:** Launch Claude Code from `Alpha-Peer/` folder, not `MyResearch/`.

## Key Conventions

### File Naming
- Numbers use zero-padded 3 digits: `001`, `002`, etc.
- Lowercase with hyphens for filenames
- Date format: YYYY-MM-DD (ISO 8601)
- Session files use timestamp: `docs/sessions/2025-11/2025-11-25_14-30-00 Dev.md`

### Before Creating Files
Always check `Alpha-Peer/STRUCTURE.md` for:
- Current numbering state for each category
- Correct folder location
- Naming pattern to follow

After creating numbered files, update the "Current State" section in STRUCTURE.md.

## Slash Commands

Commands are split between two locations:
- **`~/.claude/commands/`** - User-level `/q-*` commands (available in all projects)
- **`Alpha-Peer/.claude/commands/`** - Project-specific `/r-*` commands

### `/q-*` Commands (Session & Git) - User-level

| Command | Purpose |
|---------|---------|
| `/q-resume` | Analyze PLAN.md and show current progress to resume work |
| `/q-update` | Update PLAN.md with current progress (run frequently) |
| `/q-end-session` | Full end-of-session workflow (learnings, prompts, optional commit) |
| `/q-commit` | Stage and commit all changes with descriptive message |
| `/q-learnings` | Document session learnings and insights |
| `/q-prompts` | Save all user prompts from session for future reference |
| `/q-timestamp` | Get current date/time (utility, called by other commands) |
| `/q-pare` | Optimize CLAUDE.md by moving content to OFFLOAD.md |

### `/r-*` Commands (Research & Documentation) - Project-level

| Command | Purpose |
|---------|---------|
| `/r-research-tech` | Research a specific technology |
| `/r-compare-tech` | Compare two technologies for a use case |
| `/r-create-story` | Create a new user story |
| `/r-update-needs` | Update Needs.md with recent work |
| `/r-log-decision` | Document a decision with rationale |
| `/r-add-client-doc` | Process client document(s) from file_holding |
| `/r-status` | Show current project status |
| `/r-review` | Review and suggest improvements to a file |
| `/r-sync-structure` | Update STRUCTURE.md by scanning folders |
| `/r-list` | List files in a specific project folder |

## Workflow Notes

- **Client docs are read-only** - Reference them but don't modify originals
- **Needs.md is the handoff document** - Update it as decisions are made
- **Trace decisions to sources** - Link back to research, client docs, or learnings
- **file_holding/ is temporary** - Files staged here get processed and moved
