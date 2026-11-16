> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Framework Mapping

## 1. Overview

This document maps the Proposed security controls across four virtual machines to three recognized frameworks.

| VM | Role | Primary Frameworks |
|----|------|---------------------|
| VM 1 - Windows 11 Enterprise | Internal workstation/server | NIST CSF, ISO 27001, PCI DSS |
| VM 2 - Ubuntu Server | Public-facing web server | NIST CSF, ISO 27001 |
| VM 3 - pfSense | Firewall and segmentation | NIST CSF, ISO 27001, PCI DSS |
| VM 4 - Wazuh | SIEM and monitoring | NIST CSF, ISO 27001, PCI DSS |

| Framework | Version | Application |
|-----------|---------|-------------|
| NIST Cybersecurity Framework (CSF) | 2.0 | Risk assessment, controls mapping, incident response |
| ISO/IEC 27001 | 2022 | Information Security Management System (ISMS) |
| PCI DSS (Inspired) | v3.2.1 | Payment data protection, authentication, logging |

**Note:** This fictional learning scenario uses selected legacy PCI DSS 3.2.1 concepts as historical inspiration only. It is not a current PCI DSS mapping, assessment, or certification.

---

## 2. 4-VM Architecture for Framework Mapping

The following diagram illustrates how each VM contributes to the three frameworks:

**VM 1 - Windows 11 Enterprise**
- NIST CSF: Protect (PR), Detect (DE)
- ISO 27001: A.8 (Access Control, Malware, Logging)
- PCI DSS: Req 5 (Malware), Req 8 (Authentication), Req 10 (Logging)

**VM 2 - Ubuntu Server**
- NIST CSF: Identify (ID), Protect (PR)
- ISO 27001: A.8 (Network Security, Hardening)
- PCI DSS: Req 2 (Defaults), Req 4 (Encryption), Req 6 (Secure Systems)

**VM 3 - pfSense**
- NIST CSF: Protect (PR), Detect (DE)
- ISO 27001: A.8.20, A.8.22 (Network Security)
- PCI DSS: Req 1 (Firewall), Req 4 (Encryption), Req 11 (Testing)

**VM 4 - Wazuh**
- NIST CSF: Detect (DE), Respond (RS)
- ISO/IEC 27001:2022 Annex A.8.15 and A.8.16 (proposed references)
- PCI DSS: Req 10 (Tracking), Req 11 (Testing)

---

## 3. NIST CSF 2.0 Proposed Outcome Crosswalk

### 3.1 NIST CSF Functions

| Function | Description | Proposed Controls | Evidence Location | Primary VM |
|----------|-------------|---------------------|-------------------|------------|
| Govern (GV) | Establish security strategy, policies, and risk management | Risk register, security policies, executive summary | `04-Risk-Assessment/`, `07-Policies-and-Standards/` | All |
| Identify (ID) | Understand assets, risks, and business environment | Asset inventory, risk assessment, threat analysis | `04-Risk-Assessment/risk-assessment.md` | VM 2, All |
| Protect (PR) | Implement safeguards to protect assets | Password policy, access control, firewall segmentation, endpoint protection | `07-Policies-and-Standards/`, `08-Technical-Controls/` | VM 1, VM 2, VM 3 |
| Detect (DE) | Identify security events in real-time | Wazuh SIEM, failed login alerts, malware detection | `08-Technical-Controls/wazuh-monitoring.md` | VM 4 |
| Respond (RS) | Contain and mitigate security incidents | Incident response policy, alerting workflow | `07-Policies-and-Standards/incident-response-policy.md` | VM 4 |
| Recover (RC) | Restore operations after an incident | Backup documentation, recovery procedures | `08-Technical-Controls/windows-hardening.md` | VM 1 |

### 3.2 NIST CSF Category Mapping

