# CLAUDE.md

This file provides guidance to Claude Code when working in this project folder.

## Project Overview

*[Describe your research project here]*

## Folder Structure

```
Project-Name/
├── PLAN.md               # Work phases and progress tracking
├── CLAUDE.md             # This file - project guidance
├── docs/sessions/        # Session logs (created by /q-learnings, /q-prompts)
└── .claude/commands/     # Project-specific slash commands (r-*)
```

## Slash Commands

### Available Commands

**User-level (`~/.claude/commands/`)** - Available in all projects:
- `/q-resume` - Resume work by analyzing PLAN.md
- `/q-update` - Update PLAN.md with current progress
- `/q-end-session` - End session workflow (learnings, prompts, commit)
- `/q-commit` - Stage and commit changes
- `/q-learnings` - Document session learnings
- `/q-prompts` - Save session prompts
- `/q-timestamp` - Get current date/time

**Project-level (`.claude/commands/`)** - Add project-specific commands here.

## Workflow

1. Start session: `/q-resume`
2. Do work, update progress: `/q-update`
3. End session: `/q-end-session`
