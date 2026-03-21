# Skills Overview

**Created:** 2026-03-13
**Location:** `.claude/skills/r-*/SKILL.md`
**Format:** Skills 2 (`.claude/skills/{name}/SKILL.md` with `allowed-tools` and `!` interpolation)

## Purpose

Session management skills adapted from peerloop-docs (w-* series, 386+ sessions proven). These handle end-of-session documentation, plan tracking, and cross-session continuity for the prod-helpers project.

## Skill Inventory

| Skill | Type | Purpose |
|-------|------|---------|
| `/r-start` | Conversation | Pull, increment conv counter, push, transfer RESUME-STATE.md tasks to TodoWrite, then resume — sole entry point for all convs |
| `/r-end` | Conversation | Run eos sequence, save state (TodoWrite → RESUME-STATE.md), commit, push, cleanup |
| `/r-eos` | Orchestrator | Runs the 4-skill end-of-session sequence in order |
| `/r-learn-decide` | Session docs | Captures learnings and decisions to structured files |
| `/r-dump` | Session docs | Creates development transcript with verbatim user prompts |
| `/r-update-plan` | Plan tracking | Keeps PLAN.md synchronized with progress |
| `/r-docs` | Documentation | Updates project docs affected by session changes |
| `/r-save-state` | Continuity | Saves work state to RESUME-STATE.md; supports append mode (max 2 blocks); auto-deletes when all items done |
| `/r-commit` | Git | Commits only this folder's changes (includes Conv + Machine metadata) |
| `/r-resume` | Continuity | Loads PLAN.md, consolidates multi-block RESUME-STATE.md, auto-deletes when all done, conv state warnings; called internally by /r-start |

## Interaction Model

```
/r-start (conversation open)
  └── /r-resume            ← called after pull/increment/push

/r-end (conversation close)
  ├── /r-eos (orchestrator)
  │   ├── 1. /r-learn-decide  ← receives shared timestamp
  │   ├── 2. /r-dump           ← receives shared timestamp
  │   ├── 3. /r-update-plan
  │   └── 4. /r-docs
  ├── /r-save-state          ← captures TodoWrite items to RESUME-STATE.md (skipped if no pending tasks)
  ├── /r-commit              ← includes Conv: + Machine: in message
  └── git push               ← mandatory sync

/r-save-state              ← standalone, called mid-session or before /compact
  ├── fresh file           ← writes single block with conv-labeled heading
  ├── existing (1 block)   ← offers: overwrite / view / abort / append
  └── existing (2 blocks)  ← refuses append, tells user to /r-resume first

/r-resume (multi-block consolidation + conv state checks)
  ├── checks conv state: warns if no .conv-current or stale context
  ├── detects 2+ blocks in RESUME-STATE.md
  ├── walks oldest→newest, checks earlier items against current state
  ├── explains each classification with evidence (done because X, pending because Y, interaction because Z)
  ├── waits for user approval before rewriting
  ├── rewrites to single block after approval
  ├── auto-deletes RESUME-STATE.md if all remaining items are [x]
  └── then proceeds with normal resume flow
```

### Shared Timestamp Convention

`/r-eos` pre-computes a single timestamp and passes it to `/r-learn-decide` and `/r-dump` as arguments so all session files share the same prefix:

- **MONTH:** `YYYY-MM` (directory name)
- **FILENAME:** `YYYYMMDD_HHMM` (file prefix, compact, no hyphens)

Example: `docs/sessions/2026-03/20260313_2139 Learnings.md`

When skills are called standalone (not via `/r-eos`), they compute their own timestamp.

## Design Rationale

### Why r-* prefix
Disambiguates project-specific skills from parent-level `par-*` commands (available across all research subfolders) and from other projects' prefixes (`w-*` for peerloop-docs, `q-*` for translation-system).

### Why Skills 2 format
Preserves `allowed-tools` (restricts each skill to only the tools it needs) and `!` shell interpolation (pre-computes context like git status, existing files, PLAN.md state before the skill runs). These were stripped when initially adapted to the older `.claude/commands/` format — a mistake that was corrected.

### Why adapted from peerloop-docs (not translation-system)
Peerloop-docs skills are the most mature (386+ sessions). Translation-system uses the older `q-*` commands format. Peerloop-docs also has the dual-repo architecture which forced cleaner separation of concerns in its skills.

### Why wrapper scripts for `!` backtick pipes
The permission checker matches full command strings — piped commands like `sed ... | head` fail as "multiple operations." Skills now call named scripts in `.claude/scripts/` instead. This preserves build-time determinism, and the script filenames serve as self-documentation in the skill (e.g., `!`.claude/scripts/plan-status-header.sh``). One blanket permission rule `Bash(.claude/scripts/*)` covers all scripts.

### Why no detection scripts in r-docs
Peerloop-docs `/w-docs` has 4 helper bash scripts for automated change detection. These were omitted because a planning/research project doesn't have the code surface area to justify them. Simple `git diff` and `find` in `!` interpolation are sufficient. Scripts can be added later if needed.

