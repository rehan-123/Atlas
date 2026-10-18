---
type: "concept"
level: "Junior"
category: "[[Networking concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# DNS

> [!abstract] In one line
> Turns names into IP addresses. When DNS breaks, it looks like everything is broken.

> [!tip] Think of it like
> DNS is the phone book of the network: you look up a name and get back a number (the IP address).

> [!info]+ Words on this page
> **SPF**: A DNS record listing which servers may send email for a domain.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> *More in the [[Glossary]].*

## How it works

- Record types: A and AAAA (address), CNAME (alias), MX (mail), TXT (SPF, verification), SRV (AD services such as `_ldap._tcp.dc._msdcs`), PTR (reverse), NS and SOA.
- Domain-joined machines must use only internal DNS servers. Adding 8.8.8.8 as secondary DNS causes random AD failures.
- TTL controls how long answers are cached. Lower it before a migration, not during.
- Tools: `Resolve-DnsName`, `nslookup`, `dig`. Always test against a specific server to isolate the problem.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why must domain-joined PCs use only the internal DNS servers?
> Because only internal DNS knows where the domain controllers are. Public DNS like 8.8.8.8 can't find them, so logins and Group Policy fail randomly.

> [!question]- Which command tests DNS against one specific server?
> Resolve-DnsName NAME -Server SERVER (or nslookup NAME SERVER).

## See also

[[Windows DNS Server]] · [[DNS resolution failure]] · [[Active Directory]] · [[Cloudflare DNS]] · [[Cisco Umbrella]]
