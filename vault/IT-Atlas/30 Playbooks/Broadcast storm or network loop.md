---
type: "playbook"
level: "Senior"
severity: "P1"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Broadcast storm or network loop

> [!abstract] What this alert means
> Traffic is looping endlessly between switches, flooding the network until it slows to a halt.
>
> **Why it matters:** A loop can take down an entire site in seconds: phones, Wi-Fi and servers all stop.

**How urgent:** P1. See [[Severity levels]].

> [!info]+ Words on this page
> **CPU**: The processor, the part of a computer that does the calculations.
> **Wi-Fi**: Wireless network connection using radio signals.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **uplink**: The connection from a switch or site up to the next level of the network.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Whole site suddenly slow or down
- Switch CPU at 100% and port lights flashing together
- MAC flapping messages in switch logs

## First 5 minutes

1. Check switch logs for MAC flapping and STP topology changes
2. Find the ports with huge broadcast/multicast counters
3. Ask what was plugged in recently (a new desk switch, a cable between two wall ports, a VoIP phone daisy-chain)

## Find the cause

- Spanning Tree disabled or misconfigured
- Unmanaged mini-switch creating a loop
- Two uplinks without link aggregation or STP blocking

## Fix it

- Shut the looping port
- Re-enable Spanning Tree (RSTP/MSTP) everywhere; enable BPDU guard on access ports and storm control
- Remove unmanaged switches from user desks

## Ask for help (escalate) when

- The loop can't be found within 15 minutes
- Core switches affected

## Write it up

Copy this into the ticket and fill it in:

```
Site: 
Symptoms: 
Port/device causing loop: 
Action: 
Prevention (BPDU guard / storm control):
```

## See also

[[Spanning Tree]] · [[Interface errors and packet loss]] · [[Cisco Catalyst]] · [[High latency]]
