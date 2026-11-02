<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/05-design-system/05-localization.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 5bd846a601ae8c62b27b983df277a132f0da7be85fa8c85881618b921ece93c3 -->

# Localisation

**Classe : Normatif**

Locales locales initiales : `fr-CA` et `en`.

Priorité de résolution recommandée :

```text
label_key -> bundle locale module/Koali -> fallback default label
```

Les IDs restent non localisés. Les routes ne sont pas renommées par traduction.

Le code actuel possède déjà des bundles sous `public/localization/` mais ne résout pas encore systématiquement `label_key`; cette intégration est une priorité de développement.
