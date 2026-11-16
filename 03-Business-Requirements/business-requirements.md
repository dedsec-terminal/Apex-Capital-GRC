> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Business & Security Requirements

## Core Business Requirements

| ID | Requirement | Priority | Business Driver | Framework Mapping | Proposed evidence to collect (not collected) |
|----|-------------|----------|-----------------|-------------------|-------------------------|
| **BR-01** | Protect confidentiality, integrity, and availability of client financial data and PII (PAN, Aadhaar masked, bank details, demat information) | Critical | Fictional India-based context; legal applicability requires review | NIST CSF PR.DS, ISO 27001 A.8 | Access control policy, encryption (HTTPS/SSH), backup documentation |
| **BR-02** | Enable secure remote access for 150 remote advisors to internal systems and client data | Critical | Hybrid workforce model, client service delivery | NIST CSF 2.0 PR.AA / PR.IR; ISO/IEC 27001:2022 A.5.15 / A.5.18 | pfSense firewall rules restricting RDP, VPN configuration |
| **BR-03** | Implement network segmentation to isolate public-facing web servers from internal Windows systems | Critical | Prevent lateral movement in case of web server compromise | NIST CSF PR.IR-01, PCI Req 1 | pfSense firewall rules blocking DMZ to internal traffic |
| **BR-04** | Enforce least privilege and strong access controls for all users and systems | High | Prevent unauthorized access to portfolio management systems | NIST CSF PR.AA, ISO 27001 A.5.15 / A.5.18 | Windows local user roles, separate admin accounts |
| **BR-05** | Deploy robust endpoint detection and protection on all Windows workstations and servers | High | Ransomware prevention, malware detection | PCI Req 5, NIST CSF PR.PS | Microsoft Defender, EICAR test, Controlled Folder Access |
| **BR-06** | Secure payment-related processes (client fee debits via ACH/NEFT, advisor commission payments) | High | RBI payment guidelines, client trust | PCI DSS (Inspired), RBI guidelines | Network segmentation, access restriction, transaction logging |
| **BR-07** | Maintain comprehensive logging and monitoring for detection, incident response, and audit readiness | High | Evidence needs in the fictional scenario | PCI Req 10, ISO 27001 A.8.16 | Wazuh SIEM, failed login alerts, centralized logging |
| **BR-08** | Achieve and demonstrate compliance with applicable global frameworks (NIST CSF, ISO 27001) and Potential Indian regulatory obligations, if applicable after legal analysis | High | Hypothetical stakeholder assurance needs | NIST CSF, ISO 27001, SEBI (CISF) | Framework mapping documentation, evidence repository |
| **BR-09** | Minimize attack surface on internet-facing assets (customer portal, remote access points) | High | Reduce exposure to scanning, exploitation | NIST CSF PR.PS, CIS benchmarks | Ubuntu SSH hardening, UFW firewall, restricted SSH source, key-based authentication, and hardened service configuration |
| **BR-10** | Support effective incident response and business continuity with documented procedures | Medium | Ransomware preparedness, operational resilience | NIST CSF RS, ISO 27001 A.5.24 / A.5.26 | Incident response policy, backup strategy, escalation contacts |

---

## Security Requirements (Technical Translation)

| Requirement ID | Business Driver | Technical Security Requirement | Implementation Method | Validation Test |
|----------------|-----------------|-------------------------------|----------------------|-----------------|
| **BR-01** | Data protection | Data encrypted at rest and in transit | HTTPS for web, SSH for remote access, BitLocker for Windows | TLS configuration and certificate validation output; SSH negotiated cipher and host-key evidence |
| **BR-02** | Secure remote access | No direct RDP from public internet to Windows | pfSense firewall rule blocking RDP (3389) from WAN interface | RDP connection from internet fails |
| **BR-03** | Network segmentation | pfSense firewall blocks all traffic from Ubuntu (DMZ) to Windows (Internal) | Firewall rule: Block source Ubuntu subnet to Windows subnet | `nc -zv` from Ubuntu to Windows fails |
| **BR-04** | Access control | Separate user and admin accounts, password policy enforced | Local security policy, `net accounts` configuration | Weak password "[SYNTHETIC-TEST-CREDENTIAL]" rejected |
| **BR-05** | Endpoint protection | Real-time malware scanning with alerts | Microsoft Defender, Cloud-delivered protection enabled | EICAR test file downloaded → blocked within a lab-defined observation window |
| **BR-06** | Payment security | Payment systems accessible only to authorized finance users (3 users) | Windows user group restriction, folder permissions | Unauthorized user cannot access payment folder |
| **BR-07** | Logging & monitoring | Centralized log collection with failed login alerts | Wazuh agent on Windows, rule for Event ID 4625 | Failed RDP login → Wazuh alert within minutes |
| **BR-08** | Compliance | Documented evidence for each control | Test records and screenshots, to be collected after execution | Evidence catalog with 15+ screenshots |
| **BR-09** | Attack surface reduction | Minimal services running, firewall enabled | UFW deny incoming, SSH key auth, fail2ban | `nmap` scan shows only required ports |
| **BR-10** | Incident response | Documented IR plan with roles and contacts | Written policy, tested alert workflow | IR plan document, alert notification test |

