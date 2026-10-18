---
type: "guide"
level: "Junior"
area: "[[Microsoft 365 & Teams problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# OneDrive not syncing

> [!abstract] What's going on
> The OneDrive icon shows a red X, a pause sign, or files with sync errors.

> [!tip] Think of it like
> A courier between your desk and the cloud storage room. If he's paused, lost his badge (signed out) or a parcel is the wrong shape (bad file name), deliveries stop.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Microsoft 365 & Teams problems]]

> [!info]+ Words on this page
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **ransomware**: Malware that encrypts files and demands payment to unlock them.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Click the OneDrive cloud icon and read the message; resume sync if it's paused.
2. Check you're signed in and online.
3. Look for files with sync errors and rename ones with odd characters or very long names.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Reset OneDrive: run `%localappdata%\Microsoft\OneDrive\onedrive.exe /reset` (the path can be under Program Files instead), then start OneDrive again.
- Check storage: the OneDrive quota and the local disk.
- Check the path length (files deep in many folders can exceed limits) and blocked file types.
- For SharePoint libraries, check the user still has access to the site.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Sync paused or signed out | Resume or sign in. |
| File names or paths too long or invalid | Rename or shorten paths. |
| OneDrive or local disk full | Free space or upgrade storage. |
| Lost access to the SharePoint site | Restore permission. |

## Escalate when

- Files were deleted or overwritten (see Recover a deleted file)
- Ransomware suspected (many files renamed or encrypted)

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

> [!question]- A user's OneDrive shows sync errors on one folder with very long names. What's the fix?
> Shorten the folder and file names (or move the folder higher up) so the full path is within the limit.

## See also

[[SharePoint & OneDrive]] · [[Local vs cloud files]] · [[Disk full on a PC]] · [[Recover a deleted file]]

## Field notes

Add your own tips and client quirks here.
