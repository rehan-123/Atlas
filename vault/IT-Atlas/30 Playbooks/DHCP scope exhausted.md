---
type: "playbook"
level: "Mid"
severity: "P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# DHCP scope exhausted

> [!abstract] What this alert means
> The pool of IP addresses to hand out has run out.
>
> **Why it matters:** New devices can't join the network.

**How urgent:** P2. See [[Severity levels]].

> [!info]+ Words on this page
> **DHCP**: The service that hands out IP addresses to devices automatically.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **subnet**: A range of IP addresses that form one network segment.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Scope over 90% used
- Clients getting 169.254 addresses

## First 5 minutes

1. Check scope statistics and which devices hold leases
2. Check for a rogue DHCP server

## Find the cause

- Guest or IoT growth
- Lease time too long
- A device requesting many leases (misconfigured or malicious)

## Fix it

- Shorten lease time
- Remove stale leases
- Extend the scope or move the client group to a larger subnet

## Ask for help (escalate) when

- Production users unable to connect

## Write it up

Copy this into the ticket and fill it in:

```
Scope: 
Usage: 
Cause: 
Action:
```

## See also

[[DHCP]] · [[Windows DHCP Server]] · [[Subnetting & CIDR]]
