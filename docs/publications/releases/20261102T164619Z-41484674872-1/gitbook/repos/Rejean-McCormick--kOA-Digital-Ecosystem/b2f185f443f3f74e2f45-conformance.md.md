<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/40-integration/kristal-v5/conformance.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 2d86ce22d09b7b8e9faae649d28cb44f89d058e073fd15824fbe5f4702abdb93 -->

# Kristal v5 conformance for kOA

A kOA integration claiming Kristal v5 alignment must demonstrate at least:

1. exact version/tag/commit/canonicalization pin verification;
2. Structured Epistemic State support at the Kristal boundary;
3. no assumption that Claim-IR is universally required;
4. separate compile/validation/recognition/publication/activation status;
5. no universal `no compile on fail` rule;
6. preservation of Working versus Reference status;
7. Runtime Pack `source_artifact_status` preservation;
8. Reader Policy and Query Contract compatibility handling;
9. authority-recognition metadata kept distinct from signatures and validation;
10. deployment activation delegated to exactly one owner;
11. rollback/downgrade/revocation checks applied by the activation owner according to policy;
12. no kOA extension silently changes Kristal identity or epistemic semantics.

A stricter kOA production profile may block reference publication or activation after failed/insufficient validation. Such a gate must be identified as a profile/deployment policy, not a Kristal core rule.
