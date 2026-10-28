# Exploitation

Utiliser `python -m koa_audit local-plan --root "C:\mycode"` pour découvrir les dépôts, puis `python -m koa_audit local-audit --root "C:\mycode" --out reports` pour scanner localement. Les rapports sont générés sur votre disque. Pour un essai : `--limit 5`. Un outil automatisé ne peut pas évaluer vos copies locales depuis un runner GitHub Actions hébergé ; seuls les tests de code de cet outil sont exécutés dans son workflow CI.

La sortie peut inclure les chemins locaux ; garder les rapports privés. Les motifs détectés sont des observations heuristiques, pas des preuves de compromission, et le verdict `INSPECTED_NO_PATTERN_MATCH` ne démontre pas l'absence de vulnérabilités.

## Contre-vérification locale intégrée

Après un `local-audit`, utiliser l'onglet **Vérification + ZIP** du lanceur ou la commande `python -m koa_audit local-triage --root "C:\mycode" --audit-json reports/audit.json --out reports/triage.zip`. Le ZIP comporte seulement des métadonnées de diagnostic (références d'Actions, SHA, chemins et résultats de concordance des motifs), sans sources, secrets ou fichiers `.env`. Les copies Git ambigües y sont listées séparément. Réviser le ZIP avant de le partager : les chemins peuvent révéler la structure locale des projets.
