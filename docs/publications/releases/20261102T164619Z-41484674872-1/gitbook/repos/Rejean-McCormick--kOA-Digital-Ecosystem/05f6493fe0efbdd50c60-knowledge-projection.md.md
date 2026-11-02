<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/40-integration/knowledge-projection.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 7a82d9f9a0e8e0b1ad7609330592f01f0d1bc90087c41e01e3bc2f53f0e62eaf -->

# Knowledge acquisition → Kristal v6 canon → consumer/action projection

**Status:** current frozen cross-repository contract baseline — 2026-10-01

## Authority direction

```text
source acquisition / owner snapshots
    → EncyKlopedia immutable evidence / referent candidates
    → Da’at mapping / ACL
    → Kristal referent identity + Kristal State
    → rebuildable UCKK / runtime projection
    → optional authorized action request through an owner contract
```

## Current contract set

| Surface | Current identifier |
|---|---|
| Kristal Standard | `6.0.0` |
| Canonicalization | `kristal.v6:jcs-rfc8785` |
| Kristal Referent Registry | `kristal.referent-registry/1.0.0` |
| EncyKlopedia handoff | `encyklopedia.corpus-harvest-handoff/1.0.0` |
| IK build request | `kristal.build.request/2.0.0` |
| IK artifact ready | `kristal.artifact.ready/2.0.0` |
| IK revision request | `kristal.revision.request/2.0.0` |
| UCKK / Univers-Cité projection | `uckk.univers-cite-projection/1.0.0` |

Machine-readable set: [`knowledge-projection-contract-set.json`](./knowledge-projection-contract-set.json).

## Kristal v6 representation

The boundary now maps knowledge into `kristal_state` rather than v5 Structured Epistemic State. The important generalized surfaces are:

- `valuations[]`: typed boolean/categorical/ordinal/scalar/interval/probability/distribution/vector/partial-order/state/temporal values;
- `coordinates`: domain geometry/context coordinates;
- `applicability`: where/when/for whom an assertion applies;
- `record_role`: authoritative constraint, observed state, organizational rule, derived state, decision, action, reference knowledge or structural record;
- `actionability`: automation/human boundary, separate from measurement and separate from execution authority.

## Ownership

### EncyKlopedia

Owns acquisition evidence, provider/source resolution, immutable harvest handoff and referent candidates. Acquisition is not validation.

### Da’at

Owns mapping/ACL behavior at the boundary. It maps source facts and rules into the declared Kristal v6 semantics without inventing authority or silently converting high valuations into automatic actionability.

### Kristal

Owns the canonical Kristal State artifacts and their content-addressed semantics. It can preserve authoritative constraints, observations, organizational rules, derived states and actionability in one traceable model without becoming the mutable database or execution owner of the source applications.

### UCKK / consumers

Own projection/presentation state produced from pinned Kristal artifacts. Projections are rebuildable and do not become Kristal canon.

## Action projection rule

Actionability is deliberately **not** a direct actuator:

```text
Kristal assertion/action candidate
  actionability = automatic
        ↓
consumer/Da’at chooses the declared owner contract
        ↓
IK/profile admission + authority check
        ↓
owner-local operation
        ↓
receipt / observed state can return as new evidence
```

This allows the ecosystem to automate deterministic work while preserving human review/decision where the Kristal State says it is required. It also creates a feedback loop: completed actions and human decisions can be captured as new observed/decision records and improve later artifacts.

## Non-confusions

```text
acquisition evidence      ≠ validation
valuation                 ≠ action threshold
actionability             ≠ execution authority
automatic                 ≠ permission to bypass admission
record_role               ≠ ownership transfer
referent candidate        ≠ recognized referent
Kristal State             ≠ mutable application database
consumer projection       ≠ source of truth
IK transport              ≠ participant state
```

## Note de coexistence — interface EncyK v2 et hébergement Kristal v10 (2026-10-08)

The `Current contract set` above is the **frozen v6 knowledge projection** and its own historical EncyK handoff reference. EncyKlopedia 0.12.0 separately provides `encyk.source-evidence-handoff/2.0.0` to Médiathèque kOA. The latter interface targets `koa.source-catalog/2.0.0` and currently awaits a qualified receiving adapter; no drop-in compatibility with `encyklopedia.corpus-harvest-handoff/1.0.0` is asserted. The separate Kristal v10 GitHub read/sync/index path preserves v9 identity and requires independent qualification before public publication. See [C0](orchestration-c0/README.md).
