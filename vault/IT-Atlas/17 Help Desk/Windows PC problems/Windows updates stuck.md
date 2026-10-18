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

# Windows updates stuck

> [!abstract] What's going on
> Updates fail, keep retrying, or the PC sits on 'Working on updates' for a long time.

> [!tip] Think of it like
> A delivery driver who keeps getting the wrong address: the parcel (update) never arrives until the address book (update cache) is cleared.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Windows PC problems]]

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Leave the PC plugged in and on for an hour if it shows a percentage that's still moving.
2. Restart once, then go to Settings > Windows Update > Check for updates.
3. Make sure there's at least 20 GB free on C:.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Check the failure code in Settings > Windows Update > Update history and search for it.
- Run the troubleshooter: Settings > System > Troubleshoot > Other troubleshooters > Windows Update.
- Reset the update cache: stop `wuauserv` and `bits`, rename `C:\Windows\SoftwareDistribution`, start the services again.
- Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow`.
- Check the RMM or Intune patch policy isn't blocking or deferring the update.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Not enough disk space | Free space, then retry. |
| Corrupted update cache | Reset SoftwareDistribution. |
| Damaged Windows files | DISM and SFC repair. |
| Policy or deferral settings | Check the RMM, WSUS or Intune policy. |

## Escalate when

- Same update fails on many PCs
- The PC won't boot after an update
- A security update has been failing for more than two weeks

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

> [!question]- Which two services do you stop before renaming the SoftwareDistribution folder?
> Windows Update (wuauserv) and Background Intelligent Transfer Service (bits).

## See also

[[Windows Update]] · [[Updates and why they matter]] · [[Patch failure or pending reboot]] · [[Disk full on a PC]]

## Field notes

Add your own tips and client quirks here.
