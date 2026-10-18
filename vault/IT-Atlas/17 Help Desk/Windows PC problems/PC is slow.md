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

# PC is slow

> [!abstract] What's going on
> The computer takes ages to open things, or everything lags.

> [!tip] Think of it like
> A desk so covered in open files that you can't find anything. Clearing the desk (closing apps, restarting) gives you room to work again.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Windows PC problems]]

> [!info]+ Words on this page
> **Task Manager**: Windows tool (Ctrl+Shift+Esc) that shows running apps and what's using CPU, memory and disk.
> **CPU**: The processor, the part of a computer that does the calculations.
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **RAM**: Memory: the computer's short-term workspace for open apps. Cleared when you restart.
> **SSD**: Solid-state drive: fast storage with no moving parts. Much quicker than an old hard disk.
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **malware**: Any harmful software: viruses, ransomware, spyware and the like.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Save your work and restart the PC (Start > Power > Restart, not just closing the lid).
2. Close apps and browser tabs you aren't using.
3. Check the disk isn't full: open File Explorer > This PC and look at the C: drive bar.
4. Leave it plugged in and switched on over lunch if it says updates are installing.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Open Task Manager (Ctrl+Shift+Esc) > Processes and sort by CPU, Memory and Disk to see what's busy.
- Check when it last restarted: `Get-CimInstance Win32_OperatingSystem | Select LastBootUpTime`.
- Check free space on C: and storage health (Settings > System > Storage).
- Check startup apps: Task Manager > Startup apps; disable ones the user doesn't need.
- Check RMM history for CPU, memory and disk trends on this device.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Not restarted for weeks | Restart; set up a weekly restart policy. |
| Too many browser tabs or apps | Close them; explain to the user how much memory tabs use. |
| Disk almost full | Follow 'Disk full on a PC'. |
| Updates or antivirus scan running | Let it finish, then check again. |
| Old hardware: 8 GB RAM or a spinning hard disk | Recommend more RAM or a replacement with an SSD. |

## Escalate when

- It's slow even after a restart and nothing obvious is busy
- An unknown process is using a lot of CPU (could be malware)
- The disk shows SMART warnings

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

> [!question]- A user's PC is slow and Task Manager shows Disk at 100%. What are two common causes?
> Windows Update or antivirus working in the background, or a failing or old spinning hard disk.

## See also

[[How a computer works]] · [[Why restarting works]] · [[High CPU]] · [[High memory]] · [[Disk full on a PC]] · [[Windows client]]

## Field notes

Add your own tips and client quirks here.
