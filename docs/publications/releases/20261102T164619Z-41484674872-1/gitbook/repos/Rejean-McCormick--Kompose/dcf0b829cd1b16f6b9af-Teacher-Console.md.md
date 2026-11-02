<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/Teacher-Console | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: 9a0c50770842b9cb4c996345a0c2aced177e9bc00933f157b2fcb01d66de3ae9 -->

# Teacher Console and Supervision

The console is a **target interface**, not a working frontend in v0.2.0. In any real Tandem flow, its operational commands must go through **Orgo**, not a parallel KOMPOSE task engine (ADR 0008). It is designed to configure and protect sessions through their complete lifecycle.

## Recommended views

| View | Responsibilities |
|---|---|
| Preparation | Capsule, content, role capacities, accessibility, assignment policy |
| Enrollment | Attendance, resumption, admissions, overall state |
| Diagnostic | Validity and comparability, accommodations, private educational decisions |
| Casting | Allocation preview, conflicts, changes, publication |
| Adventure | Missions, phases, guardians, access, deadlock alerts, interventions |
| Closure | Reflection, deletion, minimal authorized exports, archival |

## Social constraints

An affinity must not automatically force students together. An aversion is a **temporary signal** whose use requires justification and proportionality. Safety-related separation is a hard constraint; desirable collaboration is a soft preference.

**Never expose to classmates:** reasons for incompatibilities, diagnostic scores, sensitive personal details, or peer rankings. Indirect narrative messages must not reveal them either.

## Human interventions

- Revise an assignment and record the reason privately.
- Pause and resume **from the previous state**.
- Reassign an absent guardian without changing the Kristal or silently granting new access.
- Unblock a mission through a suitable alternative **without bypassing safety rules**.
- Complete or cancel a capsule and provide appropriate feedback.

Reference commands use an **expected session version**; future services must verify actor identity, school scope, and authorization. The proposed API includes `/teacher/sessions/{sessionId}/commands`, but no server exists yet.

[[Home|← Home]] · [[Security-Privacy-and-Fairness|Security →]]
