---
type: "tool"
level: "Mid"
category: "[[Cloud & SaaS]]"
subcategory: "[[Microsoft 365 workloads]]"
vendor: "[[Microsoft]]"
deployment: "SaaS"
status: "current"
aliases:
  - "EXO"
tags:
  - "tool"
  - "cloud"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Exchange Online

> [!abstract] In plain words
> Microsoft's hosted email service inside Microsoft 365.
>
> **What kind of tool is this?** The services inside Microsoft 365 (mail, files, Teams) and the API used to manage them.

**Made by:** [[Microsoft]] · **Runs:** SaaS · **Category:** [[Cloud & SaaS]] › [[Microsoft 365 workloads]]

> [!info]+ Words on this page
> **API**: A way for programs and scripts to talk to a service directly, without the web page.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **EWS**: Exchange Web Services, an older way for apps to access mailboxes. Microsoft is retiring it in Exchange Online.
> **message trace**: Exchange tool that shows whether an email arrived, where it went and why.
> **quarantine**: A holding area for suspicious emails or files, so they can't do harm.
> *More in the [[Glossary]].*

## In more detail

Microsoft's hosted Exchange: mailboxes, shared mailboxes, mail flow rules and connectors, protected by EOP. Managed with the Exchange Online PowerShell module.

## Alerts you'll see

- Mail flow problems
- Mailboxes near quota
- Suspicious inbox rules or forwarding
- Connector failures

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Mail not arriving | Run a message trace for the sender and recipient; check quarantine and transport rules |
| User compromised | Reset the password, revoke sessions, remove malicious inbox rules and forwarding, review sign-ins |

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Connect-ExchangeOnline
Get-MessageTraceV2 -SenderAddress USER -StartDate (Get-Date).AddDays(-2) -EndDate (Get-Date)
Get-InboxRule -Mailbox USER
Get-EXOMailboxStatistics USER | Select-Object DisplayName, TotalItemSize
Get-Mailbox -ResultSize Unlimited | Where-Object ForwardingSmtpAddress
```

## Good to know

- Microsoft is retiring EWS for Exchange Online; anything still using EWS (backup tools, CRMs, scripts) must move to Microsoft Graph (verify current dates).
- Older Exchange Online module versions use Get-MessageTrace; newer ones add Get-MessageTraceV2.

## See also

[[Microsoft 365]] · [[Microsoft Defender for Office 365]] · [[Microsoft Graph]] · [[Spanning Backup]] · [[Email delivery problems]] · [[SPF, DKIM & DMARC]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
