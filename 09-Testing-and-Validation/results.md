> **Execution status:** No VM tests have been run. Every result/criteria below describes a plan or expected outcome, not a pass.

> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Test Plan and Expected Outcomes

**Execution date:** Not set; tests remain unrun.
**Version:** 1.0
**Publication classification:** Public fictional learning project
**Proposed owner role:** GRC lead

---

## 1. Overview

This document records a proposed validation plan and expected outcomes for the fictional Apex lab. None of the tests has been executed. The test scenarios are in `09-Testing-and-Validation/test-scenarios.md`.

**Proposed lab environment:** Four-VM design (Windows, Ubuntu, pfSense, Wazuh); no guests were registered at the readiness check.

**Execution period:** None; tests not run.

---

## 2. Test Summary

| Test ID | Test Name | Status | Expected outcome (not observed) | Planned evidence location (not collected) |
|---------|-----------|--------|--------|-------------------|
| T-001 | Password Policy Enforcement | Planned / not executed | Weak password rejected | evidence/weak-password-rejected.png |
| T-002 | Account Lockout | Planned / not executed | Account locked after 5 failures | evidence/account-lockout.png |
| T-003 | Windows Defender Real-time Protection | Planned / not executed | Defender active and blocking | evidence/defender-status.png |
| T-004 | EICAR Malware Detection | Planned / not executed | EICAR file blocked immediately | evidence/eicar-block.png |
| T-005 | Controlled Folder Access | Planned / not executed | Unauthorized app blocked | evidence/cfa-block.png |
| T-006 | Windows Firewall | Planned / not executed | Firewall enabled, RDP restricted | evidence/firewall-rules.png |
| T-007 | Lateral Movement Prevention | Planned / not executed | Ubuntu cannot reach Windows | evidence/segmentation-test.png |
| T-008 | pfSense Firewall Rules | Planned / not executed | Default deny, specific allows only | evidence/pfsense-rules.png |
| T-009 | Ubuntu UFW Firewall | Planned / not executed | Ports 80,443 only | evidence/ubuntu-ufw-status.png |
| T-010 | Ubuntu SSH Hardening | Planned / not executed | Password auth disabled | evidence/ubuntu-ssh-config.png |
| T-011 | Wazuh Failed Login Alert | Planned / not executed | Alert generated for failed RDP | evidence/wazuh-failed-login-alert.png |
| T-012 | Wazuh EICAR Alert | Planned / not executed | Alert level 15 generated | evidence/wazuh-eicar-alert.png |
| T-013 | Wazuh Agent Connectivity | Planned / not executed | All 3 agents connected | evidence/wazuh-agents.png |

---

## 3. Detailed Test Procedures and Expected Outcomes

### T-001: Password Policy Enforcement

| Attribute | Detail |
|-----------|--------|
| Test Date | Execution date: not set |
| Tester role | To be assigned |
| VM | VM 1 (Windows Enterprise) |
| Command | net accounts |
| Expected Result | Minimum password length = 14, complexity enabled, lockout threshold = 5 |
| Expected result (not observed) | Minimum password length = 14, complexity enabled, lockout threshold = 5 |

**Illustrative expected output format (not observed):**

Minimum password age (days): 1
Maximum password age (days): 90
Minimum password length: 14
Length of password history maintained: 24
Lockout threshold: 5
Lockout duration (minutes): 30
Lockout observation window (minutes): 30

**Weak Password Rejection Test:**

| Attempt | Password | Result |
|---------|----------|--------|
| 1 | [SYNTHETIC-TEST-CREDENTIAL] | Rejected - does not meet complexity |
| 2 | [SYNTHETIC-TEST-CREDENTIAL] | Rejected - does not meet complexity |
| 3 | [SYNTHETIC-TEST-CREDENTIAL] | Planned / not executed |

**Execution status:** Planned / not executed
---

### T-002: Account Lockout

| Attribute | Detail |
|-----------|--------|
| Test Date | Execution date: not set |
| Tester role | To be assigned |
| VM | VM 1 (Windows Enterprise) |
| Test Procedure | 5 consecutive failed RDP login attempts |
| Expected Result | Account locked after 5 failures |
| Expected result (not observed) | Account locked after 5 failures, lockout duration 30 minutes |

**Illustrative event fields to collect if observed (no event captured):**

