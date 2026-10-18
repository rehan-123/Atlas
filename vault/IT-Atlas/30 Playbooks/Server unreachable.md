---
type: "playbook"
level: "Mid"
severity: "P1 or P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Server unreachable

> [!abstract] What this alert means
> Monitoring can't reach the server at all: ping and checks are failing.
>
> **Why it matters:** Users probably can't use whatever runs on it.

**How urgent:** P1 or P2. See [[Severity levels]].

> [!info]+ Words on this page
> **BSOD**: Blue screen of death: Windows crashed.
> **NIC**: Network interface card: a computer's network adapter.
> **VLAN**: A virtual network that separates traffic on the same physical switches.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **SQL**: Structured Query Language; also short for Microsoft SQL Server.
> **ping**: A quick test that sends a small message to a device and waits for a reply.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **hypervisor**: Software that runs virtual machines on a physical server.
> *More in the [[Glossary]].*

## You'll see this when

- Ping or host check failing
- Multiple services on one server alerting at once

## First 5 minutes

1. Confirm from two places (monitoring and your own ping or port check)
2. Check if the hypervisor host, switch or site is also down
3. Open the console (hypervisor, iDRAC or iLO) to see the screen: BSOD, hung, boot loop or powered off

## Find the cause

- Powered off or crashed: read the System log after boot for events 41, 6008 and 1001 (bugcheck)
- Up but no network: check the NIC, VLAN and IP configuration from the console
- Hung: check memory and disk on the hypervisor, or a stuck backup snapshot

## Fix it

- Power on or reset from the console after capturing what is on screen
- Fix network configuration from the console
- Free disk space if the system volume is full

## Ask for help (escalate) when

- Domain controller, file, SQL or hypervisor host down for more than 10 minutes
- Hardware fault in the out-of-band logs
- Repeated crashes

## Write it up

Copy this into the ticket and fill it in:

```
Server: 
Down since: 
Console showed: 
Root cause (if known): 
Action: 
Services verified after recovery:
```

## See also

[[ICMP]] · [[Hypervisor host disconnected]] · [[Dell iDRAC]] · [[HPE iLO]] · [[Windows Event ID reference]]
