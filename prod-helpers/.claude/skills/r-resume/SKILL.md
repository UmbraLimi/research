---
name: r-resume
description: Resume work by analyzing PLAN.md and current progress
argument-hint: ""
allowed-tools: Read, Glob, Grep
---

# Resume Work Session

**Purpose:** Analyze PLAN.md to understand current progress and present a concise resumption context.

---

## Pre-computed Context

**PLAN.md exists:**
!`test -f PLAN.md && echo "yes" || echo "NO — PLAN.md not found, cannot resume"`

**Current status header:**
!`.claude/scripts/plan-status-header.sh`

**Active/WIP phase:**
!`.claude/scripts/plan-wip-markers.sh`

**Open questions:**
!`.claude/scripts/plan-open-questions.sh`

**RESUME-STATE.md:**
!`cat RESUME-STATE.md 2>/dev/null || echo "(no resume state file)"`

---

## Actions

1. **Read PLAN.md** fully if the pre-computed context above is insufficient to identify:
   - Current WIP phase (🔥 emoji)
   - Latest completed phase (🏁 emoji)
   - Next planned phase (📋 emoji)
   - Subtask checklist status

2. **Present Context** in this format:

```
📍 Current Position
─────────────────

🔥 WIP: Phase X.Y - [Phase Name]
   Progress: [X] of [Y] subtasks complete ([Z]%)

   ✅ Completed:
   - [List completed subtasks]

   ⏭️  Remaining:
   - [Next immediate task with details]
   - [Subsequent tasks]

🏁 Last Completed: Phase A.B - [Phase Name]

📋 Next Planned: Phase C.D - [Phase Name]

─────────────────
🎯 Recommended Action

[Specific, actionable next step based on current WIP.
 Include file paths and commands when relevant.]

─────────────────
💡 Quick Context

[1-2 sentence summary of what this phase accomplishes and why it matters]
```

---

## Rules

- Focus on the **next actionable step**, not high-level strategy
- Include **specific file paths** and commands when relevant
- Highlight **blockers** that need resolution before continuing
- Keep context brief but sufficient to resume without reading entire PLAN.md
- If RESUME-STATE.md exists, incorporate its context (it captures cross-session state)
