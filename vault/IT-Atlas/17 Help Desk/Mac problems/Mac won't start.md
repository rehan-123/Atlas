---
type: "guide"
level: "Mid"
area: "[[Mac problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Mac won't start

> [!abstract] What's going on
> The Mac shows a black screen, a circle with a line through it, or a folder with a question mark.

> [!tip] Think of it like
> Like a PC that won't start Windows: find whether it's power, the startup disk or the system itself.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Mac problems]]

> [!info]+ Words on this page
> **MDM**: Mobile device management: enrolling and controlling phones and laptops.
> **safe mode**: A way to start Windows or an app with only the basics, to find what's causing a problem.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Charge it for 15 minutes, then hold the power button for 10 seconds and try again.
2. Unplug accessories and docks.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Apple silicon: hold the power button until 'Loading startup options' appears to reach Recovery; Intel: hold Cmd+R.
- In Recovery, run Disk Utility > First Aid.
- Try Safe Mode (Apple silicon: hold power, choose the disk, hold Shift > Continue in Safe Mode; Intel: hold Shift at startup).
- Reinstall macOS from Recovery if needed (keeps user data when done in place).
- FileVault will ask for a password or recovery key; get it from the MDM.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Flat battery | Charge it. |
| Disk errors | First Aid. |
| Damaged system | Reinstall macOS. |
| Hardware fault | Apple repair. |

## Escalate when

- No FileVault key available
- First Aid can't repair the disk

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

> [!question]- Where do you find a Mac's FileVault recovery key in a managed company?
> In the MDM (Jamf Pro or Intune), which escrows the key.

## See also

[[macOS]] · [[FileVault]] · [[Jamf Pro]] · [[Computer won't start Windows]]

## Field notes

Add your own tips and client quirks here.
