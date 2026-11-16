> **Execution status:** No VM tests have been run. Every result/criteria below describes a plan or expected outcome, not a pass.

> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Test Scenarios

**Last Updated:** May 2026
**Version:** 1.0
**Classification:** Internal
**Owner:** GRC Lead

---

## 1. Overview

This document defines the test scenarios used to validate the security controls Proposed across all four virtual machines in the Apex Capital environment. Each test maps to specific controls, frameworks, and evidence requirements.

**Test Environment:** 4-VM setup (Windows Enterprise, Ubuntu Web Server, pfSense, Wazuh)

**Test Network:**

| VM | Hostname | IP Address | Subnet |
|----|----------|------------|--------|
| VM 1 | Windows-Enterprise | 10.0.2.10 | Internal (10.0.2.0/24) |
| VM 2 | Ubuntu-Web | 10.0.1.10 | DMZ (10.0.1.0/24) |
| VM 3 | pfSense | 10.0.1.1, 10.0.2.1, 10.0.3.1 | All |
| VM 4 | Wazuh-SIEM | 10.0.3.10 | Management (10.0.3.0/24) |

---

## 2. Test Matrix Summary

| Test ID | Test Name | Category | VM | Status |
|---------|-----------|----------|-----|--------|
| T-001 | Password Policy Enforcement | Access Control | VM 1 | Pending |
| T-002 | Account Lockout | Access Control | VM 1 | Pending |
| T-003 | Weak Password Rejection | Access Control | VM 1 | Pending |
| T-004 | Windows Defender Real-time Protection | Endpoint Security | VM 1 | Pending |
| T-005 | EICAR Malware Detection | Endpoint Security | VM 1 | Pending |
| T-006 | Controlled Folder Access | Endpoint Security | VM 1 | Pending |
| T-007 | Windows Firewall Configuration | Network Security | VM 1 | Pending |
| T-008 | RDP Restriction | Network Security | VM 1, VM 3 | Pending |
| T-009 | Lateral Movement Prevention | Network Security | VM 2, VM 3 | Pending |
| T-010 | pfSense Default Deny Rule | Network Security | VM 3 | Pending |
| T-011 | pfSense Segmentation Rules | Network Security | VM 3 | Pending |
| T-012 | Ubuntu UFW Firewall | Network Security | VM 2 | Pending |
| T-013 | Ubuntu SSH Hardening | Access Control | VM 2 | Pending |
| T-014 | Ubuntu Web Server (HTTPS) | Data Protection | VM 2 | Pending |
| T-015 | Wazuh Failed Login Alert | Monitoring | VM 1, VM 4 | Pending |
| T-016 | Wazuh EICAR Alert | Monitoring | VM 1, VM 4 | Pending |
| T-017 | Wazuh Agent Connectivity | Monitoring | VM 4 | Pending |
| T-018 | pfSense Log Forwarding to Wazuh | Monitoring | VM 3, VM 4 | Pending |

---

## 3. Access Control Tests

### T-001: Password Policy Enforcement

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify Windows password policy is correctly applied |
| **VM** | VM 1 (Windows Enterprise) |
| **Control Mapped** | NIST CSF PR.AA-05, ISO 27001 A.5.17, PCI DSS Req 8 |
| **Risk Addressed** | R-002 (Credential Theft) |

**Pre-requisites:**
- Administrator access to Windows VM
- Password policy configured via secpol.msc

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Command Prompt as Administrator | Command prompt opens |
| 2 | Run command: `net accounts` | Output shows password policy settings |
| 3 | Verify minimum password length = 14 | Minimum password length: 14 |
| 4 | Verify password history = 24 | Length of password history maintained: 24 |
| 5 | Verify maximum password age = 90 days | Maximum password age (days): 90 |
| 6 | Verify complexity enabled | Password must meet complexity requirements: Enabled |

**Evidence:** Screenshot of `net accounts` output

**Expected Result:** All 5 verification steps match expected values

---

### T-002: Account Lockout

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify account locks after 5 failed login attempts |
| **VM** | VM 1 (Windows Enterprise) |
| **Control Mapped** | NIST CSF PR.AA-03, PCI DSS Req 8.1.4 |
| **Risk Addressed** | R-002 (Credential Theft) |

