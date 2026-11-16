> **Publication status:** Fictional public lab design. This chapter describes intended firewall policy; no rules are configured or tested. The three internal zones are DMZ `10.0.1.0/24`, internal `10.0.2.0/24`, and management `10.0.3.0/24`. pfSense has a separate WAN uplink plus one interface per zone.

# Enterprise Network Architecture

## Proposed interfaces

| pfSense interface | Zone | Gateway address | Intended purpose |
|---|---|---:|---|
| WAN | Uplink | Assigned by the lab network | External connectivity; inbound access denied unless an explicit NAT and firewall rule are approved |
| OPT1 | DMZ | `10.0.1.1/24` | Ubuntu web host `10.0.1.10` |
| LAN | Internal | `10.0.2.1/24` | Windows host `10.0.2.10` |
| OPT2 | Management | `10.0.3.1/24` | Wazuh `10.0.3.10` and named administrator endpoints |

## Intended flow policy

Rules are illustrative design intent. Apply least privilege, validate stateful return behavior, and log both permitted and denied security-relevant traffic. Do not treat a written rule table as evidence that a firewall is configured.

| Source | Destination | Service | Intended decision | Conditions and purpose |
|---|---|---|---|---|
| Internet | DMZ Ubuntu | TCP 80/443 | Allow only through explicit WAN NAT/port-forward | Publish only the web service; TLS termination and certificate trust require separate validation |
| WAN | Internal or management zones | Any | Deny | No direct public access to internal or management hosts |
| Named management endpoint(s) | Ubuntu | TCP 22 | Allow | Explicit source addresses only; SSH authentication and host-key controls are separate requirements |
| Named management endpoint(s) | Windows | TCP 3389 | Allow | Restrict RDP to approved administrative source(s); do not allow the whole management subnet by default |
| Ubuntu DMZ | Windows internal | Any | Deny by default | Add only documented application dependencies after review |
| Windows and Ubuntu agents | Wazuh manager | TCP 1514 | Allow | Agent-to-manager event channel; restrict sources to enrolled agents |
| Approved enrollment source(s) | Wazuh enrollment service | TCP 1515 | Temporary/controlled allow | Use only for enrollment; restrict source, duration, and enrollment credentials, then remove exposure if no longer needed |
| pfSense | Wazuh syslog listener | UDP 514 | Optional, disabled unless configured | Enable only if the receiver and transport are intentionally configured; UDP has no transport encryption |
| Named management endpoint(s) | Wazuh dashboard | TCP 443 | Allow | Restrict source addresses; require authenticated administration |
| Any other inter-zone flow | Any | Any | Deny by default | Document exceptions with owner, rationale, expiry/review date, and validation case |

## Verification plan

When the lab is provisioned, capture the pfSense interface assignment, NAT and firewall rule exports, and timestamped positive and negative connection tests. Confirm that an allowed path works, a prohibited path fails, and firewall logs record the decision. No VM was registered at the readiness check, so this plan has not been executed.

---

**End of Network Architecture**
