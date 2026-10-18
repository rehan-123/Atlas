---
type: "moc"
level: "All"
tags:
  - "moc"
created: "2026-10-18"
updated: "2026-10-18"
---

# Networking concepts

How packets move and the protocols every network depends on.

Part of [[Concepts]].

- [[OSI model]]: Seven-layer model used to describe where a network problem lives.
- [[TCP and UDP]]: The two transport protocols: TCP is connection-oriented and reliable, UDP is connectionless and fast.
- [[Subnetting & CIDR]]: How IP ranges are written and split.
- [[DNS]]: Turns names into IP addresses. When DNS breaks, it looks like everything is broken.
- [[DHCP]]: Hands out IP addresses and options (gateway, DNS, domain) to clients.
- [[ICMP]]: The control protocol behind ping and traceroute.
- [[SNMP]]: Simple Network Management Protocol: how monitoring tools read counters and status from network devices, UPSs and printers.
- [[Syslog]]: The standard way network devices and Linux systems send log messages to a collector.
- [[NetFlow, sFlow & IPFIX]]: Flow telemetry: who talked to whom, on which port, and how much.
- [[NTP]]: Network Time Protocol keeps clocks in sync.
- [[VLAN]]: Virtual LANs split one physical switch into separate layer 2 networks.
- [[Spanning Tree]]: STP prevents layer 2 loops by blocking redundant paths.
- [[Link aggregation]]: Bundling several physical links into one logical link (LACP, 802.3ad).
- [[BGP]]: Border Gateway Protocol: routing between autonomous systems, the routing protocol of the internet.
- [[OSPF]]: Open Shortest Path First: link-state interior routing protocol inside an organization.
- [[NAT]]: Network Address Translation: rewriting IP addresses as traffic crosses a device.
- [[IPsec]]: The standard suite for encrypted site-to-site and many remote-access VPNs.
- [[SSL & TLS]]: Transport Layer Security encrypts web and many other connections. SSL is the obsolete predecessor.
- [[ARP]]: Address Resolution Protocol maps IP addresses to MAC addresses on a LAN.
- [[MTU]]: Maximum transmission unit: the largest packet a link carries without fragmenting (1500 bytes on Ethernet).
- [[QoS]]: Quality of Service prioritizes latency-sensitive traffic such as voice and video.
- [[PoE]]: Power over Ethernet powers APs, phones and cameras from the switch.
- [[First-hop redundancy]]: VRRP, HSRP and similar protocols give hosts a gateway IP that survives a router or firewall failure.
- [[SIP]]: Session Initiation Protocol sets up VoIP calls; RTP carries the audio.
- [[802.1X]]: Port-based network access control: devices authenticate before getting network access.
