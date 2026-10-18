---
type: "moc"
level: "All"
tags:
  - "moc"
created: "2026-10-18"
updated: "2026-10-18"
---

# Playbooks

Step-by-step guides for the alerts a NOC sees most: what the alert means, what to check, how to fix it, when to ask for help, and what to write in the ticket.

Back to [[Home]]. Severity definitions: [[Severity levels]].

| Playbook | What it means | How urgent |
|---|---|---|
| [[Agent offline]] | The RMM agent on a device stopped checking in, so you can't see or manage that device right now. | P3 (P2 if a server) |
| [[Server unreachable]] | Monitoring can't reach the server at all: ping and checks are failing. | P1 or P2 |
| [[Low disk space]] | A drive is nearly full. | P3 (P2 for system or database volumes) |
| [[High CPU]] | The processor has been very busy for a long time. | P3 |
| [[High memory]] | The machine is using most of its RAM. | P3 |
| [[Windows service stopped]] | A Windows service that should be running has stopped. | P3 (P2 for critical services) |
| [[Backup job failed]] | A backup didn't complete, or completed with errors. | P3 (P2 after repeated failures) |
| [[VSS writer failure]] | Windows couldn't take the consistent snapshot that the backup needs. | P3 |
| [[Backup copy & replication lag]] | The offsite copy of the backups is falling behind. | P3 |
| [[Screenshot verification failed]] | The automatic boot test of a backup didn't show a working login screen. | P3 |
| [[SaaS backup failing]] | Microsoft 365 or Google Workspace backups are failing for some or all users. | P3 (P2 if tenant-wide) |
| [[Patch failure or pending reboot]] | Updates failed to install, or are waiting for a restart. | P4 (P3 for exploited CVEs) |
| [[RAID degraded]] | A disk in a server's RAID set has failed; the server is running without its safety net. | P2 |
| [[SMART predictive failure]] | A disk is warning that it's likely to fail soon. | P3 |
| [[AD replication failure]] | Domain controllers have stopped copying changes to each other. | P2 |
| [[DNS resolution failure]] | Names can't be turned into IP addresses. | P2 |
| [[DHCP scope exhausted]] | The pool of IP addresses to hand out has run out. | P2 |
| [[Certificate expiring]] | A certificate on a website, VPN or other service is about to expire. | P3 (P1 if already expired on a public service) |
| [[Firewall WAN down]] | The firewall's internet link is down. | P1 (whole site) or P2 (one link with failover) |
| [[VPN tunnel down]] | A VPN connection between sites, or for remote users, isn't working. | P2 |
| [[Interface errors and packet loss]] | A network port is seeing damaged or dropped traffic. | P3 |
| [[High latency]] | Traffic is taking too long to get through the network. | P3 |
| [[UPS on battery]] | The UPS has lost mains power and is running on battery. | P1 if runtime is low, otherwise P2 |
| [[Temperature alarm]] | The server room or a server is getting too hot. | P2 |
| [[Hypervisor host disconnected]] | A server that runs virtual machines isn't responding to its management console. | P1 or P2 |
| [[Datastore or CSV low space]] | The storage holding virtual machines is nearly full. | P2 |
| [[Snapshot age]] | A virtual machine has an old snapshot (checkpoint) that was never cleaned up. | P3 |
| [[Account lockout storm]] | Lots of accounts, or one account over and over, are getting locked out. | P2 |
| [[Suspected ransomware]] | Signs that files are being encrypted by an attacker. | P1 |
| [[EDR threat detected]] | The security agent found something malicious or suspicious. | P2 (P1 if not mitigated or spreading) |
| [[SQL Server problems]] | The SQL database server is down, full or very slow. | P2 |
| [[Website down]] | A website isn't answering properly. | P1 or P2 |
| [[Email delivery problems]] | Mail isn't arriving, is bouncing back, or lands in spam. | P2 |
| [[FSLogix profile failed to load]] | A user's remote desktop profile couldn't be attached at login. | P2 |
| [[Time drift]] | A machine's clock is wrong. | P3 |
| [[Voice quality problems]] | Calls are choppy, one-way or dropping. | P3 |
| [[Kerberos authentication failures]] | Users or services can't authenticate with Kerberos, so access to file shares, SQL or web apps fails or falls back to NTLM. | P2 (P1 if widespread) |
| [[Group Policy not applying]] | A Group Policy setting isn't reaching the computers or users it should. | P3 (P2 for security baselines) |
| [[Entra Connect sync errors]] | Changes in on-premises Active Directory aren't reaching Microsoft Entra ID, or some objects fail to sync. | P2 if sync has stopped, P3 for single-object errors |
| [[Domain controller failure]] | A domain controller has crashed, been corrupted or is gone for good. | P1 if the last DC at a site or holding FSMO roles, otherwise P2 |
| [[Broadcast storm or network loop]] | Traffic is looping endlessly between switches, flooding the network until it slows to a halt. | P1 |
| [[High disk latency]] | Storage is taking too long to answer read and write requests. | P2 |
| [[VM won't start]] | A virtual machine fails to power on or start. | P2 (P1 for critical servers) |
| [[BitLocker recovery screens]] | One or many PCs are asking for a BitLocker recovery key at startup. | P3 (P2 if many devices) |
| [[Business email compromise]] | An attacker has control of a mailbox (or a lookalike) and is using it to trick people, often into paying fake invoices. | P1 |
| [[Bad patch rollout]] | An update deployed to many machines is causing failures: crashes, broken apps or boot problems. | P1 or P2 depending on spread |
| [[Azure VM unreachable]] | An Azure virtual machine doesn't respond to RDP, SSH or its application. | P2 (P1 for production) |
| [[Certificate trust errors]] | Clients refuse a connection because they don't trust a server's certificate. | P2 or P3 |
