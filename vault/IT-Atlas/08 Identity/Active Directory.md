---
type: "tool"
level: "Mid"
category: "[[Identity & Access]]"
vendor: "[[Microsoft]]"
deployment: "On-prem Windows Server role"
status: "current"
aliases:
  - "AD"
  - "AD DS"
  - "Active Directory Domain Services"
tags:
  - "tool"
  - "identity"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Active Directory

> [!abstract] In plain words
> The on-site directory of users, computers and groups in a Windows domain. Domain controllers run it, and almost every login in the office depends on it.
>
> **What kind of tool is this?** Identity tools hold user accounts and decide who can sign in to what. When identity breaks, nobody can work.

**Made by:** [[Microsoft]] · **Runs:** On-prem Windows Server role · **Category:** [[Identity & Access]]

> [!info]+ Words on this page
> **FSMO**: Five special Active Directory roles that only one domain controller holds at a time.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **TCP**: A connection-based network protocol that confirms delivery.
> **RPC**: Remote procedure call: how Windows machines ask each other to do things (uses port 135 and high ports).
> **LDAP**: The protocol apps use to look up users and groups in a directory.
> **SMB**: The Windows file-sharing protocol (port 445).
> **DC**: Domain controller: a server running Active Directory.
> **DFS**: Distributed File System: gives shared folders one path and keeps copies in sync between servers.
> *More in the [[Glossary]].*

## In more detail

Active Directory Domain Services: domain controllers, users, computers, groups, Group Policy, sites and replication. The identity core of most on-prem estates.

## Main parts

- Domain controllers and global catalogs
- FSMO roles
- Sites and Services (replication topology)
- SYSVOL (replicated by DFS-R)
- DNS (usually AD-integrated)
- Group Policy

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 53 DNS
- 88 Kerberos
- 135/TCP RPC endpoint mapper plus 49152-65535 dynamic RPC
- 389 LDAP and 636 LDAPS
- 445/TCP SMB
- 464 Kerberos password change
- 3268 and 3269 Global Catalog

## Alerts you'll see

- Replication failures
- DC unreachable
- Account lockouts
- Privileged group changes
- Time sync drift on the PDC emulator

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Replication failing | repadmin /replsummary, then repadmin /showrepl on the failing DC; check DNS and RPC between DCs |
| Clients cannot find a DC | nltest /dsgetdc:DOMAIN and check the client's DNS servers point only at internal DNS |
| General health | Run dcdiag /e /q to show only errors |

## Where to find its logs

- Event Viewer: Directory Service, DFS Replication, DNS Server and System logs
- Security log on DCs (4740 lockouts, 4625 failed logons)

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
dcdiag /e /q
repadmin /replsummary
repadmin /showrepl
netdom query fsmo
nltest /dsgetdc:DOMAIN
Get-ADReplicationFailure -Target DC01
```

## See also

[[Kerberos]] · [[NTLM]] · [[LDAP]] · [[FSMO roles]] · [[Group Policy]] · [[Windows DNS Server]] · [[Microsoft Entra Connect]] · [[AD replication failure]] · [[Account lockout storm]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
