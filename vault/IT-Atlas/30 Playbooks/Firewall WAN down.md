---
type: "playbook"
level: "Mid"
severity: "P1 (whole site) or P2 (one link with failover)"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Firewall WAN down

> [!abstract] What this alert means
> The firewall's internet link is down.
>
> **Why it matters:** The site may be offline, or running on its backup link.

**How urgent:** P1 (whole site) or P2 (one link with failover). See [[Severity levels]].

> [!info]+ Words on this page
> **WAN**: Wide area network: links between sites, or to the internet.
> **SD-WAN**: Smart use of several internet links, automatically picking the best one.
> **SLA**: Service level agreement: the response and fix times promised to a client. (On firewalls, an SD-WAN 'SLA' is a link-quality check.)
> **ISP**: Internet service provider.
> **UPS**: Uninterruptible power supply: a big battery that keeps equipment running in a power cut.
> **failover**: Automatically switching to a backup system when the main one fails.
> **modem**: Box that connects the building to the internet provider's line.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- WAN interface down
- SD-WAN SLA failing
- Site unreachable

## First 5 minutes

1. Check if failover worked (is the site up on a backup link?)
2. Check the ISP status page and circuit IDs
3. Check if the firewall itself is reachable on another path or through the console

## Find the cause

- Physical: link light on the ISP handoff, ONT or modem power
- ISP outage
- Firewall interface errors or misconfiguration after a change
- Power at the site (check UPS alerts)

## Fix it

- Open a ticket with the ISP with circuit ID and timestamps
- Ask on-site staff to power-cycle the modem or ONT
- Roll back a recent change

## Ask for help (escalate) when

- Whole site down
- Outage longer than 30 minutes

## Write it up

Copy this into the ticket and fill it in:

```
Site: 
Circuit / ISP: 
Down since: 
Failover worked: 
ISP ticket #: 
Restored at:
```

## See also

[[FortiGate]] · [[SD-WAN]] · [[UPS on battery]] · [[Agent offline]]
