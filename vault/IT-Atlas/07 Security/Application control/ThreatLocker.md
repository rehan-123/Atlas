---
type: "tool"
level: "Mid"
category: "[[Security]]"
subcategory: "[[Application control]]"
vendor: "[[ThreatLocker]]"
deployment: "SaaS"
status: "current"
aliases: []
tags:
  - "tool"
  - "security"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# ThreatLocker

> [!abstract] In plain words
> Only lets approved software run, and limits what that software can touch.
>
> **What kind of tool is this?** Application control only lets approved programs run, so unknown or malicious software is blocked by default.

**Made by:** [[ThreatLocker]] · **Runs:** SaaS · **Category:** [[Security]] › [[Application control]]

> [!info]+ Words on this page
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> *More in the [[Glossary]].*

## In more detail

Zero-trust endpoint control: application allowlisting, Ringfencing (limit what allowed apps can touch), elevation control, storage control and network control.

## Alerts you'll see

- Approval requests from users
- Blocked application events after updates

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| App broke after an update | Check the audit log for blocks on the new version's hash or path, then update the policy |

## See also

[[App Control for Business]] · [[Least privilege]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
