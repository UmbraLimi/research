# CLAUDE.md

This file provides guidance to Claude Code when working in this project folder.

## Project Overview

*[Describe your research project here]*

## Folder Structure

```
Project-Name/
├── PLAN.md               # Work phases and progress tracking
├── CLAUDE.md             # This file - project guidance
├── docs/sessions/        # Session logs (created by /par-learnings, /par-prompts)
└── .claude/commands/     # Project-specific slash commands (r-*)
```

## Slash Commands

### Available Commands

**Parent-level (`MyResearch/.claude/commands/`)** - Available in all projects:
- `/par-resume` - Resume work by analyzing PLAN.md
- `/par-update` - Update PLAN.md with current progress
- `/par-end-session` - End session workflow (learnings, prompts, commit)
- `/par-commit` - Stage and commit all changes in repo
- `/par-learnings` - Document session learnings
- `/par-prompts` - Save session prompts
- `/par-timestamp` - Get current date/time

**Project-level (`.claude/commands/`)** - Add project-specific commands here:
- `/r-commit` - Stage and commit only this project's changes

## Workflow

1. Start session: `/par-resume`
2. Do work, update progress: `/par-update`
3. End session: `/par-end-session`
