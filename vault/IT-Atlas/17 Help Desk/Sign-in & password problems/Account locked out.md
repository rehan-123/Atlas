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

# Account locked out

> [!abstract] What's going on
> Too many wrong passwords and the account is temporarily blocked.

> [!tip] Think of it like
> A cash machine that keeps your card after three wrong PINs. Often it's an old device still trying the old PIN, not the person.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Sign-in & password problems]]

> [!info]+ Words on this page
> **Wi-Fi**: Wireless network connection using radio signals.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **NOC**: Network operations center: the team that monitors and fixes infrastructure.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Wait 15 to 30 minutes; most lockouts clear by themselves.
2. Update your password on your phone's email app, Wi-Fi and any other device.
3. Contact IT if it keeps happening.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- AD: find locked accounts with `Search-ADAccount -LockedOut` and unlock with `Unlock-ADAccount USER`.
- Find the source: event 4740 on the PDC emulator names the caller computer.
- Look for old saved passwords: phone mail apps, mapped drives, scheduled tasks, services or an old laptop.
- Microsoft 365: check Entra sign-in logs for the failing app and location (smart lockout).

## Common causes and fixes

| Cause | Fix |
|---|---|
| Phone still using the old password | Update the phone. |
| Saved credentials on a PC or mapped drive | Clear Credential Manager. |
| Service or scheduled task using the user's account | Update it, and move it to a service account. |
| Password-guessing attack | Treat as a security incident. |

## Escalate when

- Lockouts come from unknown IP addresses or countries
- Many accounts lock at once (NOC playbook: Account lockout storm)

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

> [!question]- Which event ID shows an account lockout, and on which server do you look?
> 4740, on the domain controller holding the PDC emulator role.

## See also

[[Active Directory]] · [[Account lockout storm]] · [[Forgot password]] · [[Kerberos]]

## Field notes

Add your own tips and client quirks here.
