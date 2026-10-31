<!-- Frozen source: https://github.com/Rejean-McCormick/Akor/blob/cc86fccc9dd9a73aec937486a7e3cfbc917d0fdb/docs/wiki/Open-Decisions.md | commit: cc86fccc9dd9a73aec937486a7e3cfbc917d0fdb | SHA-256: aae4df504f4b8439fc33e7930014ecbc3e81bf706e157c5cc9f90457124e96c4 -->

# Open Decisions

Akor's name and educational direction are established. The following technical and governance decisions are **not yet resolved**.

| Topic | Decision to make | Constraint |
| --- | --- | --- |
| Runtime packaging | Library, sidecar or independent server? | No duplicate Orgo mission state |
| Identity | How does Ekole's school session map to Orgo actor/world membership? | Server verified; no implicit email linking |
| Role assignment | Student choice, teacher assignment or mixed? | Equitable, private, overridable |
| Social interaction | Face-to-face, structured messaging, co-editing or all three? | Age-appropriate moderation and audit |
| Distributed information | Which fragments require runtime authorization and what join logic? | Orgo-enforced release; no client-only secrecy |
| Missing participants | Combine roles, teacher mediator or explicit synthetic substitute? | Never fake a real pupil's contribution |
| Bakery curriculum | Keep addition version and create multiplication variant? | Preserve `qc-pri-ma-006` source and review `qc-pri-ma-008` |
| Release | How to package a reviewed bakery WorldRelease? | Orgo_Worlds canonical ownership |
| Student work | What artifacts and personal data should be persisted? | Ekole evidence boundary + retention rules |
| Teacher intervention | Which actions require human approval/audit? | Authenticated, reversible when appropriate |
| Offline | Read-only lesson fallback vs mission recovery protocol? | No silent competing mission engine |
| Accessibility | Which participation modes are supported initially? | No diagnosis labels or coercive speed ranking |
| Multilingual | Which strings need human translation review? | Narrative role texts are not guaranteed translated |

An architecture decision record (ADR) should be created when each consequential item is resolved and linked here with the date, rationale, version and affected repositories.
