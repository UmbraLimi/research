# PURPOSE.md

*Project information for creating communication thread processing skills.*

---

## Goals

Create a set of Claude Code skills that process communication threads and extract:
1. **Impact summaries** — what matters, what's significant
2. **Decision tasks** — decisions I need to make, actions required of me
3. **Expected accomplishments** — tasks others committed to that I should watch for

Output is markdown text (not files) that I copy-paste into Obsidian notes.

---

## Background Information

- Existing Obsidian vault where I manage notes and tasks
- Familiarity with Claude Code skills (how to create and invoke them)
- Communication spread across multiple platforms that needs consolidation

---

## Personal Context

- I receive communications across Slack, Telegram, and email
- Time-constrained; need quick extraction, not lengthy reading
- Want consistent output format across all source types
- Obsidian is my central knowledge/task management system

---

## Input Sources

| Platform | Format | Notes |
|----------|--------|-------|
| **Slack** | Channel threads, DMs | May include threaded replies, reactions, links |
| **Telegram** | Channel messages, group chats | May include forwarded messages, media |
| **Email** | Thread conversations | Multiple participants, quoted replies, attachments mentioned |

**Common challenges:**
- Threading/nesting varies by platform
- Distinguishing signal from noise
- Identifying who committed to what

---

## Output Format

Markdown text block ready to paste into Obsidian. Target structure:

```markdown
## Summary
[2-3 sentence impact summary: what this thread is about and why it matters]

## Decisions Needed
- [ ] [Decision or action required of me]
- [ ] [Another decision...]

## Watching For
- [ ] [Task someone else committed to] — @person, expected by [date if mentioned]
- [ ] [Another expected deliverable...]

## Key Points
- [Important detail 1]
- [Important detail 2]

---
Source: [platform] | Date: [date range] | Participants: [names]
```

---

## Requirements

**Functional:**
- Accept pasted communication thread as input
- Identify decisions/actions assigned to me specifically
- Identify commitments made by others
- Summarize for impact, not just content
- Output clean markdown I can paste directly

**Quality:**
- Distinguish "FYI" from "action required"
- Capture deadlines and dates when mentioned
- Handle multi-person threads (who said what matters)
- Work even with messy/informal communication

---

## Use Cases

1. **Weekly Slack catch-up** — Process a busy channel I haven't read in days, extract what needs my attention
2. **Email thread decision** — Long back-and-forth, need to know current state and my next action
3. **Telegram group project** — Informal chat where tasks got assigned, need to capture commitments
4. **Meeting follow-up** — Someone shared notes in a thread, extract my action items

---

## Technical Aspects

- Skills will be `.md` files in `.claude/commands/`
- May need different skills per platform (formatting differs) or one universal skill
- Input: user pastes thread content into prompt
- Output: markdown block in Claude's response (user copies manually)

**Open questions:**
- One skill per platform, or one universal `/summarize-thread` skill?
- How to handle very long threads (context limits)?
- Should skills ask clarifying questions or just process?

---

## Workflow & Process

1. Start with one platform (Slack?) as proof of concept
2. Refine output format based on actual use
3. Extend to other platforms
4. Iterate based on what's working in Obsidian

---

## Concerns & Risks

- Output format might need iteration to be useful in practice
- Platform-specific quirks may require separate handling
- Very long threads might exceed practical limits
- "My action" vs "someone else's action" detection may be tricky without knowing who "I" am

---

## Constraints

- No API integrations — input is pasted text, output is copied text
- Must work within Claude Code skill framework
- Output must be valid markdown for Obsidian

---

## Other Notes

**Future possibilities:**
- Skills for other communication types (Discord, meeting transcripts)
- Integration with Obsidian tasks plugin format
- Batch processing multiple threads

**Success criteria:**
- Using this daily saves time vs. reading everything
- Obsidian notes become reliable source of "what I owe" and "what I'm owed"