**Pre-requisites:**
- Standard user account created
- RDP enabled

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Attempt RDP login with correct username and wrong password | Access denied |
| 2 | Repeat step 1 four more times (total 5 failures) | Access denied each time |
| 3 | After 5th failure, attempt login again | Account locked message appears |
| 4 | Check Windows Event Viewer for Event ID 4740 | Account lockout event logged |
| 5 | Wait 30 minutes | Account automatically unlocks |

**Evidence:** Screenshot of account lockout message and Event ID 4740

**Expected Result:** Account locks after 5 failures and unlocks after 30 minutes

---

### T-003: Weak Password Rejection

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify system rejects weak passwords that do not meet complexity requirements |
| **VM** | VM 1 (Windows Enterprise) |
| **Control Mapped** | NIST CSF PR.AA-05, ISO 27001 A.5.17 |
| **Risk Addressed** | R-002 (Credential Theft) |

**Pre-requisites:**
- Administrator access to Windows VM
- Password complexity enabled

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Command Prompt as Administrator | Command prompt opens |
| 2 | Run command: `net user lab-test-user [SYNTHETIC-TEST-CREDENTIAL] /add` | Command fails - password does not meet complexity |
| 3 | Run command: `net user lab-test-user [SYNTHETIC-TEST-CREDENTIAL] /add` | Command fails - password does not meet complexity |
| 4 | Run command: `net user lab-test-user [SYNTHETIC-TEST-CREDENTIAL] /add` | Command succeeds |
| 5 | Clean up: `net user lab-test-user /delete` | Account removed |

**Evidence:** Screenshot of weak password rejection error

**Expected Result:** Weak passwords rejected, strong password accepted

---

## 4. Endpoint Security Tests

### T-004: Windows Defender Real-time Protection

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify Microsoft Defender real-time protection is enabled |
| **VM** | VM 1 (Windows Enterprise) |
| **Control Mapped** | NIST CSF DE.CM-09, ISO 27001 A.8.7, PCI DSS Req 5 |
| **Risk Addressed** | R-003 (Ransomware) |

**Pre-requisites:**
- Administrator access to Windows VM

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open PowerShell as Administrator | PowerShell opens |
| 2 | Run command: `Get-MpComputerStatus` | Output shows Defender status |
| 3 | Verify RealTimeProtectionEnabled = True | RealTimeProtectionEnabled: True |
| 4 | Verify AntivirusEnabled = True | AntivirusEnabled: True |
| 5 | Verify BehaviorMonitorEnabled = True | BehaviorMonitorEnabled: True |

**Evidence:** Screenshot of `Get-MpComputerStatus` output

**Expected Result:** All protection features enabled

---

### T-005: EICAR Malware Detection

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify Defender detects and blocks EICAR test file |
| **VM** | VM 1 (Windows Enterprise) |
| **Control Mapped** | NIST CSF DE.CM-09, ISO 27001 A.8.7, PCI DSS Req 5 |
| **Risk Addressed** | R-003 (Ransomware) |

**Pre-requisites:**
- Defender real-time protection enabled
- Internet access

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Notepad | Notepad opens |
| 2 | Copy EICAR test string: X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H* | String copied |
| 3 | Save as C:\eicar.com | File blocked/deleted immediately |
| 4 | Open Windows Security > Protection history | Threat detected - EICAR Test File |
| 5 | Check Wazuh dashboard | Alert level 15 generated |

**Evidence:** Screenshot of Defender blocking EICAR and Wazuh alert

**Expected Result:** EICAR file blocked within 5 seconds

---

### T-006: Controlled Folder Access (CFA)

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify Controlled Folder Access blocks unauthorized applications |
| **VM** | VM 1 (Windows Enterprise) |
| **Control Mapped** | NIST CSF DE.CM-09, ISO 27001 A.8.7 |
| **Risk Addressed** | R-003 (Ransomware) |

**Pre-requisites:**
- CFA enabled via `Set-MpPreference -EnableControlledFolderAccess Enabled`
- Test script created

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create test.bat with: `echo test > C:\Users\%USERNAME%\Documents\test.txt` | File created |
| 2 | Run test.bat as standard user | Access denied or blocked |
| 3 | Check Windows Event Viewer for Event ID 1123 | CFA block event logged |
| 4 | Check Wazuh dashboard | Alert generated |

**Evidence:** Screenshot of CFA block event

**Expected Result:** Unauthorized application blocked from writing to protected folders

---

## 5. Network Security Tests

