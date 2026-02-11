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

**Schema:** `reference/schemas/project.md` *(not yet created)*
**Location:** `~/Vaults/main/projects/{ProjectName}/`
**Status:** Schema planned. PeerLoop folder structure exists as the reference pattern.

A project is a body of work with its own repo, vault folder, and lifecycle. Unlike other entities, projects use **containment** — a folder with multiple files — because they accumulate session logs, decisions, learnings, tasks, and plans.

### What lives inside a project folder

| File/folder | Purpose |
|-------------|---------|
| `{Project}-plan.md` | Project plan and task tracking |
| `{Project}-decisions.md` | Net decisions for this project |
| `{Project}-learnings.md` | Accumulated learnings |
| `{Project}-tasks.md` | Task backlog extracted from daily notes |
| `sessions/` | Session notes (one per project per day) |

### What you can ask CC to do

- **"Set up a vault folder for MyNewProject"** — use `/cco-project-init` (this one has a skill).
- **"Archive the PeerLoop project"** — CC marks the project inactive, updates status. *(Process TBD — define when the first project completes.)*

---

## People

**Schema:** `reference/schemas/person.md` *(not yet created)*
**Location:** TBD — likely `~/Vaults/main/reference/people/` or `~/Vaults/main/business/contacts/`
**Status:** Schema planned. No notes exist yet.

A person is anyone you interact with professionally — clients, collaborators, contractors, vendor contacts. Referenced from meeting cards (`who` field), project notes, and vendor notes.

### What lives inside a person note

| Concept | Representation |
|---------|---------------|
| Contact details | Frontmatter or body fields |
| Roles/relationships | Body sections (e.g., client, collaborator) |
| Project associations | Wikilinks to project notes |
| Communication preferences | Body notes |

The exact structure will be defined when the person schema is created.

### What you can ask CC to do

- **"Create a person note for Gabriel Rymberg"** — CC reads the schema, creates the note with appropriate frontmatter.
- **"Add Gabriel's Zoom link to his note"** — CC updates the existing person note.

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
