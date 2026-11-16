> **Risk status:** Likelihood/impact values and target residual scores are illustrative scenario judgments. Target scores are proposals only; controls were not executed, effectiveness was not tested, and no residual risk was accepted.

> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Risk Register

## Risk Scoring Matrix

| Level | Impact Score | Likelihood Score |
|-------|--------------|------------------|
| Critical | 5 | 5 |
| High | 4 | 4 |
| Medium | 3 | 3 |
| Low | 2 | 2 |
| Negligible | 1 | 1 |

**Risk Score Calculation:** Likelihood x Impact

| Score Range | Rating | Required Action |
|-------------|--------|-----------------|
| 20-25 | Critical | Immediate remediation |
| 13-19 | High | Remediation within 30 days |
| 7-12 | Medium | Remediation within 90 days |
| 1-6 | Low | Accept or monitor |

---

## Master Risk Register

| Risk ID | Risk Description | Likelihood | Impact | Score | Rating | Proposed Control Intent | Status | Owner |
|---|---|---:|---:|---:|---|---|---|---|
| R-001 | Lateral movement from compromised Ubuntu web server to internal Windows network | 3 | 5 | 15 | High | Proposed segmentation and firewall policy | Planned / not executed | Network security owner |
| R-002 | Credential theft via brute force or phishing leading to unauthorized access | 4 | 5 | 20 | Critical | Proposed authentication, access and monitoring controls | Planned / not executed | IAM owner |
| R-003 | Ransomware disrupts systems or damages data | 4 | 5 | 20 | Critical | Proposed endpoint protection and recovery controls | Planned / not executed | Endpoint and resilience owner |
| R-004 | Incomplete logging or evidence impairs investigation | 3 | 4 | 12 | Medium | Proposed centralized logging and evidence process | Planned / not executed | Security operations owner |
| R-005 | Public web host compromise exposes systems or data | 3 | 5 | 15 | High | Proposed host hardening and exposure controls | Planned / not executed | Application / infrastructure owner |
| R-006 | Insider misuse of authorized access exposes sensitive data | 2 | 5 | 10 | Medium | Proposed access governance and monitoring | Planned / not executed | Data and IAM owners |
| R-007 | Supplier weakness affects confidentiality or availability | 3 | 5 | 15 | High | Supplier due diligence workflow proposed; not built | Planned / not executed | Third-party risk owner |
| R-008 | Firewall configuration drift exposes a protected path | 3 | 4 | 12 | Medium | Proposed change review and regression checks | Planned / not executed | Network security owner |
## Detailed Risk Register

### R-001: Lateral Movement (Web Server to Internal Network)

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | An attacker compromises the public-facing Ubuntu web server (customer portal) and attempts to move laterally to internal Windows systems containing client portfolio data |
| **Likelihood** | 3 (Possible) |
| **Impact** | 5 (Critical) |
| **Risk Score** | 15 (High) |
| **Affected Assets** | Ubuntu Web Server, Windows Application Servers, Client Data |
| **Threat Source** | Cybercriminals, automated scanners |
| **Existing Controls (Pre-Engagement)** | None |
| **Proposed Control Intent** | pfSense firewall rule blocking all traffic from Ubuntu subnet to Windows subnet; DMZ isolation |
| **Planned Validation** | `nc -zv` from Ubuntu to Windows port 445 fails; pfSense logs show blocked attempts |
| **Proposed Target Residual Score (Unvalidated)** | 4 (Low) |
| **Status** | Planned / not executed |
| **Owner** | Network Security |
| **Review Date** | Quarterly |

---

### R-002: Credential Theft (Brute Force / Phishing)

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | Attacker uses brute force or phishing to obtain advisor credentials, then accesses client data and executes unauthorized trades |
| **Likelihood** | 4 (Likely) |
| **Impact** | 5 (Critical) |
| **Risk Score** | 20 (Critical) |
| **Affected Assets** | Windows Workstations, Application Servers, Client Data |
| **Threat Source** | Phishing campaigns, brute force tools |
| **Existing Controls (Pre-Engagement)** | Default Windows settings, no lockout policy |
| **Proposed Control Intent** | Password policy (14 characters, complexity, 5-attempt lockout); Wazuh failed login alerting |
| **Planned Validation** | Weak password "[SYNTHETIC-TEST-CREDENTIAL]" rejected; `net accounts` shows lockout threshold 5; Wazuh alerts on failed login |
| **Proposed Target Residual Score (Unvalidated)** | 8 (Medium) |
| **Status** | Planned / not executed |
| **Owner** | Identity Management |
| **Review Date** | Quarterly |
| **Further Reduction** | MFA recommended for Phase 2 |

---

### R-003: Ransomware (Endpoint Malware)

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | Employee downloads and executes ransomware via email attachment or malicious website, encrypting client portfolio data and demanding payment |
| **Likelihood** | 4 (Likely) |
| **Impact** | 5 (Critical) |
| **Risk Score** | 20 (Critical) |
| **Affected Assets** | Windows Workstations, Application Servers, File Servers |
| **Threat Source** | Ransomware gangs (LockBit, BlackCat), phishing emails |
| **Existing Controls (Pre-Engagement)** | Antivirus installed but not validated |
| **Proposed Control Intent** | Microsoft Defender real-time protection; Controlled Folder Access; EICAR test validation |
| **Planned Validation** | EICAR test file downloaded → blocked within a lab-defined observation window; Defender history shows detection |
| **Proposed Target Residual Score (Unvalidated)** | 5 (Low) |
| **Status** | Planned / not executed |
| **Owner** | Endpoint Security |
| **Review Date** | Monthly (EICAR test) |