Log Name: Security
Source: Microsoft-Windows-Security-Auditing
Event ID: 4740
Description: A user account was locked out.
Subject: Account Name: lab-user
Target Account: lab-user
Caller Computer: 10.0.3.10

**Expected outcome:** A configured detection rule generates an alert; timing and severity must be set and measured during testing.

**Execution status:** Planned / not executed
---

### T-003: Windows Defender Real-time Protection

| Attribute | Detail |
|-----------|--------|
| Test Date | Execution date: not set |
| Tester role | To be assigned |
| VM | VM 1 (Windows Enterprise) |
| Command | Get-MpComputerStatus |
| Expected Result | Real-time protection enabled |
| Expected result (not observed) | Real-time protection enabled, cloud protection active |

**Illustrative expected output format (not observed):**

AntivirusEnabled              : True
RealTimeProtectionEnabled     : True
BehaviorMonitorEnabled        : True
IoavProtectionEnabled         : True
OnAccessProtectionEnabled     : True
CloudProtectionEnabled        : True
TamperProtectionEnabled       : True

**Execution status:** Planned / not executed
---

### T-004: EICAR Malware Detection

| Attribute | Detail |
|-----------|--------|
| Test Date | Execution date: not set |
| Tester role | To be assigned |
| VM | VM 1 (Windows Enterprise) |
| Test Procedure | Download EICAR test file from eicar.org |
| Expected Result | File blocked and quarantined |
| Expected result (not observed) | File blocked within a lab-defined observation window, quarantined |

**Defender Detection:**

Threat Name: EICAR Test File
Detection Time: Execution date: not set 14:23:05
Status: Removed (Quarantined)
Action: Blocked
Source: Download

**Wazuh Alert:** Alert level 15 generated.

**Execution status:** Planned / not executed
---

### T-005: Controlled Folder Access (CFA)

| Attribute | Detail |
|-----------|--------|
| Test Date | Execution date: not set |
| Tester role | To be assigned |
| VM | VM 1 (Windows Enterprise) |
| Test Procedure | Unauthorized script attempts to write to Documents folder |
| Expected Result | Access blocked by CFA |
| Expected result (not observed) | Access blocked, Event ID 1123 logged |

**Event Log Entry (Event ID 1123):**

Log Name: Microsoft-Windows-Windows Defender/Operational
Event ID: 1123
Description: Controlled Folder Access blocked an application.
Application: C:\temp\test.exe
Protected Folder: C:\Users\lab-user\Documents

**Execution status:** Planned / not executed
---

### T-006: Windows Firewall

| Attribute | Detail |
|-----------|--------|
| Test Date | Execution date: not set |
| Tester role | To be assigned |
| VM | VM 1 (Windows Enterprise) |
| Command | Get-NetFirewallProfile |
| Expected Result | Firewall enabled on all profiles |
| Expected result (not observed) | Firewall enabled on Domain, Private, Public profiles |

**Illustrative expected output format (not observed):**

| Profile | Enabled | Default Inbound | Default Outbound |
|---------|---------|-----------------|------------------|
| Domain | True | Block | Allow |
| Private | True | Block | Allow |
| Public | True | Block | Allow |

**RDP Restriction Rule Present:** Yes - Block RDP from 10.0.1.0/24

**Execution status:** Planned / not executed
---

### T-007: Lateral Movement Prevention

| Attribute | Detail |
|-----------|--------|
| Test Date | Execution date: not set |
| Tester role | To be assigned |
| VM | VM 2 (Ubuntu) to VM 1 (Windows) |
| Test Procedure | Attempt connections from Ubuntu (10.0.1.10) to Windows (10.0.2.10) |
| Expected Result | All connections refused |
| Expected result (not observed) | All connections refused or timeout |

**Test Results:**

| Port | Service | Command | Result |
|------|---------|---------|--------|
| 445 | SMB | nc -zv 10.0.2.10 445 | Connection refused |
| 3389 | RDP | nc -zv 10.0.2.10 3389 | Connection refused |
| 22 | SSH | nc -zv 10.0.2.10 22 | Connection refused |
| ICMP | Ping | ping -c 4 10.0.2.10 | 100% packet loss (illustrative expected output only) |

**pfSense Log Entry:**

