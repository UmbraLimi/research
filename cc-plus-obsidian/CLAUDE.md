# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

This is a **planning project** (no code yet) designing a **practice management vault** — a solopreneur's unified knowledge base, work log, and project management system built on Obsidian and integrated with Claude Code. The vault handles multiple coding projects, business operations, reference material, and daily journaling. PeerLoop is the first project onboarded; any project follows the same conventions.

The core design principles:

- **Repos hold code only.** All narrative (session logs, plans, decisions, learnings) lives in an Obsidian vault.
- **A local MCP server** gives CC full read access to the main vault with `===` credential redaction.
- **CC writes to the vault via global skills** — session docs (`/cco-session-close`) and daily note processing (`/cco-process-daily`).
- **Daily notes are the human capture surface.** You write under `[[wikilinked]]` headings; CC processes them into structured atomic notes and card-type records.
- **Truly private content** lives in a separate private vault at `~/Vaults/private/` (deferred — see PLANNING.md).

The full design document is `PLANNING.md`. The `README.md` is Minimum-Project template boilerplate and can be deleted.

## Architecture Summary

**Two vaults:**
- `~/Vaults/main/` — CC-accessible, all FULL access
- `~/Vaults/private/` — CC-denied, local LLM only (deferred)

**Main Vault structure** — all CC: FULL:

| Folder | Purpose |
|--------|---------|
| `journal/daily/` | Daily notes (human capture surface) |
| `log/notes/` | Atomic notes extracted from daily notes |
| `log/coding/` | Coding timecard cards (CC-generated from git) |
| `log/non-coding/` | Non-coding timecard cards |
| `log/meetings/` | Meeting, phone call, and site visit cards |
| `log/slack/` | Slack thread cards |
| `log/email/` | Email thread cards |
| `log/telegram/` | Telegram thread cards |
| `projects/` | Per-project logs, tasks, plans, sessions, decisions, learnings |
| `reference/` | Tech notes, vendors, schemas, patterns, templates |
| `business/` | Clients, proposals, operations |

**Four CC global skills** (prefixed `cco-`):

| Skill | Purpose |
|-------|---------|
| `/cco-session-close` | Writes CC session docs + generates coding timecard from git |
| `/cco-process-daily` | Processes daily note headings into atomic notes and cards |
| `/cco-migrate-schema` | Backfills schema changes to existing card notes |
| `/cco-project-init` | Sets up repo CLAUDE.md + vault project folder |

## Key Files

| File | Purpose |
|------|---------|
| `DECISIONS.md` | **Authoritative net decisions.** Always check here first for current project decisions. |
| `PLANNING.md` | Full design document with rationale, alternatives considered, and specs. |
| `PLAN.md` | Task tracking and current sequence. What to work on next. |
| `COMPLETED-PLAN.md` | Archive of completed phase details. |

## Content Rules

**Never delete or collapse plan content without explicit instruction.** When told to "defer", "pause", or "skip" something:
- Add a `*(deferred)*` marker and a one-line rationale
- Keep all tasks, sub-phases, and detail intact
- Only the status changes — the content stays in full

**Your goal is never to make files shorter.** If you feel content can be removed, confirm the specific content being removed with the user first.

## Git Rules

**Always ask for explicit permission before running any history-changing git command:**
- `rebase`, `merge`, `reset --hard`, `push --force`, `commit --amend`
- Explain *why* you want to run the command and let the user decide

**Safe commands (no permission needed):**
- `push`, `pull --ff-only`, `add`, `commit`, `status`, `log`, `diff`, `branch`

## Git Commit Workflow

| Command | Scope |
|---------|-------|
| `/r-commit` | This folder's changes only |
| `/repo-commit` | All changes across the MyResearch repo |

## Slash Commands

**Parent-level** (`/par-*`): `/par-resume`, `/par-update`, `/par-end-session`, `/par-learnings`, `/par-prompts`, `/par-timestamp`, `/par-pare`

**Project-level**: `/r-commit`

## Session History

| Date | Summary |
|------|---------|
| 2026-02-09 (2) | Implementation session. Built vault (`~/Vaults/main/`), 7 schemas, 4 `cco-*` global skills, relocated PeerLoop repo. Integration tested process-daily, project-init, migrate-schema. Created DECISIONS.md. |
| 2026-02-09 (1) | Initial planning session. Created PLANNING.md and CLAUDE.md. Designed vault structure, daily note processing workflow, card types (6), schema system, mobile strategy, PLAN.md format. Resolved all 8 open questions. |
