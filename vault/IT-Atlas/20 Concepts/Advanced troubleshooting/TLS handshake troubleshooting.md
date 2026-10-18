---
type: "concept"
level: "Senior"
category: "[[Advanced troubleshooting]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# TLS handshake troubleshooting

> [!abstract] In one line
> Diagnosing failures when a client and server can't agree on a secure connection.

> [!tip] Think of it like
> Two people trying to talk who don't share a language: the line is open, but no conversation happens.

> [!info]+ Words on this page
> **TLS**: The encryption behind HTTPS and many other secure connections.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **registry**: Windows' central settings database.
> *More in the [[Glossary]].*

## How it works

- Causes: protocol mismatch (server needs TLS 1.2+, old client only does 1.0), no shared cipher suite, certificate problems, SNI missing, TLS inspection on the firewall.
- `openssl s_client -connect HOST:443 -servername HOST` shows the handshake; `Test-NetConnection` only proves the port.
- On Windows, Schannel events in the System log show handshake errors (e.g. event 36874, 36887).
- Old apps may need .NET or OS registry settings to use TLS 1.2.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Port 443 is open but the app still can't connect over HTTPS. What do you test next?
> The TLS handshake itself (openssl s_client or Schannel events) for protocol, cipher or certificate problems.

## See also

[[SSL & TLS]] · [[Packet capture]] · [[Certificate chain troubleshooting]]
