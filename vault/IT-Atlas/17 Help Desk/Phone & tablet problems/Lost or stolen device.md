---
type: "guide"
level: "Mid"
area: "[[Phone & tablet problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Lost or stolen device

> [!abstract] What's going on
> A laptop or phone with work data has been lost or stolen.

> [!tip] Think of it like
> Losing your keys: change the locks (passwords, sessions) quickly, then try to find the keys.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Phone & tablet problems]]

> [!info]+ Words on this page
> **MDM**: Mobile device management: enrolling and controlling phones and laptops.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Tell IT immediately, even outside hours. Speed matters more than anything.
2. Report theft to the police and get a reference number if needed.
3. Use Find My (Apple) or Find My Device (Android, Windows) if it's your own device.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Reset the user's password and revoke sign-in sessions (Entra: Revoke sessions, or `Revoke-MgUserSignInSession -UserId USER`).
- Intune or Jamf: Lock the device; wipe it if it can't be recovered (follow policy; personal phones get a work-data-only wipe).
- Confirm the disk was encrypted (BitLocker or FileVault status in the MDM).
- Record it as a security incident with the device serial number and what data was on it.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Device encrypted and managed | Lock, wipe, revoke sessions. |
| Device not encrypted | Assume data exposure: escalate to security. |
| Personal phone with work apps | Selective wipe of work data. |

## Escalate when

- The device wasn't encrypted
- It held sensitive or regulated data
- It belonged to an executive or admin

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

> [!question]- Why reset the password and revoke sessions even when the device is encrypted?
> Apps on the device may still be signed in; revoking sessions and changing the password cuts off that access.

## See also

[[Microsoft Intune]] · [[BitLocker]] · [[FileVault]] · [[Jamf Pro]] · [[Account hacked or sending spam]]

## Field notes

Add your own tips and client quirks here.
