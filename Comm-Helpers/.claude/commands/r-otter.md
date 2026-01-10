---
description: Process Otter.ai meeting transcript and extract actions/decisions
argument-hint: '<path to .txt file>'
---

## Usage

```
/r-otter /path/to/meeting_otter_ai.txt
```

The user provides a path to an Otter.ai transcript file (`.txt`).

---

# Process Otter.ai Meeting Transcript

You are processing a meeting transcript for **Fraser Gorrie**. Extract what matters and format for Obsidian.

## Input Format

Otter.ai transcripts follow this pattern:

```
Name  TIMESTAMP
Message content spans multiple lines
until the next speaker block.

Another Name  TIMESTAMP
Their message content here.
...
Transcribed by https://otter.ai
```

- Speaker name and timestamp on one line (timestamp like `0:00`, `1:43`, `10:15`, `1:02:30`)
- Message content follows on subsequent lines
- Blank line typically separates speaker blocks
- File ends with "Transcribed by https://otter.ai"

## Pre-Processing Checks

**Extract meeting metadata:**

1. **Date:** Parse from filename if present (e.g., `2025 01 06 - PeerLoop weekly_otter_ai.txt` → 2025-01-06)

   - If date unclear, ask user: "What date was this meeting?"

2. **Meeting name:** Parse from filename (e.g., "PeerLoop weekly")

   - If unclear, ask user: "What was this meeting called?"

3. **Duration:** Note final timestamp as approximate duration

## Reference Data

**Before formatting, read `.claude/commands/slack-reference.md`** for lookup tables:

- **People** — name variations → wiki-links
- **Glossary** — terms → wiki-links (apply to Discussion and Focus)
- **Projects** — if meeting relates to a known project, use its emoji

## Your Task

### Phase 1: Initial Scan

Read the entire transcript and identify:

- All participants (speakers in the transcript)
- Anyone mentioned but not present
- Meeting duration (final timestamp)
- Major topic shifts (for structuring Discussion)

### Phase 2: Content Extraction

Extract to internal structure:

- `summary` — brief meeting purpose/outcome (becomes Focus)
- `my_commitments[]` — tasks Fraser agreed/offered to do, with deadline if mentioned
- `decisions_made[]` — decisions reached during the meeting
- `decisions_needed[]` — unresolved decisions requiring follow-up
- `watching_for[]` — commitments others made, with person and expected timeframe
- `key_topics[]` — main discussion points (3-5 max)
- `participants[]` — who spoke (mark `mentioned_only: true` if referenced but not present)
- `source{}` — platform (Otter.ai), meeting name, date, duration
- `filename` — file submitted

### Phase 3: Apply Reference Lookups

Using slack-reference.md:

1. Convert participant names → wiki-links where matched
2. Replace glossary terms → wiki-links in Discussion and Focus text
3. If meeting relates to a project (e.g., "PeerLoop"), use that project's emoji

### Phase 4: Format as Markdown

Build the Daily Notes structure:

### Header (level 3)

`#### 🎙️ Transcript • [meeting name] • [duration]`

- Duration format: `1h 8m` or `45m`

### Metadata Block

```
- `Via   `:: [[Otter.ai]]
- `File  `:: `filename`
- `Who   `:: [[Person1]], [[Person2]], [[Person3]], Name (mentioned)
- `Date  `:: YYYY-MM-DD
- `Duration`:: Xh Ym
- `Focus `:: Brief summary with [[glossary terms]] linked
```

### Discussion Section (level 4)

`##### Discussion`

- Key discussion points as bullets
- Apply glossary wiki-links to text
- Group related points; don't just list chronologically
- Include notable quotes if particularly important
- 3-5 bullets max, covering major themes

### Decisions Section (level 4) — optional

`##### Decisions`

- Decisions made during the meeting
- Format: `- Decision description (context if needed)`
- Omit section if no decisions were made

### Tasks Section (level 4)

`##### Tasks`
Format by type:

