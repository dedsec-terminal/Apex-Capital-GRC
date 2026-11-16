> **Risk status:** Likelihood/impact values and target residual scores are illustrative scenario judgments. Target scores are proposals only; controls were not executed, effectiveness was not tested, and no residual risk was accepted.

> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Risk Assessment

## 1. Risk Assessment Methodology

This risk assessment follows the methodology defined in **NIST SP 800-30 (Guide for Conducting Risk Assessments)** and aligned with **ISO 27001:2022 Clause 6.1 (Actions to address risks and opportunities)**.

### 1.1 Risk Calculation Formula

`Risk Score = Impact x Likelihood`

| Level      | Impact Score | Likelihood Score |
| ---------- | ------------ | ---------------- |
| Critical   | 5            | 5                |
| High       | 4            | 4                |
| Medium     | 3            | 3                |
| Low        | 2            | 2                |
| Negligible | 1            | 1                |

### 1.2 Risk Levels

| Score Range | Risk Level | Required Action |
|-------------|------------|-----------------|
| 20-25 | Critical | Immediate remediation required |
| 13-19 | High | Remediation within 30 days |
| 7-12 | Medium | Remediation within 90 days |
| 1-6 | Low | Accept or monitor |

### 1.3 Risk Appetite Statement

Apex Capital (fictional lab scenario) maintains the following risk appetite:

| Risk Category | Appetite | Rationale |
|---------------|----------|-----------|
| Client data confidentiality | Low | Regulatory (SEBI) and reputational impact |
| Financial loss due to cyber incident | Low | Direct business impact |
| Regulatory compliance (SEBI) | Low | Potential fines and license implications |
| Operational disruption | Medium | Accepts up to 4 hours downtime |
| Technology modernization delays | Medium | Accepts controlled delays for security |

---

## 2. Asset Inventory (Risk Context)

| Asset ID | Asset Type | Description | Confidentiality | Integrity | Availability |
|----------|------------|-------------|-----------------|-----------|--------------|
| A-001 | Client Data | PAN, Aadhaar (masked), bank details, demat information, investment holdings | High | High | Medium |
| A-002 | Windows Workstations | 200 HQ + 150 remote employee endpoints | Medium | Medium | Medium |
| A-003 | Ubuntu Web Server | Customer investment portal (public-facing) | Low | High | High |
| A-004 | Windows Application Servers | Portfolio management, order execution | High | High | High |
| A-005 | pfSense Firewall | Network segmentation, traffic filtering | Medium | High | High |
| A-006 | Wazuh SIEM | Centralized logging, alerting | Medium | High | Medium |
| A-007 | Internal File Servers | Client document storage (account openings, KYC) | High | High | Medium |
| A-008 | Payment Systems | ACH/NEFT processing, advisor commission payments | High | High | Medium |

---

## 3. Threat Sources

Based on SEBI cybersecurity guidance and industry threat intelligence for Indian financial services:

| Threat Source | Motivation | Relevance to Apex Capital |
|---------------|------------|--------------------------|
| Cybercriminals (domestic/international) | Financial gain | Ransomware, data theft for resale |
| Phishing campaigns | Credential theft | 150 remote advisors = high attack surface |
| Insider threats (malicious) | Personal gain, disgruntlement | Access to client financial data |
| Insider threats (unintentional) | Human error | Weak passwords, misconfigured settings |
| Nation-state actors (advanced) | Espionage, disruption | Lower probability but high impact |
| Script kiddies | Curiosity, reputation | Web server scanning, defacement |
| Competitors | Business intelligence | Unauthorized access to client lists |

---

## 4. Risk Register Summary

> Inherent scores match the scenario register; target scores remain illustrative and unvalidated.

