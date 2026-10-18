---
type: "tool"
level: "Mid"
category: "[[Endpoint & Patch Management]]"
subcategory: "[[UEM & MDM]]"
vendor: "[[Microsoft]]"
deployment: "Cloud"
status: "current"
aliases: []
tags:
  - "tool"
  - "endpoint"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows Autopilot

> [!abstract] In plain words
> Lets a brand-new Windows laptop set itself up for the company the first time the user signs in.
>
> **What kind of tool is this?** Device management tools enrol laptops and phones, push settings and apps to them, and check they meet security rules.

**Made by:** [[Microsoft]] · **Runs:** Cloud · **Category:** [[Endpoint & Patch Management]] › [[UEM & MDM]]

> [!info]+ Words on this page
> **Autopilot**: Windows Autopilot: sets up a new company laptop automatically when the user first signs in.
> **UEM**: Unified endpoint management: managing all kinds of devices from one tool.
> **MDM**: Mobile device management: enrolling and controlling phones and laptops.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> **tenant**: One organization's own space in a cloud service such as Microsoft 365.
> *More in the [[Glossary]].*

## In more detail

Zero-touch Windows provisioning: hardware hashes registered to a tenant, so devices join Entra ID and enroll in Intune at first boot.

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Autopilot profile not applied | Confirm the hardware hash is registered and the profile is assigned before first boot |

## See also

[[Microsoft Intune]] · [[Microsoft Entra ID]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
