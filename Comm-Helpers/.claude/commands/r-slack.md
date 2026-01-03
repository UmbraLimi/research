---
description: Process Slack thread and extract actions/decisions
argument-hint: <paste thread text OR drag screenshot first>
---

## Usage

**Text input:**
```
/r-slack <paste thread text here>
```

**Screenshot input:**
1. Drag/drop screenshot into chat
2. Then type `/r-slack`

Screenshots are preferred when reactions or completion confirmations matter.

---

# Process Slack Thread

You are processing a Slack thread for **Fraser Gorrie**. Extract what matters and format for Obsidian.

## Input

The user provides a Slack thread as either **text** (copy-paste) or **screenshot**.

**Text format** typically shows:
- Name and timestamp on one line
- Message content below
- Continuation messages from same user may show only timestamp
- Threaded replies may be indented or marked

**Screenshot format** shows:
- Avatar, name, and timestamp visually grouped
- Multi-line messages clearly belong to one block
- Reactions visible (👍, etc.)
- "Sent" or completion confirmations visible

**When to recommend screenshots:**
- If text is ambiguous about message grouping
- When reactions or confirmations matter for task status
- For threads where completion status is important

Screenshots capture completion signals (like "Sent." or reactions) that text selection often misses.

## Pre-Processing Checks

**First, identify the source channel and date:**

Check if the screenshot includes:
- **Channel:** Message input placeholder (e.g., "Message 🔒translation-system")
- **Date:** Date picker/header in the screenshot

**Relative dates:** If the date header shows "Today", "Yesterday", or similar relative terms, ask the user for the actual date before processing:
- "The screenshot shows '[Today/Yesterday]' — what is today's date?"

Convert to absolute date (YYYY-MM-DD) for the output.

If channel or date is missing, ask the user before processing:
- "What channel is this from?" (show numbered list below)
- "What date is this thread from?"

If channel is visible but not in the reference list, ask which Via to use.

```
Which channel is this thread from?

**CFU Workspace:**
1. ai-dev (🔵 UBT)
2. dj-dev (🔵 DJ)
3. dtub-dev (🔵 DTUB)
4. dev-works (🔵 CFU-W)
5. translation-system (🟢 XLATE)
6. CFU DM Gabriel
7. CFU DM Rick

**AIM Workspace:**
8. peer-loop-team (🟠 Peer Loop)
9. AIM DM Brian
10. AIM DM Gabriel

(Enter number or name)
```

Map their response to the Via link and Project from `slack-reference.md`.

**Then check for missing content:**

1. **Thread replies:** If you see "1 reply" or "X replies" under a message but no Thread panel is visible on the right side of the image, STOP and output:
   ```
   Thread replies detected but not expanded.

   Please click on the reply indicator to open the Thread panel, then recapture the screenshot.
   ```
   Thread replies often contain important responses, decisions, or confirmations.

2. **Voice recordings:** If an audio message is visible, the user should provide the full transcript text alongside the screenshot. Look for transcript text in the input.
   - If transcript is provided: incorporate it into the analysis
   - If only partial transcript visible (shows "View transcript" link) and no full text provided, ask:
     ```
     Audio detected without full transcript. Please paste the transcript text (click "View transcript" in Slack and copy).
     ```

3. **Attachments:** If images, files, or audio are present, list them in order at the start of output:
   ```
   **Attachments:**
   1. `filename.png` — [brief description of content]
   2. Audio (@person, 10:53 AM, 0:50) — [brief description or key quote]
   3. `another-file.png` — [brief description]
   ```
   For audio: use format `Audio (@person, [time], [duration])` since audio messages don't have filenames.

