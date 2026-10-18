---
type: "moc"
level: "All"
tags:
  - "moc"
  - "monitoring"
created: "2026-10-18"
updated: "2026-10-18"
---

# Network monitoring

> [!abstract] In plain words
> Network monitoring tools keep checking routers, switches, firewalls and servers over the network and alert you when something stops answering or gets overloaded.

Part of [[Monitoring & Observability]].

- [[PRTG Network Monitor]]: Monitoring software you install on a Windows server. Each thing it checks (a ping, a disk, a website) is a 'sensor', and you pay by the number of sensors.
- [[SolarWinds NPM]]: A large, well-known network monitoring product. Also famous as the target of a major 2020 hack.
- [[Auvik]]: A cloud tool that automatically discovers a client's network, draws a map of it, and backs up switch and firewall settings.
- [[Zabbix]]: A free, open-source monitoring system that can watch almost anything.
- [[Nagios]]: One of the oldest open-source monitoring tools. Many others copy its way of reporting OK, WARNING and CRITICAL.
- [[Checkmk]]: An open-source monitoring tool, descended from Nagios, that discovers what to monitor automatically.
- [[LibreNMS]]: A free tool that discovers and graphs network devices using SNMP.
- [[ManageEngine OpManager]]: ManageEngine's network and server monitoring tool.
- [[Domotz]]: Cloud network monitoring for MSPs, using a small box or agent at each site.
- [[WhatsUp Gold]]: A network monitoring tool from Progress that draws maps of your devices.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "02 Monitoring/Network monitoring"
WHERE type = "tool"
SORT file.name ASC
```
