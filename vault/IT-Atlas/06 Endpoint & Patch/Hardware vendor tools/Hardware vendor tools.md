---
type: "moc"
level: "All"
tags:
  - "moc"
  - "endpoint"
created: "2026-10-18"
updated: "2026-10-18"
---

# Hardware vendor tools

> [!abstract] In plain words
> Hardware vendor tools keep a laptop's drivers, BIOS and firmware up to date, which Windows Update doesn't fully cover.

Part of [[Endpoint & Patch Management]].

- [[Dell Command Update]]: Dell's tool that installs the right drivers, BIOS and firmware updates for a Dell PC.
- [[HP Image Assistant]]: HP's tool that checks an HP PC against the latest drivers, BIOS and software and installs what's missing.
- [[Lenovo System Update]]: Lenovo's tool for keeping ThinkPad and ThinkCentre drivers and BIOS current; Commercial Vantage is the newer app.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "06 Endpoint & Patch/Hardware vendor tools"
WHERE type = "tool"
SORT file.name ASC
```
