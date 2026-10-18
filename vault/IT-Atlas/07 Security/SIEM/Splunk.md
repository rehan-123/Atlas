---
type: "tool"
level: "Mid"
category: "[[Security]]"
subcategory: "[[SIEM]]"
vendor: "[[Cisco]]"
deployment: "On-prem or Splunk Cloud"
status: "current"
aliases:
  - "Splunk Enterprise Security"
tags:
  - "tool"
  - "security"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Splunk

> [!abstract] In plain words
> A powerful log search and security platform, now owned by Cisco.
>
> **What kind of tool is this?** A SIEM collects security logs from everywhere and looks for patterns that mean an attack.

**Made by:** [[Cisco]] · **Runs:** On-prem or Splunk Cloud · **Category:** [[Security]] › [[SIEM]]

> [!info]+ Words on this page
> **SIEM**: A system that collects security logs from everywhere and looks for attacks.
> **TCP**: A connection-based network protocol that confirms delivery.
> **forwarder**: Something that passes things on: a DNS forwarder sends lookups it can't answer to another DNS server; a log forwarder ships logs to a central system.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Log search and analytics with SPL; Enterprise Security is its SIEM. Cisco bought Splunk in 2024.

## Main parts

- Universal Forwarders
- Indexers
- Search heads
- SPL
- Enterprise Security app

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 9997/TCP forwarder to indexer
- 8000/TCP web UI
- 8089/TCP management

## See also

[[Elastic Stack]] · [[Microsoft Sentinel]] · [[Syslog]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
