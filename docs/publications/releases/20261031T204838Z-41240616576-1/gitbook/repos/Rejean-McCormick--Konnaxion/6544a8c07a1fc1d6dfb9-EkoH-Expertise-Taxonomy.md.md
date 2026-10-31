<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion/wiki/EkoH-Expertise-Taxonomy | commit: 62c3bb451bacb4cfbbeb68181c1edfc7ba47a8f9 | SHA-256: 0cae6a41a5ca506031f240210a2517f8c563828737031e51252af97377e36ca5 -->

# EkoH Expertise Taxonomy — ISCED-F 2013

EkoH uses **UNESCO ISCED-F 2013 / CITE-F 2013** as its external backbone for classifying expertise domains. ISCED-F is a classification of **fields of education and training**; EkoH reuses its field hierarchy as stable domain identifiers.

An ISCED-F code is **not** by itself a credential, an expertise score, a merit score or a voting weight.

## EkoH profile

The full ISCED-F 2013 classification has **11 broad fields**, **29 narrow fields** and about **80 detailed fields**. EkoH deliberately uses the expertise-bearing subset below:

| Level | EkoH profile | Code shape |
|---|---:|---|
| Broad | **10** (`01`–`10`) | 2 digits |
| Narrow | **26** substantive fields | 3 digits |
| Detailed | **77** substantive fields | 4 digits |
| **Total** | **113 categories** | — |

The default EkoH profile excludes `00` (*Generic programmes and qualifications*) plus field-unknown and special not-further-defined/interdisciplinary/not-elsewhere-classified coding buckets from expertise scoring.

## Hierarchy

```text
07  Engineering, manufacturing and construction
└── 071  Engineering and engineering trades
    └── 0714  Electronics and automation
```

In `ExpertiseCategory`, broad/narrow/detailed categories map to `depth = 0/1/2` and are connected by `parent` plus a PostgreSQL `ltree` path.

## Rules

- Official ISCED-F codes and labels remain unchanged.
- Any Konnaxion-specific finer-grained extension must be explicitly namespaced or mapped; it must not look like an official ISCED-F code.
- Expertise remains domain-bounded.
- Smart Vote may reference relevant EkoH categories, but there is no universal personal Smart Vote weight.
- Konnaxion is version-pinned to **ISCED-F 2013** until an explicit migration/crosswalk is approved.

## Implementation

```text
backend/konnaxion/ekoh/models/taxonomy.py
backend/konnaxion/ekoh/fixtures/isced_f_2013.json
backend/konnaxion/ekoh/management/commands/load_isced.py
```

Synchronization:

```text
python manage.py load_isced
```

The target profile invariant is **10 / 26 / 77 = 113 categories**.

## See also

- [[EkoH]]
- [[Smart Vote|Smart-Vote]]
- [[Implementation Alignment|Implementation-Alignment]]

External reference: UNESCO Institute for Statistics, ISCED-F 2013 and the current ISCED revision process.