4. **Links:** If URLs are shared, list them after Attachments:
   ```
   **Links:**
   - [brief description]: `https://...` (truncate long URLs with [...])
   ```
   Capture meeting links, shared docs, resources. Truncate long URLs but keep them recognizable.

5. **Multi-day threads:** If the thread spans multiple days (date separators visible like "December 2nd, 2025" then "December 3rd, 2025"), produce **separate outputs for each day**. Each day becomes its own Daily Notes entry with:
   - Its own header and start time
   - Its own `Date::` (single date, not a range)
   - Its own Discussion and Tasks

   This allows pasting each block into its respective Daily Note. Even if the conversation is continuous, split by calendar day.

## Reference Data

**Before formatting, read `.claude/commands/slack-reference.md`** for lookup tables:
- **Projects** — channel → project name + emoji
- **Channels → Via** — channel → wiki-link for Via field
- **People** — name variations → wiki-links
- **Glossary** — terms → wiki-links (apply to Discussion and Focus)

## Your Task

**Step 1: Extract to JSON (internal)**

Mentally construct the extraction schema defined in PURPOSE.md:
- `attachments[]` — files, images, audio with metadata
- `links[]` — URLs shared in thread
- `summary` — brief impact summary (becomes Focus)
- `my_commitments[]` — tasks Fraser agreed/offered to do, with deadline if mentioned
- `decisions_needed[]` — actions required of Fraser, with context
- `watching_for[]` — commitments others made, with person and expected timeframe
- `key_points[]` — specific assertions/commitments (mark `from_audio: true` if from transcript)
- `participants[]` — who's in the thread (mark `mentioned_only: true` if referenced but not present)
- `source{}` — platform, channel, time range

**Step 2: Apply Reference Lookups**

Using slack-reference.md:
1. Look up channel → get Project name and emoji (omit if no match)
2. Look up channel → get Via wiki-link (default: `[[Slack • <channel>]]`)
3. Convert participant names → wiki-links where matched
4. Replace glossary terms → wiki-links in Discussion and Focus text

**Step 3: Format as Markdown**

Build the Daily Notes structure:

### Header (level 3)
`### 💬 Slack • [emoji] [Project] • [channel/DM] • [start time]`
- Omit project and emoji if no match in reference
- Use channel name or "DM Name" for DMs

### Metadata Block
```
- `Via   `:: [[Slack • ...]]
- `Who   `:: [[Person1]], [[Person2]], [[Person3]] (mentioned)
- `Date  `:: YYYY-MM-DD
- `Times `:: HH:MM - HH:MM
- `Focus `:: Brief summary with [[glossary terms]] linked
```
- Date: helps verify paste into correct Daily Note
- Who: comma-separated wiki-links; append `(mentioned)` for mentioned_only participants
- Focus: one line summary with glossary wiki-links applied

### Discussion Section (level 4)
`#### Discussion`
- Key points as bullets
- Append `(audio)` if from_audio is true
- Reference attachments/links inline where contextually relevant
- Apply glossary wiki-links to text
- 3-5 bullets max

### Attachments Section (level 4) — optional
`#### Attachments`
- Inventory of files, images, or audio shared in thread
- Format: `- \`filename.png\` — brief description`
- For audio: `- Audio (@person, HH:MM, duration) — brief description or key quote`
- Omit section entirely if no attachments

### Links Section (level 4) — optional
`#### Links`
- Inventory of URLs shared in thread
- Format: `- Description — \`https://...\`` (truncate long URLs with `[...]`)
- Omit section entirely if no links

### Tasks Section (level 4)
`#### Tasks`
Format by type:
- **My commitments**: `- [ ] task description 🔺 ⏳ YYYY-MM-DD` (date only if deadline mentioned)
- **Decisions needed** (attribute to correct decision-maker):
  - Fraser decides: `- [ ] Decide: task description (context) 🔺`
  - Another person decides: `- [ ] [[expect]] - [[Person]] to decide [description]`
  - Group decides: `- [ ] We need to decide: [description] 🔺`
  - Unclear who: `- [ ] Decide (Who?): [description] 🔺`
- **Watching for**: `- [ ] [[expect]] - [[Person]] to do X by timeframe`

**Always include the Tasks section**, even if empty (write "None" if no tasks).

**Be aggressive about inferring tasks** — better to identify implied tasks that can be deleted than miss ones the user didn't catch. Examples of implied tasks:
- If someone sends something to a third party for action, watch for that action to complete
- If a meeting was discussed but not scheduled, that's a decision/commitment needed
- If someone said "I'll look into it" without a deadline, still track it
- If someone says "Sent" or confirms they sent something to Fraser, create `[[expect]] - [[Person]] to deliver [object]` to track receipt
- If someone states future intent ("I will send...", "They will probably send...", "She is going to email us..."), create `[[expect]] - [[Person]] to deliver [object]` to track it

### Separator
End with `---`

## Output Format