### Why no shadow docs for individual skills
Each SKILL.md is self-documenting — it contains purpose, usage, and design in its frontmatter and body. This overview captures the system-level concerns (interactions, shared conventions, rationale) that individual files can't express.

## Conversation Lifecycle

### What is a "Conv"?

A **conv** (conversation) = one Claude Code invocation with continuous memory. A conv can produce zero or many commits. All commits within a conv share the same conv number (e.g. `Conv: 003`). This gives a human-friendly sense of recency that git hashes lack.

### Key Files

| File | Committed? | Purpose |
|------|-----------|---------|
| `CONV-COUNTER` | Yes | Persistent integer, incremented each conv. Cross-machine sync via git. |
| `.conv-current` | No (gitignored) | Zero-padded conv number for the active session (e.g. `003`). Ephemeral — deleted by `/r-end`. |
| `RESUME-STATE.md` | Yes | Captures work state for resumption after `/clear` or new session. Conv-labeled blocks (`# State — Conv NNN`), max 2 before consolidation. Includes TodoWrite items, conv state, remaining work. |

### Single Entry Point

Always run `/r-start`. It handles both cold and warm starts — it calls `/r-resume` internally, which picks up RESUME-STATE.md if present.

```
$ claude
> /r-start       ← git pull, read CONV-COUNTER, increment, commit+push, then /r-resume
```
`/r-start` ensures the conv counter is synced from remote before incrementing. The push happens before any work begins, so the other machine will always see it.

For warm restarts (fresh context, same sitting), the user runs `/r-end` → `/r-start`. The `/r-end` saves pending tasks to RESUME-STATE.md, and the next `/r-start` transfers them back to TodoWrite.

### Closing a Conv

```
> /r-end          ← /r-eos (4 sub-skills), /r-save-state, /r-commit, git push, rm .conv-current
```
Always push. HALT on push failure. This is what syncs everything for the other machine.

### Common Flows

**Single session, end for the day:**
```
/r-start → [work] → /r-end → exit
```

**Multiple convs, same sitting:**
```
/r-start → [work] → /r-end → /r-start → [work] → /r-end → exit
```

**Cross-machine:**
```
Machine A: /r-start → [work] → /r-end → exit
Machine B: /r-start → [work] → /r-end → exit
```

### Edge Cases

| Situation | What happens |
|-----------|-------------|
| `.conv-current` exists at `/r-start` | Warning (prior conv didn't `/r-end` cleanly). Proceeds — `CONV-COUNTER` post-pull is source of truth. |
| Push fails in `/r-start` or `/r-end` | HALT. Do not proceed. Conv counter is not synced. |
| Network down at `/r-start` | Pull fails → HALT. Cannot guarantee counter is current. |
| Network down at `/r-end` | Push fails → HALT. Do not report success. User must push manually when network returns. |

### Commit Message Metadata

Every commit via `/r-commit` includes:
```
Conv: 003
Machine: MacMiniM4
```
These are pre-computed via `!` backticks reading `.conv-current` and `~/.claude/.machine-name`.

---

## Conventions

### Session file naming
All session files go to `docs/sessions/YYYY-MM/` with format `YYYYMMDD_HHMM {Type}.md`:
- `{prefix} Learnings.md` — insights, gotchas, patterns
- `{prefix} Decisions.md` — choices between alternatives (skipped if none)
- `{prefix} Dev.md` — chronological transcript with verbatim user prompts

### Topic tags
Learnings and decisions are tagged with topics from this list (extensible):
`dynalist`, `obsidian`, `joplin`, `tags`, `agents`, `skills`, `migration`, `credentials`, `youtube`, `workflow`

### Decision routing
Important decisions from session files are also added to `DECISIONS.md` under categories: Data Architecture, Tag System, Migration Strategy, Agent Design, Tooling & APIs.

### PLAN.md is forward-looking only
Completed phases move to `COMPLETED_PLAN.md`. PLAN.md never contains finished work.

## History

- 2026-03-13: Created — 7 skills adapted from peerloop-docs w-* series for prod-helpers project setup session
- 2026-03-14: Added `/r-resume`, extracted piped `!` backtick commands into `.claude/scripts/` wrapper scripts across 6 skills
- 2026-03-14: Added `/r-start`, `/r-end`, `/r-pre-clear` for conversation lifecycle; added Conv + Machine metadata to `/r-commit`
- 2026-03-14: Added append mode to `/r-save-state` (conv-labeled blocks, max 2); added multi-block consolidation to `/r-resume` (walk → evaluate → merge → rewrite)
- 2026-03-14: Unified entry point — `/r-start` is sole entry for all convs; `/r-resume` internal only. Added conv state warnings and all-done auto-delete to `/r-resume` and `/r-save-state`
- 2026-03-21: Simplified workflow — removed `/r-pre-clear`; `/r-end` now auto-calls `/r-save-state` to capture TodoWrite items; `/r-start` now transfers RESUME-STATE.md tasks back to TodoWrite. Closed-loop task persistence across sessions.
