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

**Before processing, check for missing content:**

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

## Your Task

Analyze the thread and produce a markdown block with these sections:

### 1. Summary (2-3 sentences)
What is this thread about? Why does it matter? Focus on impact, not just content.

### 2. My Commitments
Tasks **Fraser Gorrie agreed to do or offered to do**.
- Things Fraser said he would do ("I'll report back", "I'll check on this")
- Use `- [ ]` checkbox format
- If none, write "None identified"

### 3. Decisions Needed
Actions or decisions required **of Fraser Gorrie specifically**.
- Only include items where Fraser needs to decide or act
- Use `- [ ]` checkbox format
- Be specific about what's needed
- If none, write "None identified"

### 4. Watching For
Commitments or tasks **others** said they would do.
- Include the person's name with @
- Include expected date/timeframe if mentioned
- Use `- [ ]` checkbox format
- If none, write "None identified"

### 5. Key Points
Capture **specific assertions and commitments** people made—not just what happened.
- Quote or paraphrase key statements that matter (e.g., **"Don't worry about the budget"**)
- Highlight commitments, constraints cleared, requirements stated
- Note status confirmations with evidence (e.g., "Sent to Carlos, 👍 by Fraser")
- If a key point derives from audio transcript, add **(audio)** at the end
- 3-5 bullet points max
- Skip generic summaries—capture what was actually said/claimed

### 6. Participants
List unique participants in the thread.
- Format: `@Name` for each person
- Include people mentioned but not present (e.g., "@Carlos (mentioned)")
- Order: active participants first, then mentioned

### 7. Source metadata
Single line: `Source: Slack (#channel-name) | Date: [date range from thread]`

## Output Format

```markdown
**Attachments:** (if any)
1. `filename.png` — [description]
2. Audio (@person, 10:53 AM, 0:50) — [description or key quote]

**Links:** (if any)
- Zoom meeting: `https://events.zoom.us/[...]`
- Shared doc: `https://docs.google.com/[...]`

## Summary
[Your 2-3 sentence summary]

## My Commitments
- [ ] [Task Fraser agreed/offered to do]

## Decisions Needed
- [ ] [Specific decision or action for Fraser]

## Watching For
- [ ] [What someone committed to] — @person, expected [timeframe]

## Key Points
- [Key detail 1]
- [Key detail 2] (audio)

## Participants
@Name1, @Name2, @Name3 (mentioned)

---
Source: Slack (#channel-name) | Date: [dates]
```

## Guidelines

- Distinguish "FYI" from "action required"
- If someone asks Fraser a question, that's a decision/action needed
- If Fraser said "I'll do X" or "I'll check on Y", that's "My Commitments"
- If Fraser asked someone to do something and they agreed, that's "Watching For"
- Capture deadlines explicitly when mentioned
- Keep it scannable—this goes into Obsidian for quick reference

---

**Thread content to process:**

$ARGUMENTS
