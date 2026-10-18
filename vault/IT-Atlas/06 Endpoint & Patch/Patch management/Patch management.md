---
type: "moc"
level: "All"
tags:
  - "moc"
  - "endpoint"
created: "2026-10-18"
updated: "2026-10-18"
---

# Patch management

> [!abstract] In plain words
> Patching means installing updates, mostly security fixes. These tools decide what gets installed, when, and report what's missing.

Part of [[Endpoint & Patch Management]].

- [[Windows Update]]: The built-in Windows service that downloads and installs updates. When patching fails, the cause is usually here.
- [[WSUS]]: A Windows Server role that lets you approve and hand out Microsoft updates from your own server. Microsoft has stopped developing it.
- [[Windows Update for Business]]: Controls Windows updates from the cloud: which devices update first and how long others wait.
- [[Patch My PC]]: Keeps third-party apps like Chrome and Zoom updated through Intune or SCCM.
- [[Automox]]: Cloud patching for Windows, Mac and Linux.
- [[Action1]]: Cloud patching and basic remote management.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "06 Endpoint & Patch/Patch management"
WHERE type = "tool"
SORT file.name ASC
```
