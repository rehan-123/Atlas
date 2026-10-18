---
type: "moc"
level: "All"
tags:
  - "moc"
  - "security"
created: "2026-10-18"
updated: "2026-10-18"
---

# SIEM

> [!abstract] In plain words
> A SIEM collects security logs from everywhere and looks for patterns that mean an attack.

Part of [[Security]].

- [[Microsoft Sentinel]]: Microsoft's cloud SIEM: it collects security logs and raises incidents when something looks like an attack.
- [[Splunk]]: A powerful log search and security platform, now owned by Cisco.
- [[Wazuh]]: A free, open-source security monitoring platform with agents.
- [[Blumira]]: A simpler SIEM for small IT teams and MSPs.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "07 Security/SIEM"
WHERE type = "tool"
SORT file.name ASC
```
