> **Risk status:** Likelihood/impact values and target residual scores are illustrative scenario judgments. Target scores are proposals only; controls were not executed, effectiveness was not tested, and no residual risk was accepted.

> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Residual Risk and Recommendations

**Last Updated:** May 2026
**Version:** 1.0
**Classification:** Internal
**Owner:** GRC Lead

---

## 1. Overview

This document records proposed risk-treatment targets for a fictional lab scenario. No controls were implemented or tested, so residual risk has not been assessed. Each target is a discussion hypothesis, not an accepted risk level.

**Assessment Period:** May 2026
**Risk Appetite:** Low for client data confidentiality and regulatory compliance; Medium for operational disruption

---

## 2. Proposed Target Risk Summary

> Target scores are hypotheses for discussion, not calculated residual risk or risk acceptance.

| Risk ID | Risk Description | Inherent Score | Proposed Target Residual Score (Unvalidated) | Target Rating | Status |
|---|---|---:|---:|---|---|
| R-001 | Lateral movement from DMZ to internal network | 15 (High) | 4 (Low) | Proposed target only | Not accepted |
| R-002 | Credential theft via brute force or phishing | 20 (Critical) | 8 (Medium) | Proposed target only | Not accepted |
| R-003 | Ransomware disrupts systems or data | 20 (Critical) | 5 (Low) | Proposed target only | Not accepted |
| R-004 | Incomplete logging or evidence | 12 (Medium) | 3 (Low) | Proposed target only | Not accepted |
| R-005 | Public web host compromise | 15 (High) | 4 (Low) | Proposed target only | Not accepted |
| R-006 | Insider misuse of access | 10 (Medium) | 4 (Low) | Proposed target only | Not accepted |
| R-007 | Supplier weakness | 15 (High) | 8 (Medium) | Proposed target only | Not accepted |
| R-008 | Firewall configuration drift | 12 (Medium) | 2 (Low) | Proposed target only | Not accepted |
## 3. Residual Risk Details

### R-001: Lateral Movement (Web Server to Internal Network)

| Attribute | Detail |
|-----------|--------|
| Risk Description | Attacker compromises Ubuntu web server and attempts lateral movement to internal Windows systems |
| Inherent Score (scenario register) | 15 (High) |
| Proposed Target Residual Score (Unvalidated) | 4 (Low) |
| Residual Risk Level | Not assessed |
| Proposed Control Intent | pfSense firewall rule blocking 10.0.1.0/24 to 10.0.2.0/24 |
| Proposed Treatment Rationale (Unvalidated) | Indicative rationale only; no effectiveness evidence or risk-owner acceptance exists |
| Status | Proposed treatment only; not accepted |
| Review Frequency | Quarterly |

### R-002: Credential Theft (Brute Force / Phishing)

| Attribute | Detail |
|-----------|--------|
| Risk Description | Attacker uses brute force or phishing to obtain advisor credentials |
| Inherent Score (scenario register) | 20 (Critical) |
| Proposed Target Residual Score (Unvalidated) | 8 (Medium) |
| Residual Risk Level | Not assessed |
| Proposed Control Intent | Password policy (14 char, lockout), Wazuh failed login alerts |
| Proposed Treatment Rationale (Unvalidated) | Indicative rationale only; no effectiveness evidence or risk-owner acceptance exists |
| Status | Proposed treatment only; not accepted |
| Recommended Action | Implement MFA for all remote access and administrative accounts |
| Review Frequency | Monthly |

### R-003: Ransomware (Endpoint Malware)

| Attribute | Detail |
|-----------|--------|
| Risk Description | Employee downloads ransomware via email or website, encrypting data |
| Inherent Score (scenario register) | 20 (Critical) |
| Proposed Target Residual Score (Unvalidated) | 5 (Low) |
| Residual Risk Level | Not assessed |
| Proposed Control Intent | Microsoft Defender, EICAR validation, Controlled Folder Access |
| Proposed Treatment Rationale (Unvalidated) | Indicative rationale only; no effectiveness evidence or risk-owner acceptance exists |
| Status | Proposed treatment only; not accepted |
| Review Frequency | Monthly (EICAR test) |

### R-004: Audit Failure (Missing Evidence)

