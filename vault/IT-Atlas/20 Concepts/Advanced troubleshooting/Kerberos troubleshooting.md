---
type: "concept"
level: "Senior"
category: "[[Advanced troubleshooting]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Kerberos troubleshooting

> [!abstract] In one line
> Finding why Kerberos sign-ins fail: time, names (SPNs), tickets and encryption types.

> [!tip] Think of it like
> A festival wristband system: wrong date on your watch, or two stages with the same name, and the staff won't let you in.

> [!info]+ Words on this page
> **SPN**: Service principal name: the name Kerberos uses to find which account runs a service.
> **DC**: Domain controller: a server running Active Directory.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> *More in the [[Glossary]].*

## How it works

- Check time first: more than 5 minutes of skew breaks Kerberos.
- `klist` shows the user's tickets; `klist purge` clears them to retry.
- **Duplicate or missing SPNs** cause failures for services: `setspn -Q HTTP/server` and `setspn -X` to find duplicates.
- Event 4771 (pre-auth failed) and 4769 (service ticket) on DCs; System log events for KDC errors.
- Accessing by IP address falls back to NTLM: use the DNS name.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Which command finds duplicate SPNs in the domain?
> setspn -X

> [!question]- Why does browsing to \\10.0.0.5\share use NTLM instead of Kerberos?
> Kerberos needs a service name to look up an SPN; an IP address has none, so Windows falls back to NTLM.

## See also

[[Kerberos]] · [[NTP]] · [[Kerberos authentication failures]] · [[NTLM]]