### T-007: Windows Firewall Configuration

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify Windows Firewall is enabled and correctly configured |
| **VM** | VM 1 (Windows Enterprise) |
| **Control Mapped** | NIST CSF PR.IR-01, ISO 27001 A.8.20 |
| **Risk Addressed** | R-001 (Lateral Movement) |

**Pre-requisites:**
- Administrator access to Windows VM

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open PowerShell as Administrator | PowerShell opens |
| 2 | Run command: `Get-NetFirewallProfile` | Output shows firewall status |
| 3 | Verify Domain profile Enabled = True | Enabled: True |
| 4 | Verify Private profile Enabled = True | Enabled: True |
| 5 | Verify Public profile Enabled = True | Enabled: True |
| 6 | Verify DefaultInboundAction = Block | DefaultInboundAction: Block |

**Evidence:** Screenshot of `Get-NetFirewallProfile` output

**Expected Result:** Firewall enabled on all profiles with default inbound block

---

### T-008: RDP Restriction

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify RDP is restricted to management subnet only |
| **VM** | VM 1 (Windows Enterprise), VM 3 (pfSense) |
| **Control Mapped** | NIST CSF PR.IR-01, ISO 27001 A.8.22 |
| **Risk Addressed** | R-001 (Lateral Movement) |

**Pre-requisites:**
- RDP enabled on Windows
- pfSense firewall rule configured

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | From Ubuntu VM (10.0.1.10) attempt RDP to Windows (10.0.2.10:3389) | Connection refused or timeout |
| 2 | From Management subnet (10.0.3.0/24) attempt RDP to Windows | Connection successful |
| 3 | Check pfSense logs for blocked attempt | Block rule logged |

**Evidence:** Screenshot of failed RDP connection and successful connection

**Expected Result:** RDP only accessible from management subnet

---

### T-009: Lateral Movement Prevention

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify DMZ (Ubuntu) cannot communicate with Internal (Windows) |
| **VM** | VM 2 (Ubuntu), VM 3 (pfSense) |
| **Control Mapped** | NIST CSF PR.IR-01, ISO 27001 A.8.22, PCI DSS Req 1 |
| **Risk Addressed** | R-001 (Lateral Movement) |

**Pre-requisites:**
- pfSense firewall rule blocking 10.0.1.0/24 to 10.0.2.0/24

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | SSH into Ubuntu VM (10.0.1.10) | Successful login |
| 2 | Run: `nc -zv 10.0.2.10 445` | Connection refused or timeout |
| 3 | Run: `nc -zv 10.0.2.10 3389` | Connection refused or timeout |
| 4 | Run: `nc -zv 10.0.2.10 22` | Connection refused or timeout |
| 5 | Run: `ping -c 4 10.0.2.10` | 100% packet loss |
| 6 | Check pfSense firewall logs | Block rule (Rule 3) logged |

**Evidence:** Screenshot of nc commands showing connection refused

**Expected Result:** All connections from Ubuntu to Windows blocked

---

### T-010: pfSense Default Deny Rule

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify pfSense has default deny rule on WAN interface |
| **VM** | VM 3 (pfSense) |
| **Control Mapped** | NIST CSF PR.IR-01, PCI DSS Req 1 |
| **Risk Addressed** | R-001 (Lateral Movement), R-008 (Firewall Misconfiguration) |

**Pre-requisites:**
- Access to pfSense WebGUI

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Login to pfSense WebGUI | Dashboard loads |
| 2 | Navigate to Firewall > Rules > WAN | Rules list displayed |
| 3 | Locate default deny rule | Last rule is "Default deny" |
| 4 | Verify rule action is "Deny" | Action: Deny |
| 5 | Verify rule is enabled | Enabled checkbox checked |

**Evidence:** Screenshot of WAN rules showing default deny

**Expected Result:** Default deny rule present and active on WAN

---

### T-011: pfSense Segmentation Rules

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify pfSense has correct segmentation rules |
| **VM** | VM 3 (pfSense) |
| **Control Mapped** | NIST CSF PR.IR-01, ISO 27001 A.8.22 |
| **Risk Addressed** | R-001 (Lateral Movement) |

