---
type: "reference"
level: "All"
tags:
  - "reference"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Linux command cheat sheet

Linux commands for first-response troubleshooting.

```bash
# System
uptime; hostnamectl; cat /etc/os-release
systemctl --failed
journalctl -p err -b
journalctl -u SERVICE --since "1 hour ago"

# Disk
df -h; df -i
du -xh / --max-depth=1 2>/dev/null | sort -h | tail
lsblk; findmnt
smartctl -a /dev/sda

# CPU and memory
top        # or htop
free -m
vmstat 1 5
ps aux --sort=-%mem | head

# Network
ip a; ip r
ss -tulpn
ping -c 4 HOST
mtr -rw HOST
dig NAME @SERVER
curl -vI https://HOST
tcpdump -i eth0 port 53

# Packages
apt update && apt list --upgradable     # Debian, Ubuntu
dnf check-update                         # RHEL family
```
