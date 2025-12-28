---
description: Update PLAN.md with current progress
argument-hint: ""
---

# Update Documentation

**Purpose:** Keep PLAN.md synchronized with current progress. Run this frequently during development to ensure documentation is always up-to-date in case the session needs to end.

## Actions

1. **Update Current Status section:**
   - Update phase number and emoji (🔥 for WIP)
   - Update test count if tests were added/fixed
   - Update other status indicators as needed

2. **Update WIP Phase (🔥) section:**
   - Check off completed subtasks with [x]
   - Add new subtasks discovered during work
   - Update "Work Completed" section with session accomplishments
   - Update "Current Glossary" or other relevant status blocks
   - Document any blockers or issues discovered

3. **If phase completed, restructure:**
   - Move completed phase from 🔥 WIP to 🏁 LATEST COMPLETE
   - Move oldest 🏁 to ✅ ARCHIVED (title + one line only)
   - Move 📋 NEXT phase to 🔥 WIP
   - Update phase emojis accordingly

4. **Update "Last Updated" timestamp** at bottom

5. **Confirm completion** with brief message showing:
   - What was updated
   - Current phase status
   - Next step to work on

## Example Response

```
✅ PLAN.md Updated

- Updated Phase 4.4 🔥 (WIP) with session progress
- Checked off subtasks 4.4.1 and 4.4.2
- Added findings about DeepL glossary behavior
- Updated "Last Updated" timestamp: 2025-11-21

Current Status: Phase 4.4 (DeepL Glossary Investigation) - 2 of 4 subtasks complete
Next: Continue with subtask 4.4.3 (Incremental testing)
```
