> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# pfSense Network Security

**Last Updated:** May 2026
**Version:** 1.0
**VM Role:** Firewall, Routing, Network Segmentation
**Classification:** Internal

---

## 1. Framework References

| Framework | Control Reference | Control Description |
|-----------|-------------------|---------------------|
| NIST CSF 2.0 | PR.IR-01 | Network segregation is enforced |
| NIST CSF 2.0 | DE.CM-09 | Malware protection is Proposed |
| ISO 27001:2022 | A.8.20 | Networks security |
| ISO 27001:2022 | A.8.21 | Security of network services |
| ISO 27001:2022 | A.8.22 | Segregation of networks |
| Historical PCI DSS 3.2.1-inspired reference (not current compliance) | Requirement 1 | Install and maintain firewall configuration |

**External References:**
- pfSense Documentation: https://docs.netgate.com/pfsense/en/latest/
- NIST SP 800-41: Guidelines on Firewalls and Firewall Policy

---

## 2. Purpose

pfSense serves as the primary firewall and router for Apex Capital's virtual environment, enforcing network segmentation between public-facing (DMZ) and internal networks to prevent lateral movement and unauthorized access.

**Risk Addressed:** R-001 (Lateral Movement), R-008 (Firewall Misconfiguration)

---

## 3. Network Architecture Overview

### 3.1 Interface Configuration

| Interface | Name | Subnet | Purpose | VM Connected |
|-----------|------|--------|---------|--------------|
| WAN (em0) | Public / DMZ | 10.0.1.0/24 | Public-facing web server, internet gateway | VM 2 (Ubuntu) |
| LAN (em1) | Internal | 10.0.2.0/24 | Internal workstations and servers | VM 1 (Windows) |
| OPT1 (em2) | Management | 10.0.3.0/24 | Management and monitoring | VM 4 (Wazuh) |

### 3.2 IP Assignment

| Device | Interface | IP Address | Subnet | Gateway |
|--------|-----------|------------|--------|---------|
| pfSense WAN | em0 | 10.0.1.1 | 10.0.1.0/24 | N/A |
| pfSense LAN | em1 | 10.0.2.1 | 10.0.2.0/24 | N/A |
| pfSense OPT1 | em2 | 10.0.3.1 | 10.0.3.0/24 | N/A |
| Ubuntu Web Server | WAN | 10.0.1.10 | 10.0.1.0/24 | 10.0.1.1 |
| Windows Enterprise | LAN | 10.0.2.10 | 10.0.2.0/24 | 10.0.2.1 |
| Wazuh SIEM | Management | 10.0.3.10 | 10.0.3.0/24 | 10.0.3.1 |

---

## 4. Firewall Rules

### 4.1 Default Policy

| Direction | Action | Rationale |
|-----------|--------|-----------|
| Inbound (WAN) | Deny all | Default deny for all incoming internet traffic |
| Inbound (LAN) | Deny all | Only explicitly allowed traffic from internal network |
| Inbound (Management) | Deny all | Restrict management access |
| Outbound | Allow all (with logging) | Users need internet access; logging enabled |

### 4.2 WAN (Public/DMZ) Rules

| Rule Number | Source | Destination | Port | Protocol | Action | Description |
|-------------|--------|-------------|------|----------|--------|-------------|
| 1 | Any | 10.0.1.10 | 80 | TCP | Allow | HTTP to Ubuntu web server |
| 2 | Any | 10.0.1.10 | 443 | TCP | Allow | HTTPS to Ubuntu web server |
| 3 | 10.0.3.0/24 | 10.0.1.10 | 22 | TCP | Allow | SSH from management subnet only |
| 4 | Any | Any | Any | Any | Deny | Default deny for all other WAN traffic |

### 4.3 LAN (Internal) Rules

| Rule Number | Source | Destination | Port | Protocol | Action | Description |
|-------------|--------|-------------|------|----------|--------|-------------|
| 1 | 10.0.2.10 | Any | 80,443 | TCP | Allow | Windows internet access (HTTP/HTTPS) |
| 2 | 10.0.2.10 | 10.0.3.10 | 1514 | TCP | Allow | Wazuh agent logs to SIEM |
| 3 | 10.0.1.0/24 | 10.0.2.0/24 | Any | Any | Block | Prevent lateral movement from DMZ to Internal |
| 4 | Any | Any | 3389 | TCP | Block | Block direct RDP from any subnet |
| 5 | 10.0.3.0/24 | 10.0.2.10 | 3389 | TCP | Allow | RDP only from management subnet |
| 6 | Any | Any | Any | Any | Deny | Default deny for all other LAN traffic |

### 4.4 Management (OPT1) Rules

| Rule Number | Source | Destination | Port | Protocol | Action | Description |
|-------------|--------|-------------|------|----------|--------|-------------|
| 1 | 10.0.3.0/24 | 10.0.2.10 | 3389 | TCP | Allow | RDP to Windows from management |
| 2 | 10.0.3.0/24 | 10.0.1.10 | 22 | TCP | Allow | SSH to Ubuntu from management |
| 3 | Windows and Ubuntu agents | 10.0.3.10 | 1514 | TCP | Allow | Agent events to Wazuh manager |
| 4 | Any | Any | Any | Any | Deny | Default deny for all other management traffic |