| Category | Subcategory | Control Proposed | Evidence | Primary VM |
|----------|-------------|---------------------|----------|------------|
| GV.PO | Policy and procedures are established | 6 security policies documented | `07-Policies-and-Standards/` | All |
| GV.RM | Risk management processes are established | Risk register with 8 identified risks | `04-Risk-Assessment/risk-register.md` | All |
| ID.AM | Assets are inventoried and managed | 4-VM asset inventory table | Below | All |
| ID.RA | Risks are identified and analyzed | Risk heatmap, detailed risk analysis | `04-Risk-Assessment/risk-heatmap.md` | All |
| PR.AA | Identities and credentials are managed | Password policy (14 char, lockout), user roles | `07-Policies-and-Standards/password-policy.md` | VM 1 |
| PR.IR-01 | Network segregation enforced | pfSense firewall, public vs private subnets | `08-Technical-Controls/pfsense-network.md` | VM 3 |
| PR.DS | Data is protected at rest and in transit | HTTPS, SSH encryption | `08-Technical-Controls/ubuntu-web-server.md` | VM 2 |
| PR.PS | Malware protection is Proposed | Microsoft Defender, EICAR testing | `08-Technical-Controls/windows-hardening.md` | VM 1 |
| DE.AE | Security events are analyzed | Wazuh SIEM, failed login alerts | `08-Technical-Controls/wazuh-monitoring.md` | VM 4 |
| DE.CM | Systems are monitored for threats | Wazuh agent on Windows, log collection | `08-Technical-Controls/wazuh-monitoring.md` | VM 4 |
| RS.AN | Incident investigations are performed | Incident response policy, alert triage | `07-Policies-and-Standards/incident-response-policy.md` | VM 4 |
| RS.MI | Incidents are contained and eradicated | Documented IR plan, escalation contacts | `07-Policies-and-Standards/incident-response-policy.md` | VM 3, VM 4 |
| RC.RP | Recovery plans are executed | Backup and recovery procedures | `08-Technical-Controls/windows-hardening.md` | VM 1 |

### 3.3 Asset Inventory (4-VM)

| Asset ID | VM | Hostname | IP Address | Subnet | NIST Classification |
|----------|-----|----------|------------|--------|---------------------|
| A-001 | VM 1 | Windows-Enterprise | 10.0.2.10 | Internal | High |
| A-002 | VM 2 | Ubuntu-Web | 10.0.1.10 | Public (DMZ) | Medium |
| A-003 | VM 3 | pfSense | 10.0.1.1, 10.0.2.1, 10.0.3.1 | All | High |
| A-004 | VM 4 | Wazuh-SIEM | 10.0.3.10 | Management | Medium |

### 3.4 Proposed NIST CSF mapping presence by VM (not implementation status)

| VM | Govern mapping | Identify mapping | Protect mapping | Detect mapping | Respond mapping | Recover mapping |
|-----|--------|----------|---------|--------|---------|---------|
| VM 1 (Windows) | Proposed / not assessed | Yes | Proposed / not assessed | Yes | Not assessed; candidate scope gap | Proposed / not assessed |
| VM 2 (Ubuntu) | Proposed / not assessed | Yes | Proposed / not assessed | Not assessed; candidate scope gap | No | Not assessed; candidate scope gap |
| VM 3 (pfSense) | Proposed / not assessed | Yes | Proposed / not assessed | Yes | Proposed / not assessed | Not assessed; candidate scope gap |
| VM 4 (Wazuh) | Proposed / not assessed | Yes | Not assessed; candidate scope gap | Proposed / not assessed | Yes | Not assessed; candidate scope gap |

---

## 4. ISO 27001:2022 Mapping

### 4.1 Clauses 4-10 (ISMS Requirements)

