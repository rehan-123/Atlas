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

# Wireshark filters

> [!abstract] In one line
> The display filters that turn a huge capture into the few packets that matter.

> [!tip] Think of it like
> Search filters on a huge spreadsheet: same data, only the rows you care about.

## How it works

```
ip.addr == 10.0.0.5
tcp.port == 443
dns
kerberos
tcp.analysis.retransmission
tcp.flags.reset == 1
tls.handshake.type == 1
```
- Combine with `&&` and `||`. Right-click a field > Apply as filter to build one quickly.
- Statistics > Conversations shows who talked to whom the most.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Which filter shows only TCP retransmissions?
> tcp.analysis.retransmission

## See also

[[Packet capture]]
