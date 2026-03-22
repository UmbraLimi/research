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
!`.claude/scripts/plan-status-header.sh`

**Open questions:**
!`.claude/scripts/plan-open-questions.sh`

---

## Actions

1. **Update active phase tasks:**
   - Check off completed subtasks with [x]
   - Add new subtasks discovered during work
   - Document any blockers or issues

2. **If a sub-phase completes:**
   - Strip it from PLAN.md
   - Add it to the phase's "Completed:" one-liner summary at the top
   - Keep detail for remaining items only

3. **If a full phase completes:**
   - Add terse entry to `COMPLETED_PLAN.md` (phase name + 1-line summary + conv range)
   - Remove entire completed phase from PLAN.md — no stub, no link, no "see COMPLETED_PLAN.md"
   - Fold deferred items from the completing phase into other relevant phases
   - Update "Current Status" at top of PLAN.md

4. **Update Open Questions** — add new questions, remove resolved ones

5. **Update Decisions** — if any decisions were made, note them (and ensure they're in `DECISIONS.md`)

6. **Confirm completion** with brief message

---

## What Lives Where

| Content | Location | Notes |
|---------|----------|-------|
| **Remaining work** | `PLAN.md` | Active phases only |
| **Completed phase archive** | `COMPLETED_PLAN.md` | Terse: name + 1-line summary + conv range |
| **Conv details** | `docs/sessions/` | Full conv logs |
| **Decision records** | `DECISIONS.md` | Project decisions |
| **Workflow conventions** | `PLAYBOOK.md` | Repo workflow decisions |
| **Project goals and context** | `PURPOSE.md` | |
| **API reference** | `docs/reference/` | |
| **Architecture designs** | `docs/architecture/` | |

**Do NOT put in PLAN.md:**
- Completed work details (use COMPLETED_PLAN.md)
- Conv notes or timestamps (use docs/sessions/)
- Decision rationale (use DECISIONS.md or PLAYBOOK.md)

---

## Phase Completion Rules

### While a Phase is Active

**Only show remaining work.** When a sub-phase completes:
- Strip it from PLAN.md
- Add it to the phase's "Completed:" one-liner summary at the top
- Keep detail for remaining items only

### When a Phase Fully Completes

1. **Add terse entry to COMPLETED_PLAN.md:**
   ```markdown
   ## Phase N: Phase Name ✓
   Brief 1-line summary of deliverables. Convs: NNN-NNN (YYYY-MM-DD)
   ```

2. **Remove entire phase from PLAN.md** — no stub, no link

3. **Fold deferred items** from the completing phase into other relevant phases

4. **Update "Current Status"** at top of PLAN.md

### Phases Are Forward-Looking Only

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
