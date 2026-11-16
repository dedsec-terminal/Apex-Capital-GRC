> **Evidence status:** Referenced screenshots and logs are planned artifacts and are not present in this public edition. Entries are evidence requests, not completed evidence.

> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Evidence Summary

**Last Updated:** May 2026
**Version:** 1.0
**Classification:** Internal
**Owner:** GRC Lead

---

## 1. Overview

This document catalogs all evidence collected during the security control implementation and validation phase. Each evidence item includes a description, source VM, framework mapping, and collection status.

**Evidence Repository Location:** `10-Evidence/screenshots/`

**Total Evidence Items:** 25
**Status:** All pending collection

---

## 2. Evidence by VM

### 2.1 VM 1 - Windows Enterprise Evidence

| Evidence ID | Description | File Path | Framework Mapping | Status |
|-------------|-------------|-----------|-------------------|--------|
| EV-WIN-001 | Password policy output - net accounts | screenshots/windows/net-accounts.png | NIST PR.AA-05, ISO A.5.17, PCI Req 8 | Pending |
| EV-WIN-002 | Weak password rejection error | screenshots/windows/weak-password-reject.png | NIST PR.AA-05, ISO A.5.17 | Pending |
| EV-WIN-003 | Account lockout message | screenshots/windows/account-lockout.png | NIST PR.AA-03, PCI Req 8.1.4 | Pending |
| EV-WIN-004 | Event ID 4740 - Account locked out | screenshots/windows/event-4740.png | NIST PR.AA-03 | Pending |
| EV-WIN-005 | Windows Defender status (Get-MpComputerStatus) | screenshots/windows/defender-status.png | NIST DE.CM-09, ISO A.8.7, PCI Req 5 | Pending |
| EV-WIN-006 | EICAR test file blocked by Defender | screenshots/windows/eicar-block.png | NIST DE.CM-09, ISO A.8.7, PCI Req 5 | Pending |
| EV-WIN-007 | Controlled Folder Access blocked event (Event ID 1123) | screenshots/windows/cfa-block.png | NIST DE.CM-09, ISO A.8.7 | Pending |
| EV-WIN-008 | Windows Firewall profile status | screenshots/windows/firewall-profiles.png | NIST PR.IR-01, ISO A.8.20 | Pending |
| EV-WIN-009 | Windows Firewall RDP block rule | screenshots/windows/firewall-rdp-block.png | NIST PR.IR-01, ISO A.8.22 | Pending |
| EV-WIN-010 | Local user accounts (standard vs admin) | screenshots/windows/local-users.png | NIST PR.AA-05, ISO A.8.2 | Pending |
| EV-WIN-011 | Administrator account renamed | screenshots/windows/admin-renamed.png | NIST PR.AA-05 | Pending |
| EV-WIN-012 | Audit policy configuration | screenshots/windows/audit-policy.png | ISO A.8.15, PCI Req 10 | Pending |
| EV-WIN-013 | Wazuh agent service status | screenshots/windows/wazuh-service.png | NIST DE.CM-7 | Pending |

### 2.2 VM 2 - Ubuntu Web Server Evidence

| Evidence ID | Description | File Path | Framework Mapping | Status |
|-------------|-------------|-----------|-------------------|--------|
| EV-UBU-001 | OS version and kernel information | screenshots/ubuntu/os-version.png | NIST ID.AM-1 | Pending |
| EV-UBU-002 | UFW firewall status (sudo ufw status verbose) | screenshots/ubuntu/ufw-status.png | NIST PR.IR-01, ISO A.8.20 | Pending |
| EV-UBU-003 | UFW rules listing (allow 80,443, SSH from mgmt) | screenshots/ubuntu/ufw-rules.png | NIST PR.IR-01 | Pending |
| EV-UBU-004 | SSH configuration - PasswordAuthentication no | screenshots/ubuntu/ssh-password-auth.png | NIST PR.AA-03, PCI Req 2 | Pending |
| EV-UBU-005 | SSH configuration - PermitRootLogin no | screenshots/ubuntu/ssh-root-login.png | NIST PR.AA-03 | Pending |
| EV-UBU-006 | SSH configuration - MaxAuthTries 3 | screenshots/ubuntu/ssh-max-auth-tries.png | NIST PR.AA-03 | Pending |
| EV-UBU-007 | fail2ban status (active) | screenshots/ubuntu/fail2ban-status.png | NIST PR.AA-03 | Pending |
| EV-UBU-008 | Nginx security headers (curl -I output) | screenshots/ubuntu/nginx-security-headers.png | NIST PR.DS-2, PCI Req 4 | Pending |
| EV-UBU-009 | HTTPS/TLS configuration (SSL Labs or nmap) | screenshots/ubuntu/tls-config.png | PCI Req 4 | Pending |
| EV-UBU-010 | Nginx server tokens off | screenshots/ubuntu/nginx-server-tokens.png | NIST PR.PS-01 | Pending |
| EV-UBU-011 | Automatic security updates enabled | screenshots/ubuntu/auto-updates.png | NIST PR.PS-02 | Pending |
| EV-UBU-012 | Wazuh agent status (systemctl status wazuh-agent) | screenshots/ubuntu/wazuh-agent-status.png | NIST DE.CM-7 | Pending |
| EV-UBU-013 | Auditd rules configured | screenshots/ubuntu/auditd-rules.png | ISO A.8.15 | Pending |

