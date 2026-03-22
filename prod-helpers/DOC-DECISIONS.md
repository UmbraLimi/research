# DOC-DECISIONS.md

This document tracks decisions about **how the prod-helpers repo itself works** — its organization, workflows, conventions, and tooling. For technical/architectural decisions (data, agents, APIs), see `DECISIONS.md`.

**Last Updated:** 2026-03-22

---

## How This Document Works

- **Latest Wins:** If a newer decision contradicts an older one, only the newer decision appears here
- **Organized by Category:** Workflow conventions, future enhancements
- **Dates Included:** Each decision shows when it was made
- **Updated By:** `/r-learn-decide` routes docs-repo decisions here

---

## 1. Workflow Conventions

### TodoWrite Discipline: Capture Everything
**Date:** 2026-03-14 (adopted from peerloop-docs Session 386)

Any unresolved issue, opportunity, question, or implied action item must be added to TodoWrite immediately. Signal words: "should", "might", "could", "need to", "do later", "soon", "eventually". The user decides priority, not the assistant.

**Rationale:** TodoWrite items carry forward via `/r-save-state` → RESUME-STATE.md. Silently skipping items means they're lost in conversation noise.

### Skill `!` Backtick Pipes: Use Wrapper Scripts
**Date:** 2026-03-14

When a skill's `!` backtick pre-computed command contains shell pipes (`|`), extract it into a named script in `.claude/scripts/`. The script filename serves as self-documentation in the skill. One blanket permission rule `Bash(.claude/scripts/*)` covers all scripts.

**Rationale:** The permission checker matches full command strings — pipes cause "multiple operations" failures. Wrapper scripts are a single command from the checker's perspective. Broad `Bash(sed:*)` patterns also work but script names improve skill readability.

### `!` Backtick Paths: Relative in SKILL.md, Resolved in Scripts
**Date:** 2026-03-21

`!` backtick lines in SKILL.md must use relative paths (`.claude/scripts/foo.sh`), NOT `$CLAUDE_PROJECT_DIR`. The env var is not available during `!` backtick pre-computation. Scripts internally resolve paths via `${CLAUDE_PROJECT_DIR:-$(pwd)}` for portability across machines.

**Rationale:** `$CLAUDE_PROJECT_DIR` works in hook `command` fields but does NOT expand in `!` backtick execution. Relative paths work because skills execute from the project root. This is a refinement of the wrapper-scripts convention (2026-03-14).

### "Conv" Terminology Standard
**Date:** 2026-03-21

All skills and docs use "conv" (conversation) not "session". A conv maps 1:1 to a `/r-start` → `/r-end` cycle. Session files in `docs/sessions/` keep the directory name for backward compatibility but file headings use "Conv".

**Rationale:** Consistency across prod-helpers and peerloop-docs. "Conv" is more precise and matches the counter mechanism.

### Dual Decision Routing: DECISIONS.md + DOC-DECISIONS.md
**Date:** 2026-03-21

`/r-learn-decide` routes project-domain decisions (data, APIs, agents, migration) to `DECISIONS.md` and workflow/repo-convention decisions (skills, session management, docs structure) to `DOC-DECISIONS.md`.

**Rationale:** Keeps DECISIONS.md focused on the productivity system itself. Ported from peerloop-docs where this separation proved useful.

### Multi-Session Block Tracking via CURRENT-BLOCK-PLAN.md
**Date:** 2026-03-14 (adopted from peerloop-docs Session 276)

For blocks too large for one session, create `CURRENT-BLOCK-PLAN.md` at project root with per-item checkboxes, key files table, and progress summary. Each session reads it first, works through unchecked items, updates progress. Deleted when block completes.

**Rationale:** PLAN.md is too high-level for per-item tracking. RESUME-STATE.md is session-specific and gets deleted on resume. This fills the gap for multi-session continuity.

### Skills 2 Format for All Project Skills
**Date:** 2026-03-13

All skills use `.claude/skills/r-*/SKILL.md` format. This preserves `allowed-tools` restrictions and `!` backtick interpolation.

**Rationale:** Skills 2 format is required for `!` backtick pre-computation and tool scoping.

### Simplified r-docs Without Detection Scripts
**Date:** 2026-03-13

Use `git diff` + `find` instead of dedicated bash scripts for change detection in r-docs. Add detection scripts later if needed.

**Rationale:** Avoid premature infrastructure. The simpler approach works until the project grows.

### Machine Tracking in Commits
**Date:** 2026-03-14

Pre-compute `~/.claude/.machine-name` in r-commit SKILL.md. Commit body includes `Machine:` line.

**Rationale:** Two machines share this repo. Commit metadata makes it clear which machine produced the work.

### Auto-Synced CONV-COUNTER with Mandatory Pull/Push
**Date:** 2026-03-14

`/r-start` pulls + increments + pushes. `/r-end` commits + pushes. Both HALT on sync failure.

**Rationale:** Two machines sharing a repo need the conv counter synced via git. Halting on failure prevents counter drift.

### Separate /r-start and /r-end Skills
**Date:** 2026-03-14

Start wraps resume. End wraps eos + commit + push. No combined skill.

**Rationale:** Clear entry/exit points with distinct responsibilities. Start handles sync-in, end handles sync-out.

### RESUME-STATE.md Append Mode with Max 2 Blocks
**Date:** 2026-03-14

Oldest-first ordering, conv-labeled headings. `/r-save-state` refuses a 3rd append.

**Rationale:** Prevents unbounded state accumulation. Two blocks is enough for handoff context.

### /r-resume as Consolidation Point for Multi-Block State
**Date:** 2026-03-14

Walks blocks oldest→newest, evaluates with evidence, rewrites to single block after user approval.

**Rationale:** Prevents stale state from accumulating across sessions.

