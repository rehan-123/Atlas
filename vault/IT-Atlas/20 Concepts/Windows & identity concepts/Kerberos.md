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

# Kerberos

> [!abstract] In one line
> Active Directory's default authentication protocol, using tickets from the KDC on domain controllers.

> [!tip] Think of it like
> Kerberos is a ticket booth: you show ID once at login and get a ticket, then show tickets (not your password) to each service.

> [!info]+ Words on this page
> **SPN**: Service principal name: the name Kerberos uses to find which account runs a service.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **domain controller**: A server running Active Directory that checks logins.
> *More in the [[Glossary]].*

## How it works

- Port 88. TGT (ticket-granting ticket) at logon, then service tickets per service (SPN).
- Breaks on clock skew over 5 minutes, duplicate or missing SPNs, and DNS problems.
- `klist` shows tickets; `klist purge` clears them.
- Security events: 4768 (TGT requested), 4769 (service ticket), 4771 (pre-authentication failed).

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Name two things that commonly break Kerberos.
> Clock differences over 5 minutes, and DNS problems (also duplicate or missing SPNs).

## See also

[[Active Directory]] · [[NTLM]] · [[NTP]] · [[LDAP]]