### 2.3 VM 3 - pfSense Evidence

| Evidence ID | Description | File Path | Framework Mapping | Status |
|-------------|-------------|-----------|-------------------|--------|
| EV-PFS-001 | pfSense dashboard (interfaces overview) | screenshots/pfsense/dashboard.png | NIST ID.AM-1 | Pending |
| EV-PFS-002 | WAN firewall rules (including default deny) | screenshots/pfsense/wan-rules.png | NIST PR.IR-01, PCI Req 1 | Pending |
| EV-PFS-003 | LAN firewall rules (including block from DMZ) | screenshots/pfsense/lan-rules.png | NIST PR.IR-01, ISO A.8.22 | Pending |
| EV-PFS-004 | Lateral movement block rule (Rule 3 detail) | screenshots/pfsense/block-rule-detail.png | NIST PR.IR-01 | Pending |
| EV-PFS-005 | Management subnet (OPT1) rules | screenshots/pfsense/opt1-rules.png | NIST PR.IR-01 | Pending |
| EV-PFS-006 | NAT outbound rules configuration | screenshots/pfsense/nat-rules.png | PCI Req 1 | Pending |
| EV-PFS-007 | pfSense firewall log showing blocked connections | screenshots/pfsense/firewall-log.png | NIST DE.CM-1 | Pending |
| EV-PFS-008 | Syslog forwarding to Wazuh (10.0.3.10:514) | screenshots/pfsense/syslog-forward.png | NIST DE.CM-7 | Pending |
| EV-PFS-009 | WebGUI HTTPS configuration | screenshots/pfsense/webgui-https.png | PCI Req 4 | Pending |
| EV-PFS-010 | pfSense version and update status | screenshots/pfsense/version.png | NIST PR.PS-02 | Pending |

### 2.4 VM 4 - Wazuh Evidence

| Evidence ID | Description | File Path | Framework Mapping | Status |
|-------------|-------------|-----------|-------------------|--------|
| EV-WAZ-001 | Wazuh dashboard overview | screenshots/wazuh/dashboard.png | NIST DE.AE-1 | Pending |
| EV-WAZ-002 | Agents list showing all 3 agents connected | screenshots/wazuh/agents-list.png | NIST DE.CM-7 | Pending |
| EV-WAZ-003 | Agent details for Windows (logs received) | screenshots/wazuh/agent-windows.png | NIST DE.CM-7 | Pending |
| EV-WAZ-004 | Agent details for Ubuntu (logs received) | screenshots/wazuh/agent-ubuntu.png | NIST DE.CM-7 | Pending |
| EV-WAZ-005 | Failed login alert (Event ID 4625) | screenshots/wazuh/failed-login-alert.png | NIST DE.AE-1, PCI Req 10 | Pending |
| EV-WAZ-006 | EICAR malware detection alert (Level 15) | screenshots/wazuh/eicar-alert.png | NIST DE.CM-3, PCI Req 5 | Pending |
| EV-WAZ-007 | pfSense firewall block alert | screenshots/wazuh/pfsense-block-alert.png | NIST DE.CM-1 | Pending |
| EV-WAZ-008 | SSH failed login alert (Ubuntu) | screenshots/wazuh/ssh-failed-alert.png | NIST DE.AE-1 | Pending |
| EV-WAZ-009 | Wazuh rule configuration (local_rules.xml) | screenshots/wazuh/local-rules.png | NIST DE.AE-1 | Pending |
| EV-WAZ-010 | Compliance dashboard (NIST CSF) | screenshots/wazuh/compliance-nist.png | NIST All | Pending |
| EV-WAZ-011 | Compliance dashboard (PCI DSS) | screenshots/wazuh/compliance-pci.png | PCI Req 10 | Pending |
| EV-WAZ-012 | Security events timeline | screenshots/wazuh/events-timeline.png | NIST DE.AE-1 | Pending |

