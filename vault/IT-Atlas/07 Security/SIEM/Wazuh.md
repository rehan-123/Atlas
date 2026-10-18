---
type: "tool"
level: "Mid"
category: "[[Security]]"
subcategory: "[[SIEM]]"
vendor: "[[Wazuh]]"
deployment: "Self-hosted (open source) or cloud"
status: "current"
aliases: []
tags:
  - "tool"
  - "security"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Wazuh

> [!abstract] In plain words
> A free, open-source security monitoring platform with agents.
>
> **What kind of tool is this?** A SIEM collects security logs from everywhere and looks for patterns that mean an attack.

**Made by:** [[Wazuh]] · **Runs:** Self-hosted (open source) or cloud · **Category:** [[Security]] › [[SIEM]]

> [!info]+ Words on this page
> **SIEM**: A system that collects security logs from everywhere and looks for attacks.
> **TCP**: A connection-based network protocol that confirms delivery.
> **API**: A way for programs and scripts to talk to a service directly, without the web page.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **vulnerability**: A weakness an attacker can use.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Open-source security platform (OSSEC fork): agents for log analysis, file integrity monitoring, vulnerability detection and compliance, with an OpenSearch-based dashboard.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 1514/TCP agent events
- 1515/TCP agent enrollment
- 55000/TCP API

## See also

[[Elastic Stack]] · [[Syslog]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
