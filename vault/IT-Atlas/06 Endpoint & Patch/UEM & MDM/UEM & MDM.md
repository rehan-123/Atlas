---
type: "moc"
level: "All"
tags:
  - "moc"
  - "endpoint"
created: "2026-10-18"
updated: "2026-10-18"
---

# UEM & MDM

> [!abstract] In plain words
> Device management tools enrol laptops and phones, push settings and apps to them, and check they meet security rules.

Part of [[Endpoint & Patch Management]].

- [[Microsoft Intune]]: Microsoft's cloud tool for managing laptops and phones: it enrols devices, pushes settings and apps, and checks they're compliant.
- [[Windows Autopilot]]: Lets a brand-new Windows laptop set itself up for the company the first time the user signs in.
- [[Jamf Pro]]: The main tool for managing Macs, iPhones and iPads.
- [[Apple Business Manager]]: Apple's portal that ties company-bought Apple devices to your management tool automatically.
- [[Omnissa Workspace ONE]]: Device management for laptops and phones, formerly VMware Workspace ONE.
- [[Addigy]]: Mac management built for MSPs.
- [[Microsoft Configuration Manager]]: Microsoft's on-site tool for managing Windows PCs (often called SCCM).
- [[Kandji]]: A Mac and iPhone management platform with ready-made security settings.
- [[Mosyle]]: An Apple device management platform popular with schools and small businesses.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "06 Endpoint & Patch/UEM & MDM"
WHERE type = "tool"
SORT file.name ASC
```
