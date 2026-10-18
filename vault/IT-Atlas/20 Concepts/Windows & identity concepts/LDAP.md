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

# LDAP

> [!abstract] In one line
> Lightweight Directory Access Protocol: how apps query and bind to Active Directory.

> [!tip] Think of it like
> LDAP is how apps look things up in Active Directory, like querying a phone book of users and groups.

## How it works

- 389 (LDAP), 636 (LDAPS), 3268 and 3269 (Global Catalog).
- Require LDAP signing and channel binding; apps doing simple binds over 389 send passwords in clear text.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Which port is LDAP over TLS?
> 636 (plain LDAP is 389).

## See also

[[Active Directory]] · [[Kerberos]]