---

## 5. Critical Rule: Lateral Movement Prevention

**Rule R-001 Mitigation:**

| Attribute | Value |
|-----------|-------|
| Rule Action | Block |
| Source | 10.0.1.0/24 (DMZ / Ubuntu subnet) |
| Destination | 10.0.2.0/24 (Internal / Windows subnet) |
| Port | Any |
| Protocol | Any |
| Direction | Inbound on LAN interface |

**Purpose:** If an attacker compromises the Ubuntu web server (VM 2), this rule prevents them from initiating any connection to the Windows internal network (VM 1).

**Validation Test:**
From Ubuntu VM (10.0.1.10) attempt to connect to Windows VM (10.0.2.10)

Commands to run:
nc -zv 10.0.2.10 445
nc -zv 10.0.2.10 3389
nc -zv 10.0.2.10 22

**Expected Result:** Connection refused or timeout for all ports.

---

## 6. NAT (Network Address Translation) Configuration

| Rule Number | Interface | Source | Destination | NAT Address | Description |
|-------------|-----------|--------|-------------|-------------|-------------|
| 1 | WAN | 10.0.2.0/24 | Any | Interface Address | Outbound NAT for internal network |
| 2 | WAN | 10.0.3.0/24 | Any | Interface Address | Outbound NAT for management network |

**Purpose:** Allows internal VMs to access the internet while hiding their private IP addresses.

---

## 7. DNS Configuration

| Setting | Value | Purpose |
|---------|-------|---------|
| DNS Servers | 8.8.8.8, 8.8.4.4 (Google) | Primary DNS |
| DNS Servers (backup) | 1.1.1.1 (Cloudflare) | Secondary DNS |
| DNS Forwarder | Enabled | Forward internal DNS queries |
| DNS Resolution | Only for configured interfaces | Security |

---

## 8. DHCP Configuration

### 8.1 LAN (Internal) DHCP

| Setting | Value |
|---------|-------|
| Range | 10.0.2.100 - 10.0.2.200 |
| Default Gateway | 10.0.2.1 |
| DNS Servers | 10.0.2.1, 8.8.8.8 |

### 8.2 Management (OPT1) DHCP

| Setting | Value |
|---------|-------|
| Range | 10.0.3.100 - 10.0.3.200 |
| Default Gateway | 10.0.3.1 |
| DNS Servers | 10.0.3.1, 8.8.8.8 |

**Note:** WAN (DMZ) has DHCP disabled (static IPs only).

---

## 9. Advanced Security Settings

### 9.1 Disable ICMP Redirects

| Setting | Value | Location |
|---------|-------|----------|
| Disable ICMP redirects | Enabled | System > Advanced > Networking |

### 9.2 Block Private Networks

| Setting | Value | Location |
|---------|-------|----------|
| Block private networks on WAN | Enabled | Interfaces > WAN |

### 9.3 Anti-Lockout Rule

| Setting | Value | Purpose |
|---------|-------|---------|
| Anti-lockout rule | Enabled | Prevents accidental lockout from LAN interface |

### 9.4 WebGUI Security

| Setting | Value | Location |
|---------|-------|----------|
| Protocol | HTTPS only | System > Advanced > Admin Access |
| HTTP Strict Transport Security (HSTS) | Enabled | System > Advanced > Admin Access |
| WebGUI redirect | HTTP to HTTPS | System > Advanced > Admin Access |

---

## 10. Logging and Monitoring

### 10.1 Firewall Log Settings

| Setting | Value | Location |
|---------|-------|----------|
| Log packets matched from default block rules | Enabled | Status > System Logs > Settings |
| Log packets matched from pass rules | Enabled (critical rules only) | Status > System Logs > Settings |

### 10.2 Log Retention

| Log Type | Retention | Location |
|----------|-----------|----------|
| Firewall logs | 90 days | /var/log/filter.log |
| System logs | 90 days | /var/log/system.log |
| DHCP logs | 30 days | /var/log/dhcpd.log |

### 10.3 Syslog Forwarding to Wazuh (VM 4)

| Setting | Value | Purpose |
|---------|-------|---------|
| Remote syslog server | 10.0.3.10:514 | Forward logs to Wazuh SIEM |
| Log format | BSD | Standard syslog format |
| Facilities to send | All except VPN | Comprehensive logging |

---

## 11. Backup and Recovery

### 11.1 Configuration Backup

| Method | Command | Location |
|--------|---------|----------|
| WebGUI backup | System > Backup/Restore | Download XML file |
| Manual backup | cp /cf/conf/config.xml | /root/config-backup/ |

### 11.2 Backup Schedule

| Frequency | Retention | Location |
|-----------|-----------|----------|
| Daily | 7 days | Local pfSense |
| Weekly | 4 weeks | IT shared drive |
| Monthly | 12 months | Offsite backup |

---

## 12. Hardening Checklist