---

## 4-VM Architecture Reference

| VM | Hostname | IP Address | Subnet | Role |
|----|----------|------------|--------|------|
| VM 1 | Windows-Enterprise | 10.0.2.10 | Internal (10.0.2.0/24) | Workstation / Server |
| VM 2 | Ubuntu-Web | 10.0.1.10 | DMZ (10.0.1.0/24) | Public Web Server |
| VM 3 | pfSense | 10.0.1.1, 10.0.2.1, 10.0.3.1 | All | Firewall / Router |
| VM 4 | Wazuh-SIEM | 10.0.3.10 | Management (10.0.3.0/24) | SIEM / Monitoring |

---

## pfSense Firewall Rules for Security Requirements

| Rule | Interface | Source | Destination | Port | Action | Requirement Addressed |
|------|-----------|--------|-------------|------|--------|----------------------|
| 1 | WAN | Any | Ubuntu (10.0.1.10) | 80,443 | Allow | BR-01, BR-09 |
| 2 | WAN | Any | Windows (10.0.2.10) | 3389 | Block | BR-02 |
| 3 | LAN | DMZ (10.0.1.0/24) | Internal (10.0.2.0/24) | Any | Block | BR-03 |
| 4 | Management | Management (10.0.3.0/24) | Windows (10.0.2.10) | 3389 | Allow | BR-02, BR-04 |
| 5 | Management | Management (10.0.3.0/24) | Ubuntu (10.0.1.10) | 22 | Allow | BR-09 |

---

## Success Criteria

| Criterion | Target State | Validation Method | Status Target |
|-----------|--------------|-------------------|---------------|
| Scenario treatment options documented and risk-owner review recorded | Risk register includes inherent scores and unvalidated target proposals; no residual levels assigned | Risk register review, control effectiveness assessment | Proposed target; date to be set by scenario owner |
| Controls validated through testing with documented evidence | Each control has corresponding test and screenshot | Evidence repository with 10+ validated controls | Proposed target; date to be set by scenario owner |
| Policies formally documented and approved | 6 core policies written and version controlled | Policy documents in `07-Policies-and-Standards/` | Proposed target; date to be set by scenario owner |
| Audit-ready evidence repository established | Evidence organized, timestamped, and reproducible | Screenshots with validation steps in `10-Evidence/` | Proposed target; date to be set by scenario owner |
| Network segmentation verified | Ubuntu cannot communicate with Windows on any port | `nc -zv` test, pfSense log review | Proposed target; date to be set by scenario owner |
| Malware detection operational | EICAR test triggers Defender block | Screenshot of EICAR download blocked | Proposed target; date to be set by scenario owner |
| Failed login alerting active | Wazuh dashboard shows failed login events | Alert screenshot with timestamp | Proposed target; date to be set by scenario owner |

---

## Constraints & Assumptions

| Type | Description |
|------|-------------|
| **Technical Constraint** | Implementation limited to local VM environment (Windows Enterprise, Ubuntu, pfSense, Wazuh) |
| **Technical Constraint** | No cloud services (AWS, Azure) used |
| **Budget Constraint** | Only open-source or built-in Windows tools (no third-party commercial software) |
| **Scope Constraint** | Full penetration testing and third-party vendor assessments excluded |
| **Assumption** | Client provides administrative access to Windows and Ubuntu VMs |
| **Assumption** | Existing network infrastructure supports VLANs/subnetting for pfSense |
| **Assumption** | No regulatory applicability or compliance conclusion is made. SEBI obligations require separate legal and applicability analysis; NIST/ISO crosswalks do not establish them. |

---

## Requirements Traceability Matrix

| Business Requirement | Technical Implementation | Test Validation | Evidence File |
|---------------------|-------------------------|-----------------|---------------|
| BR-01 | HTTPS, SSH, BitLocker | TLS protocol/cipher and certificate validation output | `evidence/encryption-https.png` |
| BR-02 | pfSense firewall block RDP from WAN | RDP connection from internet fails | `evidence/firewall-rdp-block.png` |
| BR-03 | pfSense block rule | `nc -zv` connection refused | `evidence/segmentation-block.png` |
| BR-04 | Password policy (14 char, lockout) | "[SYNTHETIC-TEST-CREDENTIAL]" rejected | `evidence/weak-password-reject.png` |
| BR-05 | Microsoft Defender + CFA | EICAR blocked | `evidence/eicar-block.png` |
| BR-06 | Finance user group restriction | Unauthorized access denied | `evidence/payment-access-denied.png` |
| BR-07 | Wazuh SIEM + Event ID 4625 | Failed login alert | `evidence/wazuh-failed-login.png` |
| BR-08 | Framework mapping table | Cross-reference complete | `06-Framework-Mapping/` |
| BR-09 | UFW + SSH hardening | `nmap` limited ports | `evidence/ubuntu-nmap-scan.png` |
| BR-10 | IR policy document | Document approved | `07-Policies/incident-response-policy.md` |

---

**End of Business & Security Requirements**