| Attribute | Detail |
|-----------|--------|
| Risk Description | Unable to produce evidence for SEBI/SEC/client audits |
| Inherent Score (scenario register) | 12 (Medium) |
| Proposed Target Residual Score (Unvalidated) | 3 (Low) |
| Residual Risk Level | Not assessed |
| Proposed Control Intent | Wazuh centralized logging, evidence repository, documented policies |
| Proposed Treatment Rationale (Unvalidated) | Indicative rationale only; no effectiveness evidence or risk-owner acceptance exists |
| Status | Proposed treatment only; not accepted |
| Review Frequency | Quarterly |

### R-005: Web Server Breach (Vulnerable Ubuntu)

| Attribute | Detail |
|-----------|--------|
| Risk Description | Ubuntu web server has unpatched vulnerability leading to compromise |
| Inherent Score (scenario register) | 15 (High) |
| Proposed Target Residual Score (Unvalidated) | 4 (Low) |
| Residual Risk Level | Not assessed |
| Proposed Control Intent | SSH hardening, UFW firewall, service minimization, automatic updates |
| Proposed Treatment Rationale (Unvalidated) | Indicative rationale only; no effectiveness evidence or risk-owner acceptance exists |
| Status | Proposed treatment only; not accepted |
| Review Frequency | Monthly (patch review) |

### R-006: Insider Threat (Data Exfiltration)

| Attribute | Detail |
|-----------|--------|
| Risk Description | Disgruntled employee exports client list to competitor |
| Inherent Score (scenario register) | 10 (Medium) |
| Proposed Target Residual Score (Unvalidated) | 4 (Low) |
| Residual Risk Level | Not assessed |
| Proposed Control Intent | Access control (least privilege), user behavior logging |
| Proposed Treatment Rationale (Unvalidated) | Indicative rationale only; no effectiveness evidence or risk-owner acceptance exists |
| Status | Proposed treatment only; not accepted |
| Review Frequency | Quarterly (access reviews) |

### R-007: Third-Party Vendor Breach

| Attribute | Detail |
|-----------|--------|
| Risk Description | Cloud vendor (Salesforce, Microsoft 365) breach exposes client data |
| Inherent Score (scenario register) | 15 (High) |
| Proposed Target Residual Score (Unvalidated) | 8 (Medium) |
| Residual Risk Level | Not assessed |
| Proposed Control Intent | None Proposed in Phase 1 |
| Proposed Treatment Rationale (Unvalidated) | Indicative rationale only; no effectiveness evidence or risk-owner acceptance exists |
| Status | Proposed treatment only; not accepted |
| Recommended Action | Establish quarterly vendor risk assessment program |
| Review Frequency | Quarterly |

### R-008: Firewall Misconfiguration

| Attribute | Detail |
|-----------|--------|
| Risk Description | pfSense firewall misconfigured exposing internal network |
| Inherent Score (scenario register) | 12 (Medium) |
| Proposed Target Residual Score (Unvalidated) | 2 (Low) |
| Residual Risk Level | Not assessed |
| Proposed Control Intent | Change management process, quarterly firewall rule audit |
| Proposed Treatment Rationale (Unvalidated) | Indicative rationale only; no effectiveness evidence or risk-owner acceptance exists |
| Status | Proposed treatment only; not accepted |
| Review Frequency | Quarterly |

---

## 4. Residual Risk Heatmap

Likelihood (X-axis): 1 = Rare, 2 = Unlikely, 3 = Possible, 4 = Likely, 5 = Almost Certain

Impact (Y-axis): 1 = Negligible, 2 = Low, 3 = Medium, 4 = High, 5 = Critical

**Illustrative target grid:**

| Impact / Likelihood | 1 Rare | 2 Unlikely | 3 Possible | 4 Likely | 5 Almost certain |
|---|---|---|---|---|---|
| 5 Critical | R-003 | - | - | - | - |
| 4 High | - | R-002, R-007 | - | - | - |
| 3 Medium | R-004 | - | - | - | - |
| 2 Low | R-008 | R-001, R-005, R-006 | - | - | - |
| 1 Negligible | - | - | - | - | - |

| Target band | Count | Risks |
|---|---:|---|
| Critical | 0 | None proposed |
| High | 0 | None proposed |
| Medium | 2 | R-002, R-007 |
| Low | 6 | R-001, R-003, R-004, R-005, R-006, R-008 |

The grid is a planning example only. Every actual residual-risk rating remains **not assessed**. The absence of critical or high target values is not evidence that these risks have been reduced.

---

## 5. Recommendations

### 5.1 High Priority Recommendations

#### REC-001: Implement Multi-Factor Authentication (MFA)

