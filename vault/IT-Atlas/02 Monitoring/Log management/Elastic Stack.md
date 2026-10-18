---
type: "tool"
level: "Mid"
category: "[[Monitoring & Observability]]"
subcategory: "[[Log management]]"
vendor: "[[Elastic]]"
deployment: "Self-hosted or Elastic Cloud"
status: "current"
aliases:
  - "ELK"
  - "Elasticsearch"
  - "Kibana"
tags:
  - "tool"
  - "monitoring"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Elastic Stack

> [!abstract] In plain words
> A set of tools (Elasticsearch, Kibana and others) for collecting and searching huge amounts of logs.
>
> **What kind of tool is this?** Log tools gather the logs from many systems into one searchable place, so you don't have to log in to each machine.

**Made by:** [[Elastic]] · **Runs:** Self-hosted or Elastic Cloud · **Category:** [[Monitoring & Observability]] › [[Log management]]

> [!info]+ Words on this page
> **SIEM**: A system that collects security logs from everywhere and looks for attacks.
> **TCP**: A connection-based network protocol that confirms delivery.
> **HTTP**: The protocol web pages use (port 80, unencrypted).
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Elasticsearch, Logstash, Kibana and Beats or Elastic Agent: search and analytics for logs and metrics, also used as a SIEM.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 9200/TCP Elasticsearch HTTP
- 5601/TCP Kibana
- 5044/TCP Logstash Beats input

## See also

[[Graylog]] · [[Syslog]] · [[Grafana]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
