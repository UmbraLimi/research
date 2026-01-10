## Usage

**Forward method (preferred):**
1. Click Forward on the email thread in Gmail
2. Don't send — copy the content from the compose window
3. Paste here: `/r-email <paste>`

**Print view method:**
1. Open thread in Gmail → three dots → "Print all"
2. In print preview, Select All → Copy
3. Paste here: `/r-email <paste>`

Process complete threads only (when conversation has concluded).

---

# Process Email Thread

You are processing an email thread for **Fraser Gorrie**. Extract what matters and format for Obsidian.

## Input Formats

**Forward format:**
```
---------- Forwarded message ---------
From: Name <email@domain.com>
Date: Day, Mon DD, YYYY at H:MM AM/PM
Subject: Re: Subject line
To: Name <email@domain.com>
Cc: Name <email@domain.com>, Name <email@domain.com>

[Body text]

On Day, Mon DD, YYYY at H:MM AM/PM Name <email@domain.com> wrote:
[Quoted message]
```

**Print view format:**
```
Account Name    User <user@email.com>
Subject line
Sender Name <sender@email.com>    Day, Mon DD, YYYY at H:MM AM/PM
To: Recipient <recipient@email.com>
Cc: Person <email>, Person <email>

[Body text]

On Day, Mon DD, YYYY at H:MM AM/PM Name <email@domain.com> wrote:
[Quoted message]

X attachments
        filename.ext
SIZE
```

## Pre-Processing Checks

**1. Identify Gmail account:**

Check if Print view header shows account (e.g., `Bio-Software Mail`). If not detectable, ask:

```
Which Gmail account?

1. fraser@frasergorrie.com (Personal)
2. fraser@meristics.com (Meristics)
3. fgorrie@bio-software.com (Bio-Software)

(Enter number)
```

**2. Parse thread structure:**

Extract each message in the thread:
- Most recent message: structured headers at top
- Quoted messages: `On [date] at [time] [Name] <email> wrote:` pattern

**3. Check for multi-day threads:**

If messages span multiple calendar days, produce **separate outputs for each day**. Each day becomes its own Daily Notes entry with:
- Its own header and time
- Its own `Date::` field
- `prev`/`next` links connecting to adjacent days
- Thread Summary appears **only on the final day's entry**

## Reference Data

**Before formatting, read `.claude/commands/email-reference.md`** for lookup tables:
- **Gmail accounts** — account identification
- **Email → Person** — email addresses → wiki-links
- **Projects** — domain patterns → project name + emoji (optional)
- **Glossary** — terms → wiki-links (apply to Focus, Discussion, Thread Summary)

## Your Task

### Phase 1: Edge Case Scan

**Scan for these elements:**

| Element | What to look for | Action |
|---------|------------------|--------|
| **CC recipients** | `Cc:` line in headers | Include in `CC` field |
| **Attachments** | `X attachments` section at bottom | List in Attachments section |
| **URLs** | Links in body text | Note for Links section |
| **Mentioned people** | Names referenced but not in To/CC | Mark as `(mentioned)` |

### Phase 2: Content Extraction

For each message, extract:
- `date` — calendar date (YYYY-MM-DD)
- `time` — time sent (HH:MM, 24h format)
- `from` — sender name and email
- `to[]` — recipient(s) name and email
- `cc[]` — CC recipients (if any)
- `subject` — subject line
- `body` — message content
- `attachments[]` — filenames and sizes (if present)
- `urls[]` — links shared

Group messages by calendar date for multi-day output.

### Phase 3: Apply Reference Lookups

Using email-reference.md:
1. Look up email addresses → convert to wiki-links or "me" for Fraser
2. Look up domain patterns → get Project name and emoji (optional)
3. Replace glossary terms → wiki-links in Focus, Discussion, Thread Summary

### Phase 4: Format as Markdown

Build the Daily Notes structure for each day:

### Header (level 3)
`### 📫 Email • [Person/Subject] • HH:MM`

**Person slot logic:**
- If Fraser is recipient → use sender name
- If Fraser is sender → use primary recipient name
- Truncate subject to ~50 chars if used

