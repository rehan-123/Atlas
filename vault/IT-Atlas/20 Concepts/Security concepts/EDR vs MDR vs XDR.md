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

# EDR vs MDR vs XDR

> [!abstract] In one line
> Terms you will see on every security product.

> [!tip] Think of it like
> EDR is a security camera, MDR is the guard watching it 24x7, XDR is cameras on every door, not just the desks.

> [!info]+ Words on this page
> **EDR**: Endpoint detection and response: modern antivirus that records activity and can stop and undo attacks.
> **MDR**: Managed detection and response: a security team watching your EDR 24x7.
> **SOC**: Security operations center: the team that watches for and responds to attacks.
> **XDR**: Extended detection and response: EDR that also watches email, identity and cloud.
> **SMB**: The Windows file-sharing protocol (port 445).
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> *More in the [[Glossary]].*

## How it works

- **EDR**: software on endpoints that records activity and can isolate or remediate.
- **MDR**: a managed service where a 24x7 SOC watches the EDR and responds.
- **XDR**: detection across endpoints, identity, email, cloud and network in one platform.
- Many SMB stacks are Defender for Endpoint plus an MDR provider.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Who responds to an EDR alert at 3 a.m. if there's no MDR?
> Your own team; nobody else is watching it.

## See also

[[EDR & MDR]] · [[Microsoft Defender for Endpoint]] · [[Huntress]] · [[SentinelOne]]
