> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# NIST CSF 2.0 Mapping

## Overview

The NIST Cybersecurity Framework (CSF) 2.0 is organized into six core functions: **Govern (GV), Identify (ID), Protect (PR), Detect (DE), Respond (RS), and Recover (RC)**.

This document maps Apex Capital's Proposed security controls across four virtual machines to each NIST function and category.

| VM | Role | Primary NIST Functions |
|----|------|------------------------|
| VM 1 - Windows 11 Enterprise | Internal workstation/server | Protect (PR), Detect (DE) |
| VM 2 - Ubuntu Server | Public-facing web server | Protect (PR), Identify (ID) |
| VM 3 - pfSense | Firewall and segmentation | Protect (PR), Detect (DE) |
| VM 4 - Wazuh | SIEM and monitoring | Detect (DE), Respond (RS) |

---

## 4-VM Architecture

| Function | Primary VM | Supporting VM | Description |
|----------|------------|---------------|-------------|
| **Govern (GV)** | All VMs (design-level) | VM 1-4 | Proposed roles, policies, risk approach, and oversight apply across the lab; none are approved or assessed. |
| **Identify (ID)** | VM 1-4 | VM 3 | Inventory, classification, and scenario risk records describe the proposed lab scope. |
| **Protect (PR)** | VM 3 (pfSense) | VM 1-2 | Segmentation and host hardening are proposed for the internal, DMZ, and management zones. |
| **Detect (DE)** | VM 4 (Wazuh) | VM 1-3 | Central monitoring is designed to receive endpoint, server, and network events. |
| **Respond (RS)** | VM 4 (Wazuh) | VM 1, VM 3 | Alert triage and containment workflows are proposed; no incident exercise has been run. |
| **Recover (RC)** | VM 1-2 | VM 4 | Recovery planning is proposed for affected hosts and logging; backup restoration has not been validated. |

---

## Govern (GV)

The Govern function establishes organizational context, risk management strategy, and security policies.

| Subcategory | Description | Proposed Control | Evidence Location |
|-------------|-------------|---------------------|-------------------|
| GV.OC-01 | Organizational context is established | Company profile, business requirements | `02-Company-Profile/`, `03-Business-Requirements/` |
| GV.OC-03 | Legal, regulatory, and contractual requirements are understood and managed | Identify obligations only after jurisdiction and entity applicability review; no regulatory applicability is established here | `03-Business-Requirements/business-requirements.md` |
| GV.RR-02 | Cybersecurity roles, responsibilities, and authorities are established and communicated | Fictional role assignments are proposed for the lab scenario | `02-Company-Profile/` Section 4 |
| GV.RM-02 | Risk appetite statement is established | Risk appetite documented | `04-Risk-Assessment/risk-assessment.md` |
| ID.RA-05 | Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk | Illustrative risk register; values are unvalidated scenario judgments | `04-Risk-Assessment/risk-register.md` |
| GV.PO-01 | Policies are established | 6 security policies documented | `07-Policies-and-Standards/` |

---

## Identify (ID)

The Identify function develops understanding of assets, risks, and business environment.

| Subcategory | Description | Proposed Control | Evidence Location | Primary VM |
|-------------|-------------|---------------------|-------------------|------------|
| ID.AM-01 | Hardware assets are inventoried | 4-VM asset inventory | Below table | All |
| ID.AM-02 | Software assets are inventoried | OS and applications documented | `02-Company-Profile/` Section 3 | All |
| ID.AM-07 | Inventories of data and corresponding metadata are maintained | Proposed data inventory and classification workflow | `07-Policies-and-Standards/data-classification-policy.md` | VM 1 |
| ID.RA-01 | Vulnerabilities are identified | Risk assessment methodology | `04-Risk-Assessment/risk-assessment.md` | All |
| ID.RA-03 | Internal and external threats to the organization are identified and recorded | Illustrative threat scenarios for the fictional lab | `04-Risk-Assessment/risk-assessment.md` Section 3 | All |
| ID.RA-06 | Risk responses are chosen, prioritized, planned, tracked, and communicated | Proposed treatment options; owners and acceptance decisions remain pending | `04-Risk-Assessment/risk-register.md` | All |
| ID.RA-05 / ID.RA-06 | Inherent risk is analyzed and responses are prioritized | Illustrative scoring and proposed responses; no assessed treatment status | `04-Risk-Assessment/risk-heatmap.md` | All |

### Asset Inventory (4-VM)

| Asset ID | VM | Hostname | IP Address | Subnet | Classification |
|----------|-----|----------|------------|--------|----------------|
| A-001 | VM 1 | Windows-Enterprise | 10.0.2.10 | Internal | High |
| A-002 | VM 2 | Ubuntu-Web | 10.0.1.10 | Public (DMZ) | Medium |
| A-003 | VM 3 | pfSense | 10.0.1.1, 10.0.2.1, 10.0.3.1 | All | High |
| A-004 | VM 4 | Wazuh-SIEM | 10.0.3.10 | Management | Medium |

