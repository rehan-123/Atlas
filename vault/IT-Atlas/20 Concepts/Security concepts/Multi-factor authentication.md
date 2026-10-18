---
type: "concept"
level: "Junior"
category: "[[Security concepts]]"
aliases:
  - "MFA"
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Multi-factor authentication

> [!abstract] In one line
> Requiring two or more factors to sign in.

> [!tip] Think of it like
> Something you know (password) plus something you have (phone or key).

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **PSA**: Professional services automation: the MSP's ticketing, time and billing system.
> **MSP**: Managed service provider: a company that runs IT for other companies.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> *More in the [[Glossary]].*

## How it works

- Phishing-resistant methods (FIDO2 keys, passkeys, Windows Hello for Business, certificates) beat push and SMS.
- Push fatigue attacks spam approvals until a user taps Yes; number matching stops most of them.
- Every remote access path, backup console, RMM and PSA must have MFA. Attackers go for the MSP's tools first.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- What is MFA fatigue, and what stops it?
> Attackers spam push approvals until a user taps Yes. Number matching or phishing-resistant methods stop it.

## See also

[[Microsoft Entra ID]] · [[Duo Security]] · [[Zero Trust]]
