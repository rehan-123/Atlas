---
type: "lesson"
level: "Junior"
tags:
  - "learning"
created: "2026-10-18"
updated: "2026-10-18"
---

# Week 3 - How networks work

> [!abstract] This week
> Understand how two computers find and talk to each other. Everything else builds on this.

## Read these, in order

- [ ] [[OSI model]]
- [ ] [[TCP and UDP]]
- [ ] [[Subnetting & CIDR]]
- [ ] [[DNS]]
- [ ] [[DHCP]]
- [ ] [[ICMP]]
- [ ] [[NAT]]
- [ ] [[VLAN]]
- [ ] [[Port reference]]

## Practice

- [ ] Run `ipconfig /all` on your PC and find your IP address, subnet mask, gateway and DNS servers.
- [ ] Run `Resolve-DnsName google.com` and then `Test-NetConnection google.com -Port 443`.
- [ ] Run `tracert 8.8.8.8` and count how many hops it takes to leave your network.
- [ ] Explain to a colleague, in one minute, what happens when you type a website name into a browser.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Your PC has 169.254.x.x. What failed?
> DHCP: the PC couldn't get an address.

> [!question]- Which port does HTTPS use?
> 443.

> [!question]- Ping works but the website doesn't load. Is DNS the problem?
> Not necessarily. Test the port, the web service and its certificate.

---
Part of the [[Learning path]]. Previous: [[Week 2 - Fixing everyday problems]]. Next: [[Week 4 - Windows and identity]].
