---
type: "tool"
level: "Mid"
category: "[[Monitoring & Observability]]"
subcategory: "[[Network monitoring]]"
vendor: "[[Auvik]]"
deployment: "SaaS with on-site collector"
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

# Auvik

> [!abstract] In plain words
> A cloud tool that automatically discovers a client's network, draws a map of it, and backs up switch and firewall settings.
>
> **What kind of tool is this?** Network monitoring tools keep checking routers, switches, firewalls and servers over the network and alert you when something stops answering or gets overloaded.

**Made by:** [[Auvik]] · **Runs:** SaaS with on-site collector · **Category:** [[Monitoring & Observability]] › [[Network monitoring]]

> [!info]+ Words on this page
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **MSP**: Managed service provider: a company that runs IT for other companies.
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **SNMP**: A protocol monitoring tools use to read status from network devices.
> **router**: Device that connects one network to another, such as the office to the internet.
> **subnet**: A range of IP addresses that form one network segment.
> *More in the [[Glossary]].*

## In more detail

Cloud network management popular with MSPs: automatic discovery and topology maps, device monitoring, config backup for network gear and flow analysis.

## Main parts

- Collector (Windows, Linux or VM) at each site
- Automatic discovery and topology maps
- Network config backup and change detection
- TrafficInsights (flow)
- Alerts

## Alerts you'll see

- Device offline
- Interface down or errors
- Collector offline
- Config change detected

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Collector offline | Check the collector host or VM is up and has outbound internet |
| Device not discovered | Check SNMP credentials and that the collector can reach the device's subnet |

## See also

[[SNMP]] · [[NetFlow, sFlow & IPFIX]] · [[Interface errors and packet loss]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