**Pre-requisites:**
- Access to pfSense WebGUI

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Login to pfSense WebGUI | Dashboard loads |
| 2 | Navigate to Firewall > Rules > LAN | Rules list displayed |
| 3 | Verify block rule from 10.0.1.0/24 to 10.0.2.0/24 exists | Rule present with Action: Block |
| 4 | Verify allow rule for management subnet RDP exists | Rule present with Action: Allow |
| 5 | Verify outbound NAT rules exist | NAT rules configured |

**Evidence:** Screenshot of LAN rules showing block rule

**Expected Result:** Segmentation block rule present and enabled

---

### T-012: Ubuntu UFW Firewall

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify Ubuntu UFW firewall is correctly configured |
| **VM** | VM 2 (Ubuntu Web Server) |
| **Control Mapped** | NIST CSF PR.IR-01, ISO 27001 A.8.20 |
| **Risk Addressed** | R-005 (Web Server Breach) |

**Pre-requisites:**
- SSH access to Ubuntu VM
- Sudo privileges

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | SSH into Ubuntu VM (10.0.1.10) | Successful login |
| 2 | Run: `sudo ufw status verbose` | UFW status displayed |
| 3 | Verify Status = active | Status: active |
| 4 | Verify Default incoming = deny | Default: deny (incoming) |
| 5 | Verify ports 80 and 443 are allowed | 80/tcp ALLOW IN, 443/tcp ALLOW IN |
| 6 | Verify SSH allowed only from management | 22/tcp ALLOW IN 10.0.3.0/24 |

**Evidence:** Screenshot of `sudo ufw status verbose` output

**Expected Result:** UFW active with correct allow rules

---

### T-013: Ubuntu SSH Hardening

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify SSH is hardened (no password auth, no root login) |
| **VM** | VM 2 (Ubuntu Web Server) |
| **Control Mapped** | NIST CSF PR.AA-03, PCI DSS Req 2 |
| **Risk Addressed** | R-005 (Web Server Breach) |

**Pre-requisites:**
- SSH access to Ubuntu VM
- Sudo privileges

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | SSH into Ubuntu VM (10.0.1.10) | Successful login |
| 2 | Run: `grep '^PasswordAuthentication' /etc/ssh/sshd_config` | PasswordAuthentication no |
| 3 | Run: `grep '^PermitRootLogin' /etc/ssh/sshd_config` | PermitRootLogin no |
| 4 | Run: `grep '^MaxAuthTries' /etc/ssh/sshd_config` | MaxAuthTries 3 |
| 5 | Attempt SSH login with password | Permission denied (publickey) |

**Evidence:** Screenshot of sshd_config showing PasswordAuthentication no

**Expected Result:** Password authentication disabled, root login disabled

---

### T-014: Ubuntu Web Server (HTTPS)

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify web server serves HTTPS and has security headers |
| **VM** | VM 2 (Ubuntu Web Server) |
| **Control Mapped** | NIST CSF PR.DS-2, PCI DSS Req 4 |
| **Risk Addressed** | R-005 (Web Server Breach) |

**Pre-requisites:**
- Nginx installed and configured
- SSL certificate installed

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Inspect the configured certificate and run `curl -vI https://<lab-host>` from an authorized test host | Record TLS version, certificate chain, hostname validation, expiry and negotiated cipher; a browser padlock alone is not sufficient evidence |
| 2 | Check SSL/TLS version | TLS 1.2 or 1.3 only |
| 3 | Run: `curl -I https://10.0.1.10` | HTTP 200 OK |
| 4 | Verify HSTS header | Strict-Transport-Security present |
| 5 | Verify X-Frame-Options header | X-Frame-Options: DENY |

**Planned evidence:** Certificate chain and hostname validation output, TLS negotiation details, and test timestamp. Not collected.

**Expected Result:** HTTPS working, security headers present

---

## 6. Monitoring Tests

### T-015: Wazuh Failed Login Alert

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify Wazuh generates alert for failed Windows login |
| **VM** | VM 1 (Windows), VM 4 (Wazuh) |
| **Control Mapped** | NIST CSF DE.AE-1, ISO 27001 A.8.15, PCI DSS Req 10 |
| **Risk Addressed** | R-002 (Credential Theft), R-004 (Audit Failure) |

