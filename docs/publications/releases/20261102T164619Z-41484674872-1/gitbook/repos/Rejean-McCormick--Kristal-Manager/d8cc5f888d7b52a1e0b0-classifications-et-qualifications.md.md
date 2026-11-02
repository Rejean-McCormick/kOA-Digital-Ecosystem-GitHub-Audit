<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Manager/blob/4056c084e6f705980a875f1b59ba6351a38390f7/docs/03-modele/classifications-et-qualifications.md | commit: 4056c084e6f705980a875f1b59ba6351a38390f7 | SHA-256: a0380dcd8fce7d89338b6ef95b724de6240cea672064e6297e9062a8b9afa536 -->

# Classifications ARK, PRF, UNESCO et preuves

## Modèle conceptuel

| Catégorie | Que décrit-elle ? | Qu'est-ce qui établit sa validité ? |
|---|---|---|
| ARK | Forme/structure Arketype | Preuves structurelles + validation appropriée |
| PRF | Usage dominant d'un Kristal | Analyse fonctionnelle du modèle natif, non simple correspondance domaine |
| UNESCO | Domaine/microthésaurus | Codes valides + adéquation sémantique contrôlée |
| Wikidata Q/P | Alignement externe d'identités/propriétés | Source/provenance, contrôle du référent, statut |
| Framework C1/C2/C3 | Qualification/autorisation selon contrats normatifs | Procédures officielles distinctes |

## Statuts de classification cibles

`UNOBSERVED`, `PROPOSED`, `REVIEWED`, `ACCEPTED`, `REJECTED`, `SUPERSEDED`. Un code correct mais non validé reste `PROPOSED`. `REVIEWED` atteste un examen, pas une acceptation. Les identifiants externes ne sont pas légitimés simplement parce que leur format est valide.

## Structure de décision cible

```json
{
  "target_state_ref": "urn:kristal:state:physics",
  "axis": "arketype",
  "code": "ARK-09",
  "status": "PROPOSED",
  "proposed_by": "arketype-scanner",
  "evidence_refs": ["report:..."],
  "notes": "Score structurel indicatif 2/3; sens non inspecté",
  "decision_id": null,
  "supersedes": null
}
```

## Faits actuels du corpus

Le scanner Arketype fourni retourne 127 résultats, dont 36 à candidats multiples et des scores structuraux limités à 3 critères. Le batch PRF antérieur contenait 96 attributions générales `PRF-20`, qui ne doivent **pas être gonflées en validations spécialisées**. Des mappings UNESCO proposés ont été ajoutés localement, sans certification.

## Règles produit

Une analyse peut suggérer; seule une action d'approbation traçable modifie une classification de référence. Les observations sont toujours conservées même si une décision ultérieure les rejette. Les informations de classement et les preuves peuvent évoluer sans réécrire des assertions KQ/KP.
