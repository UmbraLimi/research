---
name: r-end
description: End conversation — run end-of-conv sequence, save state, commit, and push
argument-hint: ""
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Skill, TaskList
---

# End Conversation

**Purpose:** Run the full end-of-conv sequence, commit all changes (with Conv and Machine metadata), and push to remote so the next machine has everything.

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

### Step 2: Run end-of-conv sequence

Invoke `/r-eos` via the Skill tool. It runs the 4 sub-skills sequentially:

1. `/r-learn-decide`
2. `/r-dump`
3. `/r-update-plan`
4. `/r-docs`

Wait for it to complete fully.

> **⚠️ CRITICAL: /r-eos completing is NOT the end of /r-end.**
> Steps 3–7 below MUST still execute after /r-eos finishes.
> Do NOT stop, summarize, or wait for user input — proceed immediately to Step 3.

### Step 3: Save pending work state (if any)

Check the TaskList for pending (not completed) items. If any exist:

1. Invoke `/r-save-state` via the Skill tool
2. Wait for it to complete fully
3. Note in the closing summary: `State saved ✅`

If no pending tasks exist, skip this step and note: `State saved ⏭️  (no pending tasks)`

This ensures TodoWrite items and unfinished work survive across `/clear` boundaries. RESUME-STATE.md will be included in the commit that follows.

### Step 4: Commit all project changes

Invoke `/r-commit` via the Skill tool. The commit message must include both `Conv:` and `Machine:` in the body (r-commit handles this from its own pre-computed context).

### Step 5: Push to remote

```bash
git push
```

This is **mandatory** — it syncs the work and counter state for the other machine. If the push fails, tell the user and do not report success.

### Step 6: Clean up conv lock

```bash
rm .conv-current
```

### Step 7: Display closing summary

```
╔═══════════════════════════════════╗
║  Conv {PADDED_VALUE} closed       ║
╚═══════════════════════════════════╝

End-of-Conv Complete
────────────────────
1. Learn/Decide  ✅
2. Conv Dump      ✅
3. Plan Update    ✅
4. Docs Update    ✅
5. State Saved    ✅ or ⏭️
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
