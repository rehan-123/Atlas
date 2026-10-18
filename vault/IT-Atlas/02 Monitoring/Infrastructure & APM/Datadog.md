---
type: "tool"
level: "Mid"
category: "[[Monitoring & Observability]]"
subcategory: "[[Infrastructure & APM]]"
vendor: "[[Datadog]]"
deployment: "SaaS"
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

# Datadog

> [!abstract] In plain words
> A cloud monitoring service used by many software companies for servers, apps and logs.
>
> **What kind of tool is this?** These tools collect numbers (CPU, memory, response times) from servers, apps and cloud services and draw them as graphs, so you can spot trouble before users notice.

**Made by:** [[Datadog]] · **Runs:** SaaS · **Category:** [[Monitoring & Observability]] › [[Infrastructure & APM]]

> [!info]+ Words on this page
> **CPU**: The processor, the part of a computer that does the calculations.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **TCP**: A connection-based network protocol that confirms delivery.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

SaaS observability: infrastructure metrics, APM traces, logs, synthetics and security from one agent and many integrations.

## Main parts

- Datadog Agent
- Integrations
- Monitors and dashboards
- APM and log management

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 8125/UDP DogStatsD on the agent
- 443/TCP outbound to Datadog

## See also

[[Prometheus]] · [[Grafana]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
