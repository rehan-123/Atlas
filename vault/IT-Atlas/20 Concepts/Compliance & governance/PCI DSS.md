---
type: "concept"
level: "Senior"
category: "[[Compliance & governance]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# PCI DSS

> [!abstract] In one line
> The card industry's security standard for anyone who stores, processes or transmits payment card data.

> [!tip] Think of it like
> Rules for handling cash in a shop: the fewer people and rooms that touch it, the easier it is to secure.

> [!info]+ Words on this page
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> *More in the [[Glossary]].*

## How it works

- Version 4.0 (now 4.0.1) is current; it requires MFA for access to the card data environment, strong logging and regular testing.
- Best strategy: **shrink the scope** so card data never touches your network (use hosted payment pages or P2PE terminals).
- Segment anything that does handle card data from everything else.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- What's the most effective way to reduce PCI DSS work for a small business?
> Reduce scope: use hosted payment pages or validated point-to-point encrypted terminals so card data never enters their network.

## See also

[[Network segmentation]] · [[Multi-factor authentication]] · [[SIEM]]
