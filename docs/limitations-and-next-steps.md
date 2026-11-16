# Limitations and next steps

## What this edition can support

It supports a technical discussion of a segmented four-VM lab design, risk-based control planning, selected framework cross-references, incident response decisions and structured validation. The complete incident response plan and proposed tabletop exercise connect design intent to containment, evidence preservation, communication, recovery and improvement tracking.

## What it cannot support yet

- Proof that any VM, firewall rule, endpoint policy or Wazuh integration was configured or operated.
- A passed control test, quantified reduction in risk, implemented-controls percentage or audit conclusion.
- A compliance claim for ISO 27001, NIST, PCI DSS, SEBI, or any other standard/regulation.
- A completed vendor due-diligence assessment or operational TPRM program.
- Production capacity, high availability, cloud security or real-world business impact.

## Small, reviewable next steps

1. Review the proposed four-interface flow matrix, rule order, NAT and management-source scope, then provision the isolated lab.
2. Execute T-01 in a private lab, capture sanitized configuration plus paired allowed/blocked path evidence, and record software versions.
3. Execute T-05 with a synthetic event and verify host attribution, timestamp, alert mapping and retention.
4. Complete T-07 with a fictional supplier packet: inventory entry, tiering rationale, evidence checklist, gap decision, remediation owner and reassessment date.
5. Have a reviewer challenge the risk scores and mappings, and conduct the proposed tabletop; record actual participant decisions, feedback, changes and unresolved assumptions.
6. Publish only sanitized evidence artifacts with reproducible steps and explicit test status.

The separate [Vendor Assurance Desk](https://github.com/dedsec-terminal/Vendor-Assurance-Desk) implements a synthetic supplier assessment and retest workflow with evidence checks and measured fixture results. Its software tests do not execute the Apex VM controls or establish real vendor assurance. A human review and onboarding decision remain separate requirements.
