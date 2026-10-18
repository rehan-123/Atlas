---
type: "reference"
level: "All"
tags:
  - "reference"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Port reference

Well-known ports a NOC engineer meets every day, plus every port listed on a tool note.

## Common ports

| Port | Protocol | Service |
|---|---|---|
| 20, 21 | TCP | FTP |
| 22 | TCP | SSH, SFTP |
| 23 | TCP | Telnet (should be off) |
| 25 | TCP | SMTP |
| 53 | UDP, TCP | DNS |
| 67, 68 | UDP | DHCP |
| 69 | UDP | TFTP |
| 80 | TCP | HTTP |
| 88 | TCP, UDP | Kerberos |
| 110 / 995 | TCP | POP3 / POP3S |
| 123 | UDP | NTP |
| 135 | TCP | RPC endpoint mapper |
| 137-139 | UDP, TCP | NetBIOS |
| 143 / 993 | TCP | IMAP / IMAPS |
| 161 / 162 | UDP | SNMP / SNMP traps |
| 179 | TCP | BGP |
| 389 / 636 | TCP | LDAP / LDAPS |
| 443 | TCP | HTTPS |
| 445 | TCP | SMB |
| 464 | TCP, UDP | Kerberos password change |
| 500 / 4500 | UDP | IPsec IKE / NAT traversal |
| 514 | UDP | Syslog |
| 587 | TCP | SMTP submission |
| 623 | UDP | IPMI |
| 1194 | UDP | OpenVPN |
| 1433 / 1434 | TCP / UDP | SQL Server / SQL Browser |
| 1812 / 1813 | UDP | RADIUS auth / accounting |
| 2049 | TCP | NFS |
| 3268 / 3269 | TCP | Global Catalog |
| 3306 | TCP | MySQL, MariaDB |
| 3389 | TCP, UDP | RDP |
| 5060 / 5061 | UDP, TCP | SIP / SIP over TLS |
| 5432 | TCP | PostgreSQL |
| 5900 | TCP | VNC |
| 5985 / 5986 | TCP | WinRM HTTP / HTTPS |
| 8443 | TCP | Common alternate HTTPS (management UIs) |
| 49152-65535 | TCP | Windows dynamic RPC range |
| 51820 | UDP | WireGuard |

## Ports from tool notes

