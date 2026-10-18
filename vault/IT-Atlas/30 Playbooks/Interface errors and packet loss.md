---
type: "playbook"
level: "Mid"
severity: "P3"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Interface errors and packet loss

> [!abstract] What this alert means
> A network port is seeing damaged or dropped traffic.
>
> **Why it matters:** Connections become slow and unreliable; often it's just a bad cable.

**How urgent:** P3. See [[Severity levels]].

> [!info]+ Words on this page
> **NIC**: Network interface card: a computer's network adapter.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **uplink**: The connection from a switch or site up to the next level of the network.
> *More in the [[Glossary]].*

## You'll see this when

- CRC or input errors increasing
- Loss reported by monitoring
- Interface flapping

## First 5 minutes

1. Check whether errors are still increasing (clear counters and recheck)
2. Check both ends of the link

## Find the cause

- CRC errors: cable, patch lead, optic or duplex mismatch
- Discards: congestion
- Flapping: bad cable, failing NIC or power-saving on the endpoint

## Fix it

- Replace the cable or optic
- Hard-set or correct speed and duplex
- Move to another port to isolate

## Ask for help (escalate) when

- Uplink or core link affected
- Errors continue after replacing cabling

## Write it up

Copy this into the ticket and fill it in:

```
Device / port: 
Counters: 
Cause: 
Action:
```

## See also

[[Cisco Catalyst]] · [[Auvik]] · [[ICMP]] · [[High latency]]