| Risk ID | Risk Description | Impact | Likelihood | Inherent Score | Proposed Target Score (Unvalidated) | Priority |
|---|---|---:|---:|---:|---:|---|
| R-001 | Lateral movement from compromised Ubuntu web server to internal Windows network | 5 | 3 | 15 | 4 | High |
| R-002 | Credential theft via brute force or phishing leading to unauthorized access | 5 | 4 | 20 | 8 | Critical |
| R-003 | Ransomware disrupts systems or damages data | 5 | 4 | 20 | 6 | Critical |
| R-004 | Incomplete logging or evidence impairs investigation | 4 | 3 | 12 | 3 | Medium |
| R-005 | Public web host compromise exposes systems or data | 5 | 3 | 15 | 5 | High |
| R-006 | Insider misuse of authorized access exposes sensitive data | 5 | 2 | 10 | 4 | Medium |
| R-007 | Supplier weakness affects confidentiality or availability | 5 | 3 | 15 | 6 | High |
| R-008 | Firewall configuration drift exposes a protected path | 4 | 3 | 12 | 2 | Medium |
## 5. Detailed Risk Analysis

### R-001: Lateral Movement (Web Server to Internal Network)

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | An attacker compromises the public-facing Ubuntu web server (customer portal) and attempts to move laterally to internal Windows systems containing client portfolio data |
| **Likelihood** | 3 (Possible) |
| **Impact** | 5 (Critical) |
| **Raw Score** | 15 (High) |
| **Affected Assets** | A-003 (Ubuntu Web Server), A-004 (Windows App Servers), A-001 (Client Data) |
| **Threat Source** | Cybercriminals, automated scanners |
| **Existing Controls** | No implemented baseline is assumed in the scenario |
| **Proposed Mitigation** | pfSense firewall rule blocking all traffic from Ubuntu subnet to Windows subnet; DMZ isolation |
| **Control Owner** | Network Security |
| **Proposed Target Residual Score (Unvalidated)** | 4 (Low) |
| **Proposed Treatment Rationale (Unvalidated)** | Network segmentation is intended to restrict lateral movement; effectiveness is untested |

---

### R-002: Credential Theft (Brute Force / Phishing)

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | Attacker uses brute force or phishing to obtain advisor credentials, then accesses client data and executes unauthorized trades |
| **Likelihood** | 4 (Likely) |
| **Impact** | 5 (Critical) |
| **Raw Score** | 20 (Critical) |
| **Affected Assets** | A-002 (Windows Workstations), A-004 (App Servers), A-001 (Client Data) |
| **Threat Source** | Phishing campaigns, brute force tools |
| **Existing Controls** | None (default Windows settings, no lockout) |
| **Proposed Mitigation** | Password policy (14 characters, complexity, 5-attempt lockout); failed login alerting via Wazuh |
| **Control Owner** | Identity Management |
| **Proposed Target Residual Score (Unvalidated)** | 8 (Medium) |
| **Proposed Treatment Rationale (Unvalidated)** | Password policy reduces brute force success; MFA recommended for further reduction (out of scope) |

---

### R-003: Ransomware (Endpoint Malware)

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | Employee downloads and executes ransomware via email attachment or malicious website, encrypting client portfolio data and demanding payment |
| **Likelihood** | 4 (Likely) |
| **Impact** | 5 (Critical) |
| **Raw Score** | 20 (Critical) |
| **Affected Assets** | A-002 (Windows Workstations), A-004 (App Servers), A-007 (File Servers) |
| **Threat Source** | Ransomware gangs (LockBit, BlackCat), phishing emails |
| **Existing Controls** | None (antivirus not validated) |
| **Proposed Mitigation** | Microsoft Defender real-time protection; Controlled Folder Access; EICAR test validation; daily backups |
| **Control Owner** | Endpoint Security |
| **Proposed Target Residual Score (Unvalidated)** | 5 (Low) |
| **Proposed Treatment Rationale (Unvalidated)** | Defender and protected backups are proposed safeguards; detection and recovery are untested |

---

### R-004: Audit Failure (Missing Evidence)

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | SEBI or client audit requests evidence of security controls; Apex Capital cannot produce logs, policies, or test results |
| **Likelihood** | 3 (Possible) |
| **Impact** | 4 (High) |
| **Raw Score** | 12 (Medium) |
| **Affected Assets** | A-006 (Wazuh SIEM), policies, evidence repository |
| **Threat Source** | Regulatory examination, client due diligence |
| **Existing Controls** | None (logs exist only on individual systems) |
| **Proposed Mitigation** | Wazuh centralized logging; evidence repository with 15+ screenshots; documented policies |
| **Control Owner** | GRC Lead |
| **Proposed Target Residual Score (Unvalidated)** | 3 (Low) |
| **Proposed Treatment Rationale (Unvalidated)** | Evidence availability and retrieval time have not been measured; retention and retrieval tests are pending |