---

## Protect (PR)

The Protect function describes cybersecurity safeguards. The entries below are proposed cross-references only; none are implementation findings.

| Subcategory | Description | Proposed Control | Evidence Location | Primary VM |
|-------------|-------------|---------------------|-------------------|------------|
| PR.AA-01 | Identity and credential management | Password policy (14 char, lockout, history) | `07-Policies-and-Standards/password-policy.md` | VM 1 |
| PR.IR-01 | Networks and environments protected from unauthorized logical access | No direct RDP from WAN, pfSense rules | `08-Technical-Controls/pfsense-network.md` | VM 3 |
| PR.AA-05 | Access permissions managed with least privilege and separation of duties | Separate admin accounts, user roles | `07-Policies-and-Standards/access-control-policy.md` | VM 1 |
| PR.IR-01 | Networks and environments protected from unauthorized logical access | pfSense firewall, public vs private subnets | `08-Technical-Controls/pfsense-network.md` | VM 3 |
| PR.AA-05 | Access reviews are conducted | Quarterly access review recommended | `11-Residual-Risk/residual-risk-recommendations.md` | VM 1 |
| PR.DS-01 | Data at rest is protected | NTFS permissions, BitLocker (optional) | `08-Technical-Controls/windows-hardening.md` | VM 1 |
| PR.DS-02 | Data in transit is protected | HTTPS, SSH encryption | `08-Technical-Controls/ubuntu-web-server.md` | VM 2 |
| ID.AM-07 | Data inventories and metadata are maintained | Data inventory/classification workflow is proposed | `07-Policies-and-Standards/data-classification-policy.md` | VM 1 |
| PR.DS-11 | Data backups are performed | Backup procedures documented | `08-Technical-Controls/windows-hardening.md` | VM 1 |
| DE.CM-09 | Malware protection is Proposed | Microsoft Defender, real-time scanning | `08-Technical-Controls/windows-hardening.md` | VM 1 |
| ID.RA-01 | Vulnerability management is Proposed | OS hardening, patch management policy | `08-Technical-Controls/windows-hardening.md` | VM 1, VM 2 |
| PR.PS-01 | Configuration management practices are established and applied (outcome reference only) | CIS benchmarks, hardening guides | `08-Technical-Controls/windows-hardening.md` | VM 1, VM 2 |
| PR.PS-02 | Software is updated regularly | Patch management policy | `07-Policies-and-Standards/password-policy.md` | VM 1, VM 2 |

---

## Detect (DE)

The Detect function covers outcomes for monitoring and analysis. The entries below are proposed cross-references only; none are implementation findings.

| Subcategory | Description | Proposed Control | Evidence Location | Primary VM |
|-------------|-------------|---------------------|-------------------|------------|
| DE.CM-01 | Network is monitored | pfSense logs, firewall events | `08-Technical-Controls/pfsense-network.md` | VM 3 |
| DE.CM-09 | Computing hardware and software are monitored for adverse events | Microsoft Defender, EICAR testing | `08-Technical-Controls/windows-hardening.md` | VM 1 |
| DE.CM-09 | Computing hardware and software are monitored for adverse events | Wazuh failed login alerts (Event ID 4625) | `08-Technical-Controls/wazuh-monitoring.md` | VM 4 |
| PR.PS-04 | Log records are generated and made available for continuous monitoring | Wazuh centralized logging | `08-Technical-Controls/wazuh-monitoring.md` | VM 4 |
| DE.AE-02 | Security events are analyzed | Wazuh SIEM event correlation | `08-Technical-Controls/wazuh-monitoring.md` | VM 4 |
| DE.AE-06 | Adverse-event information is provided to authorized people and tools | Wazuh alert rules (failed login, malware) | `08-Technical-Controls/wazuh-monitoring.md` | VM 4 |
| ID.IM-02 | Improvements are identified from security tests and exercises | EICAR test, failed login test | `09-Testing-and-Validation/test-scenarios.md` | VM 1, VM 4 |

### Detection Sources by VM

| VM | Detection Capability | Logs Sent to Wazuh |
|----|---------------------|---------------------|





---

## Respond (RS)

The Respond function contains and mitigates security incidents.

| Subcategory | Description                           | Proposed Control                    | Evidence Location                                       | Primary VM |
| ----------- | ------------------------------------- | -------------------------------------- | ------------------------------------------------------- | ---------- |
| ID.IM-04    | Incident response plans are established, communicated, maintained, and improved    | Incident response policy documented    | `07-Policies-and-Standards/incident-response-policy.md` | All        |
| GV.RR-02    | Cybersecurity roles, responsibilities, and authorities are established   | CISO, GRC Lead, IT teams roles defined | `07-Policies-and-Standards/incident-response-policy.md` | All        |
| RS.AN-03    | Incident investigations are performed | Alert triage process defined           | `07-Policies-and-Standards/incident-response-policy.md` | VM 4       |
| RS.AN-07    | Incident data and metadata are collected with integrity and provenance            | Wazuh logs, evidence repository        | `10-Evidence/`                                          | VM 4       |
| RS.MI-01    | Incidents are contained               | Containment procedures documented      | `07-Policies-and-Standards/incident-response-policy.md` | VM 3       |
| RS.MI-02    | Incidents are eradicated              | Eradication procedures documented      | `07-Policies-and-Standards/incident-response-policy.md` | VM 1, VM 2 |