| Attribute | Detail |
|-----------|--------|
| Risk Addressed | R-002 (Credential Theft) |
| Priority | High |
| Estimated Effort | 2-4 weeks |
| Estimated Cost | $3,000-5,000 (Microsoft 365 MFA or DUO) |
| Implementation Steps | 1. Select MFA solution (Microsoft Authenticator or DUO)
| | 2. Enroll all 150 remote employees
| | 3. Enforce MFA for all remote access
| | 4. Enforce MFA for all administrative accounts |
| Success Metric | 100% of remote users have MFA enabled |
| Target Completion | Phase 2 (Q3 2026) |

#### REC-002: Expand Wazuh SIEM to Remaining Endpoints

| Attribute | Detail |
|-----------|--------|
| Risk Addressed | R-004 (Audit Failure), R-003 (Malware Detection) |
| Priority | High |
| Estimated Effort | 4-6 weeks |
| Estimated Cost | $0 (open source) + 40 staff hours |
| Implementation Steps | 1. Deploy Wazuh agents to remaining 150 remote endpoints
| | 2. Configure log collection for all endpoints
| | 3. Establish alerting rules for remote endpoints
| | 4. Train security staff on SIEM operations |
| Success Metric | 100% endpoint coverage with active agents |
| Target Completion | Phase 2 (Q3 2026) |

---

### 5.2 Medium Priority Recommendations

#### REC-003: Establish Vendor Risk Assessment Program

| Attribute | Detail |
|-----------|--------|
| Risk Addressed | R-007 (Third-Party Vendor Breach) |
| Priority | Medium |
| Estimated Effort | Ongoing process |
| Estimated Cost | $0 (internal process) |
| Implementation Steps | 1. Create vendor risk assessment template
| | 2. Identify top 10 vendors by data sensitivity
| | 3. Assess vendors annually
| | 4. Document vendor security posture |
| Success Metric | Top 10 vendors assessed within 12 months |
| Target Completion | Phase 2 (Q4 2026) |

#### REC-004: Conduct Annual Penetration Testing

| Attribute | Detail |
|-----------|--------|
| Risk Addressed | R-001, R-002, R-003, R-005 |
| Priority | Medium |
| Estimated Effort | 2-3 weeks |
| Estimated Cost | $10,000-20,000 (external vendor) |
| Implementation Steps | 1. Engage qualified penetration testing firm
| | 2. Test external-facing assets (web server, remote access)
| | 3. Test internal network segmentation
| | 4. Remediate identified vulnerabilities |
| Success Metric | No critical or high findings in pen test report |
| Target Completion | Phase 3 (Q1 2027) |

#### REC-005: Implement Data Loss Prevention (DLP)

| Attribute | Detail |
|-----------|--------|
| Risk Addressed | R-006 (Insider Threat) |
| Priority | Medium |
| Estimated Effort | 4-6 weeks |
| Estimated Cost | $5,000-10,000 (Microsoft Purview DLP) |
| Implementation Steps | 1. Define sensitive data types (PAN, SSN, financial data)
| | 2. Create DLP policies for email and endpoints
| | 3. Monitor and refine policies |
| Success Metric | Unauthorized data transfers blocked or alerted |
| Target Completion | Phase 3 (Q1 2027) |

---

### 5.3 Low Priority Recommendations

#### REC-006: Conduct Tabletop Incident Response Exercises

| Attribute | Detail |
|-----------|--------|
| Risk Addressed | R-004 (Audit Failure), Incident Response |
| Priority | Low |
| Estimated Effort | 2 days |
| Estimated Cost | $0 (internal) |
| Implementation Steps | 1. Develop ransomware tabletop scenario
| | 2. Conduct exercise with IRT members
| | 3. Document lessons learned
| | 4. Update IR policy based on findings |
| Success Metric | IR plan tested and updated annually |
| Target Completion | Phase 3 (Q4 2026) |

#### REC-007: Implement Just-in-Time (JIT) Privileged Access

| Attribute | Detail |
|-----------|--------|
| Risk Addressed | R-002, R-006 |
| Priority | Low |
| Estimated Effort | 4-8 weeks |
| Estimated Cost | $0-5,000 (Microsoft PIM) |
| Implementation Steps | 1. Deploy Privileged Identity Management (PIM)
| | 2. Require approval for admin access
| | 3. Enforce time-limited access |
| Success Metric | All admin access requests approved and logged |
| Target Completion | Phase 3 (Q2 2027) |

