<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/blob/9d4f7e74ed87b5a4c8d284dad891029d834911e4/docs/guides/INTEGRATOR.md | commit: 9d4f7e74ed87b5a4c8d284dad891029d834911e4 | SHA-256: 8ccd44d29144919a78700c4e9b6df3574cb4f14141cbbcb2d6fcd08e775fd74f -->

# Guide intégrateur Kristal

## Chemin recommandé

1. publier un Kristal v6 valide ;
2. vérifier son identité ;
3. fournir une Reader Policy ;
4. tester l'import dans Konstellation ;
5. ajouter une Lens seulement si nécessaire ;
6. ajouter des navigationHints seulement pour clarifier la structure ;
7. créer des golden tests.

## Hints

Préférer :

```json
{
  "schemaVersion": "0.1",
  "affordances": {"temporal": 1},
  "relationAffordances": {"precedes": ["temporal", "sequence"]}
}
```

Ne fournissez jamais de code UI.

## Critère de réussite

Un nouveau Kristal doit être utile en mode générique avant toute personnalisation : recherche, facettes, liste/tableau/Constellation et inspecteur.