### Metadata Block
```
- `prev  `:: [[Mon-DD-YYYY Day#from Person HH MM]]   ← omit if first in thread
- `next  `:: [[Mon-DD-YYYY Day#from Person HH MM]]   ← omit if last in thread
- `From  `:: [[Person]] or me
- `To    `:: [[Person]], [[Person]]
- `CC    `:: [[Person]], [[Person]]                  ← omit if none
- `Subj  `:: Subject line
- `Focus `:: Brief summary with [[glossary terms]] linked
- `Date  `:: YYYY-MM-DD
- `Time  `:: HH:MM
```

**Link format for prev/next:**
- Date: `Mon-DD-YYYY Day` (e.g., `Dec-14-2025 Sun`)
- Anchor: `#from Person HH MM` (spaces, no colons in time)

### Message Body Section (level 5)
`##### from: [Sender] : HH:MM`

For each message on that day:
```
##### from: Brian : 09:45
> Message body here
> Can be multiple lines
> Preserve paragraph structure
```

- Use `>` blockquotes for message content
- Multiple messages same day → multiple `##### from:` sections in chronological order

### Attachments Section (level 4) — optional
`#### Attachments`
- Only if attachments present
- Format: `- \`filename.ext\` — SIZE`

### Links Section (level 4) — optional
`#### Links`
- Only if URLs shared in thread
- Format: `- Description — \`https://...\`` (truncate long URLs)

### Thread Summary Section (level 4) — FINAL ENTRY ONLY
`#### Thread Summary`
- Appears only on the last day's entry
- Summarizes entire thread arc: what started it, key exchanges, decisions, outcome
- Written in first person for Fraser
- Apply wiki-links to people and glossary terms
- Detailed enough to understand thread without reading each day

### Tasks Section (level 4)
`#### Tasks`
Format by type:
- **My commitments**: `- [ ] task description 🔺 ⏳ YYYY-MM-DD` (date only if deadline mentioned)
- **Decisions needed**:
  - Fraser decides: `- [ ] Decide: task description (context) 🔺`
  - Another person decides: `- [ ] [[expect]] - [[Person]] to decide [description]`
  - Group decides: `- [ ] We need to decide: [description] 🔺`
- **Watching for**: `- [ ] [[expect]] - [[Person]] to do X by timeframe`

**Always include Tasks section**, even if empty (write "None").

**Be aggressive about inferring tasks:**
- If someone says they'll do something → `[[expect]]` task
- If a question was asked → decision needed
- If next steps were discussed but not confirmed → track them
- If attachments need review → task to review

### Separator
End each day's entry with `---`

## Output Format

**IMPORTANT:** Wrap the entire output in a fenced code block (` ```markdown ... ``` `) so the user can copy raw markdown that pastes correctly into Obsidian.

### Single-Day Example

~~~
```markdown
### 📫 Email • Brian • Re: Legal stuff • 07:05
- `From  `:: [[Brian LeBlanc]]
- `To    `:: me
- `Subj  `:: Re: Legal stuff
- `Focus `:: Brian confirms lawyer will handle agreement changes
- `Date  `:: 2025-12-16
- `Time  `:: 07:05
##### from: Brian : 07:05
> No worries I'll get the lawyer on it. Thanks
#### Thread Summary
[[Brian LeBlanc]] sent two legal documents (an Amendment and Agreement) for review. I identified structural issues: the documents incorrectly referenced [[Gabriel Rymberg|Gabriel]]'s Engagement letter and named me personally rather than my corporation. I requested three changes: (1) rework the Amendment to be a standalone Agreement, (2) reference [[Technifar Corporation]] / [[Meristics]] as "Developer", and (3) add corporate entity wording parallel to [[Alpha Peer]], LLC structure. Brian agreed and will have his lawyer revise the documents.
#### Tasks
- [ ] [[expect]] - [[Brian LeBlanc]] to deliver revised agreement from lawyer
---
```
~~~

### Multi-Day Example

