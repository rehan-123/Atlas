---
type: "moc"
level: "All"
tags:
  - "moc"
  - "endpoint"
created: "2026-10-18"
updated: "2026-10-18"
---

# Software deployment

> [!abstract] In plain words
> Software deployment tools install or update apps on many computers at once, without clicking through installers.

Part of [[Endpoint & Patch Management]].

- [[winget]]: Windows' built-in command-line app installer: one command installs or updates an app.
- [[Chocolatey]]: A command-line app installer for Windows with a big library of apps.
- [[PDQ Deploy & Inventory]]: Pushes software and scripts to many Windows PCs at once, and lists what's installed on each.
- [[Ninite Pro]]: A simple service that silently installs and updates common free apps like browsers, Zoom and 7-Zip.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "06 Endpoint & Patch/Software deployment"
WHERE type = "tool"
SORT file.name ASC
```
