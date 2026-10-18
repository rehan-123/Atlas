---
type: "guide"
level: "Junior"
area: "[[Software & app problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# App crashes or won't open

> [!abstract] What's going on
> An app closes as soon as it opens, or nothing happens when you click it.

> [!tip] Think of it like
> A car that stalls on start: check the fuel (updates), the key (license) and then the engine (reinstall).

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Software & app problems]]

> [!info]+ Words on this page
> **EDR**: Endpoint detection and response: modern antivirus that records activity and can stop and undo attacks.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Restart the PC.
2. Check for app updates.
3. Try opening a different file to see if one file is the problem.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Event Viewer > Application log: event 1000 shows the crashing module.
- Repair or reinstall (Settings > Apps > the app > Modify or Uninstall).
- Test with another user profile to separate user settings from the app.
- Check the EDR or application control (ThreatLocker, App Control) didn't block it.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Damaged install | Repair or reinstall. |
| User settings corrupt | Reset the app's settings or profile. |
| Blocked by security tool | Review the block; approve if legitimate. |
| Incompatible after an update | Update or roll back. |

## Escalate when

- Many users crash after the same update
- Security tool blocks a business app

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

> [!question]- An app works for an admin account but not for the user. What does that suggest?
> Something in the user's profile or permissions: settings, a missing permission, or a policy applied to that user.

## See also

[[Frozen app or Not Responding]] · [[ThreatLocker]] · [[Windows Event Log]]

## Field notes

Add your own tips and client quirks here.