**IMPORTANT:** Wrap the entire output in a fenced code block (` ```markdown ... ``` `) so the user can copy raw markdown that pastes correctly into Obsidian.

Output this structure:

~~~
```markdown
### 💬 Slack • 🟠 Peer Loop • #peerloop-general • 10:17
- `Via   `:: [[Slack • AIM • #peerloop-general]]
- `Who   `:: [[Brian LeBlanc]], [[Sarah Chen]], Carlos (mentioned)
- `Date  `:: 2025-12-31
- `Times `:: 10:17 - 10:45
- `Focus `:: [[Cloudflare]] setup for [[Peer Loop]] landing page
#### Discussion
- [[Brian LeBlanc]] available today to walk through setup
- Current landing page hosted on [[Cloudflare]] Pages
- Need dashboard access to configure DNS — shared `architecture.png` showing current setup (audio)
- [[Brian LeBlanc]] pointed to [[Cloudflare]] docs for SSL config
#### Attachments
- `architecture.png` — diagram of current hosting setup
- Audio (@Brian, 10:32, 1:15) — explains DNS requirements
#### Links
- Cloudflare SSL docs — `https://developers.cloudflare.com/ssl/[...]`
#### Tasks
- [ ] Get [[Cloudflare]] dashboard access from [[Brian LeBlanc]] 🔺 ⏳ 2025-12-20
- [ ] Decide: Use subdomain or main domain? (affects SSL config) 🔺
- [ ] [[expect]] - [[Brian LeBlanc]] to send login credentials by EOD
---
```
~~~

**Multi-day example** — each day is a separate code block:

~~~
```markdown
### 💬 Slack • 🟢 XLATE-Pilot • #translation-system • 10:30
- `Via   `:: [[Slack • CFU • translation-system]]
- `Who   `:: [[Gabriel Rymberg|Gabriel]], Carlos (mentioned)
- `Date  `:: 2025-12-02
- `Times `:: 10:30 - 14:27
- `Focus `:: Coordinating [[Cloudflare]] Pages setup for translation review
#### Discussion
- I asked [[Gabriel Rymberg|Gabriel]] to set up [[Cloudflare]] Pages for translation review
- [[Gabriel Rymberg|Gabriel]] shared "Get Started" screenshot, unsure how to proceed
- Time zone conflict — rescheduled setup session to next day
#### Attachments
- `image.png` — [[Cloudflare]] Pages "Get Started" screen
#### Tasks
- [ ] [[expect]] - [[Gabriel Rymberg|Gabriel]] to do [[Cloudflare]] Pages setup together (next day)
---
```

```markdown
### 💬 Slack • 🟢 XLATE-Pilot • #translation-system • 01:11
- `Via   `:: [[Slack • CFU • translation-system]]
- `Who   `:: [[Gabriel Rymberg|Gabriel]], Carlos (mentioned)
- `Date  `:: 2025-12-03
- `Times `:: 01:11 - 12:42
- `Focus `:: Carlos completed first translation review — positive feedback
#### Discussion
- [[Gabriel Rymberg|Gabriel]] praised review system and forwarded to Carlos
- Carlos completed review — shared JSON file with edits
#### Attachments
- `human-edits-carlos-COMPLETE` — JSON with Carlos's completed review
#### Links
- Zoom events — `https://events.zoom.us/ejl/[...]`
#### Tasks
None
---
```
~~~

**Note:** No blank lines between sections — CSS handles vertical spacing via headings.

## Guidelines

**First-person narrative for Fraser:**
- When summarizing what Fraser said/did, use "I" not "[[Fraser Gorrie]]"
- Example: "I requested Advanced Papers 3, 4, and 9 be sent to Carlos"
- When others reference Fraser, use judgment on how to summarize

**Task identification:**
- Distinguish "FYI" from "action required"
- If someone asks Fraser a question, that's a decision needed → `Decide:` task
- If Fraser said "I'll do X" or "I'll check on Y" → My commitment with 🔺
- If Fraser asked someone to do something and they agreed → `[[expect]]` task
- Capture deadlines explicitly with `⏳ YYYY-MM-DD` format

**Formatting:**
- Apply wiki-links from reference tables to all people and glossary terms
- Keep Focus to one line—detailed points go in Discussion
- Keep it scannable—this goes into Obsidian Daily Notes

---

**Thread content to process:**

$ARGUMENTS
