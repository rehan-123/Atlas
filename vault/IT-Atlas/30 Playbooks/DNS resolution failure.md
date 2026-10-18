---
type: "playbook"
level: "Mid"
severity: "P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# DNS resolution failure

> [!abstract] What this alert means
> Names can't be turned into IP addresses.
>
> **Why it matters:** Almost everything (logins, websites, email) depends on DNS, so it looks like everything is broken.

**How urgent:** P2. See [[Severity levels]].

> [!info]+ Words on this page
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **DHCP**: The service that hands out IP addresses to devices automatically.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **forwarder**: Something that passes things on: a DNS forwarder sends lookups it can't answer to another DNS server; a log forwarder ships logs to a central system.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Users cannot reach sites or internal resources by name
- Monitoring DNS checks failing

## First 5 minutes

1. Test the same name against the internal DNS server and a public resolver
2. Check whether it is internal names, external names or both

## Find the cause

- External only: forwarders down or outbound 53 blocked
- Internal only: zone or AD problem
- One client only: wrong DNS servers on that client or a stale cache

## Fix it

- Fix or replace forwarders
- Restart the DNS service
- Flush client and server caches
- Correct DHCP DNS options

## Ask for help (escalate) when

- All DNS servers failing
- Any sign of DNS hijacking

## Write it up

Copy this into the ticket and fill it in:

```
Name(s): 
Server(s) tested: 
Result: 
Cause: 
Action:
```

## See also

[[DNS]] · [[Windows DNS Server]] · [[Active Directory]]
