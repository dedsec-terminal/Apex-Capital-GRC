# Validation plan and evidence register

## Current status

An elevated VM inventory check at `2026-11-16 14:35:09 UTC` found zero registered virtual machines. The lab therefore is not ready to run these VM-dependent cases. **All cases below are planned and not executed.** No pass/fail result is asserted.

## Prioritized test cases

| Test | Risk | Procedure summary | Expected result | Evidence artifact | Status |
|---|---|---|---|---|---|
| T-01 Segmentation | R-001 | From DMZ test host, attempt only authorized, approved connections to internal lab host; inspect firewall logs | Prohibited paths denied and logged; allowed paths match approved matrix | Timestamped command output, source/destination, pfSense rule export and log entry | Planned; evidence pending |
| T-02 Management access | R-001, R-008 | Test SSH/RDP from management and non-management zones | Admin access limited to approved management sources | Sanitized connectivity results and effective firewall rules | Planned; evidence pending |
| T-03 Windows policy | R-002, R-006 | Export effective local/security policy and test access with synthetic accounts | Configured access restrictions match approved baseline | Policy export, test matrix, account cleanup record | Planned; evidence pending |
| T-04 Endpoint protection | R-003 | Verify endpoint protection status using safe vendor test procedure in isolated VM | Protection state is visible and test event is recorded | Timestamped status output and security event; no real malware | Planned; evidence pending |
| T-05 Logging pipeline | R-004 | Generate a controlled failed authentication event and trace source-to-alert | Event is received with correct host/time and expected alerting | Redacted source event, Wazuh record, timestamps and rule ID | Planned; evidence pending |
| T-06 Backup restore | R-003 | Restore a synthetic file or system artifact into an isolated target | Data restored and integrity checked within a defined objective | Backup job, restore log, checksum and measured duration | Planned; evidence pending |
| T-07 Supplier review tabletop | R-007 | Assess a fictional critical SaaS supplier packet against a documented rubric; record gaps and decision | Reviewer identifies evidence gaps, treatment, approver and reassessment trigger | Synthetic vendor packet, completed scorecard and decision log | Planned; evidence pending |
| T-08 Change/config regression | R-008 | Compare firewall export to approved baseline; review an authorized rule change and retest affected paths | Change has approval and rollback; tests detect unexpected path changes | Before/after config diff, approval record and regression output | Planned; evidence pending |

## Evidence quality rules

For each run, capture test ID, date/time and timezone, tester role, target version/configuration, exact steps, expected and observed result, artifact path, redaction notes, reviewer and disposition. Store raw artifacts privately; publish only synthetic or irreversibly sanitized evidence. Hash artifacts if integrity tracking is needed. Do not mark “Pass” from an expected result or command transcript alone.

## Execution guardrails

Run only in an isolated lab that you own or are authorized to test. Use synthetic identities and data. Avoid public exposure of management services. For endpoint test content, follow the platform vendor’s safe test procedure and isolate the VM. Restore snapshots and remove temporary test accounts after validation.
