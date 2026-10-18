---
type: "tool"
level: "Mid"
category: "[[Backup & DR]]"
subcategory: "[[SaaS backup]]"
vendor: "[[Kaseya]]"
deployment: "SaaS"
status: "current"
aliases:
  - "Spanning"
  - "Spanning 365"
tags:
  - "tool"
  - "backup"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Spanning Backup

> [!abstract] In plain words
> Backs up Microsoft 365 (mail, OneDrive, SharePoint, Teams) and Google Workspace, so deleted or encrypted data can be restored. Each user needs a licence to be protected.
>
> **What kind of tool is this?** SaaS backup keeps your own copy of Microsoft 365 or Google data (mail, OneDrive, SharePoint, Teams). Microsoft and Google keep the service running, but restoring deleted or encrypted data is your job.

**Made by:** [[Kaseya]] · **Runs:** SaaS · **Category:** [[Backup & DR]] › [[SaaS backup]]

> [!info]+ Words on this page
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **DR**: Disaster recovery: getting systems back after a major failure.
> **API**: A way for programs and scripts to talk to a service directly, without the web page.
> **EWS**: Exchange Web Services, an older way for apps to access mailboxes. Microsoft is retiring it in Exchange Online.
> *More in the [[Glossary]].*

## In more detail

SaaS backup for Microsoft 365 (Exchange, OneDrive, SharePoint, Teams), Google Workspace and Salesforce, with per-user licensing and an admin and API layer.

## Main parts

- Per-tenant Spanning admin portal
- Per-user licensing and assignment
- Backup of mailboxes, OneDrive, SharePoint sites and Teams
- Point-in-time and granular restores
- Spanning API (per-tenant API keys)

## Alerts you'll see

- Unprotected users or shared mailboxes
- Backup errors per user or site
- Re-authorization required
- License shortfall

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Users unprotected | Compare licensed mailboxes in Microsoft 365 with protected users in Spanning; check auto-assign settings |
| Backups failing tenant-wide | Check the Spanning service account or app authorization in Microsoft 365 has not been revoked or expired |
| SharePoint sites missing | Check site discovery and whether the app has rights to the sites |

## Good to know

- Microsoft is retiring Exchange Web Services (EWS) for Exchange Online. SaaS backup vendors are moving to Microsoft Graph, which can require re-authorization (verify current dates).

## See also

[[Microsoft 365]] · [[Exchange Online]] · [[SharePoint & OneDrive]] · [[Microsoft Graph]] · [[SaaS backup failing]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
