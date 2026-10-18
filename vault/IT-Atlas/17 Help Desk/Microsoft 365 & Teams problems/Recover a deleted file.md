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

# Recover a deleted file

> [!abstract] What's going on
> Someone deleted or overwrote a file and needs it back.

> [!tip] Think of it like
> A shredder with a delay: for a while, deleted things wait in a bin before they're gone for good.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Microsoft 365 & Teams problems]]

> [!info]+ Words on this page
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **ransomware**: Malware that encrypts files and demands payment to unlock them.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Check the Recycle Bin (PC) or the OneDrive or SharePoint Recycle bin in the browser.
2. For an overwritten Office file, open it in the browser > File > Version history.
3. Tell IT the file name, folder and roughly when it was last OK.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- OneDrive or SharePoint: first-stage and second-stage recycle bins keep files for a limited time (93 days in total by default).
- OneDrive 'Restore your OneDrive' can roll back a whole OneDrive to a point in time.
- File server: right-click the folder > Properties > Previous Versions, or restore from backup.
- Use the backup product (Veeam, Datto, Spanning, Microsoft 365 Backup) for older items.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Deleted recently | Recycle bin. |
| Overwritten | Version history or Previous Versions. |
| Deleted long ago | Restore from backup. |

## Escalate when

- Many files deleted or renamed at once (possible ransomware)
- The data isn't covered by any backup

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

> [!question]- A Word file in SharePoint was overwritten yesterday. What's the quickest fix?
> Version history: restore yesterday's version.

## See also

[[SharePoint & OneDrive]] · [[SaaS shared responsibility]] · [[Backups for everyone]] · [[Microsoft 365 Backup]] · [[Spanning Backup]]

## Field notes

Add your own tips and client quirks here.