Time: Execution date: not set 14:30:22
Interface: LAN
Source: 10.0.1.10:54321
Destination: 10.0.2.10:445
Protocol: TCP
Action: Block
Rule: 3 (Block DMZ to Internal)

**Execution status:** Planned / not executed
---

### T-008: pfSense Firewall Rules

| Attribute | Detail |
|-----------|--------|
| Test Date | Execution date: not set |
| Tester role | To be assigned |
| VM | VM 3 (pfSense) |
| Command | pfSense WebGUI > Firewall > Rules |
| Expected Result | Default deny, specific allow rules only |
| Expected result (not observed) | Rules configured as expected |

**WAN Rules Summary:**

| Rule | Source | Destination | Port | Action |
|------|--------|-------------|------|--------|
| 1 | Any | 10.0.1.10 | 80 | Allow |
| 2 | Any | 10.0.1.10 | 443 | Allow |
| 3 | 10.0.3.0/24 | 10.0.1.10 | 22 | Allow |
| 4 | Any | Any | Any | Deny (Default) |

**LAN Rules Summary:**

| Rule | Source | Destination | Port | Action |
|------|--------|-------------|------|--------|
| 1 | 10.0.2.10 | Any | 80,443 | Allow |
| 2 | 10.0.2.10 | 10.0.3.10 | 1514 | Allow |
| 3 | 10.0.1.0/24 | 10.0.2.0/24 | Any | Block |
| 4 | Any | Any | 3389 | Block |
| 5 | 10.0.3.0/24 | 10.0.2.10 | 3389 | Allow |

**Execution status:** Planned / not executed
---

### T-009: Ubuntu UFW Firewall

| Attribute | Detail |
|-----------|--------|
| Test Date | Execution date: not set |
| Tester role | To be assigned |
| VM | VM 2 (Ubuntu Web Server) |
| Command | sudo ufw status verbose |
| Expected Result | Default deny incoming, allow 80,443 only |
| Expected result (not observed) | Correct configuration verified |

**Illustrative expected output format (not observed):**

Status: active
Default: deny (incoming), allow (outgoing), disabled (routed)

| To | Action | From |
|----|--------|------|
| 80/tcp | ALLOW IN | Anywhere |
| 443/tcp | ALLOW IN | Anywhere |
| 22/tcp | ALLOW IN | 10.0.3.0/24 |

**Execution status:** Planned / not executed
---

### T-010: Ubuntu SSH Hardening

| Attribute | Detail |
|-----------|--------|
| Test Date | Execution date: not set |
| Tester role | To be assigned |
| VM | VM 2 (Ubuntu Web Server) |
| Command | sudo cat /etc/ssh/sshd_config |
| Expected Result | Password authentication disabled, root login disabled |
| Expected result (not observed) | PasswordAuthentication no, PermitRootLogin no |

**Key Configuration Values:**

| Setting | Value |
|---------|-------|
| PermitRootLogin | no |
| PasswordAuthentication | no |
| PubkeyAuthentication | yes |
| MaxAuthTries | 3 |
| ClientAliveInterval | 300 |
| ClientAliveCountMax | 2 |

**Execution status:** Planned / not executed
---

### T-011: Wazuh Failed Login Alert

| Attribute | Detail |
|-----------|--------|
| Test Date | Execution date: not set |
| Tester role | To be assigned |
| VM | VM 4 (Wazuh) |
| Test Procedure | Trigger failed RDP login on Windows (Event ID 4625) |
| Expected Result | Wazuh generates alert level 10 |
| Expected result (not observed) | Alert generated within 2 minutes |

**Alert Details:**

{
  "rule": {
    "id": "100001",
    "level": 10,
    "description": "Windows Failed Login Attempt"
  },
  "agent": {
    "name": "windows-enterprise-01",
    "ip": "10.0.2.10"
  },
  "data": {
    "win": {
      "eventID": 4625,
      "account": "lab-user",
      "sourceIp": "10.0.3.10"
    }
  }
}

**Execution status:** Planned / not executed
---

### T-012: Wazuh EICAR Alert

| Attribute | Detail |
|-----------|--------|
| Test Date | Execution date: not set |
| Tester role | To be assigned |
| VM | VM 4 (Wazuh) |
| Test Procedure | Trigger EICAR test file download on Windows |
| Expected Result | Wazuh generates alert level 15 |
| Expected result (not observed) | Alert generated immediately |

