---
name: r-update-plan
description: Update PLAN.md with current progress
argument-hint: ""
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Update PLAN.md

**Purpose:** Keep PLAN.md synchronized with current progress. Run this frequently to ensure documentation stays current.

---

## Pre-computed Context

**Current PLAN.md status:**
!`head -10 PLAN.md 2>/dev/null || echo "(PLAN.md not found)"`

**Open questions:**
!`sed -n '/^## Open Questions/,/^## /p' PLAN.md 2>/dev/null | head -20 || echo "(none found)"`

---

## Actions

1. **Update active phase tasks:**
   - Check off completed subtasks with [x]
   - Add new subtasks discovered during work
   - Document any blockers or issues

2. **If a sub-phase completes:**
   - Mark all its tasks as done
   - Note completion in the phase header

3. **If a full phase completes:**
   - Add terse entry to `COMPLETED_PLAN.md` (phase name + 1-line summary)
   - Remove completed phase from PLAN.md
   - Update "Current Status" at top of PLAN.md

4. **Update Open Questions** — add new questions, remove resolved ones

5. **Update Decisions** — if any decisions were made, note them (and ensure they're in `DECISIONS.md`)

6. **Confirm completion** with brief message

---

## What Lives Where

| Content | Location |
|---------|----------|
| **Remaining work** | `PLAN.md` |
| **Completed phase archive** | `COMPLETED_PLAN.md` |
| **Session details** | `docs/sessions/` |
| **Decision records** | `DECISIONS.md` |
| **Project goals and context** | `PURPOSE.md` |
| **API reference** | `docs/reference/` |
| **Architecture designs** | `docs/architecture/` |

**Do NOT put in PLAN.md:**
- Completed work details (use COMPLETED_PLAN.md)
- Session notes or timestamps (use docs/sessions/)
- Decision rationale (use DECISIONS.md)

---

## Phase Completion Rules

### While a Phase is Active

**Only show remaining work.** When a sub-phase completes, note it briefly and keep detail for remaining items only.

### When a Phase Fully Completes

1. **Add terse entry to COMPLETED_PLAN.md:**
   ```markdown
   ## Phase N: Phase Name ✓
   Brief 1-line summary of what was accomplished.
   ```

2. **Remove entire phase from PLAN.md** — no stub, no link

3. **Update "Current Status"** at top of PLAN.md

---

## PLAN.md is Forward-Looking Only

PLAN.md contains only work that remains to be done. Completed work lives exclusively in COMPLETED_PLAN.md.

---

## Confirmation

```
PLAN.md Updated

Changes:
- [What was updated]

Current Status:
- Active: [Current active phase]
- Completed: [Phase that just completed, if any]

Next: [Immediate next action]
```
