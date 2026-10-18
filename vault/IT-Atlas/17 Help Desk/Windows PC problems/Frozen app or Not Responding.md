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

# Frozen app or Not Responding

> [!abstract] What's going on
> One program stops reacting and its title bar says 'Not Responding'.

> [!tip] Think of it like
> A person who's thinking very hard and can't hear you. Sometimes you wait; sometimes you have to tap them on the shoulder (end the task).

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Windows PC problems]]

> [!info]+ Words on this page
> **Task Manager**: Windows tool (Ctrl+Shift+Esc) that shows running apps and what's using CPU, memory and disk.
> **safe mode**: A way to start Windows or an app with only the basics, to find what's causing a problem.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Wait one minute: it may be saving or loading something big.
2. Open Task Manager (Ctrl+Shift+Esc), select the app and click End task.
3. Reopen it; Office apps usually offer to recover your document.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Check whether it freezes on a particular file, add-in or network drive.
- Office: start in safe mode (`outlook.exe /safe`, `winword /safe`) to test add-ins.
- Check Event Viewer > Application log for event 1000 (app crash) or 1002 (app hang).
- Repair or reinstall the app (Settings > Apps > the app > Modify or Repair).

## Common causes and fixes

| Cause | Fix |
|---|---|
| Waiting on a slow network drive | Fix the connection or move the file locally. |
| Faulty add-in | Disable it from the app's add-ins menu. |
| Very large file | Split it or let it load. |
| Damaged install | Repair or reinstall. |

## Escalate when

- Many users have the same app freezing
- Data may be lost or a file is damaged

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

> [!question]- Which two Application log events point to a crashing or hanging app?
> 1000 (application error) and 1002 (application hang).

## See also

[[App crashes or won't open]] · [[Windows Event Log]] · [[PC is slow]]

## Field notes

Add your own tips and client quirks here.
