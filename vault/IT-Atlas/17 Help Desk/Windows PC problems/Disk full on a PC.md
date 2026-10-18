---
type: "guide"
level: "Junior"
area: "[[Windows PC problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Disk full on a PC

> [!abstract] What's going on
> The C: drive is red in File Explorer, and apps or updates fail because there's no space.

> [!tip] Think of it like
> A wardrobe so full the door won't close: you need to throw out old things or move some to storage (OneDrive).

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Windows PC problems]]

> [!info]+ Words on this page
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Empty the Recycle Bin and clear the Downloads folder of things you no longer need.
2. Move big personal files (videos, photos) to OneDrive or a network share.
3. Run Disk Cleanup (search 'Disk Cleanup', tick Windows Update Cleanup and Temporary files).

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Find what's big with WizTree or TreeSize, or `Get-ChildItem C:\Users -Recurse -File -ErrorAction SilentlyContinue | Sort Length -Desc | Select -First 20 FullName,Length`.
- Turn on Storage Sense (Settings > System > Storage) and OneDrive Files On-Demand.
- Check for large Outlook data files (.ost or .pst) and old user profiles.
- Run `DISM /Online /Cleanup-Image /StartComponentCleanup` to clean old Windows updates.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Downloads and personal media | Delete or move to OneDrive. |
| OneDrive syncing everything locally | Turn on Files On-Demand and free up space. |
| Large Outlook cache | Reduce the 'mail to keep offline' period. |
| Old Windows update files | Disk Cleanup or DISM cleanup. |

## Escalate when

- Space disappears again quickly (something is writing huge files)
- The disk is simply too small for the user's work

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

> [!question]- What OneDrive setting stops synced files from filling the disk?
> Files On-Demand ('Free up space'): files stay in the cloud and only download when opened.

## See also

[[Files, folders and drives]] · [[Local vs cloud files]] · [[Low disk space]] · [[OneDrive not syncing]]

## Field notes

Add your own tips and client quirks here.
