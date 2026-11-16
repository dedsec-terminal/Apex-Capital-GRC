# Risk register

## Method

The source method assigns likelihood and impact from 1–5 and multiplies them (score 1–25). Ratings are Critical 20–25, High 13–19, Medium 7–12, Low 1–6. This is an initial qualitative prioritization model, not a calibrated quantitative risk model. Scores below are **inherent scenario estimates**; residual scores are intentionally omitted until control operation and evidence are reviewed.

## Risks and accountability

| ID | Scenario risk | L | I | Score | Indicative owner role | Control intent / evidence still needed |
|---|---|---:|---:|---:|---|---|
| R-001 | A compromised DMZ host reaches internal systems | 3 | 5 | 15 High | Network security owner | Default-deny inter-zone policy; rule export and paired connectivity tests |
| R-002 | Credential compromise enables unauthorized access or data exposure | 4 | 5 | 20 Critical | IAM owner | MFA/least privilege/lockout design; effective-policy output and access review evidence |
| R-003 | Ransomware disrupts systems or damages data | 4 | 5 | 20 Critical | Endpoint and resilience owner | Endpoint protection, protected backups and restore exercise evidence |
| R-004 | Incomplete logging or retained evidence impairs investigation/audit | 3 | 4 | 12 Medium | Security operations owner | Source coverage, time sync, retention and retrieval test artifacts |
| R-005 | Public service compromise exposes the host or provides a foothold | 3 | 5 | 15 High | Application / infrastructure owner | Hardened baseline, vulnerability remediation and external-surface verification |
| R-006 | Authorized insider misuses access to sensitive information | 2 | 5 | 10 Medium | Data owner and IAM owner | Role-based access, segregation of duties and periodic access review |
| R-007 | Supplier or service-provider weakness affects confidentiality or availability | 3 | 5 | 15 High | Procurement / third-party risk owner | Supplier inventory, criticality, due diligence, decision record and monitoring evidence |
| R-008 | Firewall configuration drift or rule error exposes a protected path | 3 | 4 | 12 Medium | Network security owner | Approved baseline, change review, config backup and regression testing |

Owners are proposed role assignments for the scenario, not identified people or accepted risk owners. Scores should be revisited with business owners using actual asset, threat, exposure and control evidence.

## Supplier-risk thread

R-007 is a scenario risk only; no vendor assessment has been performed. A minimal future workflow should record supplier service/data access, criticality rationale, evidence requested and reviewed, control gaps, treatment decision, accountable approver, contract requirements, reassessment date and offboarding trigger. Evidence should be proportionate to supplier criticality and must not be inferred from marketing claims alone.
