---
type: "guide"
level: "Mid"
area: "[[Windows PC problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Blue screen (BSOD)

> [!abstract] What's going on
> Windows crashed and showed a blue (or black) screen with a sad face and a stop code, then restarted.

> [!tip] Think of it like
> A circuit breaker tripping: Windows switches itself off on purpose to avoid damage when something goes badly wrong.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Windows PC problems]]

> [!info]+ Words on this page
> **RAM**: Memory: the computer's short-term workspace for open apps. Cleared when you restart.
> **NOC**: Network operations center: the team that monitors and fixes infrastructure.
> **stop code**: The error name shown on a blue screen, such as DRIVER_IRQL_NOT_LESS_OR_EQUAL.
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **firmware**: The software built into hardware such as firewalls, disks and servers.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Write down or photograph the stop code (for example DRIVER_IRQL_NOT_LESS_OR_EQUAL).
2. Note what you were doing and whether anything new was plugged in or installed.
3. Restart and save your work often until IT has checked it.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Check crash events: `Get-WinEvent -FilterHashtable @{LogName='System'; Id=41,1001,6008} -MaxEvents 10`.
- Look in `C:\Windows\Minidump` for crash dumps; WinDbg (or BlueScreenView) shows the driver blamed.
- Update the drivers named in the dump (graphics, network, dock firmware) from the manufacturer.
- Run `sfc /scannow` and a memory test (mdsched.exe) if crashes are random.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Faulty or outdated driver | Update or roll back that driver. |
| Recent update or new software | Uninstall it and test. |
| Bad RAM or overheating | Run a memory test; clean vents; replace hardware. |
| Damaged system files | `sfc /scannow` and DISM repair. |

## Escalate when

- Crashes keep happening after driver updates
- Several PCs crash with the same code after an update (possible bad patch: tell the NOC)
- Memory test shows errors

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

> [!question]- Which Windows event ID tells you the PC restarted without shutting down cleanly?
> Event 41 (Kernel-Power). 1001 records the bugcheck (stop code) and 6008 an unexpected shutdown.

## See also

[[Windows Event Log]] · [[Windows Event ID reference]] · [[Drivers]] · [[Sysinternals Suite]]

## Field notes

Add your own tips and client quirks here.
