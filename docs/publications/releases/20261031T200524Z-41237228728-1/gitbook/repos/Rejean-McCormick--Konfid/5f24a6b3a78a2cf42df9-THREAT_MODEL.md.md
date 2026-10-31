<!-- Frozen source: https://github.com/Rejean-McCormick/Konfid/blob/e3d96da8e880815dc6e6d75e8662f2ab6e871bfc/docs/THREAT_MODEL.md | commit: e3d96da8e880815dc6e6d75e8662f2ab6e871bfc | SHA-256: 12c4ec440fb61f940cde91d72469c9d8438ae8b39a1cd08b9716fa3a0d43ae40 -->

# Threat model summary

Protected assets include identity bindings, grants, policy state, response authority, approval receipts, signing credentials and audit evidence.

Key threats and structural mitigations:

- **Compromised email:** email cannot establish canonical identity.
- **Compromised Konnaxion:** workload scopes and actor assertions prevent arbitrary cross-system authority.
- **Compromised Orgo:** Orgo cannot execute; Konfid revalidates approver roles, digest and quorum.
- **Compromised detector:** detectors have no enforcement credentials.
- **False positive:** response policy and minimal containment sit between signal and action.
- **Replay/duplicate:** action IDs, idempotency keys and receipts.
- **Cross-tenant confusion:** authenticated caller tenant is checked against request tenant.
- **Telemetry DoS:** production should isolate Overwatch workers from authorization/revocation capacity.
- **IdP outage:** existing bounded sessions and sovereign break-glass paths remain separate concerns.
- **Insider admin:** avoid wildcard credentials; use separation of duties, short-lived elevation and immutable audit.
