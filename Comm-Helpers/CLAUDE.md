# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

This project creates Claude Code skills for processing communication threads (Slack, Telegram, email) and extracting:
- Impact summaries
- Decisions/actions required of the user
- Commitments others made that should be tracked

Output is markdown text for copy-paste into Obsidian.

## Key Files

| File | Purpose |
|------|---------|
| `PURPOSE.md` | Project goals, requirements, output format specification |
| `PLAN.md` | Current progress and next steps (create after setup) |
| `.claude/commands/` | Skills created by this project |

## Skill Development

Skills are `.md` files in `.claude/commands/`. When creating thread-processing skills:

1. Input: User pastes communication thread content
2. Output: Markdown block matching the format in PURPOSE.md (Summary, Decisions Needed, Watching For, Key Points, Source metadata)
3. No API integrations—paste in, copy out

See PURPOSE.md for the exact output format template and platform-specific considerations.

## Slash Commands

| Command | Scope | Purpose |
|---------|-------|---------|
| `/r-commit` | This folder | Commit only Comm-Helpers changes |
| `/repo-commit` | All projects | Commit all repo changes |
| `/par-resume` | — | Load PLAN.md and continue work |
| `/par-update` | — | Save progress to PLAN.md |
| `/par-end-session` | — | Wrap up: learnings, prompts, optional commit |
