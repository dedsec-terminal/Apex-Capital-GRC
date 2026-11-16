> **Historical learning appendix only:** This source chapter discusses PCI DSS 3.2.1-inspired control concepts. It is not current PCI DSS guidance, an assessment, or a compliance claim.

# PCI DSS Inspired Controls (Payment-Related)

## Overview

Apex Capital (fictional lab scenario) processes client fee debits via ACH/NEFT and advisor commission payments. Credit card processing is limited and not stored. Therefore, full PCI DSS compliance is not required. However, PCI DSS inspired controls are applied where payment data is involved.

| Payment Type | Processing Method | Cardholder Data Stored | PCI DSS Required |
|--------------|-------------------|------------------------|------------------|
| Client fee debits | ACH/NEFT | No | No (inspired only) |
| Advisor commissions | Bank transfer | No | No (inspired only) |
| Credit card payments (limited) | Third-party gateway | No | No (inspired only) |

**Note:** This engagement applies PCI DSS controls as a **security best practice framework** for financial services, not as a formal certification.

---

## 4-VM Architecture for PCI Controls

| VM | Role | PCI Requirements Addressed |
|----|------|---------------------------|
| VM 1 - Windows 11 Enterprise | Internal workstation/server | Req 2, 5, 6, 7, 8, 10 |
| VM 2 - Ubuntu Server | Public-facing web server | Req 1, 2, 4, 6 |
| VM 3 - pfSense | Firewall and segmentation | Req 1, 4, 11 |
| VM 4 - Wazuh | SIEM and monitoring | Req 10, 11 |

---

## Requirement Mapping

### Requirement 1: Install and Maintain Firewall Configuration

| Control | Description | Implementation | Evidence | Primary VM |
|---------|-------------|----------------|----------|------------|
| 1.1 | Firewall configuration standards | pfSense rules documented | Firewall rule screenshots | VM 3 |
| 1.2 | Deny all traffic by default | Default deny rule on WAN interface | pfSense rule list | VM 3 |
| 1.3 | Restrict inbound/outbound traffic | Public vs private subnet segregation | Segmentation test screenshot | VM 3 |
| 1.4 | Personal firewall configuration | Windows Defender Firewall enabled | Firewall settings screenshot | VM 1 |

### Requirement 2: Do Not Use Vendor-Supplied Defaults

| Control | Description | Implementation | Evidence | Primary VM |
|---------|-------------|----------------|----------|------------|
| 2.1 | Change default passwords | Password policy enforced | Weak password rejection | VM 1 |
| 2.2 | Remove unnecessary services | Windows service minimization, Ubuntu minimal install | Services list screenshot | VM 1, VM 2 |
| 2.3 | Configure system security parameters | CIS benchmarks, hardening guides | Hardening documentation | VM 1, VM 2 |

### Requirement 3: Protect Stored Cardholder Data

| Control | Description | Implementation | Evidence | Primary VM |
|---------|-------------|----------------|----------|------------|
| 3.1 | Minimize cardholder data storage | No cardholder data stored | Data classification policy | VM 1 |
| 3.2 | Protect stored data | NTFS permissions, data classification | Data classification policy | VM 1 |
| 3.3 | Mask PAN when displayed | Not applicable (no PAN stored) | N/A | N/A |

**Note:** Apex Capital does not store cardholder data. Client fee debits are processed via ACH/NEFT, not credit cards.

### Requirement 4: Encrypt Transmission of Cardholder Data

| Control | Description | Implementation | Evidence | Primary VM |
|---------|-------------|----------------|----------|------------|
| 4.1 | Use strong cryptography | HTTPS enforcement on web server | Browser padlock screenshot | VM 2 |
| 4.2 | Encrypt transmissions over open networks | SSH for remote access, TLS for web | SSH config, HTTPS cert | VM 2, VM 3 |

### Requirement 5: Protect All Systems Against Malware

| Control | Description | Implementation | Evidence | Primary VM |
|---------|-------------|----------------|----------|------------|
| 5.1 | Deploy anti-malware software | Microsoft Defender enabled | Defender settings screenshot | VM 1 |
| 5.2 | Keep anti-malware software current | Automatic updates enabled | Update settings screenshot | VM 1 |
| 5.3 | Anti-malware mechanisms are active | Real-time protection enabled | Real-time protection status | VM 1 |
| 5.4 | Test anti-malware mechanisms | EICAR test file detection | EICAR block screenshot | VM 1 |

### Requirement 6: Develop and Maintain Secure Systems

| Control | Description | Implementation | Evidence | Primary VM |
|---------|-------------|----------------|----------|------------|
| 6.1 | Install security patches | Patch management policy | Patch schedule documentation | VM 1, VM 2 |
| 6.2 | Develop secure applications | SSH hardening, service minimization | `sshd_config` screenshot | VM 2 |
| 6.3 | Change management process | Documented change log | Firewall rule change log | VM 3 |
| 6.4 | Separate development/test environments | Not applicable (no dev environment) | N/A | N/A |
| 6.5 | Address common coding vulnerabilities | Ubuntu server hardening | Hardening documentation | VM 2 |

