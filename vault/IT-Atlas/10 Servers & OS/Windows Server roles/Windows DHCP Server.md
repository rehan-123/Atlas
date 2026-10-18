---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Windows Server roles]]"
vendor: "[[Microsoft]]"
deployment: "Windows Server role"
status: "current"
agent_service: "DHCPServer"
aliases: []
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows DHCP Server

> [!abstract] In plain words
> The DHCP service on Windows servers. It hands out IP addresses automatically to devices on the network.
>
> **What kind of tool is this?** Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

**Made by:** [[Microsoft]] · **Runs:** Windows Server role · **Category:** [[Servers & Operating Systems]] › [[Windows Server roles]]

> [!info]+ Words on this page
> **DHCP**: The service that hands out IP addresses to devices automatically.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **VLAN**: A virtual network that separates traffic on the same physical switches.
> **failover**: Automatically switching to a backup system when the main one fails.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

The Windows DHCP role: scopes, reservations, options and DHCP failover (load balance or hot standby) between two servers.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`DHCPServer`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 67/UDP server
- 68/UDP client

## Alerts you'll see

- Scope nearly full or exhausted
- Failover partner down or out of sync
- Rogue DHCP server detected
- Service not authorized in AD

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Scope full | Get-DhcpServerv4ScopeStatistics; shorten the lease time, clean up stale leases or extend the range |
| Clients get 169.254 addresses | Check the DHCP service, the IP helper or relay on the client VLAN, and scope free addresses |

## Where to find its logs

- Event Viewer: Microsoft > Windows > DHCP-Server
- `C:\Windows\System32\dhcp (DhcpSrvLog-*.log audit logs)`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-DhcpServerv4Scope
Get-DhcpServerv4ScopeStatistics
Get-DhcpServerv4Failover
Get-DhcpServerInDC
```

## See also

[[DHCP]] · [[DHCP scope exhausted]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
