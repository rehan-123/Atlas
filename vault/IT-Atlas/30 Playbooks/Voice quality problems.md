---
type: "playbook"
level: "Mid"
severity: "P3"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Voice quality problems

> [!abstract] What this alert means
> Calls are choppy, one-way or dropping.
>
> **Why it matters:** Phones are business-critical for many clients.

**How urgent:** P3. See [[Severity levels]].

> [!info]+ Words on this page
> **WAN**: Wide area network: links between sites, or to the internet.
> **NAT**: Network address translation: many private devices sharing one public IP.
> **SIP**: The protocol that sets up internet phone calls.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **ISP**: Internet service provider.
> **latency**: Delay: how long data takes to get from A to B.
> **jitter**: How much delay varies from packet to packet. Bad for voice and video.
> **uplink**: The connection from a switch or site up to the next level of the network.
> *More in the [[Glossary]].*

## You'll see this when

- Choppy audio, one-way audio, dropped calls

## First 5 minutes

1. Get call examples with times
2. Check WAN utilization, latency, jitter and loss at those times

## Find the cause

- One-way audio: NAT or SIP ALG
- Choppy: jitter or loss, often a saturated uplink
- Drops at around 30 seconds or 15 minutes: SIP session timers or NAT timeouts

## Fix it

- Disable SIP ALG
- Apply QoS and shape bulk traffic
- Adjust firewall UDP timeouts

## Ask for help (escalate) when

- Persistent ISP issues
- Many users affected

## Write it up

Copy this into the ticket and fill it in:

```
Calls / times: 
Metrics: 
Cause: 
Action:
```

## See also

[[SIP]] · [[QoS]] · [[High latency]] · [[3CX]]
