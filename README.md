# Apex Capital security controls lab

**A fictional, four-VM financial-services security design and validation plan.** This publication turns the source notes into a reviewable case study covering segmentation, endpoint hardening, centralized monitoring, risk ownership and audit evidence. It is a lab/documentation project, not a client engagement, compliance attestation or claim that the controls have been deployed.

## What the work demonstrates

- Translates business protection goals into network zones, firewall intent, system baselines and test scenarios.
- Uses an 8-risk register with a transparent 1–5 likelihood × 1–5 impact method and named accountable roles.
- Connects selected safeguards to exact NIST Cybersecurity Framework 2.0 and ISO/IEC 27001:2022 references.
- Defines a repeatable evidence plan for segmentation, access controls, endpoint protection, logging and recovery.
- Identifies supplier assurance as an explicit risk area and describes the missing workflow needed to assess vendors.

## Review the project

1. Open [the project overview](site/index.html) for a visual summary and architecture.
2. Read [scope and assumptions](docs/scope-and-assumptions.md) before interpreting the fictional business context.
3. Review the [architecture](docs/architecture.md), [risk register](docs/risk-register.md), and [control crosswalk](docs/control-mapping.md).
4. Check [validation and evidence status](docs/validation-plan.md) and [source provenance](docs/provenance.md).
5. See [references](docs/references.md) for primary framework and product documentation.

## Status at publication

The source contains proposed architecture, control descriptions and test procedures. It does not contain the referenced screenshots or raw execution logs. Therefore, tests are presented as **planned; execution evidence pending**. No residual risk reduction, successful test outcome, deployment status, certification, audit opinion, or regulatory compliance is asserted.

## Scope boundary

The lab models an internal environment with a DMZ, an internal subnet and a management/monitoring subnet. It is not a cloud deployment and does not implement a complete third-party risk management (TPRM) program. Supplier risk is included as a risk scenario and control-mapping thread; vendor inventory, evidence review, decision workflow, contractual review and ongoing monitoring remain proposed next work.

See [limitations and next steps](docs/limitations-and-next-steps.md) for the specific evidence and implementation work required before making operational claims.
