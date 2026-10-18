---
type: "concept"
level: "Senior"
category: "[[Architecture & design]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Tiered administration

> [!abstract] In one line
> Separating admin accounts by what they can touch, so a compromised workstation can't lead straight to domain admin.

> [!tip] Think of it like
> Bank vault keys never leave the vault room: the cashier's keys can't open the vault, and the vault key is never used at the counter.

> [!info]+ Words on this page
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **domain controller**: A server running Active Directory that checks logins.
> *More in the [[Glossary]].*

## How it works

- **Tier 0**: identity control (domain controllers, Entra Connect, AD CS, PAM). **Tier 1**: servers and apps. **Tier 2**: workstations and users.
- Admins have separate accounts per tier and never log on to a lower tier with a higher-tier account.
- Tier 0 is administered only from privileged access workstations.
- Microsoft now calls the model the Enterprise Access Model; the principle is the same.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why should a Domain Admin never log on to a normal workstation?
> If that workstation is compromised, the admin's credentials can be stolen from memory and used to take over the domain.

## See also

[[Least privilege]] · [[Active Directory]] · [[Microsoft Entra Privileged Identity Management]] · [[Windows LAPS]]
