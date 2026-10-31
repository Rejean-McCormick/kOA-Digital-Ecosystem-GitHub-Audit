<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/Operations-and-Incidents | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: 5f4112decf9c5049755ff36dba0163e62ccb193f3963f679df8a81de3ee459c9 -->

# Operations, Recovery, and Incidents

These are **target procedures** for a future production service. In Tandem, the operational workflow and its audit/transaction guarantees must belong to **Orgo** (ADR 0008), not the KOMPOSE simulator. The local repository does not include monitoring, hosting, network logs, or a transactional database.

## Session incidents

| Incident | Expected response |
|---|---|
| Leaked or expired code | Revoke/rotate it; verify identity independently |
| Disconnected student | Resume from authorized server state without duplicate enrollment |
| Teacher pause | Stop active progression; restore previous state upon resumption |
| Absent guardian | Propose reassignment or another access route |
| Blocked mission | Display missing prerequisites; inspect dependencies |
| No feasible casting | Block publication and privately explain hard-constraint conflicts |
| Private information disclosed | Stop exposure, contain incident, preserve records, follow school procedure |
| Incorrect or unauthorized source | Withdraw version, correct content, notify as required by editorial policy |

## Target backup and consistency model

Persist state, `session_version`, decisions, and events **atomically**, using an outbox, deduplication, and idempotent recovery. After reconnection, clients load an **audience-filtered projection**. Private data must have a retention policy separate from published documents.

## Logging

Do not place real names, rankings, aversions, private content, or raw diagnostics in general access logs. Sensitive operations should be auditable only by authorized staff.

## Before a live pilot

Define security ownership, support, restoration, incident notifications, content review, staff roles, retention periods, and session-shutdown procedures.

[[Home|← Home]] · [[Security-Privacy-and-Fairness|Student protection →]]
