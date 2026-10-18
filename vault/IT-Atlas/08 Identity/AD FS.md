---
type: "tool"
level: "Mid"
category: "[[Identity & Access]]"
vendor: "[[Microsoft]]"
deployment: "On-prem"
status: "current"
aliases:
  - "Active Directory Federation Services"
tags:
  - "tool"
  - "identity"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# AD FS

> [!abstract] In plain words
> An older on-site system that handles sign-ins to cloud apps for Active Directory users. Being replaced by Entra ID.
>
> **What kind of tool is this?** Identity tools hold user accounts and decide who can sign in to what. When identity breaks, nobody can work.

**Made by:** [[Microsoft]] · **Runs:** On-prem · **Category:** [[Identity & Access]]

> [!info]+ Words on this page
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **SAML**: A standard that lets an identity provider sign users in to other apps (single sign-on).
> **TCP**: A connection-based network protocol that confirms delivery.
> **token**: A temporary digital key used to prove you're allowed in.
> **proxy**: A middleman server that passes traffic on, for web filtering or to do work for a central server.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> *More in the [[Glossary]].*

## In more detail

Active Directory Federation Services: on-prem SAML and WS-Federation token issuing, published through Web Application Proxy. Microsoft recommends moving apps to Entra ID.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 443/TCP

## Alerts you'll see

- Token-signing certificate expiry
- Service or proxy trust failures

## See also

[[Microsoft Entra ID]] · [[Certificates & PKI]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
