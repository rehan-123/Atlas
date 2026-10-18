---
type: "tool"
level: "Mid"
category: "[[Cloud & SaaS]]"
subcategory: "[[Microsoft 365 workloads]]"
vendor: "[[Microsoft]]"
deployment: "SaaS"
status: "current"
aliases:
  - "SharePoint Online"
  - "OneDrive"
  - "OneDrive for Business"
tags:
  - "tool"
  - "cloud"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# SharePoint & OneDrive

> [!abstract] In plain words
> Where Microsoft 365 files live: SharePoint for shared team files, OneDrive for each person's own files.
>
> **What kind of tool is this?** The services inside Microsoft 365 (mail, files, Teams) and the API used to manage them.

**Made by:** [[Microsoft]] · **Runs:** SaaS · **Category:** [[Cloud & SaaS]] › [[Microsoft 365 workloads]]

> [!info]+ Words on this page
> **API**: A way for programs and scripts to talk to a service directly, without the web page.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **tenant**: One organization's own space in a cloud service such as Microsoft 365.
> **ransomware**: Malware that encrypts files and demands payment to unlock them.
> *More in the [[Glossary]].*

## In more detail

SharePoint Online sites (including every Team's files) and OneDrive personal storage. Tenant storage is pooled; versions and the recycle bin are not backups.

## Alerts you'll see

- Tenant storage near limit
- Sync client errors
- Mass deletions or renames (ransomware)
- External sharing changes

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Connect-SPOService -Url https://TENANT-admin.sharepoint.com
Get-SPOSite -Limit All | Select-Object Url, StorageUsageCurrent
```

## See also

[[Microsoft 365]] · [[Microsoft Teams]] · [[Spanning Backup]] · [[Microsoft 365 Backup]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
