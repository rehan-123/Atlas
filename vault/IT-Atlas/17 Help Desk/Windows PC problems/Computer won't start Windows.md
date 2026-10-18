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

# Computer won't start Windows

> [!abstract] What's going on
> The PC turns on but gets stuck on the logo, keeps restarting, or shows a repair screen.

> [!tip] Think of it like
> A book whose first few pages are torn: the cover opens, but the story can't start. Repair tools rebuild those pages.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Windows PC problems]]

> [!info]+ Words on this page
> **BIOS**: The low-level setup program that starts a PC before Windows loads (UEFI on modern PCs).
> **safe mode**: A way to start Windows or an app with only the basics, to find what's causing a problem.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Unplug USB drives and docks, then restart.
2. If you see 'Automatic Repair', let it finish once.
3. If it asks for a BitLocker recovery key, don't guess: contact IT with the key ID shown on screen.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Boot into Windows Recovery (Shift + Restart, or interrupt boot three times) and try Startup Repair.
- Try Safe Mode (Troubleshoot > Advanced options > Startup Settings).
- Uninstall the latest quality update from Recovery if it started after patching.
- Look up the BitLocker recovery key in Entra ID, Intune or Active Directory using the key ID.
- Check the disk: `chkdsk C: /scan` from the recovery command prompt.

## Common causes and fixes

| Cause | Fix |
|---|---|
| A bad update | Uninstall the latest update from Recovery. |
| Damaged system files | `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` once Windows starts. |
| BIOS or hardware change triggered BitLocker | Enter the recovery key, then suspend and resume BitLocker. |
| Failing disk | Back up what you can and replace the disk or device. |

## Escalate when

- No recovery key can be found
- The disk shows errors or clicking
- Startup Repair fails repeatedly: reimage the device

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

> [!question]- A PC asks for a BitLocker recovery key after a BIOS update. Where do you find the key?
> In Microsoft Entra ID or Intune (device > BitLocker keys), or in Active Directory if keys are stored there. Match the key ID shown on screen.

## See also

[[BitLocker]] · [[Windows Update]] · [[Blue screen (BSOD)]] · [[PC won't turn on]]

## Field notes

Add your own tips and client quirks here.
