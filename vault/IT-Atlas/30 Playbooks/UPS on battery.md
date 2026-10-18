---
type: "playbook"
level: "Junior"
severity: "P1 if runtime is low, otherwise P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# UPS on battery

> [!abstract] What this alert means
> The UPS has lost mains power and is running on battery.
>
> **Why it matters:** When the battery runs out, everything plugged into it switches off.

**How urgent:** P1 if runtime is low, otherwise P2. See [[Severity levels]].

> [!info]+ Words on this page
> **UPS**: Uninterruptible power supply: a big battery that keeps equipment running in a power cut.
> **hypervisor**: Software that runs virtual machines on a physical server.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- UPS reports on battery
- Low runtime warning

## First 5 minutes

1. Check remaining runtime
2. Check whether it is a site power cut (other UPSs, site devices offline) or one circuit
3. Confirm graceful shutdown is configured and working

## Find the cause

- Utility outage
- Tripped breaker or circuit
- UPS fault or failed self-test

## Fix it

- Contact the site to confirm power status
- If runtime will run out, shut down non-critical systems first, then hypervisors and storage in order

## Ask for help (escalate) when

- Runtime under 15 minutes with no power restoration
- Battery replacement needed

## Write it up

Copy this into the ticket and fill it in:

```
Site / UPS: 
On battery since: 
Runtime: 
Actions: 
Power restored at:
```

## See also

[[APC Smart-UPS]] · [[Eaton UPS]] · [[Environmental monitoring]] · [[Firewall WAN down]]
