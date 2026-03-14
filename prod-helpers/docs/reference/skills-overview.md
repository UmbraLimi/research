# Skills Overview

**Created:** 2026-03-13
**Location:** `.claude/skills/r-*/SKILL.md`
**Format:** Skills 2 (`.claude/skills/{name}/SKILL.md` with `allowed-tools` and `!` interpolation)

## Purpose

Session management skills adapted from peerloop-docs (w-* series, 386+ sessions proven). These handle end-of-session documentation, plan tracking, and cross-session continuity for the prod-helpers project.

## Skill Inventory

| Skill | Type | Purpose |
|-------|------|---------|
| `/r-start` | Conversation | Pull, increment conv counter, push, then resume |
| `/r-end` | Conversation | Run eos sequence, commit, push, cleanup — replaces manual /r-eos + /r-commit |
| `/r-eos` | Orchestrator | Runs the 4-skill end-of-session sequence in order |
| `/r-learn-decide` | Session docs | Captures learnings and decisions to structured files |
| `/r-dump` | Session docs | Creates development transcript with verbatim user prompts |
| `/r-update-plan` | Plan tracking | Keeps PLAN.md synchronized with progress |
| `/r-docs` | Documentation | Updates project docs affected by session changes |
| `/r-save-state` | Continuity | Saves work state to RESUME-STATE.md for cross-session resume |
| `/r-commit` | Git | Commits only this folder's changes (includes Conv + Machine metadata) |
| `/r-resume` | Continuity | Loads PLAN.md and presents resumption context |

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
  ├── /r-commit             ← includes Conv: + Machine: in message
  └── git push              ← mandatory sync

/r-save-state              ← standalone, called mid-session or before /compact
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
- 2026-03-14: Added `/r-start`, `/r-end` for conversation lifecycle; added Conv + Machine metadata to `/r-commit`
