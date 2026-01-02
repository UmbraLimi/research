# PLAN.md

## Current Status

**Phase 1.2** — Testing Slack skill

---

## Phase 1: Proof of Concept (Slack)

### 1.1 Design first skill
- [x] Decide: one universal skill vs platform-specific skills
- [x] Draft skill structure and prompting approach
- [x] Define how user identifies themselves (for "my action" detection)

### 1.2 Build Slack skill
- [x] Create `/r-slack` skill in `.claude/commands/`
- [x] Test with real Slack thread (text + screenshot comparison)
- [x] Add screenshot guidance to skill
- [x] Add pre-processing checks (threads, audio, attachments, links)
- [x] Add My Commitments section
- [x] Add Participants section
- [x] Add (audio) annotation for transcript-derived key points
- [ ] Specify exact markdown file format for thread output

### 1.3 Validate in practice
- [ ] Use skill on 3-5 real threads
- [ ] Paste results into Obsidian, evaluate usefulness
- [ ] Document what works and what needs adjustment

---

## Phase 2: Extend to Other Platforms

### 2.1 Email skill
- [ ] Adapt for email thread format (quoted replies, multiple participants)
- [ ] Test and refine

### 2.2 Telegram skill
- [ ] Adapt for Telegram format (forwarded messages, informal style)
- [ ] Test and refine

---

## Phase 3: Polish and Iterate

### 3.1 Refinements based on usage
- [ ] Adjust output format for Obsidian workflow
- [ ] Handle edge cases (long threads, unclear attribution)
- [ ] Document any platform-specific quirks

---

## Decisions Made

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Skill architecture | Per-platform | Tailored prompts for each format |
| User identification | Hardcoded "Fraser Gorrie" | Zero friction, update if needed |

## Open Decisions

| Decision | Options | Status |
|----------|---------|--------|
| Long thread handling | Truncate vs summarize in chunks | Pending |

---

## Notes

- Start simple, iterate based on real use
- Output format in PURPOSE.md is the target, may evolve
