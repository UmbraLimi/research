# ENTITIES

A guide to the entity types managed in the vault — what they are, how they're structured, what's nested inside them, and what you can ask CC to do with each one.

**Entities vs. cards:** Entities are long-lived reference notes (vendor, person, project, software) created manually at low volume. Cards are timestamped log entries (coding, meeting, slack, etc.) created at high volume by CC skills. This document covers entities only. Card schemas live in `reference/schemas/`.

**Sub-resources are headings, not separate notes.** Accounts, services, channels, databases — anything that belongs to an entity — lives as a heading inside the entity note. Link with `[[EntityName#heading]]`. This keeps the vault flat and avoids stub-note clutter.

**Schemas:** Each entity type has a schema in `~/Vaults/main/reference/schemas/`. CC reads the schema when creating or updating an entity note. `/cco-migrate-schema` backfills schema changes to existing notes.

---

## Vendors

**Schema:** `reference/schemas/vendor.md`
**Location:** `~/Vaults/main/reference/vendors/{VendorName}.md`
**Status:** Schema v1 complete. 8 vendor notes exist.

A vendor is any external platform, service, or provider you use — Cloudflare, GitHub, Slack, Resend, etc.

### What lives inside a vendor note

| Concept | Representation | Example |
|---------|---------------|---------|
| Account | `##` heading | `## Meristics`, `## CFU` |
| Service category | `###` heading | `### CFU • Pages` |
| Specific resource | `####` heading | `#### CFU • D1 • essays` |
| Credentials | Inline with `===` markers | `===token-value===` |
| Product/service list | `## Offerings` section | Cloudflare's account > service > instance hierarchy |

Accounts, services, and resources are **not** separate entity types — they are headings within the vendor note, linked via `[[Vendor#heading]]`.

### What you can ask CC to do

- **"Create a vendor note for Stripe"** — CC reads the schema, picks simple or multi-account template, creates the note.
- **"Add Pages and Workers to the Cloudflare note"** — CC reads the existing note, adds `###`/`####` sections following its established heading pattern.
- **"I signed up for a second AWS account for PeerLoop"** — CC adds a new `##` account section with a `---` separator.
- **"Add Resend as an email provider"** — CC creates the note with `type: [vendor, email-provider]`.

CC will always check for an existing vendor note before creating a new one.

---

## Projects

**Schema:** `reference/schemas/project.md`
**Location:** `~/Vaults/main/projects/{project}/` (lowercase folder)
**Status:** Schema v1 complete. 7 project folders exist.

A project is a body of work with its own vault folder and lifecycle. Unlike other entities, projects use **containment** — a folder with multiple files — because they accumulate session logs, decisions, learnings, tasks, and plans. Not all projects have code repos — hobby, in-house, and planning-only projects have vault folders only.

### What lives inside a project folder

| File/folder | Purpose |
|-------------|---------|
| `{Project}.md` | Project log (schema-governed frontmatter) |
| `{Project}-tasks.md` | Task backlog extracted from daily notes |
| `plan.md` | Project plan and task tracking |
| `decisions.md` | Net decisions for this project |
| `learnings.md` | Accumulated learnings |
| `sessions/` | Session notes (one per project per day) |

### Classification & status

Use the `type` list: `[project, client-work]`, `[project, hobby]`, `[project, in-house]`, `[project, research]`.

The `status` field tracks lifecycle: `active`, `paused`, `completed`, `abandoned`.

The `repo` field links to a code repo (empty for non-coding projects, populated by `/cco-project-link-repo`).

### Two skills for projects

| Skill | Purpose | When to use |
|-------|---------|-------------|
| `/cco-project-init` | Creates vault folder structure | Any new project |
| `/cco-project-link-repo` | Links vault project to a code repo | Coding projects with repos |

Run `/cco-project-init` first, then `/cco-project-link-repo` from the repo directory if the project has a code repo.

### What you can ask CC to do

- **"Set up a vault folder for MyNewProject"** — use `/cco-project-init`.
- **"Link PeerLoop to its repo"** — run `/cco-project-link-repo PeerLoop` from the repo directory.
- **"Pause the StickerHardlyKnowHer project"** — CC updates `status: paused` in the project note.
- **"Archive PeerLoop"** — CC updates `status: completed`.