| Clause | Requirement | How Addressed | Evidence Location | Primary VM |
|--------|-------------|---------------|-------------------|------------|
| Clause 4 | Context of the organization | Company profile, business requirements, 4-VM architecture | `02-Company-Profile/`, `03-Business-Requirements/` | All |
| Clause 5 | Leadership and commitment | Executive summary, policy approvals, CISO accountability | `01-Executive-Summary/`, `07-Policies-and-Standards/` | All |
| Clause 6 | Planning (risk assessment) | Risk assessment methodology, risk register, treatment plan | `04-Risk-Assessment/` | All |
| Clause 7 | Support (resources, competence) | Documentation structure, evidence repository | `10-Evidence/` | All |
| Clause 8 | Operation (controls implementation) | Technical controls on 4 VMs, testing and validation | `08-Technical-Controls/`, `09-Testing-and-Validation/` | VM 1,2,3,4 |
| Clause 9 | Performance evaluation | Planned Validation, test results, evidence catalog | `09-Testing-and-Validation/results.md` | VM 1,2,3,4 |
| Clause 10 | Improvement | Residual risk review, recommendations, roadmap | `11-Residual-Risk/` | All |

### 4.2 Annex A Control References (Proposed; Not Assessed)

| Control ID | Control Description | Planned / not executed | Evidence Location | Primary VM |
|------------|---------------------|-------------|-------------------|------------|
| A.5.1 | Policies for information security | Proposed / not assessed | `07-Policies-and-Standards/` (6 policies) | All |
| A.5.2 | Information security roles and responsibilities | Proposed / not assessed | `02-Company-Profile/` Section 4 | All |
| A.5.15 | Access control policy | Proposed / not assessed | `07-Policies-and-Standards/access-control-policy.md` | VM 1 |
| A.5.23 | Information security for use of cloud services | Proposed / not assessed | R-007 documented, vendor assessment Planned | All |
| A.5.24 | Incident management planning | Proposed / not assessed | `07-Policies-and-Standards/incident-response-policy.md` | VM 4 |
| A.8.2 | Privileged access rights | Proposed / not assessed | Access control policy, separate admin accounts | VM 1 |
| A.5.18 | Access rights review | Proposed / not assessed | Windows hardening, local user role separation | VM 1 |
| A.8.4 | Access to source code | Not assessed; candidate scope gap | Out of scope | N/A |
| A.8.7 | Protection against malware | Proposed / not assessed | Microsoft Defender, EICAR testing | VM 1 |
| A.8.8 | Management of technical vulnerabilities | Proposed / not assessed | OS hardening, patching schedule documented | VM 1, VM 2 |
| A.8.9 | Configuration management | Proposed / not assessed | Windows hardening, Ubuntu SSH hardening, pfSense rules | VM 1, VM 2, VM 3 |
| A.5.33 | Protection of records | Proposed / not assessed | Wazuh log retention configured | VM 4 |
| A.8.13 | Backup and recovery | Proposed / not assessed | Backup procedures documented | VM 1 |
| A.8.15 | Logging and monitoring | Proposed / not assessed | Wazuh SIEM implementation | VM 4 |
| A.8.16 | Monitoring activities | Proposed / not assessed | Wazuh agent, failed login alerts | VM 4 |
| A.8.20 | Networks security | Proposed / not assessed | pfSense segmentation, firewall rules | VM 3 |
| A.8.21 | Security of network services | Proposed / not assessed | pfSense configuration, service minimization | VM 3 |
| A.8.22 | Segregation of networks | Proposed / not assessed | Public vs private subnets, DMZ isolation | VM 3 |
| A.8.24 | Use of cryptography | Proposed / not assessed | HTTPS, SSH encryption Proposed | VM 2 |
| A.8.25 | Secure development lifecycle | Not assessed; candidate scope gap | Out of scope | N/A |
| A.8.26 | Application security requirements | Proposed / not assessed | Ubuntu web server hardening | VM 2 |
| A.8.28 | Secure coding | Not assessed; candidate scope gap | Out of scope | N/A |
| A.8.29 | Security testing | Proposed / not assessed | EICAR test, segmentation test, password test | VM 1, VM 3 |
| A.8.30 | Outsourced development | Not assessed; candidate scope gap | Out of scope | N/A |
| A.8.31 | Separation of environments | Proposed / not assessed | Public (DMZ) vs Private subnets | VM 3 |
| A.8.32 | Change management | Proposed / not assessed | Change log documented, firewall rule review | VM 3 |
| A.5.24, A.5.26 | Incident management preparation and response | Proposed / not assessed | Incident response policy, alerting workflow | VM 4 |
| A.5.30 | ICT readiness for business continuity | Proposed / not assessed | Backup and recovery procedures documented | VM 1 |

