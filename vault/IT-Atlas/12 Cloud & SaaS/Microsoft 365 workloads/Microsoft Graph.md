---
type: "tool"
level: "Mid"
category: "[[Cloud & SaaS]]"
subcategory: "[[Microsoft 365 workloads]]"
vendor: "[[Microsoft]]"
deployment: "API"
status: "current"
aliases:
  - "Graph API"
  - "MS Graph"
tags:
  - "tool"
  - "cloud"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Microsoft Graph

> [!abstract] In plain words
> The API (programmatic interface) scripts and tools use to read and change Microsoft 365 and Entra ID.
>
> **What kind of tool is this?** The services inside Microsoft 365 (mail, files, Teams) and the API used to manage them.

**Made by:** [[Microsoft]] · **Runs:** API · **Category:** [[Cloud & SaaS]] › [[Microsoft 365 workloads]]

> [!info]+ Words on this page
> **API**: A way for programs and scripts to talk to a service directly, without the web page.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **HTTP**: The protocol web pages use (port 80, unencrypted).
> **throttling**: Deliberately slowing something down, for example limiting backup bandwidth during the day.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **tenant**: One organization's own space in a cloud service such as Microsoft 365.
> *More in the [[Glossary]].*

## In more detail

The unified API for Microsoft 365 and Entra ID. App registrations get delegated or application permissions; the Microsoft Graph PowerShell SDK wraps it.

## Main parts

- App registrations and service principals
- Delegated vs application permissions
- Admin consent
- Reports API
- Microsoft Graph PowerShell SDK

## Alerts you'll see

- Throttling (HTTP 429 with Retry-After)
- Expired client secrets or certificates
- Consent revoked

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| 403 or accessDenied | Check the app has the right permission type and that admin consent was granted |
| Reports show hashed user names | The tenant's report concealment setting is on; turn it off in the Microsoft 365 admin center to see names |
| 429 Too Many Requests | Honour the Retry-After header and batch requests |

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Connect-MgGraph -Scopes 'User.Read.All'
Get-MgContext
Invoke-MgGraphRequest -Method GET -Uri 'https://graph.microsoft.com/v1.0/organization'
```

## See also

[[Microsoft Entra ID]] · [[Microsoft 365]] · [[PowerShell]] · [[Exchange Online]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
