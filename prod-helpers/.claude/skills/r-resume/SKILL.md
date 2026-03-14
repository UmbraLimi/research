---
name: r-resume
description: Resume work by analyzing PLAN.md and current progress
argument-hint: ""
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
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

## Multi-Block Consolidation

If `RESUME-STATE.md` contains multiple state blocks (detected by more than one `# State — Conv` heading), consolidate **before** presenting the resume context:

### Step A: Walk blocks oldest → newest

Read each block's **Remaining** section. For each item in an earlier block:

1. **Check if done** — use `Grep`, `Glob`, `Read`, or `git log --oneline` (via Bash) to determine if the work was completed. Look for the files/changes the item describes.
2. **Check for interactions** — does a later block's Remaining or Completed reference the same files, features, or decisions? Flag overlaps or conflicts.

### Step B: Explain what you intend to do and why

For each item across both blocks, explain your reasoning:

```
🔄 Consolidating RESUME-STATE.md (2 blocks)
─────────────────────────────────────────────

Block 1: Conv NNN (date) — [1-line summary]
Block 2: Conv MMM (date) — [1-line summary]

✅ Marking as done:
- [item] — done because [evidence: file exists, git log shows commit, etc.]
- [item] — done because [evidence]

⚠️  Interactions between blocks:
- [item from block 1] and [item from block 2] touch the same [file/feature/decision] — [explain the relationship and how you propose to handle it]

⏭️  Carrying forward (still pending):
- [item] — not done because [evidence: file not found, no commits touching this, etc.]
- [item] — not done because [evidence]

🗑️  Dropping:
- [item] — [reason: superseded by block 2 item X / no longer relevant because Y]
```

**Explain every classification.** The user needs to see your reasoning to catch mistakes — you may misjudge whether something is done or misread an interaction. Wait for user approval before rewriting.

### Step C: Rewrite as single block

Rewrite `RESUME-STATE.md` as a single `# State — Conv MMM (date)` block (using the latest conv) that merges:
- **Completed**: items from both blocks that are done
- **Remaining**: items from both blocks that are still pending, deduplicated
- **Key Context**: merged from both blocks, dropping stale entries
- **TodoWrite Items**: carried from the latest block only (earlier ones are stale)

This ensures the next `/r-pre-clear` can only ever create a 2-block file.

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
- If RESUME-STATE.md exists with a single block, incorporate its context (it captures cross-session state)
- If RESUME-STATE.md has multiple blocks, run **Multi-Block Consolidation** (above) before presenting the resume context
