---
type: "moc"
level: "All"
tags:
  - "moc"
  - "monitoring"
created: "2026-10-18"
updated: "2026-10-18"
---

# Monitoring & Observability

Everything that watches infrastructure from outside or inside: network monitoring, metrics and APM, uptime checks, alert routing and log platforms.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Monitor services and user outcomes, not just devices: a green server with a dead app is still an outage.
> - Every alert needs an owner, a threshold based on baselines and a playbook; delete alerts nobody acts on.
> - Correlate: one site outage should be one incident, not 300 alerts.
> - Keep monitoring independent of what it monitors (external uptime checks, out-of-band alerts).

## [[Network monitoring]]

Network monitoring tools keep checking routers, switches, firewalls and servers over the network and alert you when something stops answering or gets overloaded.

- [[PRTG Network Monitor]]
- [[SolarWinds NPM]]
- [[Auvik]]
- [[Zabbix]]
- [[Nagios]]
- [[Checkmk]]
- [[LibreNMS]]
- [[ManageEngine OpManager]]
- [[Domotz]]
- [[WhatsUp Gold]]

## [[Infrastructure & APM]]

These tools collect numbers (CPU, memory, response times) from servers, apps and cloud services and draw them as graphs, so you can spot trouble before users notice.

- [[LogicMonitor]]
- [[Datadog]]
- [[Prometheus]]
- [[Grafana]]
- [[New Relic]]
- [[Dynatrace]]
- [[Azure Monitor]]
- [[Amazon CloudWatch]]

## [[Uptime monitoring]]

Uptime monitors check from the outside, like a customer would, that a website or service still answers.

- [[Uptime Kuma]]
- [[UptimeRobot]]
- [[Pingdom]]
- [[Better Stack]]

## [[Alerting & on-call]]

On-call tools decide who gets woken up for an alert, and keep paging until someone responds.

- [[PagerDuty]]
- [[Opsgenie]]
- [[Splunk On-Call]]

## [[Log management]]

Log tools gather the logs from many systems into one searchable place, so you don't have to log in to each machine.

- [[Elastic Stack]]
- [[Graylog]]

## Playbooks for this area

[[Azure VM unreachable]] · [[Interface errors and packet loss]] · [[Website down]]

## Database view

```dataview
TABLE vendor, subcategory, deployment, status, agent_service AS "Agent"
FROM "02 Monitoring"
WHERE type = "tool"
SORT subcategory ASC, file.name ASC
```
