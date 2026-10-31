<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/40-integration/kristal-v5/legacy-compat.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: da5cea2e07db6f7790b46fe3fc53cd59c7186880ba81d80be0914f5bb5f1d3fd -->

# Kristal v4/v3 compatibility migration

The previous kOA documentation encoded several older assumptions that are now compatibility-only.

| Legacy assumption / field | v5-aligned treatment |
|---|---|
| `kristal.v3:jcs-rfc8785` | `kristal.v5:jcs-rfc8785` |
| mandatory Claim-IR pipeline | optional extractor/resolution profile |
| single Exchange/canon concept | Working Exchange and Reference Exchange are distinct |
| validation `PASS/FAIL` only | v5 validation status + optional `validated_as`/certainty/scope |
| validation failure blocks all compilation | profile-specific gates; Working compilation may still occur |
| `pack_id` | normalize to `runtime_pack_id` |
| `exchange_ref` in pack context | normalize to `source_exchange_ref` |
| `query_contract` | normalize to `query_contract_ref` |
| activation means trusted/reference | activation is an operational state only |
| “source of truth” / “canonical truth” | reference source / recognized reference, with explicit scope |

Legacy parsers may accept documented aliases, but newly emitted v5 records should use v5 field names and semantics.
