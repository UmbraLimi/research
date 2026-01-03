# DECISIONS.md

Authoritative record of current project decisions. Session-level decision files provide historical context; this file reflects the latest resolved state.

*Last Updated: 2026-01-03 10:35*

---

## Operating Decisions (OP)

Decisions about how we do things frequently — embedded in skill behavior.

---

### OP-01: Input Method
**Choice:** Both text and screenshot; prefer screenshots

Screenshots capture reactions, "Sent" confirmations, and completion signals that text selection often misses. Recommend screenshots when these signals matter.

---

### OP-02: Audio Handling
**Choice:** User provides transcript with screenshot

Slack's "View transcript" opens in a modal that can't be captured in the main screenshot. User pastes transcript text alongside the screenshot.

---

### OP-03: Multi-day Threads
**Choice:** Separate outputs per calendar day

Each calendar day becomes its own markdown block for pasting into the respective Daily Note. Even if conversation is continuous, split by date separator visible in Slack.

---

### OP-04: Attachments and Links
**Choice:** Both inline references AND dedicated sections

Inline references in Discussion tell the story ("shared `architecture.png` showing current setup"). Dedicated `#### Attachments` and `#### Links` sections provide a clean inventory. Both serve different purposes.

---

### OP-05: Relative Dates
**Choice:** Ask user for actual date

When screenshot shows "Today" or "Yesterday" instead of a date, ask user to provide the actual date before processing. Convert to YYYY-MM-DD for output.

---

### OP-06: Delivery Confirmations
**Choice:** Create expect tasks

When someone says "Sent" or states future intent ("I will send...", "She is going to email..."), create `[[expect]] - [[Person]] to deliver [object]` task. Better to track implied deliverables than miss them.

---

### OP-07: Long Threads
**Choice:** Process one calendar day at a time

Very long threads cause accuracy issues when processed all at once. For threads with extensive discussion, process one day at a time to maintain accuracy and produce cleaner output.

---

### OP-08: Channel Confirmation
**Choice:** Always ask

Even when conversation context suggests the channel, always ask user to confirm. The pre-processing check exists for a reason — assumptions lead to incorrect Via links.

---

### OP-09: Task Inference
**Choice:** Aggressive (over-identify)

Better to identify implied tasks that can be deleted than miss ones the user didn't catch. Examples: implied follow-ups, unscheduled meetings, vague commitments.

---

### OP-10: Tasks Section
**Choice:** Always include, even if empty

Write "None" if no tasks identified. Consistent format makes scanning easier.

---

### OP-11: Section Spacing
**Choice:** No blank lines between sections

User's Obsidian CSS handles vertical spacing via headings. Blank lines add unnecessary height.

---

### OP-12: DM Format
**Choice:** Person name in header, no project emoji

DMs don't belong to projects. Header format: `### 💬 Slack • Gabriel DM • 10:17`

---

### OP-13: Narrative Voice
**Choice:** First-person for Fraser

When summarizing what Fraser said/did, use "I" not "[[Fraser Gorrie]]". More natural reading in personal Daily Notes.

---

### OP-14: Decision Task Attribution
**Choice:** Attribute to correct decision-maker

Not all decisions are Fraser's to make. Format based on who decides:
- **Fraser decides:** `- [ ] Decide: [description] 🔺`
- **Another person decides:** `- [ ] [[expect]] - [[Person]] to decide [description]`
- **Group decides collectively:** `- [ ] We need to decide: [description] 🔺`
- **Unclear who decides:** `- [ ] Decide (Who?): [description] 🔺`

Ascertain from context who has authority/responsibility for the decision.

---

### OP-15: Edge Case Scan (Phase 1)
**Choice:** Explicit scan before content extraction

Process screenshots in phases: Phase 1 scans entire image for reply indicators, audio transcripts, attachments, URLs, and huddles BEFORE reading content. This ensures edge cases aren't missed during content extraction.

---

### OP-16: Missing Content Handling
**Choice:** Ask for text, not recapture

When reply indicators ("X replies") or audio transcripts ("View transcript") are found without expanded content, pause and ask user to paste the text rather than asking them to recapture the screenshot. More efficient workflow. Include "skip" option for inconsequential items.

---

## General Decisions (GN)

Architectural and strategic decisions — less frequently revisited.

---

### GN-01: Skill Architecture
**Choice:** Per-platform skills

Separate `/r-slack`, `/r-email`, `/r-telegram` rather than one universal skill. Tailored prompts for each format's quirks; explicit user choice; easier to maintain platform-specific logic.

---

### GN-02: User Identification
**Choice:** Hardcoded "Fraser Gorrie"

Name embedded directly in skill files. Zero friction during use; easy to update if needed; avoids repetitive prompting.

---

### GN-03: Output Format
**Choice:** Daily Notes integration

Output matches user's existing Obsidian Daily Notes structure: `### 💬 Slack •` header, Dataview metadata block (`Via::`, `Who::`, `Date::`, `Times::`, `Focus::`), `#### Discussion`, `#### Tasks`. Seamless integration with existing workflow.

---

### GN-04: Reference Data
**Choice:** Separate `slack-reference.md` file

Channel/people/glossary lookup tables live in `.claude/commands/slack-reference.md`. User can edit mappings without touching skill logic. Cleaner separation of concerns.

---

### GN-05: Task Markers
**Choice:** 🔺 for priority, `[[expect]]` for watching

- My commitments: `- [ ] task 🔺 ⏳ YYYY-MM-DD`
- Decisions needed: `- [ ] Decide: task 🔺`
- Watching for: `- [ ] [[expect]] - [[Person]] to do X`

Consistent with user's Obsidian Tasks setup.

---

### GN-06: Extraction Approach
**Choice:** JSON schema (internal), markdown output

Skill mentally constructs structured extraction per schema in PURPOSE.md, then formats as markdown. JSON is not output to user. Structured extraction ensures consistency.

---

### GN-07: Participants Display
**Choice:** Who field in metadata with wiki-links

Comma-separated wiki-links in `Who::` field. Append "(mentioned)" for people referenced but not present in thread.

---

## Open Decisions

Decisions pending resolution.

*(none currently)*

---

## Decision History

For full context on when and why decisions were made, see session files:
- `docs/sessions/YYYY-MM/YYYY-MM-DD_HH-MM-SS Decisions.md`
