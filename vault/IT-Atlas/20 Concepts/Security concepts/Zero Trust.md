---
type: "concept"
level: "Mid"
category: "[[Security concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Zero Trust

> [!abstract] In one line
> Never trust by network location; verify identity, device and context for every access.

> [!tip] Think of it like
> Check ID at every door, not just at the front gate.

> [!info]+ Words on this page
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **Conditional Access**: Microsoft Entra rules that allow or block sign-ins based on user, device, location and risk.
> **ZTNA**: Zero-trust network access: app-by-app access with checks on every connection, replacing a broad VPN.
> **VPN**: An encrypted tunnel over the internet to a private network.
> **RDP**: Remote Desktop Protocol: Windows' built-in remote desktop, on port 3389.
> *More in the [[Glossary]].*

## How it works

- Strong MFA, device compliance, least privilege and segmentation.
- In practice: Conditional Access, ZTNA instead of flat VPN, no inbound RDP, and admin accounts separate from daily accounts.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Name two Zero Trust practices in Microsoft 365.
> MFA everywhere, and Conditional Access based on device compliance (also separate admin accounts).

## See also

[[Multi-factor authentication]] · [[Least privilege]] · [[SASE & ZTNA]] · [[Microsoft Entra ID]]