### Auto-Delete RESUME-STATE.md When All Items Complete
**Date:** 2026-03-14

Both `/r-resume` and `/r-save-state` detect all-done state and delete. File exists only for pending work.

**Rationale:** Keeps the repo clean. Git history preserves the state if needed later.

### Unified Entry Point — Always /r-start
**Date:** 2026-03-14

`/r-start` is the sole entry point for cold and warm starts. `/r-resume` is internal only, called by `/r-start` Step 6.

**Rationale:** One entry point eliminates confusion about which command to run.

### Per-Project Conv Numbering with 3-Letter Prefix
**Date:** 2026-03-21

PRH-004 format. Each project owns its CONV-COUNTER. Prefix registered in repo-root PROJECTS.yaml.

**Rationale:** Multiple projects in the same repo need distinct conv numbering.

### Hyphenated Prefix Format (PRH-009) for All Conv Labels
**Date:** 2026-03-22

Hyphenated format `{PREFIX}-{CONV}` used in commit messages, conv headers, and session doc filenames. `.conv-current` stays as pure 3-digit counter (`009`); prefix composed at point of use via `grep '^prefix:' PROJECT.yaml`.

**Rationale:** Hyphen works in filenames, commits, and display. Counter and label are separate concerns — counter auto-increments, label is a display composition.

### YAML Project Identity Files
**Date:** 2026-03-21

Subfolder `PROJECT.yaml` has prefix. Repo-root `PROJECTS.yaml` is the authoritative registry. Template gets XXX placeholder.

**Rationale:** Lightweight identity system for multi-project repos.

### Bulk-Sync r-* Skills from Peerloop-Docs
**Date:** 2026-03-21

All 10 skills updated: dirty-repo guard, structured commits, insight capture, TodoWrite-all-gaps, DOC-DECISIONS routing.

**Rationale:** Peerloop-docs had accumulated improvements over 386+ sessions that prod-helpers lacked.

### Unified Docs Folder Structure (6 Standard Folders)
**Date:** 2026-03-22

Six standard folders: `sessions/`, `requirements/`, `reference/`, `as-designed/`, `as-built/`, `guides/`. Lifecycle: requirements → as-designed → build → as-built. Folders created as needed, never pre-created empty. Documented in ~/research/CLAUDE.md and Minimum-Project/README.md.

**Rationale:** Reviewed four projects (prod-helpers, peerloop-docs, Comm-Helpers, Minimum-Project). Needed a unified convention for both coding and non-coding projects.

### as-designed/ and as-built/ Replace architecture/
**Date:** 2026-03-22

`as-designed/` for pre-build specs. `as-built/` for post-build documentation of implemented systems. The `as-` prefix makes the temporal distinction unmistakable.

**Rationale:** "architecture" was ambiguous — could mean intent or reality. User: "design is for what's being designed, architecture is what got built."

### Merge vendors/ into reference/
**Date:** 2026-03-22

Single `reference/` folder for all external tool, API, and service documentation. No distinction between API reference and vendor integration notes.

**Rationale:** User: "I fail to see the distinction between vendor and reference."

### Rename PLAYBOOK.md → DOC-DECISIONS.md
**Date:** 2026-03-22

Pairs with DECISIONS.md. Project decisions vs documentation/workflow decisions. Explicit naming over evocative naming.

**Rationale:** "PLAYBOOK" didn't convey that the file holds convention decisions.

### RFCs and User Stories in docs/requirements/
**Date:** 2026-03-22

`docs/requirements/` with `user-stories.md` (or dir), `rfcs/` subfolder with `INDEX.md` and numbered `RFC-001/` folders. Processed outputs only — no raw source material in the standard.

**Rationale:** Requirements sit upstream of design. Common to both coding and non-coding projects.

### Machine-Specific Credential Storage
**Date:** 2026-03-22

`credentials/` directory, one `.env` per machine (`MacMiniM4.env`, etc.), entire directory gitignored.

**Rationale:** API tokens differ per machine. Directory-based separation avoids merge conflicts on untracked files.

---

## 2. Deferred Enhancements

Patterns identified from the peerloop-docs project (386+ sessions) that are not yet needed here. Adopt when the trigger condition is met.

### Feature Tracking Rule
**Trigger:** When the project has enough docs and discussion that features could be mentioned outside PLAN.md and lost.

Any time a feature is mentioned — in a doc, discussion, or code comment — it must be added to PLAN.md with a cross-reference back to the source. Tech docs describe *how* and *why*; PLAN.md is the single source of truth for *what needs to be done*.

**Where to add:** CLAUDE.md (as a rule) + MEMORY.md (as feedback)

### Durable Insight Capture
**Trigger:** When DECISIONS.md or DOC-DECISIONS.md has enough entries that insights would add value.

During learn-decide processing, qualifying insights are co-located with the decision they illuminate as `> **Insight:**` blockquotes. An insight qualifies if it connects a decision to broader professional context or would teach someone starting a similar project.

**Where to add:** CLAUDE.md or `/r-learn-decide` skill instructions

### Test Suite Workflow: Run Once, Fix Individually
**Trigger:** When there is a test suite to run.

Run the full suite once and capture output. Extract failures into a list. Present to user before proceeding. Fix tests one by one with targeted runs. Don't re-run the full suite until all identified failures are fixed.

**Where to add:** CLAUDE.md (as a workflow rule)

### Generated Docs Must Have a Single Regeneration Command
**Trigger:** When there are scripts that produce committed documentation artifacts.

Any doc derived from code must be regenerable with a single command. One-off scripts that produce committed artifacts must be folded into permanent tooling in the same session they're created.

**Where to add:** CLAUDE.md (as a rule) or DOC-DECISIONS.md (as a convention)
