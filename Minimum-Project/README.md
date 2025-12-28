# Minimum-Project Template

This folder is a template for new research projects in the MyResearch repository.

## Usage

1. Copy this entire folder and rename it for your new project:
   ```bash
   cp -r Minimum-Project My-New-Project
   ```

2. Launch Claude Code from your new project folder:
   ```bash
   cd My-New-Project
   claude
   ```

3. Update `CLAUDE.md` with your project-specific guidance

4. Update `PLAN.md` with your initial phases and tasks

## What's Included

| File/Folder | Purpose |
|-------------|---------|
| `CLAUDE.md` | Project guidance for Claude Code - customize for your project |
| `PLAN.md` | Work tracking with phases and tasks - required for `/par-resume` and `/par-update` |
| `docs/sessions/` | Session logs created by `/par-learnings` and `/par-prompts` |
| `.claude/commands/` | Project-specific slash commands (includes `/r-commit` by default) |

## Available Slash Commands

When you launch Claude Code from any project folder, you get:

**Parent-level commands** (from `MyResearch/.claude/commands/`):
- `/par-resume` - Load PLAN.md and show where you left off
- `/par-update` - Save progress to PLAN.md (run frequently!)
- `/par-end-session` - Full wrap-up: learnings, prompts, optional commit
- `/par-commit` - Stage and commit all changes in repo
- `/par-learnings` - Document what you learned this session
- `/par-prompts` - Save prompts used this session
- `/par-timestamp` - Utility for other commands
- `/par-pare` - Optimize CLAUDE.md by offloading content

**Project-level commands** (from `.claude/commands/`):
- `/r-commit` - Stage and commit only this project's changes

## Adding Project-Specific Commands

Create `.md` files in `.claude/commands/` with this format:

```markdown
---
description: Brief description shown in command list
argument-hint: "<optional-arg>"
---

# Command Name

Instructions for Claude to follow when this command is invoked.
```

Suggested prefix: Use `/r-` for project-specific commands to distinguish from parent `/par-*` commands.

## Caveats

- **PLAN.md is required** - The `/par-resume` and `/par-update` commands expect this file. Don't rename or delete it.

- **Two commit options** - Use `/r-commit` to commit only this project's changes, or `/par-commit` to commit all changes across the repo.

- **Session files are auto-organized** - `/par-learnings` and `/par-prompts` create files in `docs/sessions/YYYY-MM/` automatically.

## Suggestions

- **Run `/par-update` frequently** - Don't wait until end of session. If Claude Code crashes or you lose context, PLAN.md is your recovery point.

- **Keep CLAUDE.md focused** - Put only essential guidance here. Use `/par-pare` if it gets too long.

- **Use phases in PLAN.md** - Break work into numbered phases (1.1, 1.2, 2.1...) for clear progress tracking.

- **Delete this README** - Once you've set up your project, you don't need these instructions cluttering your folder.
