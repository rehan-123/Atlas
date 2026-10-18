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

# NTLM

> [!abstract] In one line
> Legacy challenge-response authentication, used when Kerberos cannot be (IP addresses, workgroups, some old apps).

> [!tip] Think of it like
> NTLM is the older, weaker way Windows checks passwords, used when Kerberos can't be.

> [!info]+ Words on this page
> **DC**: Domain controller: a server running Active Directory.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> *More in the [[Glossary]].*

## How it works

- Weaker than Kerberos and abused in relay attacks. Microsoft is phasing it out; audit before blocking.
- Security event 4776 logs NTLM validation on DCs.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- When does Windows fall back to NTLM?
> When you connect by IP address instead of name, in workgroups, or with old apps.

## See also

[[Kerberos]] · [[Active Directory]]
