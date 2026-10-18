---
type: "concept"
level: "Junior"
category: "[[IT basics]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Domain-joined vs cloud-joined PCs

> [!abstract] In one line
> How a business PC is tied to the company: to on-premises Active Directory, to Entra ID in the cloud, or both.

> [!tip] Think of it like
> A staff card from head office's filing room (AD) versus one checked online from anywhere (Entra ID). Some companies issue both.

> [!info]+ Words on this page
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **domain controller**: A server running Active Directory that checks logins.
> *More in the [[Glossary]].*

## How it works

- **Domain-joined**: signs in against Active Directory domain controllers; Group Policy applies.
- **Entra joined**: signs in against Microsoft Entra ID; managed by Intune; no office connection needed.
- **Hybrid joined**: both at once.
- `dsregcmd /status` shows which one a PC is.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Which command shows whether a PC is Entra joined, domain joined or both?
> `dsregcmd /status`.

## See also

[[Active Directory]] · [[Microsoft Entra ID]] · [[Microsoft Intune]] · [[Trust relationship failed]]
