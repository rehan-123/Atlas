---
type: "guide"
level: "Mid"
area: "[[New starters & leavers]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# New laptop setup

> [!abstract] What's going on
> Setting up a new or replacement laptop for a user.

> [!tip] Think of it like
> Moving into a new flat: the keys (sign-in), furniture (apps) and boxes (files) all need to arrive.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[New starters & leavers]]

> [!info]+ Words on this page
> **Autopilot**: Windows Autopilot: sets up a new company laptop automatically when the user first signs in.
> **MDM**: Mobile device management: enrolling and controlling phones and laptops.
> **EDR**: Endpoint detection and response: modern antivirus that records activity and can stop and undo attacks.
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **Known Folder Move**: OneDrive feature that moves Desktop, Documents and Pictures into OneDrive so they're synced.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Back up anything saved only on the old laptop (Desktop, Downloads) to OneDrive.
2. Note the apps you use every day for IT.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Use Autopilot or the MDM so the laptop sets itself up on first sign-in.
- Check encryption, antivirus or EDR, RMM agent and backup agent are installed and reporting.
- Check OneDrive sync and Known Folder Move (Desktop, Documents, Pictures).
- Wipe and retire the old laptop properly (remove from Intune, AD and RMM).

## Common causes and fixes

| Cause | Fix |
|---|---|
| Files only on the old laptop | Copy them before wiping. |
| Missing apps | Assign them in the deployment tool. |
| Agents missing | Fix before handing over. |

## Escalate when

- Old device must be kept for legal reasons

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

> [!question]- What OneDrive feature moves Desktop and Documents to the cloud automatically?
> Known Folder Move.

## See also

[[Windows Autopilot]] · [[Microsoft Intune]] · [[Local vs cloud files]] · [[New starter setup]]

## Field notes

Add your own tips and client quirks here.
