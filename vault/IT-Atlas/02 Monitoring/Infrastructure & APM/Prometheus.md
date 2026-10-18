---
type: "tool"
level: "Mid"
category: "[[Monitoring & Observability]]"
subcategory: "[[Infrastructure & APM]]"
vendor:
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

# Prometheus

> [!abstract] In plain words
> A free tool that collects numbers (metrics) from servers and apps over time. Usually paired with Grafana for graphs.
>
> **What kind of tool is this?** These tools collect numbers (CPU, memory, response times) from servers, apps and cloud services and draw them as graphs, so you can spot trouble before users notice.

**Runs:** Self-hosted (open source) · **Category:** [[Monitoring & Observability]] › [[Infrastructure & APM]]

> [!info]+ Words on this page
> **CPU**: The processor, the part of a computer that does the calculations.
> **TCP**: A connection-based network protocol that confirms delivery.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Open-source pull-based metrics system with a time-series database, PromQL and Alertmanager. The standard for Kubernetes and cloud-native monitoring.

## Main parts

- Prometheus server (scrapes /metrics endpoints)
- Exporters (node_exporter, windows_exporter, snmp_exporter)
- Alertmanager
- PromQL

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 9090/TCP Prometheus
- 9093/TCP Alertmanager
- 9100/TCP node_exporter

## See also

[[Grafana]] · [[SNMP]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