#### REC-008: Establish Security Awareness Training Program

| Attribute | Detail |
|-----------|--------|
| Risk Addressed | R-002, R-003 |
| Priority | Low |
| Estimated Effort | Ongoing |
| Estimated Cost | $2,000-5,000 per year |
| Implementation Steps | 1. Deploy security awareness training platform
| | 2. Conduct quarterly phishing simulations
| | 3. Track completion rates and click rates |
| Success Metric | 95% completion rate, <10% phishing click rate |
| Target Completion | Phase 3 (Q4 2026) |

---

## 6. Security Roadmap

| Phase | Timeline | Activities | Success Criteria |
|-------|----------|------------|------------------|
| Phase 1 (Design Draft; Not Executed) | Months 1-3 | Risk assessment, policies, technical controls (Windows, Ubuntu, pfSense, Wazuh), testing, evidence collection | All Phase 1 controls implemented, tested, evidenced and reviewed (future target; not achieved) |
| Phase 2 (Next) | Months 4-6 | MFA rollout, Wazuh expansion to 150 endpoints, vendor risk assessment program | MFA enabled for all remote users; 100% endpoint coverage |
| Phase 3 (Future) | Months 7-12 | Penetration testing, DLP implementation, IR tabletop exercises, security awareness training | No critical findings; DLP policies active |
| Phase 4 (Long-term) | Months 13-18 | JIT privileged access, SOAR integration, threat hunting | Automated response; proactive threat detection |

---

## 7. Proposed risk treatment review

No residual risk has been approved or accepted. Reviewers should evaluate the following evidence before making an acceptance decision.

| Risk ID | Proposed treatment rationale | Acceptance evidence still required |
|---|---|---|
| R-001 | Segmentation is intended to restrict lateral movement | Reviewed rule export and paired allowed/denied tests |
| R-002 | Authentication and least privilege are intended to limit credential abuse | Effective policy, MFA scope and access-test evidence |
| R-003 | Endpoint controls and protected backups are intended to support containment and recovery | Safe control test, isolated restore, recovery checks and owner review |
| R-004 | Logging and evidence handling are intended to support investigation | Source coverage, time consistency, retention and retrieval tests |
| R-005 | Hardening is intended to reduce unnecessary exposure | Verified baseline, patch assessment and service exposure checks |
| R-006 | Least privilege and logging are proposed safeguards; effectiveness is untested | Role review, access tests and proportionate monitoring evidence |
| R-007 | Supplier due diligence is intended to identify evidence gaps and dependencies | Scoped review, unresolved findings and accountable business decision |
| R-008 | Change review and regression testing are intended to detect configuration errors | Approved change, rollback record and regression results |

**Approval record:** No sign-off recorded. A future decision must identify the risk owner, rationale, conditions, evidence and review date.

---

## 8. Proposed risk review schedule

| Risk ID | Proposed frequency | Next review date | Responsible role |
|---|---|---|---|
| R-001 | Quarterly and after a network change | To be agreed | Network security owner |
| R-002 | Monthly and after an access incident | To be agreed | IAM owner |
| R-003 | Monthly and after an endpoint or recovery change | To be agreed | Endpoint and resilience owner |
| R-004 | Quarterly and after a logging gap | To be agreed | Security operations owner |
| R-005 | Monthly and after a material service change | To be agreed | Application / infrastructure owner |
| R-006 | Quarterly and after role or data-scope changes | To be agreed | Data and IAM owners |
| R-007 | Quarterly and after a supplier/service change | To be agreed | Third-party risk owner |
| R-008 | Quarterly and after firewall changes | To be agreed | Network security owner |

Frequencies are lab planning choices, not prescribed framework intervals or approved organizational commitments.

---

## 9. Related Documents

| Document | Location |
|----------|----------|
| Risk Assessment | 04-Risk-Assessment/risk-assessment.md |
| Risk Register | 04-Risk-Assessment/risk-register.md |
| Risk Heatmap | 04-Risk-Assessment/risk-heatmap.md |
| Testing Results | 09-Testing-and-Validation/results.md |
| Evidence Summary | 10-Evidence/evidence-summary.md |

---

## 10. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | April 2026 | S. Singh | Initial draft |
| 0.5 | May 2026 | S. Singh | Added recommendations and roadmap |
| 1.0 | May 2026 | S. Singh | Draft learning edition |

---

**End of Residual Risk and Recommendations**
