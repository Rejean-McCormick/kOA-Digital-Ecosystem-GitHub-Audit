# Exploitation

Utiliser `python -m koa_audit local-plan --root "C:\mycode"` pour découvrir les dépôts, puis `python -m koa_audit local-audit --root "C:\mycode" --out reports` pour scanner localement. Les rapports sont générés sur votre disque. Pour un essai : `--limit 5`. Un outil automatisé ne peut pas évaluer vos copies locales depuis un runner GitHub Actions hébergé ; seuls les tests de code de cet outil sont exécutés dans son workflow CI.

La sortie peut inclure les chemins locaux ; garder les rapports privés. Les motifs détectés sont des observations heuristiques, pas des preuves de compromission, et le verdict `INSPECTED_NO_PATTERN_MATCH` ne démontre pas l'absence de vulnérabilités.
