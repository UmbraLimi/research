# PLAYBOOK.md

This document tracks decisions about **how the prod-helpers repo itself works** — its organization, workflows, conventions, and tooling. For technical/architectural decisions (data, agents, APIs), see `DECISIONS.md`.

**Last Updated:** 2026-03-21

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

### Dual Decision Routing: DECISIONS.md + PLAYBOOK.md
**Date:** 2026-03-21

`/r-learn-decide` routes project-domain decisions (data, APIs, agents, migration) to `DECISIONS.md` and workflow/repo-convention decisions (skills, session management, docs structure) to `PLAYBOOK.md`.

**Rationale:** Keeps DECISIONS.md focused on the productivity system itself. Ported from peerloop-docs where this separation proved useful.

### Multi-Session Block Tracking via CURRENT-BLOCK-PLAN.md
**Date:** 2026-03-14 (adopted from peerloop-docs Session 276)

For blocks too large for one session, create `CURRENT-BLOCK-PLAN.md` at project root with per-item checkboxes, key files table, and progress summary. Each session reads it first, works through unchecked items, updates progress. Deleted when block completes.

**Rationale:** PLAN.md is too high-level for per-item tracking. RESUME-STATE.md is session-specific and gets deleted on resume. This fills the gap for multi-session continuity.

---

## 2. Deferred Enhancements

Patterns identified from the peerloop-docs project (386+ sessions) that are not yet needed here. Adopt when the trigger condition is met.

### Feature Tracking Rule
**Trigger:** When the project has enough docs and discussion that features could be mentioned outside PLAN.md and lost.

Any time a feature is mentioned — in a doc, discussion, or code comment — it must be added to PLAN.md with a cross-reference back to the source. Tech docs describe *how* and *why*; PLAN.md is the single source of truth for *what needs to be done*.

**Where to add:** CLAUDE.md (as a rule) + MEMORY.md (as feedback)

### Durable Insight Capture
**Trigger:** When DECISIONS.md or PLAYBOOK.md has enough entries that insights would add value.

During learn-decide processing, qualifying insights are co-located with the decision they illuminate as `> **Insight:**` blockquotes. An insight qualifies if it connects a decision to broader professional context or would teach someone starting a similar project.

**Where to add:** CLAUDE.md or `/r-learn-decide` skill instructions

### Test Suite Workflow: Run Once, Fix Individually
**Trigger:** When there is a test suite to run.

Run the full suite once and capture output. Extract failures into a list. Present to user before proceeding. Fix tests one by one with targeted runs. Don't re-run the full suite until all identified failures are fixed.

**Where to add:** CLAUDE.md (as a workflow rule)

### Generated Docs Must Have a Single Regeneration Command
**Trigger:** When there are scripts that produce committed documentation artifacts.

Any doc derived from code must be regenerable with a single command. One-off scripts that produce committed artifacts must be folded into permanent tooling in the same session they're created.

**Where to add:** CLAUDE.md (as a rule) or PLAYBOOK.md (as a convention)
