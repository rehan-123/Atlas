---
type: "reference"
level: "All"
tags:
  - "reference"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Glossary

Plain-English meanings of the terms you'll meet in the NOC. Every page in the atlas also explains its own terms in a **Words on this page** box.

Back to [[Home]].

## A

- **AD**: Active Directory, the Windows directory of users, computers and groups.
- **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
- **alert**: A notification that something needs attention.
- **API**: A way for programs and scripts to talk to a service directly, without the web page.
- **APNs**: Apple Push Notification service; its certificate must be renewed every year for Jamf or Intune to manage Apple devices.
- **appliance**: A dedicated box (or virtual machine) built to do one job, such as backup or firewall.
- **authenticator app**: Phone app (such as Microsoft Authenticator) that approves sign-ins or shows one-time codes for MFA.
- **Autopilot**: Windows Autopilot: sets up a new company laptop automatically when the user first signs in.

## B

- **BAA**: Business Associate Agreement: the HIPAA contract required before a provider handles patient data.
- **bandwidth**: How much data a link can carry per second.
- **BCDR**: Business continuity and disaster recovery: keeping a business running, and getting it back after a disaster.
- **BDR**: Backup and disaster recovery appliance.
- **BEC**: Business email compromise: an attacker uses a real or lookalike mailbox to trick people into paying or sharing data.
- **BIOS**: The low-level setup program that starts a PC before Windows loads (UEFI on modern PCs).
- **branch**: A separate line of changes in Git, merged back into main after review.
- **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
- **BSOD**: Blue screen of death: Windows crashed.

## C

- **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
- **CBT**: Changed block tracking: the system remembers which parts of a disk changed, so backups read only those.
- **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
- **checkpoint**: Hyper-V's name for a snapshot: a saved point in time of a VM.
- **CI/CD**: Continuous integration and delivery: automatic testing and deployment of every change.
- **CLI**: Command-line interface: typing commands instead of clicking.
- **cluster**: Several servers working together so one can take over if another fails.
- **Company Portal**: Intune's app store where users install approved work apps.
- **Conditional Access**: Microsoft Entra rules that allow or block sign-ins based on user, device, location and risk.
- **console**: The screen or web portal you manage a system from.
- **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
- **cookie**: Small note a website stores in your browser, for example to remember that you're signed in.
- **CPU**: The processor, the part of a computer that does the calculations.
- **CSV**: In Hyper-V, a Cluster Shared Volume: storage that all servers in a cluster use at once. Elsewhere, a comma-separated spreadsheet file.
- **CVE**: A public ID number for a specific security vulnerability.

## D

- **datastore**: In VMware, the storage where virtual machines' disk files live.
- **DC**: Domain controller: a server running Active Directory.
- **deduplication**: Storing identical chunks of data only once to save space.
- **DFS**: Distributed File System: gives shared folders one path and keeps copies in sync between servers.
- **DHCP**: The service that hands out IP addresses to devices automatically.
- **DKIM**: An email signature that proves a message really came from your domain and wasn't changed.
- **DLP**: Data loss prevention: rules that detect and stop sensitive data leaving.
- **DMARC**: An email rule that tells receivers what to do with mail that fails SPF or DKIM checks.
- **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
- **domain**: A group of computers and users managed together by Active Directory.
- **domain controller**: A server running Active Directory that checks logins.
- **DR**: Disaster recovery: getting systems back after a major failure.
- **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
- **dump file**: A snapshot of memory saved when a program or Windows crashes, used to find the cause.

## E

- **EDR**: Endpoint detection and response: modern antivirus that records activity and can stop and undo attacks.
- **endpoint**: Any device a user works on: laptop, desktop, phone or server.
- **escalate**: Hand a problem to a more senior person or team, with your notes.
- **ESXi**: VMware's hypervisor, the software installed on the physical server that runs VMs.
- **EWS**: Exchange Web Services, an older way for apps to access mailboxes. Microsoft is retiring it in Exchange Online.

## F

- **failover**: Automatically switching to a backup system when the main one fails.
- **firmware**: The software built into hardware such as firewalls, disks and servers.
- **forwarder**: Something that passes things on: a DNS forwarder sends lookups it can't answer to another DNS server; a log forwarder ships logs to a central system.
- **FSMO**: Five special Active Directory roles that only one domain controller holds at a time.

## G

- **GFS**: Grandfather-father-son: keeping daily, weekly and monthly backups for different lengths of time.
- **GPO**: Group Policy Object: a bundle of settings pushed to Windows computers and users.

## H

- **HA**: High availability: designed so one failure doesn't cause downtime.
- **hardening**: Changing default settings to remove unnecessary features and close security gaps.
- **HTTP**: The protocol web pages use (port 80, unencrypted).
- **HTTPS**: Encrypted HTTP (port 443).
- **hypervisor**: Software that runs virtual machines on a physical server.

## I

