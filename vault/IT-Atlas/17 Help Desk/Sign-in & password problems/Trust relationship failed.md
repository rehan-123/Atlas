---
type: "guide"
level: "Mid"
area: "[[Sign-in & password problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Trust relationship failed

> [!abstract] What's going on
> At login Windows says 'The trust relationship between this workstation and the primary domain failed'.

> [!tip] Think of it like
> A club membership card that expired because you didn't visit for months: the club (domain) no longer recognizes the PC.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Sign-in & password problems]]

> [!info]+ Words on this page
> **VPN**: An encrypted tunnel over the internet to a private network.
> **LAPS**: A Windows feature that gives each PC its own rotating local admin password.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **snapshot**: A saved point in time of a VM or disk. Not a backup, and it grows the longer you keep it.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Log in with a cached account is often impossible; contact IT.
2. Keep the PC connected to the office network or VPN while IT fixes it.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Log in with a local admin account (Windows LAPS password).
- Repair the secure channel: `Test-ComputerSecureChannel -Repair -Credential DOMAIN\ADMIN`.
- If that fails, remove from the domain and rejoin (and check the computer object wasn't deleted).
- Check the PC's time matches the domain.

## Common causes and fixes

| Cause | Fix |
|---|---|
| PC was off or offline for a long time | Repair the secure channel. |
| PC restored from an old image or snapshot | Repair or rejoin. |
| Computer object deleted in AD | Rejoin the domain. |

## Escalate when

- You don't have a local admin password
- Several PCs show the same error

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

> [!question]- Which PowerShell command repairs a broken domain trust without rejoining?
> `Test-ComputerSecureChannel -Repair -Credential DOMAIN\ADMIN`.

## See also

[[Active Directory]] · [[Windows LAPS]] · [[Domain-joined vs cloud-joined PCs]] · [[Kerberos]]

## Field notes

Add your own tips and client quirks here.
