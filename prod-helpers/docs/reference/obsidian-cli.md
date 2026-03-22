# Obsidian CLI Reference (v1.12+)

## Installation & Setup

- **Shipped:** February 27, 2026 in v1.12.4 (free, all desktop users)
- **Enable:** Settings → General → Command line interface → enable + "Register CLI"
- **macOS:** Adds to `~/.zprofile`: `export PATH="$PATH:/Applications/Obsidian.app/Contents/MacOS"`
- **Requirement:** Obsidian desktop app must be running (CLI communicates via local IPC)

## Available Commands

100+ commands across these categories:

### Files

| Command | Purpose |
|---------|---------|
| `files` | List vault files |
| `read file=` | Read file content |
| `create name= [template=]` | Create new note |
| `append file= content=` | Append to file |
| `prepend file= content=` | Prepend to file |
| `move file= to=` | Move file (auto-rewrites wikilinks) |
| `delete file= [--permanent]` | Delete (trash by default) |
| `rename` | Rename file |

### Search

| Command | Purpose |
|---------|---------|
| `search query=` | Search (path-only results) |
| `search:context query= limit=` | Search with surrounding context |
| `search:open query=` | Search and open in Obsidian |

### Daily Notes

| Command | Purpose |
|---------|---------|
| `daily` | Today's daily note |
| `daily:read` | Read daily note content |
| `daily:append content=` | Append to daily note |
| `daily:prepend content=` | Prepend to daily note |
| `daily:open date=` | Open specific date's daily note |

### Properties (Frontmatter)

| Command | Purpose |
|---------|---------|
| `properties file=` | Read properties |
| `properties:set file= key=value` | Set property |
| `properties:remove file= key=` | Remove property |

### Tags & Links

| Command | Purpose |
|---------|---------|
| `tags [sort=count]` | List all tags |
| `tags:rename old= new=` | Rename tag across vault |
| `links file=` | Outgoing links |
| `backlinks file=` | Incoming links |
| `orphans` | Files with no links |
| `unresolved` | Broken links |

### Tasks

| Command | Purpose |
|---------|---------|
| `tasks [format=json]` | List tasks |
| `task:create content=` | Create task |
| `task:complete task=` | Complete task |

### Developer

| Command | Purpose |
|---------|---------|
| `devtools` | Open dev tools |
| `plugin:enable id=` | Enable plugin |
| `plugin:reload id=` | Reload plugin |
| `eval code=` | Execute JS in Obsidian runtime |
| `dev:errors` | Show errors |

### Version & Diff

| Command | Purpose |
|---------|---------|
| `version` | Show version |
| `diff file= from= to=` | Diff file versions |

## Output Formats

Append `format=` to any command: `json`, `csv`, `md`, `paths`, `yaml`, `tree`, `tsv`

## Multi-Vault

`vault="name"` as first argument to target a specific vault.

## TUI Mode

Running `obsidian` with no arguments launches interactive terminal file browser.

## Key Advantages Over Direct Filesystem

- `move` auto-rewrites all wikilinks — **the** reason to prefer CLI over `mv`
- `tags:rename` renames across entire vault
- `delete` without `--permanent` moves to trash (recoverable)
- Structured output formats (`json`, `yaml`) for programmatic use

## Alternative Interfaces

### Local REST API Plugin (Community)

- **Repo:** `coddingtonbear/obsidian-local-rest-api`
- **Connection:** HTTPS on `127.0.0.1:27124` (self-signed cert)
- **Auth:** Bearer token from plugin settings
- **Use case:** HTTP-based access (webhooks, MCP servers) — secondary to CLI

### URI Scheme (`obsidian://`)

- Built-in: `open`, `search`, `new`, `hook-get-address`
- Limited: cannot modify existing notes or manipulate frontmatter
- Advanced URI plugin extends this but is no longer maintained

### Direct Filesystem

- Vault is just a folder of markdown files
- Safe for bulk reads or when Obsidian is closed
- **Dangerous for moves/renames** — breaks wikilinks
- Use atomic writes to avoid corruption

## Limitations

- Obsidian desktop must be running
- `eval` executes arbitrary JS — do not use with untrusted input
- No rate limits documented (local IPC)
- No auth mechanism (local only)
