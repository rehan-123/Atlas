---
type: "guide"
level: "Junior"
area: "[[Internet & Wi-Fi problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# No internet

> [!abstract] What's going on
> Websites won't load and apps say you're offline.

> [!tip] Think of it like
> A blocked road out of your street. Find where the block is: your house (PC), your street (office network) or the motorway (internet provider).

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Internet & Wi-Fi problems]]

> [!info]+ Words on this page
> **Wi-Fi**: Wireless network connection using radio signals.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **DHCP**: The service that hands out IP addresses to devices automatically.
> **ISP**: Internet service provider.
> **NOC**: Network operations center: the team that monitors and fixes infrastructure.
> **WAN**: Wide area network: links between sites, or to the internet.
> **router**: Device that connects one network to another, such as the office to the internet.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Check whether other people or your phone on the same Wi-Fi have internet.
2. Turn Wi-Fi off and on, or unplug and replug the network cable.
3. Restart the PC.
4. At home: restart the router (unplug for 30 seconds).

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- `ipconfig /all`: does the PC have an IP address, gateway and DNS? 169.254.x.x means DHCP failed.
- `ping` the gateway, then `ping 8.8.8.8`, then `Resolve-DnsName microsoft.com` to find which step fails.
- If only names fail, it's DNS: `ipconfig /flushdns` and check the DNS servers.
- Reset the network stack: `netsh winsock reset` and `netsh int ip reset`, then restart.
- If the whole office is down, check the firewall and ISP (NOC playbook: Firewall WAN down).

## Common causes and fixes

| Cause | Fix |
|---|---|
| Just this PC: bad cable, Wi-Fi or driver | Reconnect, swap the cable, update the driver. |
| No IP address (169.254.x.x) | Check DHCP and the switch port. |
| DNS failing | Flush DNS, correct the DNS servers. |
| Whole site offline | Firewall or ISP issue: escalate to the NOC. |

## Escalate when

- The whole office or several users are offline
- The firewall or ISP link is down
- Only one site out of many is affected

## Write it up

Copy this into the ticket and fill it in:

```
User and contact: 
Device: 
Problem (in their words): 
Exact error message: 
Started when / what changed: 
What I checked: 
What fixed it: 
User confirmed it's fixed (yes/no): 
```

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Ping 8.8.8.8 works but websites don't open. What's broken?
> DNS: the PC can reach the internet but can't turn names into addresses.

## See also

[[How the internet reaches your desk]] · [[IP addresses]] · [[DNS]] · [[DHCP]] · [[Firewall WAN down]] · [[DNS resolution failure]]

## Field notes

Add your own tips and client quirks here.
