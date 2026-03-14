---
name: r-save-state
description: Save current work state for cross-session continuity
argument-hint: ""
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Save Session State

**Purpose:** Capture everything needed to resume the current session's work after `/compact` or in a new session.

---

## Pre-computed Context

**Existing state file:**
!`if [ -f RESUME-STATE.md ]; then echo "EXISTS — saved on:"; head -5 RESUME-STATE.md | grep 'Saved:'; else echo "No existing RESUME-STATE.md"; fi`

---

## Step 1: Check for Existing State

If `RESUME-STATE.md` already exists:

```
Existing state file found (saved [date])
─────────────────────────────────────────
[First 3 lines of ## Summary section]

Options:
1. Overwrite with current state
2. View full file first
3. Abort (keep existing)
```

Wait for user choice before proceeding.

---

## Step 2: Scan the Session

Review the full conversation to identify:

- **What we were working on** — the high-level task or goal
- **What's done** — completed items (brief, bulleted)
- **What's remaining** — incomplete items with enough detail to resume
- **Key context** — decisions made, gotchas discovered, important file paths — anything a fresh session would need to avoid re-discovering
- **Open questions** — anything unresolved that needs user input

**Be thorough.** The goal is that a new session with zero prior context can read this file and continue seamlessly. Include file paths and specific details.

---

## Step 3: Write RESUME-STATE.md

Create in the project root:

```markdown
# Resume State

**Saved:** YYYY-MM-DD ~HH:MM

## Summary

[2-3 sentence description of what this session was doing and where it stopped]

## Completed

- [Bulleted list of what's done — keep brief]

## Remaining

### [Group 1 name]
- [ ] Item with enough detail to act on
- [ ] Another item — include file paths

### [Group 2 name]
- [ ] More items...

## Key Context

[Paragraph or bullets with critical knowledge needed to resume:]
- Decisions made and why
- Gotchas discovered
- Files being modified
- Any workarounds in place

## Resume Command

To continue: read this file, then work through the **Remaining** items in order.
```

---

## Step 4: Confirm

```
State saved → RESUME-STATE.md

Summary: [1-line summary]
Remaining items: [count]
```

---

## Writing Guidelines

- **Be specific** — file paths, function names, concrete details
- **Include "why" not just "what"** — context behind decisions saves re-discovery time
- **Group remaining items** logically (by priority, by topic, by phase)
- **Use checkboxes** (`- [ ]`) for remaining items so progress is trackable
- **Keep Completed section brief** — it's for orientation, not documentation
- **Key Context is the most important section** — this is what prevents a new session from hitting the same walls
