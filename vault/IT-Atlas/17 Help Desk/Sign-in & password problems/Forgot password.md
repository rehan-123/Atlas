---
type: "guide"
level: "Junior"
area: "[[Sign-in & password problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Forgot password

> [!abstract] What's going on
> The user can't remember their password.

> [!tip] Think of it like
> Losing your house key: a trusted locksmith (IT or self-service reset) makes you a new one after checking it's really you.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Sign-in & password problems]]

> [!info]+ Words on this page
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Use self-service reset if it's set up: go to aka.ms/sspr, or click 'Forgot password' on the sign-in page.
2. Otherwise contact IT from a known phone or in person so they can confirm who you are.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Verify identity using the company's process before resetting (call back on a known number, or the manager confirms). Never reset just because someone asks by email.
- Cloud account: reset in the Microsoft 365 admin center or Entra ID.
- On-premises AD: `Set-ADAccountPassword -Identity USER -Reset -NewPassword (Read-Host -AsSecureString 'New password')` and tick 'must change at next logon'.
- With Entra Connect, check password writeback or wait for sync before the user tries Microsoft 365.
- Tell the user to update the password on their phone and other devices to avoid lockouts.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Password simply forgotten | Verified reset. |
| Password expired | Reset or let the user change it at sign-in. |
| Old password saved on phone | Update it everywhere. |

## Escalate when

- You can't confirm the caller's identity (possible social engineering)
- The account is an admin or executive account (follow the high-risk process)

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

> [!question]- Someone emails the help desk asking for a password reset for their boss. What do you do?
> Don't reset. Verify the identity through the approved process; this is a common social-engineering trick.

## See also

[[User accounts and permissions]] · [[Passwords and password managers]] · [[Microsoft Entra ID]] · [[Active Directory]] · [[Account locked out]]

## Field notes

Add your own tips and client quirks here.
