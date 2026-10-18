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

# Hybrid identity models

> [!abstract] In one line
> How on-premises Active Directory and Microsoft Entra ID are linked: password hash sync, pass-through authentication or federation.

> [!tip] Think of it like
> Three ways a club checks your membership: a copy of the list at the door (PHS), a phone call to head office (PTA), or sending you to head office in person (federation).

> [!info]+ Words on this page
> **DC**: Domain controller: a server running Active Directory.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> *More in the [[Glossary]].*

## How it works

- **Password hash sync (PHS)**: a hash of the password hash is synced to Entra ID; sign-in happens in the cloud. Simplest and most resilient; recommended default.
- **Pass-through authentication (PTA)**: Entra ID checks the password against on-premises DCs through agents. Sign-in fails if the agents or DCs are down.
- **Federation (AD FS)**: sign-in is redirected to on-premises AD FS. Most complex; most organizations are moving away from it.
- Entra Connect Sync or Entra Cloud Sync does the synchronization.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Head office DCs are down. Which model still lets users sign in to Microsoft 365?
> Password hash sync, because authentication happens in Entra ID.

> [!question]- Why is PHS recommended even alongside federation?
> It's a fallback if federation fails and it enables leaked-credential detection.

## See also

[[Microsoft Entra Connect]] · [[Entra Cloud Sync]] · [[AD FS]] · [[Microsoft Entra ID]]
