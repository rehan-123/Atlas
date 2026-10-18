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

# Packet capture

> [!abstract] In one line
> Recording the actual network traffic to see what's really happening, instead of guessing.

> [!tip] Think of it like
> A dashcam for the network: replay exactly what happened instead of relying on witnesses.

> [!info]+ Words on this page
> **TCP**: A connection-based network protocol that confirms delivery.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **TLS**: The encryption behind HTTPS and many other secure connections.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## How it works

- Tools: Wireshark, `pktmon` (built into Windows), `tcpdump` (Linux), firewall packet captures.
- Capture on both ends if you can; filter to the host and port in question.
- Look for: TCP resets, retransmissions, no reply (blocked), DNS answers, TLS handshake failures.
- Captures can contain sensitive data: store them safely and delete them afterwards.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A connection fails and the capture shows the SYN leaving but no SYN-ACK. What does that suggest?
> Something on the path (a firewall or the server's own firewall) is dropping it, or the service isn't listening and replies are blocked.

## See also

[[TCP and UDP]] · [[Wireshark filters]] · [[TLS handshake troubleshooting]]
