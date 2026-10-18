---
type: "tool"
level: "Mid"
category: "[[Voice & UC]]"
vendor: "[[3CX]]"
deployment: "Self-hosted or 3CX-hosted"
status: "current"
aliases: []
tags:
  - "tool"
  - "voice"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# 3CX

> [!abstract] In plain words
> A business phone system that runs as software on a server or in the cloud.
>
> **What kind of tool is this?** Business phone systems that run over the network or the internet.

**Made by:** [[3CX]] · **Runs:** Self-hosted or 3CX-hosted · **Category:** [[Voice & UC]]

> [!info]+ Words on this page
> **SIP**: The protocol that sets up internet phone calls.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **TCP**: A connection-based network protocol that confirms delivery.
> **trunk**: A switch port that carries several VLANs at once.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **tunnel**: An encrypted connection that carries traffic across another network.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> *More in the [[Glossary]].*

## In more detail

Software PBX on Windows or Debian with SIP trunks, desk phones and apps.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 5060/UDP and TCP SIP
- 5090 tunnel
- 9000-10999/UDP RTP media

## Alerts you'll see

- SIP trunk unregistered
- One-way or no audio
- Certificate or FQDN expiry

## Good to know

- March 2023: a supply-chain attack trojanized the 3CX desktop app.

## See also

[[SIP]] · [[Voice quality problems]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
