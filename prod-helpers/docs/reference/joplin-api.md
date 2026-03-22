# Joplin Data API Reference

## Authentication

- **Token location:** Joplin Desktop → Settings → Web Clipper → "Authorization token"
- **Usage:** Query parameter on every request: `?token=YOUR_TOKEN`
- **Port:** Default `41184`. If unavailable, scan 41184–41194 and `GET /ping` (expect `"JoplinClipperServer"`)
- **Requirement:** Joplin desktop app must be running

### Programmatic Auth Flow (for apps/extensions)

1. `POST /auth` → `{ auth_token: "TEMP_TOKEN" }`
2. Joplin shows Accept/Reject prompt
3. Poll `GET /auth/check?auth_token=TEMP_TOKEN` → `{ status: "waiting" }`
4. On accept: `{ status: "accepted", token: "PERMANENT_API_TOKEN" }`

## Endpoints

Base URL: `http://localhost:41184`

### Notes (`/notes`)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/notes` | List all notes (paginated) |
| GET | `/notes/:id` | Get single note |
| GET | `/notes/:id/tags` | Tags on note |
| GET | `/notes/:id/resources` | Attachments on note |
| POST | `/notes` | Create (`title`, `body`/`body_html`, `parent_id`) |
| PUT | `/notes/:id` | Update (partial) |
| DELETE | `/notes/:id` | Delete (trash; `?permanent=1` for hard delete) |

### Folders/Notebooks (`/folders`)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/folders` | List all (returned as tree with `children`) |
| GET | `/folders/:id` | Get single folder |
| GET | `/folders/:id/notes` | Notes in folder |
| POST | `/folders` | Create (`title`, optional `parent_id`) |
| PUT | `/folders/:id` | Update |
| DELETE | `/folders/:id` | Delete |

### Tags (`/tags`)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/tags` | List all tags |
| GET | `/tags/:id` | Get single tag |
| GET | `/tags/:id/notes` | Notes with this tag |
| POST | `/tags` | Create (`title`) |
| POST | `/tags/:id/notes` | Assign tag to note (`{ "id": "NOTE_ID" }`) |
| PUT | `/tags/:id` | Rename tag |
| DELETE | `/tags/:id` | Delete tag |
| DELETE | `/tags/:id/notes/:note_id` | Remove tag from note |

### Search (`/search`)

- `GET /search?query=QUERY` — full-text search (notes by default)
- `&type=folder` or `&type=tag` — search other types (case-insensitive, `*` wildcards)

### Resources (`/resources`)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/resources` | List resources |
| GET | `/resources/:id` | Metadata |
| GET | `/resources/:id/file` | Download file |
| GET | `/resources/:id/notes` | Notes referencing this |
| POST | `/resources` | Upload (multipart: `data=@file`, `props={"title":"..."}`) |
| PUT | `/resources/:id` | Update (optionally replace file) |
| DELETE | `/resources/:id` | Delete |

### Events (`/events`)

- `GET /events` — paginated change log (cursor-based, 90-day retention)
- Event types: 1=created, 2=updated, 3=deleted

### Export

**No export endpoint.** For bulk extraction, iterate notes with pagination.

## Rate Limits

**None.** Local-only server — no throttling. Limited only by SQLite and Joplin process capacity.

## Data Format

### General

- All JSON (except resource upload: multipart/form-data; resource download: raw bytes)
- Timestamps: Unix milliseconds
- Booleans: integers `0` or `1`

### Note Structure

| Field | Type | Notes |
|-------|------|-------|
| `id` | String | 32-char hex |
| `parent_id` | String | Folder ID |
| `title` | String | Note title |
| `body` | String | Content (Markdown or HTML) |
| `markup_language` | Integer | 1=Markdown, 2=HTML |
| `is_todo` | Integer | 0 or 1 |
| `todo_due` | Long | Unix ms |
| `todo_completed` | Long | Unix ms |
| `source_url` | String | Original URL if clipped |
| `created_time` | Long | Unix ms |
| `updated_time` | Long | Unix ms |

### Tag Structure

`id`, `title`, `created_time`, `updated_time`. Many-to-many link to notes via `/tags/:id/notes`.

### Item Type IDs

| Type | ID |
|------|-----|
| note | 1 |
| folder | 2 |
| resource | 4 |
| tag | 5 |
| note_tag | 6 |

### Pagination

All list endpoints: `{ items: [...], has_more: bool }`. Params: `page` (default 1), `limit` (max 100), `order_by`, `order_dir`.

### Field Filtering

`?fields=id,title,body` — request only specific properties.
