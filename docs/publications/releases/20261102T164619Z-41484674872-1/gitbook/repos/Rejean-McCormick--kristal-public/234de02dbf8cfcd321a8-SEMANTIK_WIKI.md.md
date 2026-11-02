<!-- Frozen source: https://github.com/Rejean-McCormick/kristal-public/blob/88d3e2035d1eedc9234d5c7c2c4bc6694a07311a/docs/SEMANTIK_WIKI.md | commit: 88d3e2035d1eedc9234d5c7c2c4bc6694a07311a | SHA-256: e59258e8e55cd2ad11aff7bbfb9f151bd395c6e576673da8fcdde9acb673896e -->

# Wiki Kristal : articulation via SemantiK Architect

## Règle d'architecture

Ce Wiki est **une projection de publication**, pas une base de connaissance autonome.

- `locals/` : autorité sémantique et sources canoniques (jamais de lien symbolique dans le repo public).
- Kristal-Manager : sélection explicite, préparation privée, contrôle C3 et publication C1/C2.
- SemantiK Architect : articulation *fidèle* des seules assertions sélectionnées par l'amont, sous un profil linguistique et RuntimeSet réellement `RELEASED`.
- `tools/wiki_export.py` : structure Markdown, navigation, liens immuables vers les surfaces publiques et preuve de génération ; **aucune formulation de faits par templates**.
- `kristal-public.wiki.git` : hébergement GitHub Wiki distinct, après activation dans les réglages GitHub et contrôle indépendant de publication. Ce patch ne le pousse jamais.

Référence SA : `semantik.kristal-v6.communication-projection/1.0` et `CommunicationRequest/1.0`. Ce contrat consomme une projection v6 explicite ; il ne se branche **pas directement** sur un index v9/C3. Un adaptateur/projection sémantique amont est donc nécessaire pour chaque page et reste responsable de la sélection des faits.

## Préconditions

1. Le commit contenant les surfaces publiques a été confirmé sur GitHub par le Manager, avec qualification C1 et autorisation C2.
2. Chaque Kristal destiné au Wiki a une projection de communication **privée**, revue et rattachée à l'état logique exact, à la surface C3 et au SHA publié.
3. `C:\mycode\Kristal\SemantiK-Architect` possède le SDK Python installable et un RuntimeSet de langue/profil **réellement qualifié**. Le dépôt GitHub SA seul ne garantit pas la présence d'un `.pgf` de production : ne pas confondre le profil de démonstration et un runtime qualifié pour les sujets publiés.
4. Tous les blocs ont une provenance (`source_refs`) et toutes les obligations sont couvertes.

## Format privé des projections

Dans un dossier hors Git, par exemple `%LOCALAPPDATA%\Kristal\private-candidates\wiki-semantic-projections\`, créer **un fichier `<slug>.json` par Kristal**. Ne jamais placer ce dossier dans `kristal-public`.

```json
{
  "format": "kristal.semantik-wiki-page/1.0",
  "binding": {
    "slug": "kristal-ai",
    "state_ref": "<state_ref EXACT de kristals/index.json>",
    "state_logical_commitment": "sha256:<digest EXACT de l'index>",
    "surface_digest": "sha256:<digest EXACT de l'index>",
    "published_revision": "<SHA git 40 hex EXACT>"
  },
  "language": "fr",
  "locale": "fr-CA",
  "capability_profile": "<profil réellement RELEASED pour ce domaine>",
  "projection": {
    "contract": "semantik.kristal-v6.communication-projection/1.0",
    "kristal_standard": "6.0.0",
    "state_ref": {"state_id":"<identifiant état portable v6>","artifact_type":"kristal_state","schema_version":"6.0"},
    "selected_assertions": [{"assertion_id":"<ID assertion autorisée>"}],
    "communication_request": {
      "schema_version": "1.0",
      "request_id": "<ID stable>",
      "semantic_graph": {"graph_id":"<ID>","nodes":[],"statements":[]},
      "obligations": [],
      "supporting_context": [],
      "context": {"target_language":"fr","target_locale":"fr-CA","channel":"offline-build"},
      "constraints": {"allowed_block_kinds":["utterance"],"opening_policy":"forbidden","closing_policy":"forbidden","list_policy":"forbidden","output_format":"structured"},
      "capability_profile": "<même profil RELEASED>",
      "runtime_selector": {"runtime_set_id":"<RuntimeSet qualifié exact>"}
    }
  }
}
```

Les champs entre chevrons et les tableaux vides sont des **placeholders non exécutables**. L'amont doit les remplir à partir d'assertions réellement sélectionnées ; l'outil rejette les obligations absentes et les assertions non traçables. Ne pas inventer un profil ou un runtime pour satisfaire le schéma.

## Export local

```powershell
python C:\mycode\Kristal\kristal-public\tools\wiki_export.py `
  --collection C:\mycode\Kristal\kristal-public `
  --repository Rejean-McCormick/kristal-public `
  --revision <SHA_COMPLET_DU_COMMIT_PUBLIE> `
  --projections "$env:LOCALAPPDATA\Kristal\private-candidates\wiki-semantic-projections" `
  --semantik-root C:\mycode\Kristal\SemantiK-Architect `
  --runtime-root C:\mycode\Kristal\SemantiK-Architect\runtime `
  --output "$env:LOCALAPPDATA\Kristal\private-candidates\wiki-projet-001" `
  --write
```

Cette commande crée un **candidat privé**, avec `Home.md`, `_Sidebar.md`, une page par Kristal et `SEMANTIK_EVIDENCE.json` (IDs de résultats, digests et RuntimeSets). Elle ne publie rien sur Internet. L'export échoue en l'absence d'un profil réellement réalisable par SA, d'une projection explicite, d'une preuve de couverture ou d'une correspondance exacte de révision.

La publication du Wiki natif nécessite une autorisation de diffusion *supplémentaire* portant sur les pages réellement générées, puis une synchronisation du dépôt Wiki. Elle ne fait pas partie de cet adaptateur.

## Limitations du moteur SemantiK

La documentation normative SA exclut la sélection automatique de faits, la génération de chapitres éditoriaux longs et l'interprétation des fichiers JSON bruts. Le présent raccordement produit des **communications bornées** dans une page Wiki ; la structure des articles/sections demeure la responsabilité du générateur et du propriétaire sémantique amont. Il ne faut pas promettre une encyclopédie entièrement rédigée à partir des index C3 tant que ces projections et profils linguistiques ne sont pas construits et qualifiés.
