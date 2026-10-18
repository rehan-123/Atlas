---
type: "tool"
level: "Mid"
category: "[[Databases & Applications]]"
vendor: "[[Microsoft]]"
deployment: "On-prem"
status: "current"
aliases:
  - "Exchange 2019"
  - "Exchange 2016"
  - "Exchange SE"
tags:
  - "tool"
  - "databases"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Exchange Server

> [!abstract] In plain words
> Microsoft's on-site email server. Old versions are out of support and are a big security risk.
>
> **What kind of tool is this?** Databases store an application's data in an organized way. Many line-of-business apps depend on one.

**Made by:** [[Microsoft]] · **Runs:** On-prem · **Category:** [[Databases & Applications]]

> [!info]+ Words on this page
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> *More in the [[Glossary]].*

## In more detail

On-prem Exchange. Exchange 2016 and 2019 reached end of support on 14 October 2025; Exchange Server Subscription Edition replaced them (verify). Hybrid setups still need one for recipient management.

## Alerts you'll see

- Queues growing
- Database copy or index unhealthy
- Certificates expiring
- Unsupported version or missing security update

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-Queue
Get-MailboxDatabaseCopyStatus
Test-ServiceHealth
Get-ExchangeCertificate | Select-Object Thumbprint, Subject, NotAfter
```

## Good to know

- 2021: ProxyLogon and ProxyShell were mass-exploited against on-prem Exchange. Internet-facing Exchange must be patched immediately.

## See also

[[Exchange Online]] · [[Certificate expiring]] · [[Email delivery problems]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