---

### R-005: Web Server Breach (Vulnerable Ubuntu)

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | Ubuntu web server has unpatched vulnerability or misconfiguration leading to unauthorized access, defacement, or data theft |
| **Likelihood** | 3 (Possible) |
| **Impact** | 5 (Critical) |
| **Raw Score** | 15 (High) |
| **Affected Assets** | A-003 (Ubuntu Web Server), A-001 (Client Data if exposed) |
| **Threat Source** | Automated scanners, vulnerability exploit |
| **Existing Controls** | None (default Ubuntu install) |
| **Proposed Mitigation** | SSH hardening (key auth, restricted management source and hardened SSH configuration); UFW firewall; regular patching; service minimization |
| **Control Owner** | Application Security |
| **Proposed Target Residual Score (Unvalidated)** | 4 (Low) |
| **Proposed Treatment Rationale (Unvalidated)** | Segmentation is intended to limit internal reachability; path tests and vulnerability review are pending |

---

### R-006: Insider Threat (Data Exfiltration)

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | Disgruntled employee exports client list (PII, financial data) to competitor or personal device |
| **Likelihood** | 2 (Unlikely) |
| **Impact** | 5 (Critical) |
| **Raw Score** | 10 (Medium) |
| **Affected Assets** | A-001 (Client Data), A-002 (Workstations) |
| **Threat Source** | Insider (malicious) |
| **Existing Controls** | None |
| **Proposed Mitigation** | Access control (least privilege); user behavior logging via Wazuh; data classification policy |
| **Control Owner** | IAM Lead |
| **Proposed Target Residual Score (Unvalidated)** | 4 (Low) |
| **Proposed Treatment Rationale (Unvalidated)** | DLP and full data audit trails are not included in this lab design |

---

### R-007: Third-Party Vendor Breach

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | Cloud vendor (Salesforce, Microsoft 365, file sharing) suffers breach exposing Apex Capital client data |
| **Likelihood** | 3 (Possible) |
| **Impact** | 5 (Critical) |
| **Raw Score** | 15 (High) |
| **Affected Assets** | A-001 (Client Data stored in vendor systems) |
| **Threat Source** | Vendor compromise |
| **Existing Controls** | None (no vendor risk assessments) |
| **Proposed Mitigation** | Vendor risk assessment program (recommended out of scope for Phase 1); contractual security clauses |
| **Control Owner** | Procurement |
| **Proposed Target Residual Score (Unvalidated)** | 8 (Medium) |
| **Proposed Treatment Rationale (Unvalidated)** | Supplier review is planned; no Apex vendor assessment has been executed |

---

### R-008: Firewall Misconfiguration

| Attribute | Detail |
|-----------|--------|
| **Risk Description** | pfSense firewall misconfigured, accidentally exposing internal network to internet or allowing unauthorized traffic |
| **Likelihood** | 3 (Possible) |
| **Impact** | 4 (High) |
| **Raw Score** | 12 (Medium) |
| **Affected Assets** | All internal assets |
| **Threat Source** | Human error (administrator) |
| **Existing Controls** | No implemented baseline is assumed in the scenario |
| **Proposed Mitigation** | Change management process; quarterly firewall rule audit; rule comments documented |
| **Control Owner** | Network Security |
| **Proposed Target Residual Score (Unvalidated)** | 2 (Low) |
| **Proposed Treatment Rationale (Unvalidated)** | Change review and periodic audits are proposed controls; effectiveness is untested |

---

## 6. Inherent risk heatmap

| Impact / Likelihood | 1 Rare | 2 Unlikely | 3 Possible | 4 Likely | 5 Almost certain |
|---|---|---|---|---|---|
| 5 Critical | - | R-006 | R-001, R-005, R-007 | R-002, R-003 | - |
| 4 High | - | - | R-004, R-008 | - | - |
| 3 Medium | - | - | - | - | - |
| 2 Low | - | - | - | - | - |
| 1 Negligible | - | - | - | - | - |