**Alert Details:**

{
  "rule": {
    "id": "100010",
    "level": 15,
    "description": "EICAR Test File Detected - Malware Test"
  },
  "agent": {
    "name": "windows-enterprise-01",
    "ip": "10.0.2.10"
  },
  "data": {
    "threat": "EICAR Test File",
    "action": "blocked"
  }
}

**Execution status:** Planned / not executed
---

### T-013: Wazuh Agent Connectivity

| Attribute | Detail |
|-----------|--------|
| Test Date | Execution date: not set |
| Tester role | To be assigned |
| VM | VM 4 (Wazuh) |
| Command | Wazuh Dashboard > Agents |
| Expected Result | All 3 agents connected |
| Expected result (not observed) | All 3 agents connected and active |

**Agent Status Summary:**

| Agent Name | IP Address | Status | Last Check In |
|------------|------------|--------|---------------|
| windows-enterprise-01 | 10.0.2.10 | Active | Execution date: not set 14:35:22 |
| ubuntu-web-01 | 10.0.1.10 | Active | Execution date: not set 14:35:18 |
| pfsense-01 | 10.0.3.1 | Active | Execution date: not set 14:35:20 |

**Execution status:** Planned / not executed
---

## 4. Planned Test Coverage by VM (None Executed)

| VM | Cases defined | Execution status | Results |
|---|---:|---|---|
| VM 1 (Windows Enterprise) | 6 | Not run | No outcome recorded |
| VM 2 (Ubuntu Web Server) | 2 | Not run | No outcome recorded |
| VM 3 (pfSense) | 2 | Not run | No outcome recorded |
| VM 4 (Wazuh) | 3 | Not run | No outcome recorded |

---
## 5. Framework References in Planned Cases (Not Tested)

| Framework reference | Role in plan | Execution status |
|---|---|---|
| NIST CSF 2.0 | Proposed outcome crosswalk | Not tested |
| ISO/IEC 27001:2022 | Proposed Annex A references | Not tested |
| Historical PCI DSS 3.2.1-inspired learning material | Historical reference only; not current PCI guidance | Not tested |

---
## 6. Evidence Requested (Not Collected)

| Evidence ID | Description | Location |
|-------------|-------------|----------|
| EV-001 | Password policy output | evidence/windows/net-accounts.png |
| EV-002 | Weak password rejection | evidence/windows/weak-password-reject.png |
| EV-003 | Account lockout event | evidence/windows/account-lockout.png |
| EV-004 | Defender status | evidence/windows/defender-status.png |
| EV-005 | EICAR block | evidence/windows/eicar-block.png |
| EV-006 | CFA block event | evidence/windows/cfa-block.png |
| EV-007 | Firewall rules | evidence/windows/firewall-rules.png |
| EV-008 | Segmentation test | evidence/windows/segmentation-test.png |
| EV-009 | pfSense rules | evidence/pfsense/rules.png |
| EV-010 | pfSense block log | evidence/pfsense/block-log.png |
| EV-011 | Ubuntu UFW status | evidence/ubuntu/ufw-status.png |
| EV-012 | Ubuntu SSH config | evidence/ubuntu/ssh-config.png |
| EV-013 | Wazuh failed login alert | evidence/wazuh/failed-login-alert.png |
| EV-014 | Wazuh EICAR alert | evidence/wazuh/eicar-alert.png |
| EV-015 | Wazuh agents list | evidence/wazuh/agents-list.png |

---

## 7. Conclusion

No VM test has been executed. The source chapter contains illustrative procedures and expected outcomes only. Control effectiveness, framework conformance, and risk reduction have not been assessed.

**Planned validation topics (not achieved outcomes):**

- Validate the proposed authentication baseline and lockout behavior
- Verify endpoint protection status and safe test handling
- Test permitted and prohibited paths across the DMZ/internal boundary
- Review exported rules, ordering, NAT and default-deny behavior
- Trace a synthetic event through collection, parsing, alerting and retention
- Verify configured endpoints enroll and deliver telemetry

**Recommendation:** Do not use this design as a production authorization. Implement in an isolated lab, validate each control with retained evidence, and obtain organizational review before any operational use.

---

**End of Testing and Validation Results**
