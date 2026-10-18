---
type: "tool"
level: "Mid"
category: "[[Monitoring & Observability]]"
subcategory: "[[Network monitoring]]"
vendor: "[[Nagios]]"
deployment: "Self-hosted"
status: "current"
aliases:
  - "Nagios Core"
  - "Nagios XI"
tags:
  - "tool"
  - "monitoring"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Nagios

> [!abstract] In plain words
> One of the oldest open-source monitoring tools. Many others copy its way of reporting OK, WARNING and CRITICAL.
>
> **What kind of tool is this?** Network monitoring tools keep checking routers, switches, firewalls and servers over the network and alert you when something stops answering or gets overloaded.

**Made by:** [[Nagios]] · **Runs:** Self-hosted · **Category:** [[Monitoring & Observability]] › [[Network monitoring]]

> [!info]+ Words on this page
> **TCP**: A connection-based network protocol that confirms delivery.
> **router**: Device that connects one network to another, such as the office to the internet.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

The classic open-source host and service checker (Nagios Core; Nagios XI is the commercial edition). Its plugin exit-code standard is used by many other tools.

## Main parts

- Nagios Core scheduler
- Plugins (check_ping, check_disk, check_http)
- NRPE or NCPA agents on remote hosts
- Notifications and escalations

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 5666/TCP NRPE

## Good to know

- Plugin exit codes: 0 OK, 1 WARNING, 2 CRITICAL, 3 UNKNOWN. Checkmk, Icinga and others use the same convention.

## See also

[[Checkmk]] · [[Monitoring thresholds and baselines]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
