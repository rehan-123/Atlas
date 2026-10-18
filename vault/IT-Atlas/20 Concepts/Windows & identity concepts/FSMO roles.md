---
type: "concept"
level: "Mid"
category: "[[Windows & identity concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# FSMO roles

> [!abstract] In one line
> Five single-master roles in Active Directory.

> [!tip] Think of it like
> Five special jobs in Active Directory that only one domain controller can do at a time.

> [!info]+ Words on this page
> **DC**: Domain controller: a server running Active Directory.
> **domain controller**: A server running Active Directory that checks logins.
> *More in the [[Glossary]].*

## How it works

- Forest-wide: Schema Master, Domain Naming Master.
- Domain-wide: PDC Emulator (time source, password changes, lockouts), RID Master (hands out RID pools), Infrastructure Master.
- `netdom query fsmo` lists holders. Transfer roles from a healthy DC; seize only when the holder is gone for good.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Which role is the domain's time source and handles lockouts?
> The PDC emulator.

## See also

[[Active Directory]] · [[NTP]]
