# Data contracts

The observer's outputs use two contract identities:

- `koa_audit.observation.v1`: current GitHub API observations, inventory provenance, completeness and historic metadata in **separate** fields. Contract: `schemas/observation.schema.json`.
- `koa_audit.legacy_record.v1`: a sanitized, historical, non-authoritative summary. Contract: `schemas/legacy-record.schema.json`.

Native schemas are not rewritten: KonnaxionDiag's security/release authorities, KorDiag subject bindings, KristalDiag's independent qualification and LevelUpDiag's campaign semantics remain owned by those systems. These normalized records **do not** carry signatures or independent cryptographic verification.

Version `v1` is a *report format*, not a declaration that these diagnostic source snapshots are currently active or that GitHub owners authorized any action. Treat unknown fields conservatively; do not generate a `PASS` or an approval from an observation report.
