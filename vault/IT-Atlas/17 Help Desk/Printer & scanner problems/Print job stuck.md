---
type: "guide"
level: "Junior"
area: "[[Printer & scanner problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Print job stuck

> [!abstract] What's going on
> A document sits in the print queue and blocks everything behind it.

> [!tip] Think of it like
> A jammed queue at a ticket counter: one confused customer at the front holds up everyone behind.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Printer & scanner problems]]

> [!info]+ Words on this page
> **spooler**: The Windows service that queues print jobs before they go to the printer.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Open the print queue, right-click the stuck document and Cancel.
2. Turn the printer off and on.
3. Restart the PC.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Stop the spooler, clear `C:\Windows\System32\spool\PRINTERS`, start the spooler: `Stop-Service Spooler -Force; Remove-Item C:\Windows\System32\spool\PRINTERS\* -Force; Start-Service Spooler`.
- On a print server, clear the job there too.
- Check whether one particular file always sticks (very large PDF, odd fonts).

## Common causes and fixes

| Cause | Fix |
|---|---|
| One corrupt job | Delete it. |
| Spooler stuck | Clear the spool folder. |
| Huge or unusual file | Print as image or to PDF first. |

## Escalate when

- The print server's spooler keeps crashing

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

> [!question]- Which folder holds waiting print jobs on Windows?
> `C:\Windows\System32\spool\PRINTERS`.

## See also

[[Print Server]] · [[Printer offline]]

## Field notes

Add your own tips and client quirks here.