~~~
```markdown
### 📫 Email • Brian • Legal stuff • 09:45
- `next  `:: [[Dec-15-2025 Mon#from Fraser 19 31]]
- `From  `:: [[Brian LeBlanc]]
- `To    `:: me
- `Subj  `:: Legal stuff
- `Focus `:: Brian sends legal agreements for review
- `Date  `:: 2025-12-14
- `Time  `:: 09:45
##### from: Brian : 09:45
> Fraser
>
> Look over these agreements and let me know what you think.
>
> Brian
#### Attachments
- `Agreement.pdf` — 150K
- `Amendment.docx` — 45K
#### Tasks
- [ ] Review legal agreements from [[Brian LeBlanc]] 🔺
---
```

```markdown
### 📫 Email • Brian • Re: Legal stuff • 19:31
- `prev  `:: [[Dec-14-2025 Sun#from Brian 09 45]]
- `next  `:: [[Dec-16-2025 Tue#from Brian 07 05]]
- `From  `:: me
- `To    `:: [[Brian LeBlanc]]
- `Subj  `:: Re: Legal stuff
- `Focus `:: I request restructuring of legal agreement around [[Meristics]]/[[Technifar Corporation]]
- `Date  `:: 2025-12-15
- `Time  `:: 19:31
##### from: Fraser : 19:31
> Hi Brian,
>
> I didn't see a way to salvage these two documents, so I would like our next steps for your lawyer:
> 1. Rework the Amendment document to be the Agreement, without reference to [[Gabriel Rymberg|Gabriel]]'s Engagement letter
> 2. Make reference to my corporation ([[Technifar Corporation]] which operates as [[Meristics]]) as the "Developer"
> 3. Add wording that states that the Developer is [[Meristics]]/[[Technifar Corporation]] and not Fraser Gorrie
>
> Then I will go over everything and ask questions, offer alternatives, etc.
>
> I am sorry that this is costly to you and I will try to keep changes minimal while being fair and helpful.
>
> Fraser
#### Tasks
- [ ] [[expect]] - [[Brian LeBlanc]]'s lawyer to rework Agreement document
---
```

```markdown
### 📫 Email • Brian • Re: Legal stuff • 07:05
- `prev  `:: [[Dec-15-2025 Mon#from Fraser 19 31]]
- `From  `:: [[Brian LeBlanc]]
- `To    `:: me
- `Subj  `:: Re: Legal stuff
- `Focus `:: Brian confirms lawyer will handle agreement changes
- `Date  `:: 2025-12-16
- `Time  `:: 07:05
##### from: Brian : 07:05
> No worries I'll get the lawyer on it. Thanks
#### Thread Summary
[[Brian LeBlanc]] sent two legal documents (an Amendment and Agreement) for review. I identified structural issues: the documents incorrectly referenced [[Gabriel Rymberg|Gabriel]]'s Engagement letter and named me personally rather than my corporation. I requested three changes: (1) rework the Amendment to be a standalone Agreement, (2) reference [[Technifar Corporation]] / [[Meristics]] as "Developer", and (3) add corporate entity wording parallel to [[Alpha Peer]], LLC structure. Brian agreed and will have his lawyer revise the documents.
#### Tasks
- [ ] [[expect]] - [[Brian LeBlanc]] to deliver revised agreement from lawyer
---
```
~~~

## Guidelines

**First-person narrative for Fraser:**
- When summarizing what Fraser said/did, use "I" not "[[Fraser Gorrie]]"
- When Fraser is sender, `From` shows "me"
- In Thread Summary, write from Fraser's perspective

**Message grouping:**
- Multiple messages on same calendar day → same entry, multiple `##### from:` sections
- Order chronologically within each day

**Thread Summary content:**
- What initiated the thread
- Key back-and-forth points
- Decisions made or pending
- Final outcome or current status
- Apply wiki-links throughout

**Task identification:**
- If someone commits to action → `[[expect]]` task
- If a question needs answering → `Decide:` task
- If attachments sent for review → review task
- Capture deadlines with `⏳ YYYY-MM-DD`

**Formatting:**
- Keep Focus to one line
- Thread Summary can be a full paragraph
- No blank lines between sections
- Apply wiki-links from reference tables

---

**Email thread to process:**

$ARGUMENTS
