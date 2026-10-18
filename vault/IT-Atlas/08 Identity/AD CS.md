---
type: "tool"
level: "Mid"
category: "[[Identity & Access]]"
vendor: "[[Microsoft]]"
deployment: "On-prem Windows Server role"
status: "current"
aliases:
  - "Active Directory Certificate Services"
  - "Microsoft CA"
tags:
  - "tool"
  - "identity"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# AD CS

> [!abstract] In plain words
> Windows' own certificate authority. It issues the digital certificates used for Wi-Fi, VPN and servers.
>
> **What kind of tool is this?** Identity tools hold user accounts and decide who can sign in to what. When identity breaks, nobody can work.

**Made by:** [[Microsoft]] · **Runs:** On-prem Windows Server role · **Category:** [[Identity & Access]]

> [!info]+ Words on this page
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **Wi-Fi**: Wireless network connection using radio signals.
> **VPN**: An encrypted tunnel over the internet to a private network.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> *More in the [[Glossary]].*

## In more detail

Active Directory Certificate Services: an enterprise PKI issuing certificates from templates for Wi-Fi, VPN, smart cards and servers. Misconfigured templates are a top privilege-escalation path (ESC1 to ESC8).

## Alerts you'll see

- CA certificate or CRL expiring
- CRL not published (revocation checks fail everywhere)
- Vulnerable template configurations

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
certutil -ping
certutil -CRL
certutil -verify -urlfetch CERT.cer
```

## See also

[[Certificates & PKI]] · [[Certificate expiring]] · [[NPS]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
