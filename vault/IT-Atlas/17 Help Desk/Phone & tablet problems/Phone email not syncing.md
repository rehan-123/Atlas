---
type: "guide"
level: "Junior"
area: "[[Phone & tablet problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Phone email not syncing

> [!abstract] What's going on
> Email on the phone is out of date or asks for the password again and again.

> [!tip] Think of it like
> The phone is a copy of the post room: if its pass is out of date, the copies stop arriving.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Phone & tablet problems]]

> [!info]+ Words on this page
> **Conditional Access**: Microsoft Entra rules that allow or block sign-ins based on user, device, location and risk.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Open Outlook and pull down to refresh.
2. Check the phone has internet and isn't in Low Power mode.
3. Remove and re-add the account if it keeps asking for the password.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Check the user isn't locked out (an old password on the phone causes lockouts).
- Check Conditional Access and Intune compliance for the device.
- Check the mobile device list for the user in Exchange (`Get-MobileDevice -Mailbox USER`).

## Common causes and fixes

| Cause | Fix |
|---|---|
| Password changed | Update it on the phone. |
| Device non-compliant | Fix compliance (update OS, set PIN). |
| Background refresh off | Allow background refresh. |

## Escalate when

- Device is blocked by policy and needs an exception

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

> [!question]- A user changed their password and now keeps getting locked out. What's a likely cause?
> The phone's mail app still uses the old password and keeps failing.

## See also

[[Account locked out]] · [[Microsoft Intune]] · [[Set up work email on a phone]]

## Field notes

Add your own tips and client quirks here.