---

### R-004: Audit Failure (Missing Evidence)

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | SEBI or client audit requests evidence of security controls; Apex Capital cannot produce logs, policies, or test results |
| **Likelihood** | 3 (Possible) |
| **Impact** | 4 (High) |
| **Risk Score** | 12 (Medium) |
| **Affected Assets** | Wazuh SIEM, policies, evidence repository |
| **Threat Source** | Regulatory examination, client due diligence |
| **Existing Controls (Pre-Engagement)** | Logs exist only on individual systems |
| **Proposed Control Intent** | Wazuh centralized logging; evidence repository with screenshots; documented policies |
| **Planned Validation** | Evidence folder contains 15+ screenshots with timestamps; policies version controlled |
| **Proposed Target Residual Score (Unvalidated)** | 3 (Low) |
| **Status** | Planned / not executed |
| **Owner** | GRC Lead |
| **Review Date** | Quarterly |

---

### R-005: Web Server Breach (Vulnerable Ubuntu)

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | Ubuntu web server has unpatched vulnerability or misconfiguration leading to unauthorized access, defacement, or data theft |
| **Likelihood** | 3 (Possible) |
| **Impact** | 5 (Critical) |
| **Risk Score** | 15 (High) |
| **Affected Assets** | Ubuntu Web Server, Client Data (if exposed) |
| **Threat Source** | Automated scanners, vulnerability exploit |
| **Existing Controls (Pre-Engagement)** | Default Ubuntu install |
| **Proposed Control Intent** | SSH hardening (key auth, restricted management source and hardened SSH configuration); UFW firewall; service minimization |
| **Planned Validation** | `sshd_config` shows password auth disabled; `ufw status` shows deny incoming; `nmap` shows only required ports |
| **Proposed Target Residual Score (Unvalidated)** | 4 (Low) |
| **Status** | Planned / not executed |
| **Owner** | Application Security |
| **Review Date** | Monthly (patch review) |

---

### R-006: Insider Threat (Data Exfiltration)

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | Disgruntled employee exports client list (PII, financial data) to competitor or personal device |
| **Likelihood** | 2 (Unlikely) |
| **Impact** | 5 (Critical) |
| **Risk Score** | 10 (Medium) |
| **Affected Assets** | Client Data, Workstations |
| **Threat Source** | Insider (malicious) |
| **Existing Controls (Pre-Engagement)** | None |
| **Proposed Control Intent** | Access control (least privilege); user behavior logging via Wazuh; data classification policy |
| **Planned Validation** | Standard user cannot install software; Wazuh logs user logins and file access |
| **Proposed Target Residual Score (Unvalidated)** | 4 (Low) |
| **Status** | Planned / not executed |
| **Owner** | IAM Lead |
| **Review Date** | Quarterly (access reviews) |

---

### R-007: Third-Party Vendor Breach

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | Cloud vendor (Salesforce, Microsoft 365, file sharing) suffers breach exposing Apex Capital client data |
| **Likelihood** | 3 (Possible) |
| **Impact** | 5 (Critical) |
| **Risk Score** | 15 (High) |
| **Affected Assets** | Client Data stored in vendor systems |
| **Threat Source** | Vendor compromise |
| **Existing Controls (Pre-Engagement)** | None (no vendor risk assessments) |
| **Proposed Control Intent** | Vendor risk assessment program (Planned); contractual security clauses |
| **Planned Validation** | Vendor assessment template created; top 3 vendors identified for Phase 2 |
| **Proposed Target Residual Score (Unvalidated)** | 6 (Low-Medium) |
| **Status** | Planned / not executed |
| **Owner** | Procurement |
| **Review Date** | Quarterly |
| **Target Completion** | Phase 2 (Q3 2026) |

---

### R-008: Firewall Misconfiguration

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | pfSense firewall misconfigured, accidentally exposing internal network to internet or allowing unauthorized traffic |
| **Likelihood** | 3 (Possible) |
| **Impact** | 4 (High) |
| **Risk Score** | 12 (Medium) |
| **Affected Assets** | All internal assets |
| **Threat Source** | Human error (administrator) |
| **Existing Controls (Pre-Engagement)** | None |
| **Proposed Control Intent** | Change management process; quarterly firewall rule audit; rule comments documented |
| **Planned Validation** | Firewall rules have descriptions; change log maintained; quarterly audit scheduled |
| **Proposed Target Residual Score (Unvalidated)** | 2 (Low) |
| **Status** | Planned / not executed |
| **Owner** | Network Security |
| **Review Date** | Quarterly |

---

## Risk Status Summary

| Status | Count | Risk IDs |
|--------|-------|----------|
| Planned / not executed | 7 | R-001, R-002, R-003, R-004, R-005, R-006, R-008 |
| Planned / not executed | 1 | R-007 |
| Not Started | 0 | - |

---

## Risk Rating Distribution

### Inherent scenario ratings

| Rating | Count | Percentage |
|---|---:|---:|
| Critical | 2 | 25% |
| High | 3 | 37.5% |
| Medium | 3 | 37.5% |
| Low | 0 | 0% |

### Proposed targets only and not assessed

| Rating | Count | Percentage |
|--------|-------|------------|
| Critical | 0 | 0% |
| High | 0 | 0% |
| Medium | 2 | 25% |
| Low | 6 | 75% |

---

## Risk Register Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | March 2026 | S. Singh | Initial risk identification |
| 0.5 | April 2026 | S. Singh | Added control mappings and validation methods |
| 1.0 | May 2026 | S. Singh | Final risk register with status updates |

---

**End of Risk Register**
