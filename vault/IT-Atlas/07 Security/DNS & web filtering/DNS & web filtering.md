---
type: "moc"
level: "All"
tags:
  - "moc"
  - "security"
created: "2026-10-18"
updated: "2026-10-18"
---

# DNS & web filtering

> [!abstract] In plain words
> DNS filtering blocks bad or unwanted websites by refusing to look up their addresses.

Part of [[Security]].

- [[Cisco Umbrella]]: Blocks dangerous websites by filtering DNS lookups, on and off the office network.
- [[DNSFilter]]: Blocks dangerous or unwanted websites by filtering DNS lookups.
- [[WebTitan]]: A DNS-based web filter popular with MSPs for blocking malicious and unwanted websites.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "07 Security/DNS & web filtering"
WHERE type = "tool"
SORT file.name ASC
```
