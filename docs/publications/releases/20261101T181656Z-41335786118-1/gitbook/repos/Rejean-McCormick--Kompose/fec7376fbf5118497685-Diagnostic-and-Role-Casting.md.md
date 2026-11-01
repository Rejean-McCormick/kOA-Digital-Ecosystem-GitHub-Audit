<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/Diagnostic-and-Role-Casting | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: 62347331014fc3042b26d7c69263d2fd36c24eeda8bab5099e887ca42c55924d -->

# Adaptive Diagnostic and Role Casting

The diagnostic's **primary purpose is to adapt learning** to each participant. Using its results to determine role-selection order is a separate, **optional** game mechanic that requires defensible comparability.

## Two assessment outputs

- **Private learning profile:** observed dimensions, accommodations, recommended instructions, and supportive formats.
- **Optional selection order:** derived only from an instrument validated for comparing results despite variations in question difficulty and permitted accommodations. If comparability cannot be shown, use a non-ranking policy.

No medical or psychological inference, no public ranking, and no exclusion due to a missed assessment.

## Reference casting policy

The `tiers_choix` policy permits an initial group to choose sequentially among compatible roles. The number of turns is `ceil(n / 3)`: **7 turns for 20 students**. Other participants receive **proposed** assignments. Publishing any plan requires teacher approval.

### Production solver requirements

1. **Hard constraints:** safety, accessibility, permissions, role capacities, and essential functions.
2. Consistent, transactional reservation of eligible role choices.
3. Relationship constraints on **required interactions between roles**, not only student–role pairs.
4. **Soft preferences:** interests, desirable cooperation, diversity of participation, reasonable challenge.
5. Clear private explanations and teacher review.
6. A fallback when no feasible solution exists, without relaxing hard constraints.

Ranking alone or a greedy allocator is inadequate when incompatibilities involve participant interactions. CP-SAT or mixed-integer programming is being considered; **this repository does not implement a full solver**.

## Affinities and aversions

Teachers may document desirable collaboration or a necessary separation. Such data must be minimal, justified, private, and session-scoped; KOMPOSE must not build a student “social score.” Safety-related separation overrides narrative preference.

## Policies without rankings

Teacher-guided assignments, rotating choices, supervised lotteries, and other accommodations. Policies must be communicated without stigmatizing anyone.

**Available code:** `src/kompose/allocation_policy.py` calculates selection quotas and simple reference rules. `examples/capsule-rivieres/allocation.preview.example.json` is a **fictional preview**, not an actual test result.

[[Home|← Home]] · [[Teacher-Console|Supervision →]]
