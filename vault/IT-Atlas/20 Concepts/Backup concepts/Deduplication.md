---
type: "concept"
level: "Mid"
category: "[[Backup concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Deduplication

> [!abstract] In one line
> Storing each unique block once to save space.

> [!tip] Think of it like
> Store each unique block once, like keeping one copy of a photo that ten people saved.

> [!info]+ Words on this page
> **bandwidth**: How much data a link can carry per second.
> *More in the [[Glossary]].*

## How it works

- Source-side dedupe saves bandwidth; target-side saves storage.
- Dedupe ratios fall with encrypted or already-compressed data.
- Deduplicated stores need verification; one damaged block can affect many backups.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why does deduplication work poorly on encrypted data?
> Encryption makes similar data look random, so there are few identical blocks to share.

## See also

[[Cove Data Protection]] · [[Arcserve UDP]] · [[Proxmox Backup Server]]
