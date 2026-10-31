<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Manager-and-Discovery | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: 71b2955c96d8ce02ee4838a69200443a37e6778e8ee6174981fd32ac74a22fbb -->

# Kristal Manager and Reader Discovery

## Why Manager and Konstellation are separate

**Manager** observes the Kristal fleet: presence, structure, inventory, Discovery metadata, and—on request—state commitments verified by the Framework reference tool. **Konstellation** consumes only authorized information and verifies the files it opens. Manager does not render the graph; Konstellation neither publishes nor qualifies the canon.

## Chain of checks

```text
Authoring Kit → builds artifacts / regenerates Discovery
Framework    → defines schemas and verifies commitments
Manager      → produces a local operational assessment
Operator     → defines exposure/read permissions
Konstellation→ shows filtered diagnosis and opens through its reader
```

## Interpreting statuses

| Status | What it establishes |
| --- | --- |
| `LOCAL_STRUCTURE_ONLY` | Local structure exists; full integrity has not been established |
| `ATTENTION_REQUIRED` | An operational issue or metadata requiring a refresh needs attention |
| `LOCAL_CHECKS_PASSED` | The local checks **actually performed** did not fail |
| `BLOCKED` | Policy or local checks blocked the operation |
| `stale` (Discovery) | Derived inventory no longer matches recorded files |
| `consistent_unverified` (Discovery) | Declarations agree, **but files were not verified** |
| `VERIFIED` (Framework state) | Referenced state check is reported as successful, within the scope that must be examined |

None of these statuses alone establishes C1/C2/C3, publication, activation, or access rights. A status can be missing, unevaluated, or outdated.

## Optional Manager export integration

The `My Kristals` prototype can consume a local Manager export under a **separate private access policy**. The server filters authorized entries first; the interface must not expose hidden objects' paths, internal errors, private fingerprints, or statistics.

Illustrative example from Manager alpha.14:

```powershell
python -m kristal_manager export C:\mycode\Kristal\locals --verify-sources --output C:\private\manager-inventory.json
```

The operator must create the access policy based on `examples/fleet/manager-access-policy.example.json`, using exact identities. **Do not use the synthetic example unchanged.** See `docs/32-manager-discovery-3.3.md` and `docs/33-kristal-v10-local-reader.md` for full configuration. Do not enable the Manager export if your only goal is the neutral selector: it works independently.

## Fixing a `stale` inventory

Regeneration belongs to the **Authoring Kit**, not Manager or Konstellation. Run `build-discovery` again, validate recorded files, and recheck with Manager/Framework. An outdated inventory does not automatically invalidate the canon's State Commitment.

See [[Security|Security-and-Privacy]] and [[Contracts and Versions|Contracts-and-Versions]].