| Tool | Ports |
|---|---|
| [[3CX]] | 5060/UDP and TCP SIP; 5090 tunnel; 9000-10999/UDP RTP media |
| [[Acronis Cyber Protect]] | 443/TCP outbound to the Acronis data center |
| [[Active Directory]] | 53 DNS; 88 Kerberos; 135/TCP RPC endpoint mapper plus 49152-65535 dynamic RPC; 389 LDAP and 636 LDAPS; 445/TCP SMB; 464 Kerberos password change; 3268 and 3269 Global Catalog |
| [[AD FS]] | 443/TCP |
| [[AnyDesk]] | 80, 443 and 6568/TCP outbound |
| [[Apache Guacamole]] | 4822/TCP guacd (internal); 8080/TCP Tomcat web app (behind a reverse proxy) |
| [[Checkmk]] | 6556/TCP Checkmk agent |
| [[Cisco Umbrella]] | 53/UDP and TCP to 208.67.222.222 and 208.67.220.220 |
| [[ConnectWise Automate]] | 80/443/TCP agent to Automate server |
| [[Datadog]] | 8125/UDP DogStatsD on the agent; 443/TCP outbound to Datadog |
| [[Datto RMM]] | 443/TCP outbound from the agent to the Datto RMM platform |
| [[Elastic Stack]] | 9200/TCP Elasticsearch HTTP; 5601/TCP Kibana; 5044/TCP Logstash Beats input |
| [[File Server & DFS]] | 445/TCP SMB |
| [[Grafana]] | 3000/TCP web UI |
| [[Graylog]] | 9000/TCP web UI (default) |
| [[IIS]] | 80/TCP; 443/TCP |
| [[Kaseya VSA]] | 5721/TCP agent check-in to the VSA server; 443/TCP web console |
| [[MeshCentral]] | 443/TCP agent and web |
| [[Microsoft SQL Server]] | 1433/TCP default instance; 1434/UDP SQL Browser (named instances) |
| [[MikroTik]] | 8291/TCP Winbox |
| [[MongoDB]] | 27017/TCP |
| [[MySQL & MariaDB]] | 3306/TCP |
| [[N-able N-central]] | 443/TCP agent and probe to the N-central server |
| [[Nagios]] | 5666/TCP NRPE |
| [[NinjaOne]] | 443/TCP outbound to the NinjaOne region endpoints |
| [[NPS]] | 1812/UDP authentication; 1813/UDP accounting |
| [[OpenSSH]] | 22/TCP |
| [[OpenVPN]] | 1194/UDP default (also often 443/TCP) |
| [[Oracle Database]] | 1521/TCP listener |
| [[PostgreSQL]] | 5432/TCP |
| [[PowerShell]] | 5985/TCP WinRM HTTP; 5986/TCP WinRM HTTPS |
| [[Prometheus]] | 9090/TCP Prometheus; 9093/TCP Alertmanager; 9100/TCP node_exporter |
| [[Proxmox Backup Server]] | 8007/TCP web UI and API |
| [[Proxmox VE]] | 8006/TCP web UI |
| [[PRTG Network Monitor]] | 443/TCP (or 80) web interface; 23560/TCP remote probe to core server |
| [[QuickBooks Desktop]] | Dynamic ports set by Database Server Manager (see its Port Monitor tab) |
| [[RD Gateway]] | 443/TCP; 3391/UDP (UDP transport) |
| [[RDP]] | 3389/TCP and 3389/UDP |
| [[RDS]] | 3389/TCP and UDP to session hosts; 443/TCP to RD Gateway |
| [[Redis]] | 6379/TCP |
| [[RustDesk]] | 21115-21119/TCP and 21116/UDP for the self-hosted servers |
| [[ScreenConnect]] | 8040/TCP web (self-hosted default); 8041/TCP relay (self-hosted default) |
| [[Splunk]] | 9997/TCP forwarder to indexer; 8000/TCP web UI; 8089/TCP management |
| [[Supermicro IPMI]] | 623/UDP IPMI |
| [[Synology NAS]] | 5000/TCP DSM HTTP; 5001/TCP DSM HTTPS |
| [[TeamViewer]] | 5938/TCP primary (falls back to 443 and 80) |
| [[Tenable Nessus]] | 8834/TCP Nessus web UI |
| [[Ubiquiti UniFi]] | 8080/TCP device inform (adoption); 8443/TCP self-hosted controller UI; 3478/UDP STUN |
| [[Uptime Kuma]] | 3001/TCP web UI |
| [[Veeam Backup & Replication]] | 9392/TCP console to backup server; 2500-3300/TCP data mover traffic between components |
| [[VMware vSphere]] | 443/TCP vSphere Client and API; 902/TCP host console and NFC data transfer; 5480/TCP vCenter appliance management (VAMI) |
| [[Wazuh]] | 1514/TCP agent events; 1515/TCP agent enrollment; 55000/TCP API |
| [[Windows Deployment Services]] | 67/UDP, 69/UDP TFTP, 4011/UDP (PXE) |
| [[Windows DHCP Server]] | 67/UDP server; 68/UDP client |
| [[Windows DNS Server]] | 53/UDP and 53/TCP |
| [[WireGuard]] | 51820/UDP default |
| [[WSUS]] | 8530/TCP HTTP; 8531/TCP HTTPS |
| [[Zabbix]] | 10050/TCP server or proxy polls agent (passive checks); 10051/TCP agent or proxy sends to server (active checks, trapper) |
