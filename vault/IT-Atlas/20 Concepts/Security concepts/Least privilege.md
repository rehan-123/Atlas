---
type: "concept"
level: "Junior"
category: "[[Security concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Least privilege

> [!abstract] In one line
> Give accounts and apps only the access they need, only when they need it.

> [!tip] Think of it like
> Give people the keys to the rooms they need, not the master key.

> [!info]+ Words on this page
> **LAPS**: A Windows feature that gives each PC its own rotating local admin password.
> **API**: A way for programs and scripts to talk to a service directly, without the web page.
> *More in the [[Glossary]].*

## How it works

- Separate admin accounts; no daily use of Domain Admin or Global Admin.
- Use LAPS for unique local admin passwords and just-in-time elevation where possible.
- Read-only API permissions for reporting tools.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why shouldn't you browse the web with a Domain Admin account?
> If that session is compromised, the attacker gets full control of the domain.

## See also

[[Windows LAPS]] · [[ThreatLocker]] · [[CyberArk]] · [[Zero Trust]]
