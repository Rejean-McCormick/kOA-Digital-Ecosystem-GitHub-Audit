<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/3-Layer-Model/klassification/CLASSIFICATION_VIEW.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: 9d3e7f39f1dbd052d6e7141e461ec5a6428b1b67cbbbdb5abbd74cab0360fc19 -->

# Klassification view — usage rules

**Status:** derived, optional, non-normative

## Minimal rule

Klassification may annotate an object; it must never become the object's authority.

```text
classification != ownership
classification != contract
classification != qualification
classification != activation
```

## Current layer dimension

Use the current `docs/3-Layer-Model/` definitions for layers `0–13`.

## Legacy dimensions retained for migration

The retired Klassification repository also used:

### Macro-zones

```text
A  Constitution interne
B  Mandat et sens
C  Épistémologie / canon
D  Orientation collective
E  Action / mémoire
F  Transmission / déploiement
X  Transversal
```

These are **legacy grouping labels**. The current Layer Model also defines its own higher-level groups; do not assume they are identical.

### Translation views

The archived code index records these view codes:

| Code | Legacy view |
|---|---|
| `N` | Native kOA |
| `T` | Technique |
| `G` | Gouvernance |
| `S` | Social / institutionnel |
| `P` | Pédagogique |
| `R` | Risque / audit |
| `M` | Mémoire / archives |
| `Y` | Symbolique / narratif |
| `E` | Externe / partenarial |
| `Q` | Séphirotique |
| `A` | Architecture externe |

These may be used as human-facing lenses. They do not alter the underlying object.

### Conceptual passages

The dedicated archived passage document defines `P0`–`P8`:

| Code | Legacy passage |
|---|---|
| `P0` | Séparation / cadrage |
| `P1` | Matière → sens |
| `P2` | Sens → proposition |
| `P3` | Proposition → résolution |
| `P4` | Résolution → canon |
| `P5` | Canon → choix |
| `P6` | Choix → travail gouverné |
| `P7` | Travail → action coordonnée |
| `P8` | Action → mémoire active |

The old code index separately lists a `P9`. Because that conflicts with the dedicated passage document, `P9` is not part of the consolidated live view unless a future explicit decision adopts it.

## Legacy coordinate syntax

For migration and archival references only, the former syntax was:

```text
K-[Zone][Layer].[Function]-[View]-P[Passage]-[Object]
```

Existing legacy coordinates may be preserved in historical metadata. New technical identifiers should use the identifier/versioning scheme owned by the relevant system or contract.

## Example of correct coexistence

```text
technical identity / owner / contract
    comes from the authoritative product, platform or integration source

classification metadata
    may optionally attach layer/view/passage labels for navigation
```

The classification label is therefore an index over the architecture, not the architecture itself.
