---
type: "tool"
level: "Mid"
category: "[[Monitoring & Observability]]"
subcategory: "[[Network monitoring]]"
vendor: "[[SolarWinds]]"
deployment: "On-prem"
status: "current"
aliases:
  - "Orion"
  - "SolarWinds Platform"
  - "Network Performance Monitor"
tags:
  - "tool"
  - "monitoring"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# SolarWinds NPM

> [!abstract] In plain words
> A large, well-known network monitoring product. Also famous as the target of a major 2020 hack.
>
> **What kind of tool is this?** Network monitoring tools keep checking routers, switches, firewalls and servers over the network and alert you when something stops answering or gets overloaded.

**Made by:** [[SolarWinds]] · **Runs:** On-prem · **Category:** [[Monitoring & Observability]] › [[Network monitoring]]

> [!info]+ Words on this page
> **SNMP**: A protocol monitoring tools use to read status from network devices.
> **WMI**: Windows Management Instrumentation: lets tools query Windows for information.
> **SQL**: Structured Query Language; also short for Microsoft SQL Server.
> **router**: Device that connects one network to another, such as the office to the internet.
> *More in the [[Glossary]].*

## In more detail

Network Performance Monitor on the SolarWinds Platform (formerly Orion): ICMP, SNMP and WMI polling, NetPath, topology and alerting for large networks.

## Main parts

- Main polling engine and additional pollers
- SQL Server database
- Modules (NPM, SAM, NTA, NCM)
- Alerts and reports

## Alerts you'll see

- Node down
- Interface down or high utilization
- Poller status

## Good to know

- 2020 SUNBURST: attackers trojanized Orion updates, compromising thousands of organizations. It is the textbook software supply-chain attack.

## See also

[[SNMP]] · [[NetFlow, sFlow & IPFIX]] · [[ICMP]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
