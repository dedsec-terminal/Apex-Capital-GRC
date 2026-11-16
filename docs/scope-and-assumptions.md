# Scope and assumptions

## Scenario

“Apex Capital” is a fictional name used for a small financial-services lab scenario. It is not a represented client, actual financial institution, or assertion of an engagement. The source notes describe protection goals for financial and personal data; those are treated here as scenario requirements, not evidence that such data or systems exist in the lab.

## In scope

- A four-VM design: pfSense routing/firewall, Ubuntu web host, Windows internal host and Wazuh monitoring host.
- Three logical IPv4 subnets and intended traffic boundaries.
- Risk identification, control intent, policy topics and test planning.
- Proposed references to NIST CSF 2.0 and ISO/IEC 27001:2022 Annex A.

## Out of scope

- A real organization, client, production environment, cloud account, or payment-card environment.
- A formal ISO certification, SOC 2 report, PCI DSS assessment, SEBI compliance determination, or legal interpretation.
- Executed penetration testing, operational monitoring, independent assurance, or risk acceptance.
- A complete supplier due-diligence or lifecycle management program.

## Assumptions requiring validation

The business size, workforce, data categories, service criticality, regulatory applicability and production topology in the original notes are scenario assumptions. The four-VM design is a simplified lab abstraction; it does not implement the multiple web, database or file servers referenced in some source requirements. No claim of a real deployment or customer data processing is made.

## Data handling

This public edition excludes sample personal identifiers, event-log usernames, credentials and purported client-specific details. Use synthetic identities and non-sensitive test data in any future demonstration. Never commit secrets, private keys, real customer records or unredacted logs.
