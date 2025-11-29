# Alpha Peer - Prompt Library

**NOTE:** For most workflows, see **commands.md** which provides Claude Code-style slash commands.
This library contains the underlying prompts that power those commands.

## Research Prompts

### Research a Technology
```
Research [technology name] for use in a web application. Focus on:
- Core capabilities and use cases
- Integration complexity
- Pricing model
- Developer experience
- Community and support

Create tech-NNN-[technology-name].md in /research/
```

### Compare Technologies
```
Compare [technology A] vs [technology B] for [specific use case].
Focus on:
- Feature comparison
- Cost comparison
- Learning curve
- Community size
- Integration with our stack

Create comp-NNN-[comparison-topic].md in /research/
```

## User Story Prompts

### Create User Story
```
Create a user story for: [brief description]

Include:
- Story title and number
- User persona
- User goal
- Acceptance criteria
- Potential technologies needed
- Dependencies

Save as story-NNN-[short-title].md in /user-stories/
```

### Map Technology to Story
```
For story-NNN-[title], evaluate which technologies could fulfill:
- [specific requirement from story]

Update the story file with technology recommendations.
```

## Session Management Prompts

### Start Session
```
Create session file for today: session-YYYY-MM-DD-N.md
Include:
- Session goals
- Starting point from last session
```

### End Session
```
Complete current session file with:
- Work completed
- Decisions made
- Learnings captured
- Next steps

Update STRUCTURE.md with new file numbers if needed.
```

## Needs.md Update Prompts

### Add to Needs.md
```
Update Needs.md to include:
- [New user story/requirement]
- [Technology decision]
- [Architecture choice]

Maintain structure and consistency with existing content.
```

## Learning Capture Prompts

### Capture Learning
```
Create learning-NNN-[topic].md for:
- [What we learned]
- Key insights
- How it affects Alpha Peer
- References/sources

Update learnings-index.md with summary.
```

## Decision Documentation Prompts

### Document Decision
```
Create decision-NNN-[topic].md for:
- What we decided
- Options considered
- Rationale
- Trade-offs accepted
- Date and context
```

## Command System

See **commands.md** for the full command system that automates these prompts.

### Quick Command Reference
- `/start-session` - Begin work session
- `/end-session` - Close session with full documentation
- `/research-tech [name]` - Research a technology
- `/compare-tech [A] vs [B] for [use]` - Compare technologies
- `/create-story [description]` - Create user story
- `/capture-learning [topic]` - Document learning
- `/log-decision [topic]` - Document decision
- `/update-needs` - Update Needs.md
- `/status` - Show project status
- `/sync-structure` - Update file numbers in STRUCTURE.md

## Custom Prompts

Add your frequently used prompts here as patterns emerge.
