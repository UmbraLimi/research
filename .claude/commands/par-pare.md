---
description: Optimize CLAUDE.md by moving content to OFFLOAD.md
argument-hint: ''
---

# Pare CLAUDE.md

**Purpose:** Optimize CLAUDE.md by moving less-critical reference material to OFFLOAD.md. Since CLAUDE.md is always loaded into context, keeping it lean improves performance and focuses on essential session guidance.

## Actions

1. **Analyze CLAUDE.md** and identify content to offload:

   **KEEP in CLAUDE.md (essential for sessions):**

   - Project overview (1-4 paragraphs)
   - Core architecture/structure overview (brief)
   - Custom slash commands list
   - Important implementation notes

   **MOVE to OFFLOAD.md (useful but less frequent):**

   - Reference links

2. **Create/Update OFFLOAD.md:**

   - Add header: "# OFFLOAD.md - Extended Documentation"
   - Add description: "This file contains detailed reference material extracted from CLAUDE.md to optimize context loading. Consult this file when you need detailed specifications."
   - Organize content by category with clear headers
   - Maintain all original content formatting

3. **Update CLAUDE.md:**

   - Add pointer section at top (after project overview):

     ```
     ## Extended Documentation

     For detailed reference material (full commands, structure, etc.), see `OFFLOAD.md`.
     This file is kept lean for optimal context loading.
     ```

   - Replace detailed sections with concise summaries + "See OFFLOAD.md for details"
   - Keep structure but reduce verbosity
   - Maintain all critical decision-making information

4. **Confirm completion** with summary:
   - List what sections were moved
   - Show before/after approximate line count or token estimate
   - Confirm CLAUDE.md remains functional

## Example Response

```
✅ CLAUDE.md Optimized

Moved to OFFLOAD.md:
- Less useful Reference links

CLAUDE.md changes:
- Before: ~325 lines
- After: ~150 lines (estimated 50% reduction)
- Added pointer to OFFLOAD.md
- Maintained all essential guidance

Both files ready. CLAUDE.md is now optimized for context loading.
```
