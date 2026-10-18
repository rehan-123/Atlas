---
type: "concept"
level: "Mid"
category: "[[Networking concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# SSL & TLS

> [!abstract] In one line
> Transport Layer Security encrypts web and many other connections. SSL is the obsolete predecessor.

> [!tip] Think of it like
> TLS is the padlock in the browser: it encrypts the connection and the certificate proves you're talking to the real site.

> [!info]+ Words on this page
> **TLS**: The encryption behind HTTPS and many other secure connections.
> **SSL**: The old name for TLS encryption.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> *More in the [[Glossary]].*

## How it works

- TLS 1.2 and 1.3 are current; disable SSL 3.0, TLS 1.0 and 1.1.
- A certificate must match the hostname, chain to a trusted root and be in date. Missing intermediates break some clients but not others.
- Public certificate lifetimes are being shortened in stages by the CA/Browser Forum, so renewals must be automated (verify the current schedule).
- Check from outside: `openssl s_client -connect host:443 -servername host`.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A website's certificate expired last night. What do users see?
> Browser security warnings, and many apps simply refuse to connect.

## See also

[[Certificates & PKI]] · [[Certificate expiring]] · [[IIS]]
