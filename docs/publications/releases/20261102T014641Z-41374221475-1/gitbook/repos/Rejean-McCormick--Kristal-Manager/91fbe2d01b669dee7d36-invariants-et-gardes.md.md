<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Manager/blob/a75b03c6799e1a8c1e7a5c794aa768210633d078/docs/00-vision/invariants-et-gardes.md | commit: a75b03c6799e1a8c1e7a5c794aa768210633d078 | SHA-256: 6308d1fa99abb434390091ff2f1da2dc9f54acc6479dac4ca8a282a3a6a8bd5e -->

# Invariants non négociables

| Référence | Garde | Comment vérifier |
|---|---|---|
| INV-01 | Lecture des sources par défaut | Aucune différence de hachage sous `locals/` après inventaire/diagnostic |
| INV-02 | Diagnostic indépendant | Le moteur ne charge pas de code ni de schéma non fiable du Kristal cible |
| INV-03 | Autorité explicite | `READY`, `PASS`, `proposed`, `C1`, `C2`, `C3` restent distincts |
| INV-04 | Preuve contextualisée | Outil, version, profil, cible, date, empreinte, chemin du rapport |
| INV-05 | Fraîcheur conservatrice | Source changée → ancien verdict `STALE_OR_UNVERIFIED` |
| INV-06 | Historique append-only logique | Un nouveau run n'écrase pas les anciens verdicts |
| INV-07 | Idempotence | Réimporter exactement un même rapport ne crée pas un doublon |
| INV-08 | Exécution explicite | Refresh/filtre/onglet n'exécute pas KristalDiag |
| INV-09 | Production hors des sources | SQLite, CSV, HTML, logs, preuves et cache en dehors de `locals/` |
| INV-10 | Aucune publication cachée | GitSink, push, activation, GitHub sur consentement et parcours séparés |
| INV-11 | Compatibilité contractuelle | Un artefact V11 n'est pas évalué comme V9 si le profil ne s'applique pas |
| INV-12 | Retour arrière | Copie, contrôle des hashes, migration versionnée et restore testé |

## Arbitrages

- **Confidentialité** : le catalogue global peut contenir du contenu riche. N'exporter que le périmètre nécessaire; préférer agrégats et références aux données brutes.
- **Performance** : un index accéléré peut être incomplet; la fraîcheur et la portée de l'index doivent rester visibles.
- **Ergonomie** : cacher un outil dans « Avancé » ne signifie jamais supprimer sa fonctionnalité.
- **Correction** : une valeur requise par un schéma n'est pas automatiquement vraie; un correctif doit reposer sur le comportement réel du Kit et des preuves.

Toute violation d'INV-01 à INV-10 est une **régression bloquante** pour la future refonte.