- **IaC**: Infrastructure as code: servers and settings described in files and built by tools.
- **image**: In backup, a copy of a whole disk, including the operating system.
- **immutable**: Can't be changed or deleted until a set date, even by an admin.
- **incremental**: A backup of only what changed since the last backup.
- **IOPS**: Input/output operations per second: how many reads and writes storage can handle.
- **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
- **IPS**: Intrusion prevention system: blocks traffic that looks like an attack.
- **IPsec**: A set of protocols for encrypted VPN tunnels.
- **ISMS**: Information security management system: the processes ISO 27001 certifies.
- **ISP**: Internet service provider.

## J

- **JIT**: Just-in-time access: admin rights granted only when needed, for a limited time.
- **jitter**: How much delay varies from packet to packet. Bad for voice and video.

## K

- **KB**: A Microsoft Knowledge Base number, which identifies a specific update (for example KB5034441).
- **Known Folder Move**: OneDrive feature that moves Desktop, Documents and Pictures into OneDrive so they're synced.
- **KQL**: Kusto Query Language, used to search logs in Sentinel, Defender and Azure Monitor.
- **kubectl**: The command-line tool for managing Kubernetes clusters.

## L

- **LAN**: Local area network: the network inside a building.
- **LAPS**: A Windows feature that gives each PC its own rotating local admin password.
- **latency**: Delay: how long data takes to get from A to B.
- **LDAP**: The protocol apps use to look up users and groups in a directory.
- **lease**: How long a DHCP-assigned IP address is lent to a device.

## M

- **malware**: Any harmful software: viruses, ransomware, spyware and the like.
- **managed identity**: An Azure identity given to a resource so it can reach other services without a stored password.
- **MDM**: Mobile device management: enrolling and controlling phones and laptops.
- **MDR**: Managed detection and response: a security team watching your EDR 24x7.
- **message trace**: Exchange tool that shows whether an email arrived, where it went and why.
- **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
- **modem**: Box that connects the building to the internet provider's line.
- **MSP**: Managed service provider: a company that runs IT for other companies.
- **MTU**: The largest packet size a link can carry without splitting it.

## N

- **NAS**: Network-attached storage: a box full of disks that shares files over the network.
- **NAT**: Network address translation: many private devices sharing one public IP.
- **NIC**: Network interface card: a computer's network adapter.
- **NLA**: Network Level Authentication: RDP checks your login before opening a session.
- **NOC**: Network operations center: the team that monitors and fixes infrastructure.
- **node**: One member of a cluster, or one item in a graph.
- **NTP**: Network Time Protocol, which keeps clocks in sync.

## O

- **offboarding**: Removing a leaver's access while keeping their data for the business.
- **onboarding**: Setting up a new starter's accounts, access and devices.
- **OS**: Operating system, such as Windows or Linux.
- **OST**: Outlook's local copy of your mailbox on the PC. Safe to rebuild; the real mailbox is on the server.

## P

- **packet loss**: Data that never arrives and has to be resent, which makes things slow or choppy.
- **patch**: An update that fixes bugs or security holes.
- **PHI**: Protected health information: patient data covered by HIPAA.
- **phishing**: Fake messages designed to trick people into clicking or giving away passwords.
- **ping**: A quick test that sends a small message to a device and waits for a reply.
- **pipeline**: A series of automated steps (test, build, deploy) that run on every change.
- **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
- **probe**: A small collector at a client site that monitors devices on the monitoring server's behalf.
- **proxy**: A middleman server that passes traffic on, for web filtering or to do work for a central server.
- **PSA**: Professional services automation: the MSP's ticketing, time and billing system.
- **PST**: Outlook data file stored on a PC; easy to lose and not backed up by Microsoft 365.
- **PSU**: Power supply unit.
- **pull request**: A request to review and merge changes from one branch into another.

## Q

- **quarantine**: A holding area for suspicious emails or files, so they can't do harm.
- **quorum**: The majority vote a cluster needs to keep running, so two halves can't both think they're in charge.

## R

- **RAID**: Combining several disks so one failed disk doesn't lose data. Not a backup.
- **RAM**: Memory: the computer's short-term workspace for open apps. Cleared when you restart.
- **ransomware**: Malware that encrypts files and demands payment to unlock them.
- **RDP**: Remote Desktop Protocol: Windows' built-in remote desktop, on port 3389.
- **RDS**: Remote Desktop Services: many users working on one shared Windows server.
- **registry**: Windows' central settings database.
- **replication**: Copying data or changes to another place, continuously or on a schedule.
- **repository**: Where backups are stored.
- **retention**: How long backups or logs are kept.
- **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
- **router**: Device that connects one network to another, such as the office to the internet.
- **RPC**: Remote procedure call: how Windows machines ask each other to do things (uses port 135 and high ports).
- **RPO**: Recovery point objective: the most data, measured in time, you can afford to lose.
- **RTO**: Recovery time objective: how long you can afford to be down.

