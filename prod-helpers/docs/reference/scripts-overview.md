# Scripts Overview

**Type:** script collection
**Created:** 2026-03-14
**Location:** `.claude/scripts/`

## Purpose

Wrapper scripts for piped shell commands used in skill `!` backtick pre-computed context. The permission checker rejects piped commands as "multiple operations" — wrapping them in scripts makes each a single command from the checker's perspective.

## Script Inventory

| Script | Used By | What It Does |
|--------|---------|-------------|
| `plan-status-header.sh` | r-resume | Extracts PLAN.md header up to first Phase heading |
| `plan-wip-markers.sh` | r-resume | Finds WIP/checkbox lines in PLAN.md |
| `plan-open-questions.sh` | r-resume, r-update-plan | Extracts Open Questions section from PLAN.md |
| `session-files-dev.sh` | r-dump | Lists recent Dev session files for current month |
| `session-files-learn-decide.sh` | r-learn-decide | Lists recent Learnings/Decisions files for current month |
| `decisions-categories.sh` | r-learn-decide | Extracts category headings from DECISIONS.md |
| `docs-list.sh` | r-docs | Lists all markdown files in docs/ |
| `resume-state-check.sh` | r-save-state | Checks if RESUME-STATE.md exists and shows saved date |
| `conv-read-counter.sh` | r-start, r-save-state | Reads CONV-COUNTER persistent value |
| `conv-read-current.sh` | r-commit, r-end, r-save-state | Reads .conv-current ephemeral session value |

## Permission

One blanket rule in `.claude/settings.local.json`:
```json
"Bash(.claude/scripts/*)"
```

## Design Rationale

Script filenames serve as self-documentation in skills — `!`.claude/scripts/plan-status-header.sh`` is more readable than the inline `sed -n '1,/^## Phase/p' PLAN.md 2>/dev/null | head -20`. The indirection preserves `!` backtick build-time execution.

This pattern is also used in peerloop-docs (`w-docs` skill with `${CLAUDE_SKILL_DIR}/scripts/`).

## History

- 2026-03-14: Created — 8 scripts extracted from 6 skills to resolve permission checker failures on piped commands
- 2026-03-14: Added conv-read-counter.sh and conv-read-current.sh for conversation numbering