---

## 3. Evidence by Framework Mapping

### 3.1 NIST CSF 2.0

| NIST Function | Subcategory | Evidence ID | Description |
|---------------|-------------|-------------|-------------|
| Identify (ID) | ID.AM-1 | EV-UBU-001, EV-PFS-001 | OS version, interfaces |
| Protect (PR) | PR.AA-05 | EV-WIN-001, EV-WIN-002, EV-WIN-011 | Password policy, admin renamed |
| Protect (PR) | PR.AA-05 | EV-WIN-010 | Local user roles |
| Protect (PR) | PR.IR-01 | EV-WIN-008, EV-WIN-009, EV-PFS-002, EV-PFS-003, EV-PFS-004, EV-PFS-005 | Firewall rules, segmentation |
| Protect (PR) | PR.AA-03 | EV-WIN-003, EV-WIN-004, EV-UBU-004, EV-UBU-005, EV-UBU-006 | Account lockout, SSH hardening |
| Protect (PR) | PR.DS-2 | EV-UBU-008, EV-PFS-009 | HTTPS, TLS |
| Protect (PR) | DE.CM-09 | EV-WIN-005, EV-WIN-006, EV-WIN-007 | Defender, EICAR, CFA |
| Protect (PR) | PR.PS-01 | EV-UBU-010 | Server tokens off |
| Protect (PR) | PR.PS-02 | EV-UBU-011, EV-PFS-010 | Auto updates |
| Detect (DE) | DE.AE-1 | EV-WAZ-001, EV-WAZ-005, EV-WAZ-008, EV-WAZ-009, EV-WAZ-012 | Alerts, events |
| Detect (DE) | DE.CM-1 | EV-PFS-007, EV-WAZ-007 | Firewall logs |
| Detect (DE) | DE.CM-3 | EV-WAZ-006 | Malware detection |
| Detect (DE) | DE.CM-7 | EV-WIN-013, EV-UBU-012, EV-PFS-008, EV-WAZ-002, EV-WAZ-003, EV-WAZ-004 | Agent connectivity |

### 3.2 ISO 27001:2022

| Annex A Control | Evidence ID | Description |
|-----------------|-------------|-------------|
| A.8.2 (Privileged access rights) | EV-WIN-010 | Local user roles |
| A.8.7 (Protection against malware) | EV-WIN-005, EV-WIN-006, EV-WIN-007 | Defender, EICAR, CFA |
| A.8.15 (Logging and monitoring) | EV-WIN-012, EV-UBU-013, EV-WAZ-001 to EV-WAZ-012 | Audit policy, Wazuh |
| A.8.16 (Monitoring activities) | EV-WAZ-005, EV-WAZ-006, EV-WAZ-007 | Alerts |
| A.8.20 (Networks security) | EV-WIN-008, EV-UBU-002 | Firewall |
| A.8.21 (Security of network services) | EV-PFS-002 to EV-PFS-006 | pfSense rules |
| A.8.22 (Segregation of networks) | EV-WIN-009, EV-PFS-003, EV-PFS-004 | Segmentation |
| A.5.17 (Password management) | EV-WIN-001, EV-WIN-002 | Password policy |

### 3.3 Historical PCI DSS 3.2.1-inspired learning reference (not current compliance)

