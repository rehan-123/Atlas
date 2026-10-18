---
type: "tool"
level: "Mid"
category: "[[Monitoring & Observability]]"
subcategory: "[[Infrastructure & APM]]"
vendor: "[[Grafana Labs]]"
deployment: "Self-hosted or Grafana Cloud"
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

# Grafana

> [!abstract] In plain words
> Makes dashboards and graphs from many data sources. Often the big screen on a NOC wall.
>
> **What kind of tool is this?** These tools collect numbers (CPU, memory, response times) from servers, apps and cloud services and draw them as graphs, so you can spot trouble before users notice.

**Made by:** [[Grafana Labs]] · **Runs:** Self-hosted or Grafana Cloud · **Category:** [[Monitoring & Observability]] › [[Infrastructure & APM]]

> [!info]+ Words on this page
> **NOC**: Network operations center: the team that monitors and fixes infrastructure.
> **CPU**: The processor, the part of a computer that does the calculations.
> **SQL**: Structured Query Language; also short for Microsoft SQL Server.
> **TCP**: A connection-based network protocol that confirms delivery.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Dashboards and alerting over many data sources (Prometheus, Zabbix, Elasticsearch, SQL, cloud monitors). The usual NOC wallboard.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 3000/TCP web UI

## See also

[[Prometheus]] · [[Zabbix]] · [[Elastic Stack]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
