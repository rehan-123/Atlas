---
type: "guide"
level: "Junior"
area: "[[Mac problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Mac disk full

> [!abstract] What's going on
> The Mac warns that the startup disk is almost full.

> [!tip] Think of it like
> Same wardrobe problem: store less locally, more in the cloud.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Mac problems]]

> [!info]+ Words on this page
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **snapshot**: A saved point in time of a VM or disk. Not a backup, and it grows the longer you keep it.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. System Settings > General > Storage: use the recommendations (Store in iCloud or OneDrive, empty Bin).
2. Empty the Bin and clear Downloads.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Find large folders: `du -sh ~/* | sort -h` in Terminal.
- Check OneDrive Files On-Demand is on.
- Check for old iOS backups, Xcode or large mail caches.
- Check local Time Machine snapshots: `tmutil listlocalsnapshots /`.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Downloads and media | Delete or move. |
| Cloud files all downloaded | Turn on Files On-Demand. |
| Old device backups | Delete old backups. |

## Escalate when

- Disk is too small for the user's work

## Write it up

Copy this into the ticket and fill it in:

```
User and contact: 
Device: 
Problem (in their words): 
Exact error message: 
Started when / what changed: 
What I checked: 
What fixed it: 
User confirmed it's fixed (yes/no): 
```

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Which Terminal command lists the size of each folder in your home folder?
> `du -sh ~/* | sort -h`.

## See also

[[macOS]] · [[Disk full on a PC]] · [[Local vs cloud files]]

## Field notes

Add your own tips and client quirks here.
