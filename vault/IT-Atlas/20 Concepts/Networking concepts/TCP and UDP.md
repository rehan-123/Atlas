---
type: "concept"
level: "Junior"
category: "[[Networking concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# TCP and UDP

> [!abstract] In one line
> The two transport protocols: TCP is connection-oriented and reliable, UDP is connectionless and fast.

> [!tip] Think of it like
> TCP is a phone call: you connect first and confirm everything was heard. UDP is shouting across a room: fast, but nobody checks it arrived.

> [!info]+ Words on this page
> **TCP**: A connection-based network protocol that confirms delivery.
> **HTTP**: The protocol web pages use (port 80, unencrypted).
> **SMB**: The Windows file-sharing protocol (port 445).
> **RDP**: Remote Desktop Protocol: Windows' built-in remote desktop, on port 3389.
> **SQL**: Structured Query Language; also short for Microsoft SQL Server.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **DHCP**: The service that hands out IP addresses to devices automatically.
> *More in the [[Glossary]].*

## How it works

- **TCP** does a three-way handshake (SYN, SYN-ACK, ACK), retransmits lost data and keeps order. Used by HTTP(S), SMB, RDP, SQL.
- **UDP** just sends. Used by DNS queries, DHCP, SNMP, syslog, NTP, VoIP media and WireGuard.
- A TCP port test (`Test-NetConnection HOST -Port 443`) proves something is listening. A UDP port cannot be proven open the same way; test the application instead.
- Firewalls track TCP state. Asymmetric routing breaks TCP even when ping works.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Which one does DNS normally use, and which one does RDP use?
> DNS queries normally use UDP 53. RDP uses TCP 3389 (and can also use UDP).

> [!question]- Why can't Test-NetConnection prove a UDP port is open?
> UDP has no handshake, so nothing comes back to confirm it. Test the actual service instead.

## See also

[[OSI model]] · [[Port reference]]
