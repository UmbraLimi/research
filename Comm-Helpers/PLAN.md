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
- [x] Use skill on 3-5 real threads (~20 done across CFU and AIM workspaces)
  - CFU #translation-system: Dec 2-3, 17, 18, 19-22, 23, 29-31
  - CFU DM Rick: Dec 21-23
  - CFU DM Gabriel: Dec 23, Jan 2
  - AIM #peer-loop-team: Dec 1-2, 6, 7, 8, 9-10, 12, 14-15, 16, 17, 21-23, 24, 26-Jan 1
- [x] Paste results into Obsidian, evaluate usefulness
  - Workflow works well
  - **Minor friction:** Single leading space on all lines except first `###` — workaround: highlight and Shift-Tab
- [x] Document what works and what needs adjustment
  - See `docs/sessions/` for detailed findings per session
  - See `DECISIONS.md` for current operating decisions

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

## Decisions

See `DECISIONS.md` for authoritative record of all project decisions.

---

## Notes

- Start simple, iterate based on real use
- Output format in PURPOSE.md is the target, may evolve
- Detailed findings: `docs/sessions/` (per session)
- Current decisions: `DECISIONS.md` (authoritative)

---

*Last Updated: 2026-01-03*