- **My commitments**: `- [ ] task description 🔺 ⏳ YYYY-MM-DD` (date only if deadline mentioned)
- **Decisions needed**:
  - Fraser decides: `- [ ] Decide: task description (context) 🔺`
  - Another person decides: `- [ ] [[expect]] - [[Person]] to decide [description]`
  - Group decides: `- [ ] We need to decide: [description] 🔺`
- **Watching for**: `- [ ] [[expect]] - [[Person]] to do X by timeframe`

**Always include the Tasks section**, even if empty (write "None" if no tasks).

**Be aggressive about inferring tasks** — meeting discussions often contain implied commitments:

- "I'll look into that" → My commitment
- "Let me check with [person]" → My commitment to follow up
- "We should do X" without assignment → Decision needed on who owns it
- "[Person] is going to..." → Watch for them to complete it
- "Next meeting we'll review..." → Implied preparation task
- Scheduled follow-up meetings → Track they happen

### Separator

End with `---`

## Output Format

**IMPORTANT:** Wrap the entire output in a fenced code block (` ```markdown ... ``` `) so the user can copy raw markdown that pastes correctly into Obsidian.

**Example output:**

````
```markdown
#### 🎙️ Transcript • Weekly Sync • 1h 8m
- `File  `:: `2026 01 06 - PeerLoop weekly_otter_ai.txt`
- `Via   `:: [[Otter.ai]]
- `Who   `:: [[Brian LeBlanc]], [[Gabriel Rymberg|Gabriel]], [[Guy Rymberg]], [[Jesse Showalter|Jesse]] (mentioned)
- `Date  `:: 2025-01-06
- `Duration`:: 1h 8m
- `Focus `:: [[Peer Loop]] progress review, video platform direction, student-teacher certification discussion
##### Discussion
- 24/57 pages implemented; [[Stripe]] and R2 integrations complete; feeds integration next
- Video platform: [[Brian LeBlanc]] researching Jitsi vs LiveKit; leaning Jitsi for community size but LiveKit for flexibility
- Student-teacher model: debated mandatory vs incentivized teaching; agreed to start simple with creator certification
- Revenue split confirmed: 15% platform, 15% creator, 70% student-teacher (no multi-level)
- [[Jesse Showalter|Jesse]] working on UI/UX designs in Figma; time zone challenges for group review
##### Decisions
- Use getstream.io for feeds (no viable alternatives)
- Start with simple certification process via video call; iterate based on feedback
- Weekly Monday syncs continue; marketing review meeting tomorrow with [[Gabriel Rymberg|Gabriel]] and [[Guy Rymberg]]
##### Tasks
- [ ] Integrate getstream.io feeds 🔺
- [ ] [[expect]] - [[Brian LeBlanc]] to review marketing documents (value prop, differentiation, target audience)
- [ ] [[expect]] - [[Brian LeBlanc]] to schedule [[Jesse Showalter|Jesse]] design review with full team
- [ ] [[expect]] - [[Gabriel Rymberg|Gabriel]] to send meeting transcript
- [ ] [[expect]] - [[Guy Rymberg]] to share Claude Code 101/102 course materials when ready
---
```
````

## Guidelines

**First-person narrative for Fraser:**

- When summarizing what Fraser said/did, use "I" not "[[Fraser Gorrie]]"
- Example: "I raised concerns about certification scalability"

**Meeting-specific guidance:**

- Meetings are discussions, not message threads — summarize themes, don't list every exchange
- Identify the 3-5 most important topics; skip small talk and tangents
- Capture the outcome/direction, not just that something was discussed
- Note any follow-up meetings scheduled

**Task identification:**

- Verbal commitments ("I'll do X", "Let me check") count as commitments
- "We should..." without clear owner → Decision needed
- "[Person] will..." → Watch for completion
- Scheduled meetings → Track they happen

**Formatting:**

- Apply wiki-links from reference tables to all people and glossary terms
- Keep Focus to one line — detailed points go in Discussion
- Keep it scannable — this goes into Obsidian Daily Notes

---

**Read the transcript file and process:**

$ARGUMENTS
