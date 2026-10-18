---
type: "tool"
level: "Mid"
category: "[[Endpoint & Patch Management]]"
subcategory: "[[Software deployment]]"
vendor: "[[Microsoft]]"
deployment: "Built into Windows 10 and 11"
status: "current"
aliases:
  - "Windows Package Manager"
tags:
  - "tool"
  - "endpoint"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# winget

> [!abstract] In plain words
> Windows' built-in command-line app installer: one command installs or updates an app.
>
> **What kind of tool is this?** Software deployment tools install or update apps on many computers at once, without clicking through installers.

**Made by:** [[Microsoft]] · **Runs:** Built into Windows 10 and 11 · **Category:** [[Endpoint & Patch Management]] › [[Software deployment]]

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> *More in the [[Glossary]].*

## In more detail

Windows Package Manager: command-line install, upgrade and export of apps from the winget community and Microsoft Store sources.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
winget upgrade --all --silent --accept-source-agreements --accept-package-agreements
winget list
winget export -o apps.json
```

## Good to know

- Under SYSTEM (RMM scripts) winget is not on PATH; call it from its WindowsApps install folder.

## See also

[[Chocolatey]] · [[PDQ Deploy & Inventory]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
