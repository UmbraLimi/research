# PURPOSE.md

*Initial project information dump. Fill in whatever you know now—it doesn't need to be complete or polished. Claude Code will use this to help create CLAUDE.md and PLAN.md.*

---

## Goals

*Why did I create this project? What am I trying to accomplish?*

The goals are:
- to collect all the skills and agents I might need to assist me in productivity tasks in one folder
- to launch agents if they can be functional and with adequate guard rails to turn themselves off when they encounter new situations not explicutly covered in their working directives
- help compile a 2nd Brain (in Obsidian) from various external sources either on demand (via Skills) or as strict conditions dictate (via Agents)
- to reduce the disparate software I use now into a defined set if destinations: 1) Dynalist for Tasks, 2) Obsidian for notes and each with very specific formats and tagging
- to implement a common tagging system between Dynalist and Obsidian (to be set up and maintined by the skills and agents) - yet to be decided
- to allow cross application searches (e.g. find me the credentials (Dynalist) for Cloudflare for the DTUB project and the URL to bring up all deployent targets (Obsidian))
- to move existing contet out of Joplin and into either Dynalist (tasks) or into Obsidian (everything else)
- to move all tasks in Obsidian into Dynalist
- to move marjed node trees inside Dynalist into Obsidian as notes

---

## Background Information

*What existing knowledge, documents, or resources can I bring into this folder?*
- I have data in 3 applicatoions: Joplin (to be retired), Dynalist and Obsidian. 
- I have some data in Dynalist that needs to move to Obsidian
- I have some data in Obsidian that needs to move to Dynalist
- ALl of the Joplin data needs to move, some of it to Dynalist, some of it to Obsidian
- I also have a sister folder to this folder "Comm-Helpers" which takes Slack, Email, and Telegram conversations/threads and summarizes them currently into Obsidian as paste-able text. They isolate the tasks from summaries.
- one of the principal differences between my use of Obsidian and Dynalist is as follows:
1. Dynalist for tasks. By far the fastest entry and searching with context visible
2. Project and Event Journaling and practically everything other than tasks
3. Obfuscated credentials for sites and projects and vendors in JSON or YAML files. You will execute a lookup inside the JSON to get a key and run a protected compiled progam to generate the true credentials
4. I collect a lot of URLs (80% are youtube shorts) where I want to get a transcrip and a thumbnail (because the YT shorts often disappear over time) and store in Obsidian. I have MacWhisper Pro for transcription if needed, and am open to using OpenAI's Whisper if it is a downloadable program.

---

## Personal Context

*Anything about me that might affect how this project evolves? (skills, experience, time availability, etc.)*

- I have been programming for 44 years, always for clients
- I have a lot of project + vendor + client credentials to keep track of securely, but most of the other information is unstructured and so must reside in notes to allow for the variations (Obsidian) yet be deeply cross-reference (links and backlinks)
- this is a life-project for me. I have been trying to create a Freelancer's Assistant for 35 of the 44 years

---

## Content & Sources

*Ideas, topics, materials, or elements you want to include. What raw ingredients do you have?*

- I think a common tag naming convention (between Dynalist, Obsidian and YAML/JSON) will be crucial, but probably impractical. In that case, a 1:1 tranlation table maintined outside of both Obsidian and Dynalist might be more practical

---

## Concerns & Risks

*What aspects worry you? What could go wrong? Known issues to watch out for?*

- a likely problem will be slowness of accessing data inside Joplin, Dynalist and Obsidian, though Joplin has an API via it's clipper browser extension, Dynalist has an API and Obsidian just released a CLI interface for v1.12 
- deciding what format each tye of note from Joplin, or Dynalist that is movomg to Obsidian
- creating the mapping table of tags in Dynalist and Joplin and Notes titles (which I have been using as tags in Obsidian)

---

## Constraints

*What boundaries must this project live within? (budget, dependencies, limitations, etc.)*

- no budgetary constraints
- we will be using CLaude Code for more of this, via the Max subscription ($100 or $200 per month level as need) 
- we might enlist Ollama and a local LLM for parts as appropriate
- we could also choose a lower cost model on Anthropic


---

## Preferences

*Any preferences for how things should be done? (style, approach, tone, tools, etc.)*

- I like to document each session with things learned, things, decided and capture what I have asked (word for word) and how are interaction proceeded. These are separate session docs with date and time in the filenames
- each agent, skill, python and bash script writtent will have a shadow document where we capture the state of that file, rationale for its existence, how it is used, etc

---

## Workflow & Process

*How do you like to work? (e.g., research first then write, outline before drafting, iterative revisions, etc.) Any phases or milestones you already envision?*

- I like tests
- I like to be able to test that a skill or agent will work under guarrail conditions and will fail overtly when unexpectd situations arise

---

## Technical Aspects

*If the topic involves technology, tools, or technical concepts—what are they?*



---

## Outputs & Platforms

*What will this project produce? Where will it be published or delivered?*



---

## Other Notes

*Anything else relevant that doesn't fit above?*


