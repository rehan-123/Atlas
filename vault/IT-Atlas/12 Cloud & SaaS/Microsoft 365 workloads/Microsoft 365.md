---
type: "tool"
level: "Mid"
category: "[[Cloud & SaaS]]"
subcategory: "[[Microsoft 365 workloads]]"
vendor: "[[Microsoft]]"
deployment: "SaaS"
status: "current"
aliases:
  - "M365"
  - "Office 365"
  - "O365"
tags:
  - "tool"
  - "cloud"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Microsoft 365

> [!abstract] In plain words
> Microsoft's online suite: email (Exchange Online), files (SharePoint and OneDrive), Teams and the Office apps.
>
> **What kind of tool is this?** The services inside Microsoft 365 (mail, files, Teams) and the API used to manage them.

**Made by:** [[Microsoft]] · **Runs:** SaaS · **Category:** [[Cloud & SaaS]] › [[Microsoft 365 workloads]]

> [!info]+ Words on this page
> **API**: A way for programs and scripts to talk to a service directly, without the web page.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> *More in the [[Glossary]].*

## In more detail

Microsoft's SaaS suite: Exchange Online, SharePoint, OneDrive, Teams and the Office apps on top of Entra ID. The admin center shows service health and the message center.

## Alerts you'll see

- Service health incidents
- License shortfalls
- Risky users and compromised accounts
- Message center changes that affect integrations

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Connect-MgGraph -Scopes 'Organization.Read.All'
Get-MgSubscribedSku | Select-Object SkuPartNumber, ConsumedUnits
Connect-ExchangeOnline
```

## See also

[[Exchange Online]] · [[SharePoint & OneDrive]] · [[Microsoft Teams]] · [[Microsoft Graph]] · [[Microsoft Entra ID]] · [[Spanning Backup]] · [[Microsoft 365 Backup]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