| PCI Requirement | Evidence ID | Description |
|-----------------|-------------|-------------|
| Req 1 (Firewall) | EV-PFS-002, EV-PFS-003, EV-PFS-006 | pfSense rules, NAT |
| Req 2 (Defaults) | EV-UBU-004, EV-UBU-005 | SSH hardening |
| Req 4 (Encryption) | EV-UBU-008, EV-UBU-009, EV-PFS-009 | HTTPS, TLS |
| Req 5 (Malware) | EV-WIN-005, EV-WIN-006, EV-WAZ-006 | Defender, EICAR |
| Req 8 (Authentication) | EV-WIN-001, EV-WIN-003 | Password policy, lockout |
| Req 10 (Logging) | EV-WIN-012, EV-WAZ-005, EV-WAZ-011 | Audit logs, Wazuh alerts |

---

## 4. Evidence by Control Test

| Test ID | Test Name | Evidence ID | Evidence Description |
|---------|-----------|-------------|----------------------|
| T-001 | Password Policy Enforcement | EV-WIN-001 | net accounts output |
| T-002 | Account Lockout | EV-WIN-003, EV-WIN-004 | Lockout message, Event 4740 |
| T-003 | Weak Password Rejection | EV-WIN-002 | Weak password error |
| T-004 | Windows Defender Status | EV-WIN-005 | Get-MpComputerStatus |
| T-005 | EICAR Malware Detection | EV-WIN-006, EV-WAZ-006 | EICAR block, Wazuh alert |
| T-006 | Controlled Folder Access | EV-WIN-007 | CFA block event |
| T-007 | Windows Firewall | EV-WIN-008, EV-WIN-009 | Firewall profiles, RDP rule |
| T-008 | RDP Restriction | EV-WIN-009 | RDP block rule |
| T-009 | Lateral Movement Prevention | EV-PFS-004, EV-PFS-007 | Block rule, firewall log |
| T-010 | pfSense Default Deny | EV-PFS-002 | WAN rules default deny |
| T-011 | pfSense Segmentation | EV-PFS-003, EV-PFS-004 | LAN block rule |
| T-012 | Ubuntu UFW Firewall | EV-UBU-002, EV-UBU-003 | UFW status, rules |
| T-013 | Ubuntu SSH Hardening | EV-UBU-004, EV-UBU-005, EV-UBU-006 | SSH config |
| T-014 | Ubuntu HTTPS | EV-UBU-008, EV-UBU-009 | Security headers, TLS |
| T-015 | Wazuh Failed Login Alert | EV-WAZ-005 | Failed login alert |
| T-016 | Wazuh EICAR Alert | EV-WAZ-006 | EICAR alert |
| T-017 | Wazuh Agent Connectivity | EV-WAZ-002, EV-WAZ-003, EV-WAZ-004 | Agents list |
| T-018 | pfSense Log Forwarding | EV-PFS-008, EV-WAZ-007 | Syslog config, alert |

---

## 5. Evidence Collection Checklist

### 5.1 VM 1 (Windows Enterprise) - 13 items

| Checked | Evidence ID | Description |
|---------|-------------|-------------|
| [ ] | EV-WIN-001 | net accounts output |
| [ ] | EV-WIN-002 | Weak password rejection |
| [ ] | EV-WIN-003 | Account lockout message |
| [ ] | EV-WIN-004 | Event ID 4740 |
| [ ] | EV-WIN-005 | Defender status |
| [ ] | EV-WIN-006 | EICAR block |
| [ ] | EV-WIN-007 | CFA block |
| [ ] | EV-WIN-008 | Firewall profiles |
| [ ] | EV-WIN-009 | RDP block rule |
| [ ] | EV-WIN-010 | Local users |
| [ ] | EV-WIN-011 | Admin renamed |
| [ ] | EV-WIN-012 | Audit policy |
| [ ] | EV-WIN-013 | Wazuh service |

### 5.2 VM 2 (Ubuntu) - 13 items

| Checked | Evidence ID | Description |
|---------|-------------|-------------|
| [ ] | EV-UBU-001 | OS version |
| [ ] | EV-UBU-002 | UFW status |
| [ ] | EV-UBU-003 | UFW rules |
| [ ] | EV-UBU-004 | SSH password auth |
| [ ] | EV-UBU-005 | SSH root login |
| [ ] | EV-UBU-006 | SSH MaxAuthTries |
| [ ] | EV-UBU-007 | fail2ban status |
| [ ] | EV-UBU-008 | Nginx headers |
| [ ] | EV-UBU-009 | TLS config |
| [ ] | EV-UBU-010 | Server tokens |
| [ ] | EV-UBU-011 | Auto updates |
| [ ] | EV-UBU-012 | Wazuh agent |
| [ ] | EV-UBU-013 | Auditd rules |

