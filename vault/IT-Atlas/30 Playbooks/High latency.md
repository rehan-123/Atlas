---
type: "playbook"
level: "Mid"
severity: "P3"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# High latency

> [!abstract] What this alert means
> Traffic is taking too long to get through the network.
>
> **Why it matters:** Apps feel slow and voice and video calls break up.

**How urgent:** P3. See [[Severity levels]].

> [!info]+ Words on this page
> **WAN**: Wide area network: links between sites, or to the internet.
> **ISP**: Internet service provider.
> **Wi-Fi**: Wireless network connection using radio signals.
> **latency**: Delay: how long data takes to get from A to B.
> **jitter**: How much delay varies from packet to packet. Bad for voice and video.
> **threshold**: The value that triggers an alert.
> **traceroute**: A tool that shows each hop a packet takes to reach a destination (tracert on Windows).
> **uplink**: The connection from a switch or site up to the next level of the network.
> *More in the [[Glossary]].*

## You'll see this when

- Latency or jitter above threshold
- Users report slowness or call quality issues

## First 5 minutes

1. Check where latency starts with traceroute, pathping or mtr
2. Check WAN utilization

## Find the cause

- Saturated uplink (backups, updates, cloud sync)
- ISP issue beyond your edge
- Wi-Fi interference
- Bufferbloat on the firewall

## Fix it

- Rate-limit or reschedule bulk traffic
- Apply QoS for voice
- Escalate to the ISP with mtr output

## Ask for help (escalate) when

- Persistent ISP issue
- Voice or business apps unusable

## Write it up

Copy this into the ticket and fill it in:

```
Site / path: 
Latency / loss: 
Where it starts: 
Cause: 
Action:
```

## See also

[[ICMP]] · [[NetFlow, sFlow & IPFIX]] · [[QoS]] · [[Voice quality problems]]