---

## People

**Schema:** `reference/schemas/person.md`
**Location:** `~/Vaults/main/reference/people/{FirstLast}.md`
**Status:** Schema v1 complete. 9 person notes migrated from old vault.

A person is anyone you interact with — clients, collaborators, contractors, vendor contacts, family, friends. Referenced from meeting cards (`who` field), project notes, and vendor notes.

**Aliases are critical for people.** Filenames are `{FirstLast}.md` (no spaces), but people naturally write `[[Gabriel Rymberg]]` or `[[Gabriel]]`. The `aliases` field must include both the spaced full name and any short names so wikilinks resolve correctly.

### What lives inside a person note

| Concept | Representation | Example |
|---------|---------------|---------|
| Contact details | `## Contact` section | Email, phone, address |
| Professional context | `## Background` section | How you know them, org links |
| Relationships | `## Connections` section | Family, professional — wikilinks where applicable |
| Organization links | Wikilinks in body | `[[CenterForUnity]]`, `[[ForBusinessSake]]` |
| Miscellaneous | `## Notes` section | Anything else |

Sections are flexible and optional — include only what applies. No prescribed `##` convention.

### Classification

Use the `type` list for relationship classification: `[person, client]`, `[person, family]`, `[person, friend]`, `[person, vendor-contact]`, `[person, collaborator]`. Multiple secondary values are fine when someone wears multiple hats.

### What you can ask CC to do

- **"Create a person note for Gabriel Rymberg"** — CC reads the schema, creates the note with `aliases: [Gabriel Rymberg, Gabriel]`.
- **"Add Gabriel's Zoom link to his note"** — CC updates the existing person note.
- **"Brian's new email is brian@newdomain.com"** — CC updates the Contact section.
- **"Mark Jesse as a collaborator too"** — CC adds `collaborator` to the `type` list.

CC will always check for an existing person note before creating a new one.

---

## Software

**Schema:** `reference/schemas/software.md`
**Location:** `~/Vaults/main/reference/software/{Name}.md`
**Status:** Schema v1 complete. No notes migrated yet.

A software entity is a tool, library, or framework significant enough to warrant a reference note — not every npm package, but things like Obsidian, Astro, Drizzle, or Wrangler where you accumulate configuration notes, gotchas, and version-specific knowledge.

### What lives inside a software note

| Concept | Representation | Example |
|---------|---------------|---------|
| Quick links | `## Quick Links` section | Docs, repo, homepage |
| Setup/installation | `## Setup` section | `brew install`, config steps |
| Usage notes | `## Usage` section | Keyboard shortcuts, workflows |
| Gotchas | `## Gotchas` section | Version requirements, workarounds |
| Integrations | `## Integrations` section | Wikilinks to `[[Cloudflare]]`, `[[PeerLoop]]` |
| Plugins/extensions | `###`/`####` headings | `### VS Code • Extensions • ESLint` |
| Credentials/license | `## Credentials` with `===` markers | `===license-key===` |

**Heading structure is flexible** — organize by topic, version, integration, or whatever makes sense for the tool. No prescribed `##` convention (unlike vendors where `##` = account).

Plugins, extensions, and add-ons are **headings** within the parent note, not separate notes. Consistent with the sub-resource-as-heading pattern.

### Classification

Use the `type` list for platform/category: `[software, desktop-app]`, `[software, cli-tool]`, `[software, library, javascript]`, `[software, obsidian-plugin]`. One or two secondary values is typical — don't over-classify.

### Credentials and licenses

- **License keys and tool-specific logins** go in the software note with `===` markers
- **Purchase history and payment details** may go in a vendor note for the seller (e.g., Gumroad, App Store)
- No strict rule — put it where you'd look for it first

### What you can ask CC to do

- **"Create a software note for Drizzle ORM"** — CC reads the schema, creates the note with `type: [software, orm]`.
- **"Add the Wrangler D1 migration gotcha to the Wrangler note"** — CC reads the existing note, adds to the Gotchas section.
- **"Add ESLint and Prettier to the VS Code note"** — CC adds `###` headings under an Extensions section.
- **"I bought MacWhisper Pro — here's the license key"** — CC creates or updates the note with credentials in `===` markers.

CC will always check for an existing software note before creating a new one.
