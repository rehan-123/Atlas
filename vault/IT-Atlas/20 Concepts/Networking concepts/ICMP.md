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

# ICMP

> [!abstract] In one line
> The control protocol behind ping and traceroute.

> [!tip] Think of it like
> ICMP is a knock on the door: ping knocks and waits for an answer. No answer doesn't always mean nobody's home; some doors ignore knocks.

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **TCP**: A connection-based network protocol that confirms delivery.
> **ping**: A quick test that sends a small message to a device and waits for a reply.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **traceroute**: A tool that shows each hop a packet takes to reach a destination (tracert on Windows).
> **router**: Device that connects one network to another, such as the office to the internet.
> *More in the [[Glossary]].*

## How it works

- Ping (echo request and reply) proves layer 3 reachability, not that a service works.
- Many firewalls and cloud VMs block ICMP, so "no ping" is not always "down". Use a TCP port check as a second signal.
- Traceroute shows the path; `pathping` (Windows) and `mtr` (Linux) add per-hop loss over time.
- Loss shown at a middle hop but not at the destination is usually just that router rate-limiting ICMP, not real loss.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A cloud VM doesn't answer ping. Is it down?
> Not necessarily. Many firewalls block ping. Test a real port (for example 443 or 3389) before deciding.

## See also

[[Server unreachable]] · [[Interface errors and packet loss]] · [[High latency]]
