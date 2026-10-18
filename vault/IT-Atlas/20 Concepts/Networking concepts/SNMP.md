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

# SNMP

> [!abstract] In one line
> Simple Network Management Protocol: how monitoring tools read counters and status from network devices, UPSs and printers.

> [!tip] Think of it like
> SNMP is like reading a device's dashboard over the network: the monitoring tool asks for a number (traffic, temperature, battery) and the device answers.

> [!info]+ Words on this page
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **UPS**: Uninterruptible power supply: a big battery that keeps equipment running in a power cut.
> *More in the [[Glossary]].*

## How it works

- Polling uses UDP 161; traps (device-initiated alerts) go to UDP 162.
- **v1 and v2c** use a community string sent in clear text. Never use `public`. Restrict by source IP.
- **v3** adds authentication and encryption (authPriv). Use it wherever the device supports it.
- OIDs identify values; MIBs are the dictionaries that name them. Interface counters come from IF-MIB.
- Most "SNMP not working" tickets are community or credential mismatch, an ACL on the device, or UDP 161 blocked.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- What's the difference between polling and a trap?
> Polling: the monitor asks the device (UDP 161). Trap: the device sends an alert on its own (UDP 162).

> [!question]- Why is SNMPv3 better than v2c?
> v3 has real usernames, authentication and encryption. v2c sends a simple 'community' password in plain text.

## See also

[[PRTG Network Monitor]] · [[Auvik]] · [[Zabbix]] · [[LibreNMS]] · [[APC Smart-UPS]]
