---
type: "tool"
level: "Mid"
category: "[[Monitoring & Observability]]"
subcategory: "[[Network monitoring]]"
vendor: "[[Paessler]]"
deployment: "On-prem (PRTG Hosted Monitor in cloud)"
status: "current"
agent_service: "PRTG Core Server Service, PRTG Probe Service"
aliases:
  - "PRTG"
tags:
  - "tool"
  - "monitoring"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# PRTG Network Monitor

> [!abstract] In plain words
> Monitoring software you install on a Windows server. Each thing it checks (a ping, a disk, a website) is a 'sensor', and you pay by the number of sensors.
>
> **What kind of tool is this?** Network monitoring tools keep checking routers, switches, firewalls and servers over the network and alert you when something stops answering or gets overloaded.

**Made by:** [[Paessler]] · **Runs:** On-prem (PRTG Hosted Monitor in cloud) · **Category:** [[Monitoring & Observability]] › [[Network monitoring]]

> [!info]+ Words on this page
> **SNMP**: A protocol monitoring tools use to read status from network devices.
> **WMI**: Windows Management Instrumentation: lets tools query Windows for information.
> **HTTP**: The protocol web pages use (port 80, unencrypted).
> **TCP**: A connection-based network protocol that confirms delivery.
> **RPC**: Remote procedure call: how Windows machines ask each other to do things (uses port 135 and high ports).
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **ping**: A quick test that sends a small message to a device and waits for a reply.
> **router**: Device that connects one network to another, such as the office to the internet.
> *More in the [[Glossary]].*

## In more detail

Sensor-based monitoring for networks, servers and applications using ping, SNMP, WMI, HTTP, flow and more. Licensed by number of sensors.

## Main parts

- Core server (web UI, database, notifications)
- Local and remote probes
- Sensors and channels
- Notification triggers
- Maps and dashboards

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`PRTG Core Server Service, PRTG Probe Service`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 443/TCP (or 80) web interface
- 23560/TCP remote probe to core server

## Alerts you'll see

- Sensor down or warning
- Remote probe disconnected
- License sensor limit reached

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Remote probe disconnected | Check the PRTG Probe Service on the probe host and that 23560/TCP reaches the core |
| WMI sensors failing | Check credentials, Windows Firewall rules for WMI and RPC, and DCOM permissions |
| SNMP sensors failing | Check community or SNMPv3 credentials and that the device allows the probe IP |

## Where to find its logs

- `C:\ProgramData\Paessler\PRTG Network Monitor\Logs`

## See also

[[SNMP]] · [[WMI]] · [[NetFlow, sFlow & IPFIX]] · [[ICMP]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
