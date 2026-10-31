<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/08-reference/annexe-a-registre-locks.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: c4c6e12d2d57ad40fecef928969cecad486afd594ebd28dd841400d906cc03bf -->

# Annexe A — Registre des locks

La v1.1 contient exactement :

```text
LOCK-KS-SURF-001 ... LOCK-KS-SURF-154
```

Les déclarations Markdown sont la source normative.

Projection machine-readable :

```text
locks/koali-surface-layer.lock.json
```

Le registre contient pour chaque lock :

```text
id
rule
lock_class
tier
source_document
source_line
statement_sha256
change_requires_adr
```

Ne pas maintenir une liste parallèle manuelle dans cette annexe.

Validation :

```text
node tools/validate-surface-spec.mjs
```
