---
type: "concept"
level: "Senior"
category: "[[Architecture & design]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Single sign-on

> [!abstract] In one line
> Signing in once with your company account to reach many apps, using SAML or OpenID Connect.

> [!tip] Think of it like
> A wristband at a festival: shown once at the gate, it gets you into every stage.

> [!info]+ Words on this page
> **SAML**: A standard that lets an identity provider sign users in to other apps (single sign-on).
> **SCIM**: A standard for automatically creating and removing user accounts in apps.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> *More in the [[Glossary]].*

## How it works

- The app trusts the identity provider (Entra ID, Okta) instead of keeping its own passwords.
- **SAML** is common for business apps; **OpenID Connect** for modern apps.
- **SCIM** provisioning creates and removes app accounts automatically, so leavers lose access everywhere.
- Certificates on SAML apps expire: track them like any other certificate.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why pair SSO with SCIM provisioning?
> So accounts in each app are created and, more importantly, disabled automatically when people join or leave.

## See also

[[Microsoft Entra ID]] · [[Okta]] · [[Multi-factor authentication]] · [[Certificate expiring]]