### Requirement 7: Restrict Access to Cardholder Data

| Control | Description | Implementation | Evidence | Primary VM |
|---------|-------------|----------------|----------|------------|
| 7.1 | Limit access on need-to-know basis | Least privilege policy | Access control policy | VM 1 |
| 7.2 | Establish access control system | Windows user roles, separate admin accounts | User role screenshot | VM 1 |
| 7.3 | Document access privileges | Access control policy documented | Policy document | VM 1 |

### Requirement 8: Identify and Authenticate Access

| Control | Description | Implementation | Evidence | Primary VM |
|---------|-------------|----------------|----------|------------|
| 8.1 | Assign unique IDs | Individual user accounts | User list screenshot | VM 1 |
| 8.2 | Implement strong authentication | Password policy (14 char, complexity) | `net accounts` output | VM 1 |
| 8.3 | Implement multi-factor authentication | Recommended but out of scope | Residual risk recommendation | All |
| 8.4 | Lock out after invalid attempts | 5 attempts lockout policy | Lockout settings screenshot | VM 1 |
| 8.5 | Use appropriate authentication | Password authentication with complexity | Weak password rejection | VM 1 |
| 8.6 | Secure authentication data | Passwords stored with hashing | Windows default behavior | VM 1 |

### Requirement 9: Restrict Physical Access

| Control | Description | Implementation | Evidence | Primary VM |
|---------|-------------|----------------|----------|------------|
| 9.1-9.9 | Physical access controls | Out of scope (virtual environment) | N/A | N/A |

**Note:** Physical access controls are not applicable to this virtualized lab environment.

### Requirement 10: Track and Monitor All Access

| Control | Description | Implementation | Evidence | Primary VM |
|---------|-------------|----------------|----------|------------|
| 10.1 | Implement audit logging | Wazuh SIEM centralized logging | Wazuh dashboard screenshot | VM 4 |
| 10.2 | Log all access to system components | Windows Event Logs (Event ID 4625) | Event log screenshot | VM 1, VM 4 |
| 10.3 | Record audit log details | Timestamps, user IDs, source IPs | Wazuh alert details | VM 4 |
| 10.4 | Synchronize time across systems | NTP configuration | Date/time settings | All |
| 10.5 | Secure audit logs | Wazuh log retention, access controls | Wazuh configuration | VM 4 |
| 10.6 | Review audit logs | Failed login alerting | Wazuh alert screenshot | VM 4 |
| 10.7 | Retain audit logs | 90-day retention policy | Wazuh retention settings | VM 4 |

### Requirement 11: Regularly Test Security Systems

| Control | Description | Implementation | Evidence | Primary VM |
|---------|-------------|----------------|----------|------------|
| 11.1 | Run internal vulnerability scans | Not in scope (full scanning not performed) | N/A | N/A |
| 11.2 | Run external vulnerability scans | Not in scope | N/A | N/A |
| 11.3 | Perform penetration testing | Not in scope (separate engagement) | N/A | N/A |
| 11.4 | Detect intrusion | Wazuh SIEM, pfSense firewall logs | Wazuh alerts | VM 3, VM 4 |
| 11.5 | Deploy change detection | File integrity monitoring (partial) | Wazuh FIM (optional) | VM 4 |

**Testing performed in this engagement:**

| Test | Description | Result | Evidence |
|------|-------------|--------|----------|
| EICAR test | Malware detection validation | Blocked | `evidence/eicar-block.png` |
| Segmentation test | Lateral movement prevention | Blocked | `evidence/segmentation-test.png` |
| Password test | Weak password rejection | Rejected | `evidence/weak-password-rejected.png` |
| Alert test | Failed login detection | Alert generated | `evidence/wazuh-failed-login-alert.png` |

### Requirement 12: Maintain Security Policy

| Control | Description | Implementation | Evidence | Primary VM |
|---------|-------------|----------------|----------|------------|
| 12.1 | Establish security policy | 6 policies documented | `07-Policies-and-Standards/` | All |
| 12.2 | Conduct risk assessment | Risk register with 8 risks | `04-Risk-Assessment/` | All |
| 12.3 | Manage usage of critical technologies | Acceptable use policy | `07-Policies-and-Standards/acceptable-use-policy.md` | All |
| 12.4 | Define security responsibilities | Roles defined in company profile | `02-Company-Profile/` Section 4 | All |
| 12.5 | Assign information security responsibility | CISO, GRC Lead roles defined | `02-Company-Profile/` Section 4 | All |
| 12.6 | Implement security awareness | Recommended but out of scope | N/A | N/A |
| 12.7 | Screen personnel | Not applicable | N/A | N/A |
| 12.8 | Manage service providers | Vendor risk program (Planned) | R-007 in risk register | All |
| 12.9 | Incident response plan | Documented IR policy | `07-Policies-and-standards/incident-response-policy.md` | All |
| 12.10 | Test incident response plan | Recommended for Phase 2 | Residual risk recommendation | All |

