# PLAN.md

## Current Status

**Phase 1 Complete** — Slack skill validated and working

**Next:** Phase 2.1 — Email skill

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
- [x] Specify exact markdown file format for thread output
  - Added JSON extraction schema to PURPOSE.md
  - Skill now uses two-step process: extract to schema → format as markdown
  - Output wrapped in code block for clean copy-paste to Obsidian
- [x] Integrate with Obsidian Daily Notes format
  - Created `slack-reference.md` for lookup tables (projects, channels, people, glossary)
  - Output matches Daily Notes structure: `### 💬 Slack •` header, metadata block, Discussion, Tasks
  - Task formatting: 🔺 for commitments/decisions, `[[expect]]` for watching
  - Wiki-links auto-applied from reference tables
  - Dataview inline fields (`Via::`, `Who::`, `Date::`, `Times::`, `Focus::`)
  - First-person narrative for Fraser ("I" not `[[Fraser Gorrie]]`)
  - Compact output (no blank lines between sections — CSS handles spacing)
  - DM header format: `### 💬 Slack • Name DM • time` (no project emoji)
  - Channel/date detection from screenshot input placeholder
  - Aggressive task inference (better to over-identify than miss)
  - Always include Tasks section (even if empty)

### 1.3 Validate in practice
- [x] Use skill on 3-5 real threads (4 done)
  - translation-system 2025-12-31
  - translation-system 2025-12-02/03 (multi-day)
  - translation-system 2025-12-17
  - translation-system 2025-12-18
- [x] Paste results into Obsidian, evaluate usefulness
  - Workflow works well
  - **Minor friction:** Single leading space on all lines except first `###` — workaround: highlight and Shift-Tab
- [x] Document what works and what needs adjustment
  - **Finding:** Multi-day threads need separate outputs per day (for pasting into respective Daily Notes)
  - **Fix:** Added pre-processing check #5 and multi-day example to skill
  - **Finding:** Attachments/Links should be both inline (context) AND dedicated sections (inventory)
  - **Fix:** Added `#### Attachments` and `#### Links` sections, kept inline references in Discussion

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
| Output format | Daily Notes integration | Matches existing manual format, uses Dataview fields |
| Reference data | Separate `slack-reference.md` file | User can edit mappings without touching skill logic |
| Task markers | 🔺 for priority, `[[expect]]` for watching | Consistent with user's Obsidian Tasks setup |
| Narrative voice | First-person for Fraser | More natural in personal Daily Notes |
| Task inference | Aggressive (over-identify) | Better to delete unwanted than miss important |
| Tasks section | Always include (even if empty) | Consistent format |
| Section spacing | No blank lines | CSS handles vertical spacing via headings |
| DM format | Person name, no project emoji | DMs don't belong to projects |
| Multi-day threads | Separate outputs per day | Each day pastes into its own Daily Note |
| Attachments/Links | Both inline + dedicated sections | Inline for context, sections for inventory |

## Open Decisions

| Decision | Options | Status |
|----------|---------|--------|
| Long thread handling | Truncate vs summarize in chunks | Pending |

---

## Notes

- Start simple, iterate based on real use
- Output format in PURPOSE.md is the target, may evolve

---

*Last Updated: 2026-01-02*
