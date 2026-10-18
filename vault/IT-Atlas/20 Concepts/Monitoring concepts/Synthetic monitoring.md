---
type: "concept"
level: "Mid"
category: "[[Monitoring concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Synthetic monitoring

> [!abstract] In one line
> Scripted checks that act like a user: load a page, log in, query an API.

> [!tip] Think of it like
> A mystery shopper: a script pretends to be a customer and tests the real journey.

> [!info]+ Words on this page
> **API**: A way for programs and scripts to talk to a service directly, without the web page.
> *More in the [[Glossary]].*

## How it works

- Catches failures that up/down checks miss (site returns 200 but the login page is broken).
- Run from outside the network to see what customers see.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why can a site return HTTP 200 and still be broken?
> The page loads but the login or checkout behind it fails. Synthetic tests catch that.

## See also

[[Uptime monitoring]] · [[Website down]]