**Critical scenarios:** R-002 credential compromise and R-003 ransomware.

**High scenarios:** R-001 lateral movement, R-005 public-service compromise and R-007 supplier weakness.

These are illustrative inherent scores, using the same values as the canonical risk register. No control effectiveness has been measured.

---

## 7. Illustrative target risk heatmap

| Impact / Likelihood | 1 Rare | 2 Unlikely | 3 Possible | 4 Likely | 5 Almost certain |
|---|---|---|---|---|---|
| 5 Critical | R-003 | - | - | - | - |
| 4 High | - | R-002, R-007 | - | - | - |
| 3 Medium | R-004 | - | - | - | - |
| 2 Low | R-008 | R-001, R-005, R-006 | - | - | - |
| 1 Negligible | - | - | - | - | - |

These values preserve the proposed planning targets: 4, 8, 5, 3, 4, 4, 8 and 2 for R-001 through R-008. They are not observed residual risk and are not accepted thresholds. A new assessment of likelihood, impact and control evidence is required before adopting any target. No target has been achieved.

---

## 8. Risk Treatment Plan

All actions below are proposed. Owners and actual dates must be confirmed before execution.

| Risk ID | Treatment decision | Rationale | Proposed sequencing | Evidence needed for success |
|---|---|---|---|---|
| R-001 | Mitigate through default-deny segmentation and approved management paths | Limit a compromised public host from reaching internal systems | After isolated network baseline approval | Paired allowed and denied tests match the flow matrix and have correlated firewall evidence |
| R-002 | Mitigate through least privilege, appropriate MFA and account review | Reduce exposure from stolen or abused credentials | After identity baseline and account scope review | Effective access configuration and controlled access tests are reviewed; unresolved MFA dependencies remain open |
| R-003 | Mitigate through endpoint controls and protected, tested recovery | Limit propagation and establish a trustworthy recovery path | After endpoint baseline and backup design review | Safe endpoint test is recorded; isolated restore passes integrity and service checks against agreed objectives |
| R-004 | Mitigate through source coverage, retention and evidence handling | Investigation depends on complete and retrievable telemetry | After log source and retention requirements are agreed | Controlled source events can be traced to alerts and retrieved with correct host, time and integrity records |
| R-005 | Mitigate through hardening, patching and exposure review | Reduce unnecessary services and known exploitable weaknesses | After supported host and application versions are selected | Service inventory and baseline checks match approved exposure; identified vulnerabilities have recorded dispositions |
| R-006 | Mitigate through role design, access review and proportionate monitoring | Limit unauthorized use of otherwise legitimate access | After data owners define permitted roles | Positive and negative access tests match approved roles; access review exceptions are owned and tracked |
| R-007 | Assess supplier evidence and decide treatment before reliance | Supplier claims must match the service, entity, period and control scope | Before a fictional onboarding decision | Review records identify scope and gaps, record a recommendation and leave acceptance to the accountable reviewer |
| R-008 | Mitigate through controlled changes, backups and regression testing | Prevent or detect unintended changes to protected paths | Before a firewall baseline change is accepted | Change has rationale, approval and rollback; regression checks detect prohibited path changes |

---

## 9. Control Mapping to Risks

| Control ID | Control Description | Risks Mitigated | Evidence |
|------------|---------------------|-----------------|----------|
| C-01 | pfSense segmentation (block DMZ to Internal) | R-001 | Firewall rule screenshot |
| C-02 | Password policy (14 char, lockout) | R-002 | `net accounts` output |
| C-03 | Microsoft Defender + Controlled Folder Access | R-003 | EICAR block screenshot |
| C-04 | Wazuh failed login alerting | R-002, R-004 | Wazuh dashboard screenshot |
| C-05 | Ubuntu SSH hardening + UFW | R-005 | `sshd_config`, `ufw status` |
| C-06 | Windows access control (least privilege) | R-006 | User role screenshots |
| C-07 | Change management process | R-008 | Change log documentation |
| C-08 | Evidence repository | R-004 | `/10-Evidence/` folder |

---

## 10. Risk Register Export

The complete risk register with detailed scoring, ownership, and treatment status is maintained in:

**`04-Risk-Assessment/risk-register.md`**

---

**End of Risk Assessment**