## S

- **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
- **safe mode**: A way to start Windows or an app with only the basics, to find what's causing a problem.
- **SAML**: A standard that lets an identity provider sign users in to other apps (single sign-on).
- **SAN**: Storage area network: shared block storage for servers.
- **SASE**: Cloud-delivered network security that protects users wherever they are.
- **SCIM**: A standard for automatically creating and removing user accounts in apps.
- **scope**: In DHCP, the range of IP addresses that can be handed out.
- **script**: A text file of commands that runs automatically.
- **SD-WAN**: Smart use of several internet links, automatically picking the best one.
- **service**: In Windows, a background program that starts with the system (for example the print spooler).
- **SIEM**: A system that collects security logs from everywhere and looks for attacks.
- **SIP**: The protocol that sets up internet phone calls.
- **SLA**: Service level agreement: the response and fix times promised to a client. (On firewalls, an SD-WAN 'SLA' is a link-quality check.)
- **SMB**: The Windows file-sharing protocol (port 445).
- **smishing**: Phishing by text message.
- **snapshot**: A saved point in time of a VM or disk. Not a backup, and it grows the longer you keep it.
- **SNMP**: A protocol monitoring tools use to read status from network devices.
- **SoA**: Statement of Applicability: the ISO 27001 document listing which controls apply and why.
- **SOC**: Security operations center: the team that watches for and responds to attacks.
- **SPF**: A DNS record listing which servers may send email for a domain.
- **SPN**: Service principal name: the name Kerberos uses to find which account runs a service.
- **spooler**: The Windows service that queues print jobs before they go to the printer.
- **SQL**: Structured Query Language; also short for Microsoft SQL Server.
- **SSD**: Solid-state drive: fast storage with no moving parts. Much quicker than an old hard disk.
- **SSH**: Secure Shell: encrypted command-line login, mostly for Linux and network devices (port 22).
- **SSID**: The name of a Wi-Fi network.
- **SSL**: The old name for TLS encryption.
- **SSO**: Single sign-on: one login for many apps.
- **SSPR**: Self-service password reset: users reset their own password after proving who they are.
- **stop code**: The error name shown on a blue screen, such as DRIVER_IRQL_NOT_LESS_OR_EQUAL.
- **subnet**: A range of IP addresses that form one network segment.
- **switch**: A device that connects computers inside a network.

## T

- **Task Manager**: Windows tool (Ctrl+Shift+Esc) that shows running apps and what's using CPU, memory and disk.
- **TCP**: A connection-based network protocol that confirms delivery.
- **tenant**: One organization's own space in a cloud service such as Microsoft 365.
- **threshold**: The value that triggers an alert.
- **throttling**: Deliberately slowing something down, for example limiting backup bandwidth during the day.
- **throughput**: How much data moves per second, for example MB/s on a disk or Mbps on a link.
- **ticket**: A record of a request or problem in the PSA.
- **TLS**: The encryption behind HTTPS and many other secure connections.
- **token**: A temporary digital key used to prove you're allowed in.
- **TPM**: A security chip in the computer that stores encryption keys, used by BitLocker.
- **traceroute**: A tool that shows each hop a packet takes to reach a destination (tracert on Windows).
- **trunk**: A switch port that carries several VLANs at once.
- **tunnel**: An encrypted connection that carries traffic across another network.

## U

- **UDP**: A fast network protocol that doesn't confirm delivery.
- **UEM**: Unified endpoint management: managing all kinds of devices from one tool.
- **uplink**: The connection from a switch or site up to the next level of the network.
- **UPN**: User principal name: the sign-in name that looks like an email address.
- **UPS**: Uninterruptible power supply: a big battery that keeps equipment running in a power cut.

## V

- **VDI**: Virtual desktop infrastructure: desktops that run on servers and are used remotely.
- **VHDX**: A virtual hard disk file used by Hyper-V and FSLogix.
- **vishing**: Phishing by phone call.
- **VLAN**: A virtual network that separates traffic on the same physical switches.
- **VM**: Virtual machine: a computer that runs as software on a physical server.
- **VPN**: An encrypted tunnel over the internet to a private network.
- **VSS**: Volume Shadow Copy Service: takes consistent snapshots of in-use files for backups.
- **vulnerability**: A weakness an attacker can use.

## W

- **WAN**: Wide area network: links between sites, or to the internet.
- **Wi-Fi**: Wireless network connection using radio signals.
- **WMI**: Windows Management Instrumentation: lets tools query Windows for information.

## X

- **XDR**: Extended detection and response: EDR that also watches email, identity and cloud.

## Y

- **YAML**: A plain-text format used for configuration files and pipeline definitions; indentation matters.

## Z

- **zone**: In DNS, the set of records for one domain.
- **ZTNA**: Zero-trust network access: app-by-app access with checks on every connection, replacing a broad VPN.
