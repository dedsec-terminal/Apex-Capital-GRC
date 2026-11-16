# Source provenance and editorial treatment

## Inputs

This edition organizes all 29 original Markdown chapters into 13 numbered sections, retaining their substantive architecture, requirements, policies, technical procedures and testing detail while correcting unsupported claims and inconsistencies. Three additional chapters provide a capability evaluation, an incident response plan and a proposed tabletop exercise. The original working folder is preserved unchanged. No `.obsidian` configuration is included.

The summarized risk and test records displayed on the static site are also available in `data/register.json` for machine-readable review. They reflect the curated values in this edition and mark every test as planned, not executed.

## Claim handling

- Architecture addresses and VM roles are reproduced as documented design values; they were not independently observed on running VMs.
- The original risk list is retained as scenario risks, while implementation and residual-risk claims are removed pending evidence.
- The original test procedures are reformatted as plans. The source results file's 13 “Pass” assertions and missing evidence paths conflict with the detailed pending tracker; because no referenced screenshots/logs were present in the source snapshot, this edition reports execution evidence pending.
- Fictional organization context and regulatory references are not treated as client facts or legal conclusions.
- Supplier assessment is identified as an uncompleted workstream; no completed vendor review is implied.
- Framework mappings were curated to NIST CSF 2.0 and ISO/IEC 27001:2022 identifiers using a local framework catalog. They are proposed relationships, not verified control applicability or implementation.

## Sensitive information

This edition intentionally excludes raw usernames, personal identifiers, credentials, purported client details and unredacted event content. Review all future artifacts for secrets and personal data before publishing.

## Reproduction

The documented architecture and tests are sufficient to plan an isolated rebuild, but not to reproduce a validated result. Capture configuration exports, versions, sanitized raw outputs and review records before upgrading any planned test to executed or passed.