| Control objective | Target setting (not observed) | Execution status | Planned evidence (not collected) |
|-------|---------|--------|----------|
| Default password changed | Yes | Planned / not executed | Config file |
| SSH disabled on WAN | Yes | Planned / not executed | System > Advanced |
| WebGUI HTTPS only | Yes | Planned / not executed | Screenshot EV-003 |
| Default deny rule active | Yes | Planned / not executed | Screenshot EV-001 |
| Lateral movement block rule | Yes | Planned / not executed | Screenshot EV-002 |
| ICMP redirects disabled | Yes | Planned / not executed | System logs |
| Private networks blocked on WAN | Yes | Planned / not executed | Interface settings |
| Syslog forwarding to Wazuh | Yes | Planned / not executed | Screenshot EV-004 |
| NTP configured | Yes | Planned / not executed | System > General |
| Firmware up to date | Yes | Planned / not executed | System > Update |

---

## 13. Evidence Collection

| Evidence ID | Description | Command / Location | Status |
|-------------|-------------|--------------------|--------|
| EV-001 | Firewall rules screenshot | pfSense WebGUI > Firewall > Rules | Pending |
| EV-002 | Lateral movement block rule | Firewall > Rules > LAN > Rule 3 | Pending |
| EV-003 | HTTPS WebGUI configuration | System > Advanced > Admin Access | Pending |
| EV-004 | Syslog forwarding to Wazuh | Status > System Logs > Settings | Pending |
| EV-005 | Connection test from Ubuntu to Windows | nc -zv 10.0.2.10 445 | Pending |
| EV-006 | pfSense dashboard | pfSense WebGUI > Dashboard | Pending |
| EV-007 | Interface configuration | pfSense WebGUI > Interfaces | Pending |

---

## 14. Security Validation Tests

### 14.1 Lateral Movement Test

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | SSH into Ubuntu VM (10.0.1.10) | Successful login |
| 2 | Run nc -zv 10.0.2.10 445 | Connection refused or timeout |
| 3 | Run nc -zv 10.0.2.10 3389 | Connection refused or timeout |
| 4 | Run ping 10.0.2.10 | No response or timeout |
| 5 | Check pfSense log for blocked attempts | Block rule logged |

### 14.2 RDP Restriction Test

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Attempt RDP from Ubuntu to Windows (10.0.2.10:3389) | Connection refused |
| 2 | Attempt RDP from Management subnet to Windows | Connection successful |
| 3 | Check pfSense log for allowed RDP | Pass rule logged |

### 14.3 Internet Access Test

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | From Windows VM, browse to https://google.com | Successful |
| 2 | From Ubuntu VM, run curl google.com | Successful |
| 3 | Check pfSense log for outbound traffic | Pass rule logged |

---

## 15. Troubleshooting Commands

| Command | Purpose | VM |
|---------|---------|-----|
| pfctl -sr | View firewall rules | VM 3 |
| pfctl -ss | View active states | VM 3 |
| tcpdump -i em0 | Capture traffic on WAN interface | VM 3 |
| tail -f /var/log/filter.log | Monitor firewall logs | VM 3 |
| ping -c 4 10.0.2.1 | Test connectivity to pfSense LAN | VM 1 |
| traceroute 8.8.8.8 | Trace route to internet | VM 1, VM 2 |

---

## 16. Maintenance Procedures

### 16.1 Firmware Updates

| Frequency | Procedure | Downtime |
|-----------|-----------|----------|
| Monthly check | System > Update > Check for updates | None |
| Critical updates | Apply within 7 days | 5-10 minutes |
| Major version updates | Schedule maintenance window | 15-30 minutes |

### 16.2 Rule Review

| Frequency | Action | Responsible |
|-----------|--------|-------------|
| Quarterly | Review all firewall rules | Network Security |
| Quarterly | Remove unused or redundant rules | Network Security |
| Quarterly | Document rule changes | Network Security |
| Annually | Full rule audit | CISO |

### 16.3 Log Review

| Frequency | Action | Responsible |
|-----------|--------|-------------|
| Daily | Review Wazuh alerts for blocked attempts | Security Analyst |
| Weekly | Review firewall logs for patterns | IT Manager |
| Monthly | Generate log summary report | GRC Lead |

---

## 17. Known Limitations

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Single pfSense instance (no HA) | Availability risk during maintenance | Schedule maintenance during low traffic |
| No IDS/IPS enabled (resource constraints) | Limited threat detection | Wazuh on VM 4 provides some detection |
| Local VM environment | No cloud redundancy | Acceptable for lab/development |

---

## 18. Related Documents

| Document | Location |
|----------|----------|
| Network Architecture Diagram | 05-Security-Architecture/diagrams/network-architecture.md |
| Windows Hardening Guide | 08-Technical-Controls/windows-hardening.md |
| Ubuntu Web Server Guide | 08-Technical-Controls/ubuntu-web-server.md |
| Wazuh Monitoring Guide | 08-Technical-Controls/wazuh-monitoring.md |

---

## 19. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | April 2026 | S. Singh | Initial draft |
| 0.5 | May 2026 | S. Singh | Added rules and validation tests |
| 1.0 | May 2026 | S. Singh | Draft learning edition |

---

**End of pfSense Network Security**
