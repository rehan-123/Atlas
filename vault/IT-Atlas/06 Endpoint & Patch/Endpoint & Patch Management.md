---
type: "moc"
level: "All"
tags:
  - "moc"
  - "endpoint"
created: "2026-10-18"
updated: "2026-10-18"
---

# Endpoint & Patch Management

Enrolling, configuring, patching and deploying software to endpoints.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Use rings and maintenance windows; measure patch compliance by device age and criticality.
> - Cover third-party apps and firmware, not just Windows Update; browsers and PDF readers are frequent targets.
> - Cloud-native management (Autopilot, Intune, Entra join) reduces dependency on VPN and on-premises servers.

## [[UEM & MDM]]

Device management tools enrol laptops and phones, push settings and apps to them, and check they meet security rules.

- [[Microsoft Intune]]
- [[Windows Autopilot]]
- [[Jamf Pro]]
- [[Apple Business Manager]]
- [[Omnissa Workspace ONE]]
- [[Addigy]]
- [[Microsoft Configuration Manager]]
- [[Kandji]]
- [[Mosyle]]

## [[Patch management]]

Patching means installing updates, mostly security fixes. These tools decide what gets installed, when, and report what's missing.

- [[Windows Update]]
- [[WSUS]]
- [[Windows Update for Business]]
- [[Patch My PC]]
- [[Automox]]
- [[Action1]]

## [[Software deployment]]

Software deployment tools install or update apps on many computers at once, without clicking through installers.

- [[winget]]
- [[Chocolatey]]
- [[PDQ Deploy & Inventory]]
- [[Ninite Pro]]

## [[Hardware vendor tools]]

Hardware vendor tools keep a laptop's drivers, BIOS and firmware up to date, which Windows Update doesn't fully cover.

- [[Dell Command Update]]
- [[HP Image Assistant]]
- [[Lenovo System Update]]

## Playbooks for this area

[[Bad patch rollout]] · [[BitLocker recovery screens]] · [[Low disk space]] · [[Patch failure or pending reboot]]

## Database view

```dataview
TABLE vendor, subcategory, deployment, status, agent_service AS "Agent"
FROM "06 Endpoint & Patch"
WHERE type = "tool"
SORT subcategory ASC, file.name ASC
```
