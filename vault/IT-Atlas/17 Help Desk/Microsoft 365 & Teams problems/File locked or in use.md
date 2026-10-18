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

# File locked or in use

> [!abstract] What's going on
> A file says it's locked for editing by someone else, or 'in use by another program'.

> [!tip] Think of it like
> A library book already checked out: wait for it, or check who has it.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Microsoft 365 & Teams problems]]

> [!info]+ Words on this page
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Ask the named person to close the file.
2. If it's in OneDrive or SharePoint, open it in the browser and co-author instead.
3. Restart your PC if you're the one holding it.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- On a file server: Computer Management > Shared Folders > Open Files, or `Get-SmbOpenFile | Where Path -like '*NAME*'`, then close the session with care.
- Check for stale lock files (`~$NAME.docx`) in the folder.
- Excel with old formats (.xls) can't co-author; save as .xlsx.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Someone else has it open | Ask them to close it. |
| Stale lock after a crash | Close the open file session; remove the ~$ file. |
| Old file format | Convert to a modern format for co-authoring. |

## Escalate when

- Closing a file session would lose someone else's unsaved work

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

> [!question]- Which PowerShell command lists files open on a Windows file server?
> `Get-SmbOpenFile`.

## See also

[[File Server & DFS]] · [[SharePoint & OneDrive]] · [[Files, folders and drives]]

## Field notes

Add your own tips and client quirks here.
