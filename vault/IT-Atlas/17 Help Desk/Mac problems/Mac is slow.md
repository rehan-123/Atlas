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

# Mac is slow

> [!abstract] What's going on
> A Mac is laggy, the fan is loud or you see the spinning beach ball.

> [!tip] Think of it like
> Same as a cluttered desk: find what's taking up the room and clear it.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Mac problems]]

> [!info]+ Words on this page
> **CPU**: The processor, the part of a computer that does the calculations.
> **MDM**: Mobile device management: enrolling and controlling phones and laptops.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Save and restart (Apple menu > Restart).
2. Quit apps you're not using (Cmd+Q, not just closing the window).
3. Check free space: Apple menu > System Settings > General > Storage.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Activity Monitor: sort by CPU and Memory; check Memory Pressure.
- Terminal: `top -o cpu` for the busiest processes.
- Check for pending updates: `softwareupdate -l`.
- Check login items: System Settings > General > Login Items.
- Check the MDM (Jamf, Intune) for stuck policies or security tools using CPU.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Not restarted for weeks | Restart. |
| Too many apps or tabs | Quit them. |
| Low disk space | Free space (see Mac disk full). |
| Background security or sync tool stuck | Check the MDM and agent. |

## Escalate when

- A security agent uses constant high CPU
- The Mac is out of support for the current macOS

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

> [!question]- What does Memory Pressure in Activity Monitor show?
> How hard the Mac is working to find memory. Green is fine; yellow or red means it needs fewer apps or more RAM.

## See also

[[macOS]] · [[Jamf Pro]] · [[How a computer works]] · [[PC is slow]]

## Field notes

Add your own tips and client quirks here.
