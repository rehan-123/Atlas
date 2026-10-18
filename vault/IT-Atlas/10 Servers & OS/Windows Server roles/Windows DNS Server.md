---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Windows Server roles]]"
vendor: "[[Microsoft]]"
deployment: "Windows Server role"
status: "current"
agent_service: "DNS"
aliases: []
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows DNS Server

> [!abstract] In plain words
> The DNS service on Windows servers (usually the domain controllers). It turns names into IP addresses for every PC in the domain.
>
> **What kind of tool is this?** Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

**Made by:** [[Microsoft]] · **Runs:** Windows Server role · **Category:** [[Servers & Operating Systems]] › [[Windows Server roles]]

> [!info]+ Words on this page
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **TCP**: A connection-based network protocol that confirms delivery.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **domain controller**: A server running Active Directory that checks logins.
> **forwarder**: Something that passes things on: a DNS forwarder sends lookups it can't answer to another DNS server; a log forwarder ships logs to a central system.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

The Windows DNS role, usually AD-integrated on domain controllers: zones, forwarders, conditional forwarders and scavenging.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`DNS`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 53/UDP and 53/TCP

## Alerts you'll see

- DNS service stopped
- Resolution failures for internal or external names
- Event 4013 (waiting for AD initial sync) at boot
- Stale records (no scavenging)

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| External names fail | Test the forwarders; check root hints and outbound 53 on the firewall |
| Internal names fail | Check the zone exists and is AD-integrated, and that the client points only at internal DNS |
| Wrong IP returned | Look for stale or duplicate records; enable scavenging carefully |

## Where to find its logs

- Event Viewer: Applications and Services Logs > DNS Server
- DNS debug logging (enable temporarily)

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Resolve-DnsName NAME -Server DC01
nslookup NAME DC01
Get-DnsServerForwarder
Get-DnsServerZone
Clear-DnsServerCache
ipconfig /flushdns
```

## See also

[[DNS]] · [[Active Directory]] · [[DNS resolution failure]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