### 4.3 Proposed Annex A Reference Coverage by VM (Not Assessed)

| VM | Proposed Controls | Partial Controls | Out of Scope |
|----|---------------------|------------------|--------------|
| VM 1 (Windows) | A.5.15, A.8.2, A.8.3, A.8.7, A.8.13 | A.8.8, A.8.9 | A.8.4, A.8.25 |
| VM 2 (Ubuntu) | A.8.9, A.8.20, A.8.21 | A.8.8, A.8.24, A.8.26 | A.8.28 |
| VM 3 (pfSense) | A.8.9, A.8.20, A.8.21, A.8.22, A.8.31 | A.8.32 | None |
| VM 4 (Wazuh) | A.8.15, A.8.16, A.8.33 | A.8.12, A.8.29 | None |

### 4.4 Source Mapping Summary (Not a Control Assessment)

> Source inclusion counts do not represent applicability, implementation, effectiveness, or compliance decisions.

| Status | Count | Controls |
|--------|-------|----------|
| Planned / not executed | 18 | A.5.1, A.5.2, A.5.15, A.5.24, A.8.2, A.8.3, A.8.7, A.8.9, A.8.13, A.8.15, A.8.16, A.8.20, A.8.21, A.8.22, A.8.31, A.8.33 |
| Proposed / not assessed | 8 | A.5.23, A.8.8, A.8.12, A.8.24, A.8.26, A.8.29, A.8.32, A.8.34 |
| Out of Scope | 4 | A.8.4, A.8.25, A.8.28, A.8.30 |

---

## 5. Historical PCI DSS 3.2.1-inspired reference (not current compliance) Mapping (Inspired)

### 5.1 PCI DSS Requirements by VM

| Requirement | Description | Proposed Control | Primary VM | Evidence |
|-------------|-------------|---------------------|------------|----------|
| Req 1 | Install and maintain firewall configuration | pfSense firewall, segmentation rules, default deny | VM 3 | `08-Technical-Controls/pfsense-network.md` |
| Req 2 | Do not use vendor-supplied defaults | Password policy enforced, default accounts disabled | VM 1, VM 2 | `07-Policies-and-Standards/password-policy.md` |
| Req 3 | Protect stored cardholder data | Not in scope (no cardholder data stored) | N/A | N/A |
| Req 4 | Encrypt transmission of cardholder data | HTTPS for web, SSH for remote access | VM 2 | `08-Technical-Controls/ubuntu-web-server.md` |
| Req 5 | Protect all systems against malware | Microsoft Defender, EICAR testing, real-time scanning | VM 1 | `08-Technical-Controls/windows-hardening.md` |
| Req 6 | Develop and maintain secure systems | OS hardening, patch management policy | VM 1, VM 2 | `08-Technical-Controls/windows-hardening.md` |
| Req 7 | Restrict access to cardholder data | Access control policy, least privilege, role separation | VM 1 | `07-Policies-and-Standards/access-control-policy.md` |
| Req 8 | Identify and authenticate access | Password policy (14 char, complexity, lockout), unique user IDs | VM 1 | `07-Policies-and-Standards/password-policy.md` |
| Req 9 | Restrict physical access | Out of scope (virtual environment) | N/A | N/A |
| Req 10 | Track and monitor all access | Wazuh SIEM, failed login alerts, Event ID 4625 logging | VM 4 | `08-Technical-Controls/wazuh-monitoring.md` |
| Req 11 | Regularly test security systems | EICAR test, segmentation test, password test, alert test | VM 1, VM 3, VM 4 | `09-Testing-and-Validation/test-scenarios.md` |
| Req 12 | Maintain information security policy | 6 security policies documented and approved | All | `07-Policies-and-Standards/` |

