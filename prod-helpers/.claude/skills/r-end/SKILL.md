---
name: r-end
description: End conversation — run end-of-session sequence, save state, commit, and push
argument-hint: ""
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Skill, TaskList
---

# End Conversation

**Purpose:** Run the full end-of-session sequence, commit all changes (with conv number and machine), and push to remote so the next machine has everything.

---

## Pre-computed Context

**Machine:**
!`cat ~/.claude/.machine-name 2>/dev/null || echo "(unknown)"`

**Current conv:**
!`.claude/scripts/conv-read-current.sh`

**Shared timestamp:**
!`echo "MONTH: $(date '+%Y-%m')" && echo "FILENAME: $(date '+%Y%m%d_%H%M')"`

---

## Execution Flow

### Step 1: Validate conv is active

Read `.conv-current`. If it's missing or says "MISSING", **HALT** — tell the user to run `/r-start` first. Do not proceed without a locked conv number.

### Step 2: Run end-of-session sequence

Invoke the 4 sub-skills **sequentially** via the Skill tool, passing the shared timestamp. Each must complete before the next starts.

1. **`/r-learn-decide`** with args `{MONTH} {FILENAME}`
2. **`/r-dump`** with args `{MONTH} {FILENAME}`
3. **`/r-update-plan`**
4. **`/r-docs`**

### Step 3: Save pending work state

Check if any pending TodoWrite tasks exist (via `TaskList`). If there are pending tasks:

- Invoke `/r-save-state` via the Skill tool. This captures remaining TodoWrite items into `RESUME-STATE.md` so they survive across sessions.
- Note in summary: "State saved ✅"

If no pending tasks exist:

- Skip `/r-save-state`
- Note in summary: "State saved ⏭️ (no pending tasks)"

### Step 4: Commit all project changes

Invoke `/r-commit` via the Skill tool. The commit message must include both `Conv:` and `Machine:` in the body (r-commit handles this from its own pre-computed context).

### Step 5: Push to remote

```bash
git push
```

This is **mandatory** — it syncs the work and any counter state for the other machine. If the push fails, tell the user and do not report success.

### Step 6: Clean up session lock

```bash
rm .conv-current
```

### Step 7: Display closing summary

```
╔═══════════════════════════════════╗
║  Conv {PADDED_VALUE} closed       ║
╚═══════════════════════════════════╝

End-of-Session Complete
───────────────────────
1. Learn/Decide  ✅
2. Session Dump   ✅
3. Plan Update    ✅
4. Docs Update    ✅
5. State Saved    ✅ / ⏭️
6. Committed      ✅
7. Pushed         ✅

Safe to exit.
```

---

## Rules

- **HALT if no active conv** — `.conv-current` must exist
- **HALT on push failure** — do not report success if push fails
- Run sub-skills in strict order — do not skip or reorder
- If a sub-skill asks the user a question, wait for their answer before continuing
- Delete `.conv-current` only after successful push
- After displaying the closing summary, do NOT take further actions — the user should exit
