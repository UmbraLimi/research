# Dynalist API Reference

## Authentication

- **Token type:** Single API secret token per account (not OAuth, not scopeable)
- **Get token:** Log in → `https://dynalist.io/developer`
- **Usage:** Every request is POST with `token` field in JSON body
- **Security:** Full account access (read + write) — no read-only option

## Endpoints

Base URL: `https://dynalist.io/api/v1/` — all POST, all JSON.

### File-Level (Documents & Folders)

| Endpoint | Purpose |
|----------|---------|
| `/file/list` | List all documents and folders |
| `/file/edit` | Create, rename, or move documents/folders |

### Document-Level (Nodes/Items — Core CRUD)

| Endpoint | Purpose |
|----------|---------|
| `/doc/read` | Read all nodes in a document |
| `/doc/edit` | Insert, edit, move, or delete nodes |
| `/doc/check_for_updates` | Check version numbers without full read |

### Account-Level

| Endpoint | Purpose |
|----------|---------|
| `/inbox/add` | Add item to user's inbox |
| `/upload` | Upload file (Pro only) |
| `/pref/get` | Read a user preference |
| `/pref/set` | Write a user preference |

### Search

**No server-side search API.** Must fetch full document via `/doc/read` and filter client-side.

### Edit Operations (`/doc/edit` changes array)

| Action | Parameters | Notes |
|--------|-----------|-------|
| `insert` | `parent_id`, `index`, `content`, optional fields | `index: -1` = append |
| `edit` | `node_id`, fields to change | Partial update |
| `move` | `node_id`, `parent_id`, `index` | Relocate node |
| `delete` | `node_id` | Remove node |

## Rate Limits (Token Bucket)

| Endpoint | Steady Rate | Burst |
|----------|------------|-------|
| `/doc/read` | 30/min | 100 |
| `/doc/check_for_updates` | 60/min | 50 |
| `/file/list` | 6/min | 10 |
| `/doc/edit` | 60 req/min, 240 changes/min | 20 req, 500 changes |
| `/file/edit` | 60/min | 50 |
| `/inbox/add` | 60/min | 20 |
| `/upload` | 2/min | 5 |
| `/pref/get`, `/pref/set` | 60/min | 100 |

Exceeds return `_code: "TooManyRequests"`.

## Data Format

### Response Structure

All responses: JSON with `_code` (string, `"OK"` on success) and `_msg` fields.

### Error Codes

`InvalidToken`, `TooManyRequests`, `Invalid`, `LockFail`, `Unauthorized`, `NotFound`, `NodeNotFound`, `NoInbox`, `NeedPro`, `QuotaExceeded`

### Node (Item) Structure

| Field | Type | Notes |
|-------|------|-------|
| `id` | String | Unique node ID |
| `content` | String | Item text (includes inline tags) |
| `note` | String | Note text attached to item |
| `created` | Long | Unix ms |
| `modified` | Long | Unix ms |
| `children` | String[] | Child node IDs (defines hierarchy) |
| `checked` | Boolean? | Checkbox state (optional) |
| `checkbox` | Boolean | Has a checkbox (default: false) |
| `color` | Integer | Label color 0-6 (0 = none) |
| `heading` | Integer | Heading level 0-3 (0 = normal) |
| `collapsed` | Boolean | Collapsed in UI |

### File (Document/Folder) Structure

| Field | Type | Notes |
|-------|------|-------|
| `id` | String | Unique file ID |
| `title` | String | Name |
| `type` | String | `"document"` or `"folder"` |
| `permission` | Integer | 0=None, 1=Read, 2=Edit, 3=Manage, 4=Owner |
| `children` | String[] | Child file IDs (folders only) |

### Tags

Tags are **inline text** in `content` or `note` fields — not a separate data structure.
- `#tagname` — hashtag style
- `@tagname` — at-mention style

No tags API. To find tags, parse them from content strings.

### Document Hierarchy

Flat `nodes` array from `/doc/read`. Reconstruct tree via `children` arrays. Root node identified by `root_file_id` from `/file/list`.

## Key Limitations

1. No search API — must fetch and filter client-side
2. No tag-specific API — tags are inline text
3. Single unscoped token — full account access
4. No webhooks — must poll via `check_for_updates`
5. File upload requires Pro
6. API still labeled beta