### Incident Response Workflow
---
## Detection (Wazuh Alert) → Analysis (VM 4) → Containment (pfSense Block) → Eradication (VM 1,2) → Recovery (Backup)

---

## Recover (RC)

The Recover function restores operations after an incident.

| Subcategory | Description | Proposed Control | Evidence Location | Primary VM |
|-------------|-------------|---------------------|-------------------|------------|
| RC.RP-01 | Recovery portion of the incident response plan is executed | Backup and recovery procedures | `08-Technical-Controls/windows-hardening.md` | VM 1 |
| ID.IM-03 | Post-incident lessons are learned | Post-incident review process | `07-Policies-and-Standards/incident-response-policy.md` | All |

---

## Reference Mapping Counts (Not an Implementation Assessment)

| NIST CSF 2.0 function | Mapping rows in this draft | Assessment status |
|----------------------|--------------------------|-------------------|
| Govern (GV) | 6 | Proposed references; not independently assessed |
| Identify (ID) | 7 | Proposed references; not independently assessed |
| Protect (PR) | 13 | Proposed references; not independently assessed |
| Detect (DE) | 7 | Proposed references; not independently assessed |
| Respond (RS) | 6 | Proposed references; not independently assessed |
| Recover (RC) | 2 | Proposed references; not independently assessed |

Counts are the number of rows shown under each function in this draft. They are not implementation, evidence, effectiveness, or compliance counts. No VM tests have been run.

---

## NIST CSF Tiers Not Assessed

| Tier Level | Description | Apex Capital Rating |
|------------|-------------|---------------------|
| Tier 1 (Partial) | Ad hoc, reactive processes | Not assessed |
| Tier 2 (Risk Informed) | Risk-aware, but not organization-wide | **Not rated** |
| Tier 3 (Repeatable) | Repeatable governance and risk-management practices | Not assessed |
| Tier 4 (Adaptive) | Practices adapt using risk and performance information | Not assessed |

CSF Tiers characterize the rigor of cybersecurity risk governance and management practices; they are not a simple maturity score or a percentage of controls implemented. No Tier is assigned to this fictional lab. An organizational assessment would require evidence of operating practices and business context.

---

## Evidence Index by NIST Category (4-VM)

| NIST Category | Control | Evidence File | Primary VM |
|---------------|---------|---------------|------------|
| ID.RA-05 | Illustrative inherent risk analysis | `04-Risk-Assessment/risk-register.md` | All |
| GV.PO-01 | Proposed security policy framework | `07-Policies-and-Standards/` | All |
| PR.AA-01 | Password policy | `evidence/weak-password-rejected.png` | VM 1 |
| PR.IR-01 | Networks and environments protected from unauthorized logical access | `evidence/segmentation-test.png` | VM 3 |
| PR.DS-02 | Data in transit | `evidence/https-padlock.png` | VM 2 |
| DE.CM-09 | Malware protection | `evidence/eicar-block.png` | VM 1 |
| PR.PS-04 | Centralized logging | `evidence/wazuh-dashboard.png` | VM 4 |
| DE.AE-02 | Failed login alerts | `evidence/wazuh-failed-login-alert.png` | VM 4 |
| RS.MA-01 | Incident response | `07-Policies/incident-response-policy.md` | All |

---

## Control to VM Mapping Matrix

| Proposed control area | VM 1 - Windows | VM 2 - Ubuntu | VM 3 - pfSense | VM 4 - Wazuh |
|-----------------------|---------------|--------------|---------------|-------------|
| Password policy | Proposed | - | - | - |
| Microsoft Defender | Proposed | - | - | - |
| EICAR detection scenario | Proposed | - | - | VM 4 receives alert (planned) |
| SSH hardening | - | Proposed | - | VM 4 receives logs (planned) |
| UFW firewall | - | Proposed | - | VM 4 receives logs (planned) |
| Network segmentation | - | - | Proposed | - |
| Firewall rules | - | - | Proposed | VM 4 receives logs (planned) |
| Lateral movement block | VM 1 target | VM 2 source | Proposed enforcement | VM 4 receives logs (planned) |
| Wazuh agent / syslog | Proposed agent | Proposed agent | Proposed syslog | Central monitor (planned) |
| SIEM alert scenarios | Event source (planned) | Event source (planned) | Event source (planned) | Proposed analysis |

---

**End of NIST CSF 2.0 Mapping**
