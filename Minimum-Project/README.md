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
| `PLAN.md` | Work tracking with phases and tasks - required for `/q-resume` and `/q-update` |
| `docs/sessions/` | Session logs created by `/q-learnings` and `/q-prompts` |
| `.claude/commands/` | Project-specific slash commands (empty by default) |

## Available Slash Commands

When you launch Claude Code from any project folder, you get:

**User-level commands** (from `~/.claude/commands/`):
- `/q-resume` - Load PLAN.md and show where you left off
- `/q-update` - Save progress to PLAN.md (run frequently!)
- `/q-end-session` - Full wrap-up: learnings, prompts, optional commit
- `/q-commit` - Stage and commit all changes
- `/q-learnings` - Document what you learned this session
- `/q-prompts` - Save prompts used this session
- `/q-timestamp` - Utility for other commands
- `/q-pare` - Optimize CLAUDE.md by offloading content

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

Suggested prefix: Use a short project identifier (e.g., `/ap-` for Alpha-Peer, `/mn-` for My-New-Project).

## Caveats

- **Launch location matters** - Claude Code only finds `.claude/commands/` in the folder where you launch it. Always `cd` into your project folder first.

- **PLAN.md is required** - The `/q-resume` and `/q-update` commands expect this file. Don't rename or delete it.

- **Git operations work from subfolders** - Even though the git repo is at `MyResearch/`, `/q-commit` works from any subfolder.

- **Session files are auto-organized** - `/q-learnings` and `/q-prompts` create files in `docs/sessions/YYYY-MM/` automatically.

## Suggestions

- **Run `/q-update` frequently** - Don't wait until end of session. If Claude Code crashes or you lose context, PLAN.md is your recovery point.

- **Keep CLAUDE.md focused** - Put only essential guidance here. Use `/q-pare` if it gets too long.

- **Use phases in PLAN.md** - Break work into numbered phases (1.1, 1.2, 2.1...) for clear progress tracking.

- **Delete this README** - Once you've set up your project, you don't need these instructions cluttering your folder.
