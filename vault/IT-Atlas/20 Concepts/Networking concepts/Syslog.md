---
type: "concept"
level: "Mid"
category: "[[Networking concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Syslog

> [!abstract] In one line
> The standard way network devices and Linux systems send log messages to a collector.

> [!tip] Think of it like
> Syslog is a shared diary: firewalls, switches and Linux servers all send their log lines to one place.

> [!info]+ Words on this page
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **TCP**: A connection-based network protocol that confirms delivery.
> **TLS**: The encryption behind HTTPS and many other secure connections.
> **NTP**: Network Time Protocol, which keeps clocks in sync.
> *More in the [[Glossary]].*

## How it works

- UDP 514 by default; TCP 514 or 6514 (TLS) for reliable delivery.
- Severity levels 0 to 7: emergency, alert, critical, error, warning, notice, informational, debug.
- Send firewall, switch and server syslog to one collector so you can correlate events by time. That only works if every device uses NTP.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why do all devices need correct time (NTP) for syslog to be useful?
> So log lines from different devices can be lined up in the right order when you investigate.

## See also

[[Graylog]] · [[Elastic Stack]] · [[Splunk]] · [[Wazuh]] · [[NTP]]
