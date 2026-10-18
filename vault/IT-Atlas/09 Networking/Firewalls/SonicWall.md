---
type: "tool"
level: "Mid"
category: "[[Networking]]"
subcategory: "[[Firewalls]]"
vendor: "[[SonicWall]]"
deployment: "Appliance or VM"
status: "current"
aliases:
  - "SonicOS"
tags:
  - "tool"
  - "networking"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# SonicWall

> [!abstract] In plain words
> A firewall common in small and mid-sized businesses.
>
> **What kind of tool is this?** A firewall is the security guard at the edge of the network, deciding what traffic is allowed in and out. It often also handles the VPN and internet links.

**Made by:** [[SonicWall]] · **Runs:** Appliance or VM · **Category:** [[Networking]] › [[Firewalls]]

> [!info]+ Words on this page
> **VPN**: An encrypted tunnel over the internet to a private network.
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **SMB**: The Windows file-sharing protocol (port 445).
> **SSL**: The old name for TLS encryption.
> **CVE**: A public ID number for a specific security vulnerability.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **appliance**: A dedicated box (or virtual machine) built to do one job, such as backup or firewall.
> **firmware**: The software built into hardware such as firewalls, disks and servers.
> *More in the [[Glossary]].*

## In more detail

SMB and mid-market firewalls running SonicOS, with SSL VPN (NetExtender and Mobile Connect), managed by Network Security Manager.

## Good to know

- SonicWall SSL VPN and management interfaces have had repeated exploited CVEs. Keep firmware current and restrict management to trusted IPs.

## See also

[[IPsec]] · [[VPN tunnel down]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