---

## Historical PCI-inspired mapping presence by VM (not implementation or compliance status)

| Requirement | VM 1 (Windows) | VM 2 (Ubuntu) | VM 3 (pfSense) | VM 4 (Wazuh) | Status |
|-------------|----------------|---------------|----------------|--------------|--------|
| Req 1 (Firewall) | Partial | No | Yes | No | Planned / not executed |
| Req 2 (Defaults) | Yes | Yes | Yes | Yes | Planned / not executed |
| Req 3 (Storage) | Yes | N/A | N/A | N/A | Planned / not executed |
| Req 4 (Encryption) | No | Yes | Yes | No | Planned / not executed |
| Req 5 (Malware) | Yes | No | No | No | Planned / not executed |
| Req 6 (Secure systems) | Yes | Yes | Partial | No | Planned / not executed |
| Req 7 (Access) | Yes | No | No | No | Planned / not executed |
| Req 8 (Authentication) | Yes | Partial | No | No | Planned / not executed |
| Req 9 (Physical) | N/A | N/A | N/A | N/A | Out of Scope |
| Req 10 (Logging) | Partial | Partial | Partial | Yes | Planned / not executed |
| Req 11 (Testing) | Yes | Yes | Yes | Yes | Planned / not executed |
| Req 12 (Policy) | Yes | Yes | Yes | Yes | Planned / not executed |

---

## Evidence Index by PCI Requirement

| PCI Requirement | Control | Evidence File | Primary VM |
|----------------|---------|---------------|------------|
| Req 1 | Firewall segmentation | `evidence/segmentation-test.png` | VM 3 |
| Req 2 | Default password change | `evidence/weak-password-rejected.png` | VM 1 |
| Req 4 | HTTPS encryption | `evidence/https-padlock.png` | VM 2 |
| Req 5 | Malware detection | `evidence/eicar-block.png` | VM 1 |
| Req 7 | Access control | `evidence/access-denied.png` | VM 1 |
| Req 8 | Password policy | `evidence/net-accounts-output.png` | VM 1 |
| Req 10 | Failed login alert | `evidence/wazuh-failed-login-alert.png` | VM 4 |
| Req 11 | EICAR test | `evidence/eicar-block.png` | VM 1 |
| Req 11 | Segmentation test | `evidence/segmentation-test.png` | VM 3 |
| Req 12 | Security policies | `07-Policies-and-Standards/` | All |

---

## PCI DSS Applicability Statement

| Element | Status | Justification |
|---------|--------|---------------|
| Full PCI DSS compliance | Not required | No cardholder data stored or processed |
| Cardholder data environment (CDE) | Not applicable | No credit card numbers on systems |
| SAQ (Self-Assessment Questionnaire) | Not required | ACH/NEFT only, no card processing |
| PCI DSS inspired controls | Planned / not executed | 11 of 12 requirements addressed |

**Control implementation summary:**
- 11 requirements Proposed (inspired)
- 1 requirement out of scope (physical access)
- MFA recommended for further authentication strength

---

## PCI DSS Gap Analysis (Inspired Controls)

| Gap | Description | Risk Level | Remediation Plan |
|-----|-------------|------------|------------------|
| MFA not Proposed | No multi-factor authentication for remote access | Medium | Recommend for Phase 2 |
| Full vulnerability scanning | Not performed in this engagement | Low | Recommend separate engagement |
| Penetration testing | Not performed in this engagement | Low | Recommend separate engagement |
| Security awareness training | Not Proposed | Medium | HR to lead |

---

## PCI to NIST Cross Reference

| PCI Requirement | NIST CSF 2.0 Function | NIST Subcategory |
|----------------|----------------------|------------------|
| Req 1 | Protect (PR) | PR.IR-01 (Network segregation) |
| Req 2 | Protect (PR) | PR.PS-01 (Configuration management) |
| Req 4 | Protect (PR) | PR.DS-2 (Data in transit) |
| Req 5 | Protect (PR) | DE.CM-09 (Malware protection) |
| Req 7 | Protect (PR) | PR.AA-05 (Least privilege) |
| Req 8 | Protect (PR) | PR.AA-05 (Identity management) |
| Req 10 | Detect (DE) | DE.CM-7 (Log collection) |
| Req 11 | Detect (DE) | DE.AE-3 (Detection testing) |
| Req 12 | Govern (GV) | GV.PO-1 (Policies) |

---

**End of PCI DSS Inspired Controls Mapping**
