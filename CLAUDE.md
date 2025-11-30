# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a research workspace containing multiple projects in pre-development phases. Each project has its own CLAUDE.md with project-specific guidance.

```
MyResearch/
├── Alpha-Peer/           # Main research project (see Alpha-Peer/CLAUDE.md)
├── Minimum-Project/      # Template for new projects
└── file_holding/         # Temporary staging for file processing
```

## Working with Projects

**Launch Claude Code from the project folder, not MyResearch root:**
```bash
cd Alpha-Peer && claude
```

This ensures project-specific `.claude/commands/` are available.

## Git Commit Workflow

**Always commit from the root `~/MyResearch` folder:**
1. Exit the subfolder session (do NOT run `/gr-commit` from subfolder)
2. Change to `~/MyResearch`
3. Run `/gr-commit` from there

This keeps all commits at the repository root level.

## Slash Commands

Commands are split between two locations:

**User-level (`~/.claude/commands/`)** - Available in all projects:
| Command | Purpose |
|---------|---------|
| `/q-resume` | Analyze PLAN.md and resume work |
| `/q-update` | Update PLAN.md with progress |
| `/q-end-session` | End session (learnings, prompts, optional commit) |
| `/q-commit` | Stage and commit changes |
| `/q-learnings` | Document session learnings |
| `/q-prompts` | Save session prompts |
| `/q-timestamp` | Get current date/time |
| `/q-pare` | Optimize CLAUDE.md by moving content to OFFLOAD.md |

**Project-level** - See each project's CLAUDE.md for `/r-*` commands.

## file_holding/ Staging Area

Temporary location for processing files:
1. User drops files here
2. Use `/r-add-client-doc` (in Alpha-Peer) to process and move to appropriate folder
3. Files are removed after processing

## Creating New Projects

Copy the `Minimum-Project/` template:
```bash
cp -r Minimum-Project My-New-Project
cd My-New-Project
# Update CLAUDE.md and PLAN.md for your project
```
