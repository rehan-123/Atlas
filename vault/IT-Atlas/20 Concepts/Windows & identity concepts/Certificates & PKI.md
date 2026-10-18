---
type: "concept"
level: "Mid"
category: "[[Windows & identity concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Certificates & PKI

> [!abstract] In one line
> Public key infrastructure: certificate authorities issue certificates that prove identity and enable encryption.

> [!tip] Think of it like
> A certificate is an ID card for a server or user, signed by a trusted authority (the CA).

> [!info]+ Words on this page
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **VPN**: An encrypted tunnel over the internet to a private network.
> **Wi-Fi**: Wireless network connection using radio signals.
> **APNs**: Apple Push Notification service; its certificate must be renewed every year for Jamf or Intune to manage Apple devices.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **token**: A temporary digital key used to prove you're allowed in.
> *More in the [[Glossary]].*

## How it works

- Chain: root CA, intermediate CA, leaf certificate.
- Revocation via CRLs or OCSP must be reachable, or validation fails.
- Track every expiry date: web servers, RD Gateway, AD FS token signing, VPN, Wi-Fi RADIUS, Apple push (APNs), internal CAs and their CRLs.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Name three places an MSP often finds certificates that expire.
> Web servers (IIS), RD Gateway, VPN and Wi-Fi (RADIUS), AD FS, and the Apple push certificate in Jamf or Intune.

## See also

[[AD CS]] · [[SSL & TLS]] · [[Certificate expiring]] · [[AD FS]]
