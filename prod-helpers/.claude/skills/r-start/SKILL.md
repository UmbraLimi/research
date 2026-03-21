---
name: r-start
description: Start a new conversation — pull, increment conv counter, push, transfer pending tasks, then resume
argument-hint: ""
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Skill, TaskCreate
---

# Start Conversation

**Purpose:** Sync from remote, increment the conversation counter, push the new counter, transfer any pending tasks from RESUME-STATE.md into TodoWrite, lock the conv number for this session, then present resumption context. This is the **only** entry point for all conversations.

---

## Pre-computed Context

**Machine:**
!`cat ~/.claude/.machine-name 2>/dev/null || echo "(unknown)"`

**Current CONV-COUNTER value (before increment):**
!`.claude/scripts/conv-read-counter.sh`

**Existing .conv-current:**
!`test -f .conv-current && echo "WARNING: .conv-current already exists (value: $(cat .conv-current)) — a previous session may not have ended cleanly" || echo "(none — clean state)"`

---

## Execution Flow

### Step 1: Pull latest from remote

```bash
git pull --ff-only
```

If this fails (diverged branches, network error), **HALT** and tell the user. Do not proceed — the conv counter will be out of sync.

### Step 2: Read and increment the counter

Read `CONV-COUNTER`. It contains a single integer (e.g. `14`).

Compute the next value: current + 1.

Format as zero-padded 3-digit string (e.g. `015`).

### Step 3: Write the new counter and lock it

Write the new integer (unpadded) to `CONV-COUNTER`:

```bash
echo {NEW_VALUE} > CONV-COUNTER
```

Write the zero-padded value to `.conv-current`:

```bash
echo {PADDED_VALUE} > .conv-current
```

### Step 4: Commit and push the counter

```bash
git add CONV-COUNTER
git commit -m "Conv {PADDED_VALUE} start — {MACHINE}"
git push
```

If the push fails, **HALT** and tell the user. The counter increment is not synced until pushed.

### Step 5: Display conversation header

```
╔═══════════════════════════════════╗
║  Conv {PADDED_VALUE}  ·  {MACHINE}  ║
╚═══════════════════════════════════╝
```

### Step 6: Transfer pending tasks from RESUME-STATE.md

If `RESUME-STATE.md` exists:

1. Read the file and extract all unchecked items (`- [ ]`) from the `## Remaining` and `## TodoWrite Items` sections.
2. For each unchecked item, create a TodoWrite entry via `TaskCreate` with the item text as the description.
3. Delete `RESUME-STATE.md` after all items are transferred.
4. Display a summary:

```
📋 Transferred {N} pending tasks from RESUME-STATE.md → TodoWrite
```

If `RESUME-STATE.md` does not exist, skip this step silently.

### Step 7: Resume work context

Invoke `/r-resume` via the Skill tool to present the current work position and recommended next action.

---

## Rules

- **HALT on pull failure** — never increment without a successful pull
- **HALT on push failure** — the counter must be pushed before any work begins
- If `.conv-current` already exists, warn the user (prior session didn't run `/r-end`) but proceed — the counter in `CONV-COUNTER` (post-pull) is the source of truth
- The `CONV-COUNTER` file stores an unpadded integer; `.conv-current` stores a zero-padded 3-digit string
- Do NOT begin any project work until Steps 1–6 are complete
- Transfer tasks from RESUME-STATE.md **before** calling `/r-resume` — this ensures `/r-resume` sees a clean state
