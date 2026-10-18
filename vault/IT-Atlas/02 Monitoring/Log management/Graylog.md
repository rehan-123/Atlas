---
type: "tool"
level: "Mid"
category: "[[Monitoring & Observability]]"
subcategory: "[[Log management]]"
vendor: "[[Graylog]]"
deployment: "Self-hosted or cloud"
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

# Graylog

> [!abstract] In plain words
> A tool that collects logs from many systems so you can search them in one place.
>
> **What kind of tool is this?** Log tools gather the logs from many systems into one searchable place, so you don't have to log in to each machine.

**Made by:** [[Graylog]] · **Runs:** Self-hosted or cloud · **Category:** [[Monitoring & Observability]] › [[Log management]]

> [!info]+ Words on this page
> **TCP**: A connection-based network protocol that confirms delivery.
> **pipeline**: A series of automated steps (test, build, deploy) that run on every change.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Centralized log management with inputs for syslog, GELF and Beats, streams, pipelines and alerting. Built on OpenSearch or Elasticsearch plus MongoDB.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 9000/TCP web UI (default)

## See also

[[Syslog]] · [[Elastic Stack]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
