<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/07-verification/42-spec-validation.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: c73394b7a6fbe3ed3c4f3c21c20429877bbe5e427522316d886e36d5d0bbb730 -->

# 42. Validation de la spécification

La documentation de Surface Layer est elle-même un artifact à qualifier.

Commande :

```text
node tools/validate-surface-spec.mjs
```

Le validateur vérifie au minimum :

```text
JSON parse
LOCK IDs uniques
LOCK range contigu
Markdown lock source == generated lock registry
statement hashes
OPEN decision set
source pins uniqueness
DOC_INDEX coverage
required schemas present
required core documents present
```

`LOCK-KS-SURF-152` — **Dès que la v1.1 est intégrée au repository, `validate:surface-spec` doit faire partie de `QUALIFY ALL` et bloquer une baseline lorsque les locks, sources, index ou hashes divergent.**
