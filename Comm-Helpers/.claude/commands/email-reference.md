# Email Reference

Configuration file for `/r-email` skill. Edit these tables to customize output.

---

## Gmail Accounts

| Email | Display Name | Notes |
|-------|--------------|-------|
| fraser@frasergorrie.com | Personal | Primary |
| fraser@meristics.com | Meristics | Business |
| fgorrie@bio-software.com | Bio-Software | Business |

When prompting: skill will ask which account if not detected from Print view header.

---

## Email → Person Mapping

Map email addresses to wiki-links. Multiple addresses can map to the same person.

| Email | Wiki-link |
|-------|-----------|
| brian@alphapeer.com | [[Brian LeBlanc]] |
| brian@peerloop.com | [[Brian LeBlanc]] |
| brian@alr.com | [[Brian LeBlanc]] |
| gabriel@cfu.org | [[Gabriel Rymberg\|Gabriel]] |
| guy@cfu.org | [[Guy Rymberg]] |
| rick@cfu.org | [[Rick Lyon]] |
| jesse@example.com | [[Jesse Showalter\|Jesse]] |
| simon@mynaparrot.com | Simon CHABOUD |
| bob@mynaparrot.com | Bob Teng |
| support@mynaparrot.com | MynaParrot Support |
| info@plugnmeet.cloud | Plug-N-Meet Cloud |
| fraser@frasergorrie.com | me |
| fraser@meristics.com | me |
| fgorrie@bio-software.com | me |

**Notes:**
- Fraser's emails map to "me" (first-person narrative)
- Add wiki-link brackets only for people in your Obsidian vault
- External contacts can be plain text

---

## Projects (Optional)

Map email patterns or subjects to projects. Less structured than Slack channels.

| Pattern | Project | Emoji |
|---------|---------|-------|
| @alphapeer.com | [[Peer Loop]] | 🟠 |
| @peerloop.com | [[Peer Loop]] | 🟠 |
| @cfu.org | [[CFU]] | 🔵 |
| @mynaparrot.com | [[Peer Loop]] | 🟠 |
| plugnmeet | [[Peer Loop]] | 🟠 |

**Usage:** If sender/recipient domain matches, project emoji can be added to header. Optional — omit if not useful.

---

## Glossary

Terms to auto-link in Discussion, Focus, and Thread Summary sections.

| Term variations | Wiki-link |
|-----------------|-----------|
| Cloudflare | [[Cloudflare]] |
| Stripe | [[Stripe]] |
| Cloudinary | [[Cloudinary]] |
| Github, GitHub | [[Github]] |
| Plug-N-Meet, PlugNMeet | [[Plug-N-Meet]] |
| Big Blue Button, BBB | [[Big Blue Button]] |
| Meristics | [[Meristics]] |
| Technifar, Technifar Corporation | [[Technifar Corporation]] |
| Alpha Peer | [[Alpha Peer]] |

---

## Notes

- Add new rows as needed
- Email patterns are case-insensitive
- Multiple email addresses per person are common — add all variations
- Glossary matches are case-insensitive and match whole words
