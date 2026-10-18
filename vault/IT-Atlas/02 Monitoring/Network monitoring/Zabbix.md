---
type: "tool"
level: "Mid"
category: "[[Monitoring & Observability]]"
subcategory: "[[Network monitoring]]"
vendor: "[[Zabbix]]"
deployment: "Self-hosted (open source)"
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

# Zabbix

> [!abstract] In plain words
> A free, open-source monitoring system that can watch almost anything.
>
> **What kind of tool is this?** Network monitoring tools keep checking routers, switches, firewalls and servers over the network and alert you when something stops answering or gets overloaded.

**Made by:** [[Zabbix]] · **Runs:** Self-hosted (open source) · **Category:** [[Monitoring & Observability]] › [[Network monitoring]]

> [!info]+ Words on this page
> **SNMP**: A protocol monitoring tools use to read status from network devices.
> **HTTP**: The protocol web pages use (port 80, unencrypted).
> **TCP**: A connection-based network protocol that confirms delivery.
> **router**: Device that connects one network to another, such as the office to the internet.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **proxy**: A middleman server that passes traffic on, for web filtering or to do work for a central server.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Open-source enterprise monitoring: agents, SNMP, IPMI and HTTP checks, templates, triggers and proxies for remote sites.

## Main parts

- Zabbix server and database
- Zabbix agent / agent 2
- Zabbix proxy for remote sites
- Templates, items, triggers and actions
- Frontend (PHP)

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 10050/TCP server or proxy polls agent (passive checks)
- 10051/TCP agent or proxy sends to server (active checks, trapper)

## Alerts you'll see

- Trigger problems
- Agent unavailable
- Proxy not seen
- Queue growing

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Agent unavailable | Test 10050/TCP from server to host; check Server= and ServerActive= in the agent config |
| Values not arriving | Check the queue in the frontend and the proxy's last seen time |

## Where to find its logs

- `/var/log/zabbix/zabbix_server.log`
- `/var/log/zabbix/zabbix_agentd.log`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
zabbix_get -s HOST -k agent.ping
systemctl status zabbix-server zabbix-agent2
```

## See also

[[SNMP]] · [[Grafana]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