### 5.3 VM 3 (pfSense) - 10 items

| Checked | Evidence ID | Description |
|---------|-------------|-------------|
| [ ] | EV-PFS-001 | Dashboard |
| [ ] | EV-PFS-002 | WAN rules |
| [ ] | EV-PFS-003 | LAN rules |
| [ ] | EV-PFS-004 | Block rule detail |
| [ ] | EV-PFS-005 | OPT1 rules |
| [ ] | EV-PFS-006 | NAT rules |
| [ ] | EV-PFS-007 | Firewall log |
| [ ] | EV-PFS-008 | Syslog forward |
| [ ] | EV-PFS-009 | WebGUI HTTPS |
| [ ] | EV-PFS-010 | Version info |

### 5.4 VM 4 (Wazuh) - 12 items

| Checked | Evidence ID | Description |
|---------|-------------|-------------|
| [ ] | EV-WAZ-001 | Dashboard |
| [ ] | EV-WAZ-002 | Agents list |
| [ ] | EV-WAZ-003 | Windows agent |
| [ ] | EV-WAZ-004 | Ubuntu agent |
| [ ] | EV-WAZ-005 | Failed login alert |
| [ ] | EV-WAZ-006 | EICAR alert |
| [ ] | EV-WAZ-007 | pfSense block alert |
| [ ] | EV-WAZ-008 | SSH failed alert |
| [ ] | EV-WAZ-009 | Local rules |
| [ ] | EV-WAZ-010 | NIST dashboard |
| [ ] | EV-WAZ-011 | PCI dashboard |
| [ ] | EV-WAZ-012 | Events timeline |

---

## 6. Evidence Directory Structure

The evidence screenshots are organized in the following directory structure:

- 10-Evidence/
  - evidence-summary.md
  - screenshots/
    - windows/
      - net-accounts.png
      - weak-password-reject.png
      - account-lockout.png
      - event-4740.png
      - defender-status.png
      - eicar-block.png
      - cfa-block.png
      - firewall-profiles.png
      - firewall-rdp-block.png
      - local-users.png
      - admin-renamed.png
      - audit-policy.png
      - wazuh-service.png
    - ubuntu/
      - os-version.png
      - ufw-status.png
      - ufw-rules.png
      - ssh-password-auth.png
      - ssh-root-login.png
      - ssh-max-auth-tries.png
      - fail2ban-status.png
      - nginx-security-headers.png
      - tls-config.png
      - nginx-server-tokens.png
      - auto-updates.png
      - wazuh-agent-status.png
      - auditd-rules.png
    - pfsense/
      - dashboard.png
      - wan-rules.png
      - lan-rules.png
      - block-rule-detail.png
      - opt1-rules.png
      - nat-rules.png
      - firewall-log.png
      - syslog-forward.png
      - webgui-https.png
      - version.png
    - wazuh/
      - dashboard.png
      - agents-list.png
      - agent-windows.png
      - agent-ubuntu.png
      - failed-login-alert.png
      - eicar-alert.png
      - pfsense-block-alert.png
      - ssh-failed-alert.png
      - local-rules.png
      - compliance-nist.png
      - compliance-pci.png
      - events-timeline.png

---

## 7. Related Documents

| Document | Location |
|----------|----------|
| Test Scenarios | 09-Testing-and-Validation/test-scenarios.md |
| Testing Results | 09-Testing-and-Validation/results.md |
| pfSense Network Security | 08-Technical-Controls/pfsense-network.md |
| Windows Hardening Guide | 08-Technical-Controls/windows-hardening.md |
| Ubuntu Web Server Hardening | 08-Technical-Controls/ubuntu-web-server.md |
| Wazuh Monitoring | 08-Technical-Controls/wazuh-monitoring.md |

---

## 8. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | April 2026 | S. Singh | Initial draft |
| 0.5 | May 2026 | S. Singh | Added framework mappings |
| 1.0 | May 2026 | S. Singh | Draft learning edition |

---

**End of Evidence Summary**
