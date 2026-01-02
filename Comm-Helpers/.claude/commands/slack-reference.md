# Slack Reference

Configuration file for `/r-slack` skill. Edit these tables to customize output.

---

## Channel → Project Mapping

| Via link | Project | Emoji |
|----------|---------|-------|
| [[Slack • CFU • ai-dev]] | [[Urantia Book Tutor\|UBT]] | 🔵 |
| [[Slack • CFU • dj-dev]] | [[Discover Jesus\|DJ]] | 🔵 |
| [[Slack • CFU • dtub-dev]] | [[Discover the UB\|DTUB]] | 🔵 |
| [[Slack • CFU • dev-works]] | [[CFU - Website\|CFU-W]] | 🔵 |
| [[Slack • CFU • translation-system]] | [[XLATE-Pilot]] | 🟢 |
| [[Slack • AIM • peer-loop-team]] | [[Peer Loop]] | 🟠 |

## DMs (no project, use person name in header)

| Via link | Person |
|----------|--------|
| [[Slack • CFU • DM • Gabriel]] | [[Gabriel Rymberg\|Gabriel]] |
| [[Slack • AIM • DM • Brian]] | [[Brian LeBlanc]] |
| [[Slack • AIM • DM • Gabriel]] | [[Gabriel Rymberg\|Gabriel]] |

**DM header format:** `### 💬 Slack • Gabriel DM • 10:17` (no project emoji)

---

## Channels → Via

**The skill will ask which Via to use since threads don't identify their source.**

### CFU Workspace
| Via link |
|----------|
| [[Slack • CFU • ai-dev]] |
| [[Slack • CFU • dj-dev]] |
| [[Slack • CFU • dtub-dev]] |
| [[Slack • CFU • dev-works]] |
| [[Slack • CFU • DM • Gabriel]] |
| [[Slack • CFU • translation-system]] |

### AIM Workspace
| Via link |
|----------|
| [[Slack • AIM • DM • Brian]] |
| [[Slack • AIM • DM • Gabriel]] |
| [[Slack • AIM • peer-loop-team]] |

---

## People

Map name variations to wiki-links. First column can have multiple variations separated by comma.

| Name variations | Wiki-link |
|-----------------|-----------|
| Guy, Guy Rymberg | [[Guy Rymberg]] |
| Gabriel, Gabriel Rymberg, Gabe | [[Gabriel Rymberg\|Gabriel]] |
| Brian, Brian LeBlanc | [[Brian LeBlanc]] |
| Fraser, Fraser Gorrie | [[Fraser Gorrie]] |
| Jesse, Jesse Showalter | [[Jesse Showalter\|Jesse]] |
| Rick, Rick Lyon | [[Rick Lyon]] |

**Note:** Fraser Gorrie is the user — commitments by Fraser go in "My Commitments"

**Default** (if no match): Use name as-is without wiki-link

---

## Glossary

Terms to auto-link in Discussion and Focus sections.

| Term variations | Wiki-link |
|-----------------|-----------|
| Cloudflare | [[Cloudflare]] |
| Stripe | [[Stripe]] |
| Cloudinary | [[Cloudinary]] |
| Github, GitHub | [[Github]] |

---

## Notes

- Add new rows as needed
- Channel patterns are case-insensitive
- People names should include common variations (first name, full name, nicknames)
- Glossary matches are case-insensitive and match whole words