**Pre-requisites:**
- Wazuh agent installed on Windows
- Wazuh rule for Event ID 4625 configured

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Attempt RDP login with wrong password | Access denied |
| 2 | Repeat for 5 total failed attempts | Account lockout |
| 3 | Login to Wazuh dashboard (https://10.0.3.10) | Dashboard loads |
| 4 | Navigate to Alerts section | Alerts displayed |
| 5 | Search for Event ID 4625 alert | Alert appears within 5 minutes |
| 6 | Verify alert level = 10 | Level: 10 |

**Evidence:** Screenshot of Wazuh alert for failed login

**Expected Result:** Alert generated within 5 minutes of failed login

---

### T-016: Wazuh EICAR Alert

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify Wazuh generates alert for EICAR malware detection |
| **VM** | VM 1 (Windows), VM 4 (Wazuh) |
| **Control Mapped** | NIST CSF DE.CM-3, ISO 27001 A.8.16 |
| **Risk Addressed** | R-003 (Ransomware) |

**Pre-requisites:**
- Wazuh agent installed on Windows
- Defender real-time protection enabled

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Download EICAR test file | File blocked immediately |
| 2 | Login to Wazuh dashboard (https://10.0.3.10) | Dashboard loads |
| 3 | Navigate to Alerts section | Alerts displayed |
| 4 | Search for "EICAR" | Alert appears |
| 5 | Verify alert level = 15 | Level: 15 |
| 6 | Verify alert description matches | "EICAR Test File Detected" |

**Evidence:** Screenshot of Wazuh EICAR alert

**Expected Result:** Alert generated for EICAR detection

---

### T-017: Wazuh Agent Connectivity

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify all Wazuh agents are connected |
| **VM** | VM 4 (Wazuh) |
| **Control Mapped** | NIST CSF DE.CM-7, ISO 27001 A.8.15 |
| **Risk Addressed** | R-004 (Audit Failure) |

**Pre-requisites:**
- Wazuh agents installed on all VMs

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Login to Wazuh dashboard (https://10.0.3.10) | Dashboard loads |
| 2 | Navigate to Agents section | Agents list displayed |
| 3 | Verify Windows agent connected | Status: Active |
| 4 | Verify Ubuntu agent connected | Status: Active |
| 5 | Verify pfSense (syslog) connected | Status: Active |
| 6 | Check last check-in time | Less than 5 minutes ago |

**Evidence:** Screenshot of Wazuh agents list

**Expected Result:** All 3 agents show Active status

---

### T-018: pfSense Log Forwarding to Wazuh

| Attribute | Detail |
|-----------|--------|
| **Objective** | Verify pfSense forwards logs to Wazuh |
| **VM** | VM 3 (pfSense), VM 4 (Wazuh) |
| **Control Mapped** | NIST CSF DE.CM-1, ISO 27001 A.8.15 |
| **Risk Addressed** | R-001 (Lateral Movement) |

**Pre-requisites:**
- Syslog forwarding configured on pfSense

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Login to pfSense WebGUI | Dashboard loads |
| 2 | Navigate to Status > System Logs > Settings | Settings displayed |
| 3 | Verify remote syslog server = 10.0.3.10:514 | Correct IP and port |
| 4 | Trigger a firewall block (attempt RDP from Ubuntu) | Block logged |
| 5 | Check Wazuh dashboard for pfSense alert | Alert appears |

**Evidence:** Screenshot of pfSense syslog settings and Wazuh alert

**Expected Result:** pfSense logs appear in Wazuh

---

## 7. Test Execution Log

| Test ID | Tester | Start Time | End Time | Result | Notes |
|---------|--------|------------|----------|--------|-------|
| T-001 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-002 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-003 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-004 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-005 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-006 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-007 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-008 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-009 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-010 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-011 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-012 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-013 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-014 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-015 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-016 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-017 | S. Singh | May 2026 | May 2026 | Pending | - |
| T-018 | S. Singh | May 2026 | May 2026 | Pending | - |

---

## 8. Related Documents

| Document | Location |
|----------|----------|
| Testing Results | 09-Testing-and-Validation/results.md |
| pfSense Network Security | 08-Technical-Controls/pfsense-network.md |
| Windows Hardening Guide | 08-Technical-Controls/windows-hardening.md |
| Ubuntu Web Server Hardening | 08-Technical-Controls/ubuntu-web-server.md |
| Wazuh Monitoring | 08-Technical-Controls/wazuh-monitoring.md |

---

## 9. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | April 2026 | S. Singh | Initial draft |
| 0.5 | May 2026 | S. Singh | Added test procedures |
| 1.0 | May 2026 | S. Singh | Draft learning edition |

---

**End of Test Scenarios**