### 5.2 Historical PCI-inspired mapping presence by VM (not compliance status)

| Requirement | VM 1 (Windows) | VM 2 (Ubuntu) | VM 3 (pfSense) | VM 4 (Wazuh) | Status |
|-------------|----------------|---------------|----------------|--------------|--------|
| Req 1 (Firewall) | Proposed / not assessed | Not assessed; candidate scope gap | Proposed / not assessed | Not assessed; candidate scope gap | Planned / not executed |
| Req 2 (Defaults) | Proposed / not assessed | Yes | Proposed / not assessed | Yes | Planned / not executed |
| Req 3 (Storage) | Proposed / not assessed | N/A | N/A | N/A | Not Applicable |
| Req 4 (Encryption) | Not assessed; candidate scope gap | Proposed / not assessed | Yes | Not assessed; candidate scope gap | Planned / not executed |
| Req 5 (Malware) | Proposed / not assessed | Not assessed; candidate scope gap | No | Not assessed; candidate scope gap | Planned / not executed |
| Req 6 (Secure Systems) | Proposed / not assessed | Yes | Proposed / not assessed | Not assessed; candidate scope gap | Planned / not executed |
| Req 7 (Access) | Proposed / not assessed | Not assessed; candidate scope gap | No | Not assessed; candidate scope gap | Planned / not executed |
| Req 8 (Authentication) | Proposed / not assessed | Proposed / not assessed | Not assessed; candidate scope gap | No | Planned / not executed |
| Req 9 (Physical) | N/A | N/A | N/A | N/A | Out of Scope |
| Req 10 (Logging) | Proposed / not assessed | Partial | Proposed / not assessed | Proposed / not assessed | Planned / not executed |
| Req 11 (Testing) | Proposed / not assessed | Yes | Proposed / not assessed | Yes | Planned / not executed |
| Req 12 (Policy) | Proposed / not assessed | Yes | Proposed / not assessed | Yes | Planned / not executed |

### 5.3 PCI DSS Applicability Statement

| Element | Status | Justification |
|---------|--------|---------------|
| Full PCI DSS compliance | Not required | No cardholder data stored or processed |
| Cardholder data environment (CDE) | Not applicable | No credit card numbers on systems |
| SAQ (Self-Assessment Questionnaire) | Not required | ACH/NEFT only, no card processing |
| PCI DSS inspired controls | Planned / not executed | 11 of 12 requirements addressed |

---

## 6. Cross-Framework Control Mapping

This table shows how each Proposed control maps to all three frameworks and which VM is responsible:

| Proposed Control | NIST CSF 2.0 | ISO 27001:2022 | Historical PCI DSS 3.2.1-inspired reference (not current compliance) | Primary VM |
|---------------------|--------------|----------------|----------------|------------|
| pfSense network segmentation | PR.IR-01 | A.8.22 | Req 1 | VM 3 |
| Password policy (14 char, lockout) | PR.AA | A.8.2, A.8.3 | Req 8 | VM 1 |
| Microsoft Defender + EICAR testing | DE.CM-09 / PR.PS-05 | A.8.7 | Req 5 | VM 1 |
| Wazuh SIEM and alerting | DE.AE, DE.CM | A.8.15, A.8.16 | Req 10 | VM 4 |
| Ubuntu SSH hardening + UFW | PR.AA, PR.PS | A.8.20, A.8.21 | Req 2, Req 4 | VM 2 |
| Access control (least privilege) | PR.AA | A.8.2 | Req 7 | VM 1 |
| Incident response policy | ID.IM-04, RS.MI-01, RS.MI-02 | A.5.24, A.5.26 | Req 12 | VM 4 |
| Evidence repository | PR.PS-04 / DE.CM-09 | A.8.15, A.8.16 | Req 11 | All |
| Risk assessment and register | ID.RA, GV.RM | Clause 6 | Req 12 | All |
| Security policies (6 documents) | GV.PO | A.5.1 | Req 12 | All |

