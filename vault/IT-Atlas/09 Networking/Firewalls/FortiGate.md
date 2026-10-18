---
type: "tool"
level: "Mid"
category: "[[Networking]]"
subcategory: "[[Firewalls]]"
vendor: "[[Fortinet]]"
deployment: "Appliance or VM"
status: "current"
aliases:
  - "FortiOS"
  - "Fortinet firewall"
tags:
  - "tool"
  - "networking"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# FortiGate

> [!abstract] In plain words
> Fortinet's firewall, very common at MSP clients. It also handles VPNs and switching between multiple internet links.
>
> **What kind of tool is this?** A firewall is the security guard at the edge of the network, deciding what traffic is allowed in and out. It often also handles the VPN and internet links.

**Made by:** [[Fortinet]] · **Runs:** Appliance or VM · **Category:** [[Networking]] › [[Firewalls]]

> [!info]+ Words on this page
> **MSP**: Managed service provider: a company that runs IT for other companies.
> **VPN**: An encrypted tunnel over the internet to a private network.
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **IPS**: Intrusion prevention system: blocks traffic that looks like an attack.
> **SD-WAN**: Smart use of several internet links, automatically picking the best one.
> **IPsec**: A set of protocols for encrypted VPN tunnels.
> **HA**: High availability: designed so one failure doesn't cause downtime.
> **SLA**: Service level agreement: the response and fix times promised to a client. (On firewalls, an SD-WAN 'SLA' is a link-quality check.)
> *More in the [[Glossary]].*

## In more detail

Fortinet's NGFW running FortiOS: firewall policy, IPS, web filtering, SD-WAN, IPsec and remote-access VPN, and HA clusters. Managed at scale with FortiManager and FortiAnalyzer.

## Main parts

- FortiOS
- SD-WAN with performance SLAs (health checks)
- IPsec VPN and FortiClient remote access
- HA (active-passive or active-active)
- FortiManager (central config) and FortiAnalyzer (logs)
- Security Fabric (FortiSwitch, FortiAP)

## Alerts you'll see

- WAN link or SD-WAN SLA down
- HA failover or out of sync
- IPsec tunnel down
- Conserve mode (memory)
- High CPU
- Firmware with known exploited CVEs

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| WAN down | get system interface physical, then check SD-WAN SLA status and the ISP handoff |
| Traffic dropped | Run debug flow with a filter for the source and destination to see which policy or route drops it |
| Conserve mode | Check memory with diagnose sys top and diagnose hardware sysinfo conserve; often IPS or proxy features on a small model |
| IPsec down | Check phase 1 and phase 2 status and that proposals, PSK and subnets match both ends |

## Where to find its logs

- Log & Report in the GUI, or FortiAnalyzer
- Event logs: system, VPN, SD-WAN and HA

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
get system status
get system interface physical
get router info routing-table all
diagnose sys sdwan health-check
get vpn ipsec tunnel summary
diagnose vpn ike gateway list
get system ha status
diagnose debug flow filter addr 10.0.0.10
diagnose debug flow trace start 20
diagnose debug enable
diagnose sys top
```

## Good to know

- FortiOS SSL-VPN has had several critical, actively exploited vulnerabilities. Fortinet has been moving remote-access users from SSL-VPN tunnel mode to IPsec (verify for your firmware train).

## See also

[[FortiClient]] · [[SD-WAN]] · [[IPsec]] · [[Firewall WAN down]] · [[VPN tunnel down]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
