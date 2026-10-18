---
type: "tool"
level: "Mid"
category: "[[Monitoring & Observability]]"
subcategory: "[[Network monitoring]]"
vendor: "[[Checkmk]]"
deployment: "Self-hosted or SaaS"
status: "current"
aliases: []
tags:
  - "tool"
  - "monitoring"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Checkmk

> [!abstract] In plain words
> An open-source monitoring tool, descended from Nagios, that discovers what to monitor automatically.
>
> **What kind of tool is this?** Network monitoring tools keep checking routers, switches, firewalls and servers over the network and alert you when something stops answering or gets overloaded.

**Made by:** [[Checkmk]] · **Runs:** Self-hosted or SaaS · **Category:** [[Monitoring & Observability]] › [[Network monitoring]]

> [!info]+ Words on this page
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **SNMP**: A protocol monitoring tools use to read status from network devices.
> **TCP**: A connection-based network protocol that confirms delivery.
> **router**: Device that connects one network to another, such as the office to the internet.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Monitoring platform with roots in Nagios: auto-discovery of services, agents for Windows and Linux, SNMP and rule-based configuration.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 6556/TCP Checkmk agent

## See also

[[Nagios]] · [[SNMP]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