---

## 7. Framework Alignment Summary

### 7.1 NIST CSF 2.0

| Function | Proposed documentation or control concepts (not assessed) | Primary VM |
|----------|----------------------|------------|
| Govern (GV) | Documents proposed; not assessed | All |
| Identify (ID) | Documents proposed; not assessed | VM 2, All |
| Protect (PR) | Controls proposed; not assessed | VM 1, VM 2, VM 3 |
| Detect (DE) | Controls proposed; not assessed | VM 4 |
| Respond (RS) | Procedures proposed; not assessed | VM 4 |
| Recover (RC) | Procedures proposed; not assessed | VM 1 |

### 7.2 ISO 27001:2022

| Clause | Proposed documentation or control concepts (not assessed) | Primary VM |
|--------|----------------------|------------|
| Clause 4-10 (ISMS) | Planned / not executed | All |
| Annex A control references listed | Count is an unverified inventory, not assessment coverage | VM 1, VM 2, VM 3, VM 4 |
| Implementation status | Not assessed | VM 1, VM 2, VM 3, VM 4 |
| Applicability | Not determined | N/A |

### 7.3 Historical PCI DSS 3.2.1-inspired learning reference (not current compliance)

| Requirement Group | Historical learning scope only (not compliance status) | Primary VM |
|-------------------|----------------------|------------|
| Req 1-2 (Firewall + Defaults) | Planned / not executed | VM 2, VM 3 |
| Req 4-5 (Encryption + Malware) | Planned / not executed | VM 1, VM 2 |
| Req 6-7 (Secure systems + Access) | Planned / not executed | VM 1, VM 2 |
| Req 8-10 (Authentication + Logging) | Planned / not executed | VM 1, VM 4 |
| Req 11-12 (Testing + Policy) | Planned / not executed | VM 1, VM 3, VM 4 |
| Req 3 (Cardholder storage) | Not applicable | N/A |
| Req 9 (Physical access) | Out of scope | N/A |

---

## 8. Compliance Evidence Index

| Framework | Requirement | Evidence File | Primary VM |
|-----------|-------------|---------------|------------|
| NIST CSF | PR.IR-01 | `evidence/pfsense-segmentation-rule.png` | VM 3 |
| NIST CSF | PR.PS | `evidence/eicar-block.png` | VM 1 |
| NIST CSF | DE.CM | `evidence/wazuh-failed-login-alert.png` | VM 4 |
| ISO 27001 | A.8.7 | `evidence/eicar-block.png` | VM 1 |
| ISO 27001 | A.8.15 | `evidence/wazuh-dashboard.png` | VM 4 |
| ISO 27001 | A.8.22 | `evidence/pfsense-segmentation-rule.png` | VM 3 |
| PCI DSS | Req 5 | `evidence/eicar-block.png` | VM 1 |
| PCI DSS | Req 8 | `evidence/weak-password-rejected.png` | VM 1 |
| PCI DSS | Req 10 | `evidence/wazuh-failed-login-alert.png` | VM 4 |
| PCI DSS | Req 11 | `evidence/segmentation-test.png` | VM 3 |

---

## 9. VM to Framework Summary Matrix

| VM | NIST CSF Functions | ISO 27001 Controls | PCI DSS Reqs |
|----|-------------------|---------------------|--------------|
| VM 1 (Windows) | Protect, Detect | A.8.2, A.8.3, A.8.7, A.8.13 | Req 2, Req 5, Req 7, Req 8 |
| VM 2 (Ubuntu) | Identify, Protect | A.8.9, A.8.20, A.8.21 | Req 2, Req 4, Req 6 |
| VM 3 (pfSense) | Protect, Detect | A.8.20, A.8.21, A.8.22, A.8.31 | Req 1, Req 4, Req 11 |
| VM 4 (Wazuh) | Detect, Respond | A.8.15, A.8.16, A.8.33 | Req 10, Req 11 |

---

**End of Framework Mapping**
