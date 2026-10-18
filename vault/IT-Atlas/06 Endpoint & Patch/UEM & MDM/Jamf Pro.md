---
type: "tool"
level: "Mid"
category: "[[Endpoint & Patch Management]]"
subcategory: "[[UEM & MDM]]"
vendor: "[[Jamf]]"
deployment: "Cloud or on-prem"
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

# Jamf Pro

> [!abstract] In plain words
> The main tool for managing Macs, iPhones and iPads.
>
> **What kind of tool is this?** Device management tools enrol laptops and phones, push settings and apps to them, and check they meet security rules.

**Made by:** [[Jamf]] · **Runs:** Cloud or on-prem · **Category:** [[Endpoint & Patch Management]] › [[UEM & MDM]]

> [!info]+ Words on this page
> **UEM**: Unified endpoint management: managing all kinds of devices from one tool.
> **MDM**: Mobile device management: enrolling and controlling phones and laptops.
> **APNs**: Apple Push Notification service; its certificate must be renewed every year for Jamf or Intune to manage Apple devices.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **token**: A temporary digital key used to prove you're allowed in.
> *More in the [[Glossary]].*

## In more detail

Apple device management for macOS, iOS and iPadOS: enrollment through Apple Business Manager, policies, configuration profiles, Self Service and patch management.

## Main parts

- jamf binary and management framework on Macs
- Policies and scripts
- Configuration profiles (MDM)
- Smart groups and inventory
- Self Service
- Patch management

## Alerts you'll see

- Devices not checking in
- Policy failures
- Expired APNs certificate or ADE token

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Mac not checking in | Run sudo jamf checkJSSConnection, then sudo jamf recon |
| Profiles stop deploying everywhere | Check the APNs push certificate has not expired; it must be renewed, not replaced |

## Where to find its logs

- `/var/log/jamf.log`
- `/var/log/install.log`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
sudo jamf checkJSSConnection
sudo jamf recon
sudo jamf policy
sudo profiles show -type enrollment
```

## See also

[[Apple Business Manager]] · [[macOS]] · [[Microsoft Intune]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
