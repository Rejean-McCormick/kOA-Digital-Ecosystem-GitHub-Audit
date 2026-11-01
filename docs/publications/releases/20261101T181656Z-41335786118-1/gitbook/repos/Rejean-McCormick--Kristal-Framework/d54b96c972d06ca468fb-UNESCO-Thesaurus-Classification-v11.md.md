<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/UNESCO-Thesaurus-Classification-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 66be614413379b773b7beefdf4723133d9481db06c1e5ec931a4130809a25fa0 -->

# Classification thématique — Thésaurus UNESCO (profil compagnon v11)

**Statut : politique d’intégration du Kristal-Manager et du générateur d’icônes, non-normative pour les contrats v6 à v11.** Le Framework v7 a déjà épinglé le **Thésaurus UNESCO** comme premier `reference_spine` pour la navigation par sujets. La référence conservée contient **7 domaines et 88 microthésaurus**. Il ne faut pas interpréter cette page comme une nouvelle version du Framework ou comme une certification des contenus par l’UNESCO.

## Une classification de sujet, pas deux

| Dimension | Référence | Fonction |
| --- | --- | --- |
| **Sujet / domaine / navigation** | **UNESCO Thesaurus** | Une seule source de classement thématique actif pour Manager et Icon Generator |
| **Structure et usage** | **Arketype** (`ARK-*`, `PRF-*`) | Typologie du Kristal, indépendante de son sujet |
| **Identité sémantique** | `KQ`, `KP`, `KA`, `KS`, `state_ref` | Identifiants internes qui ne changent jamais à cause d’une classification externe |

Les codes **ISCED-F 2013** ne sont **plus une classification active**, ni une source des icônes. Ils peuvent subsister dans les documents historiques pour traçabilité, mais **aucune conversion automatique** `ISCED-F → Thésaurus UNESCO` n'est autorisée. Le Framework peut toujours représenter d’autres références KOS comme correspondances externes explicites, sans en faire des domaines actifs dans ces outils.

## Écrire la correspondance

Dans le `kristal.workspace.json`, on place les annotations explicites sous `classification.unesco_thesaurus` ; c’est une métadonnée de classification **non canonique** :

```json
{
  "classification": {
    "primary_archetype": "ARK-04",
    "unesco_thesaurus": {
      "kos_id": "kos:unesco-thesaurus",
      "domains": ["3"],
      "microthesauri": ["3.20"],
      "mapping_status": "reviewed",
      "mapping_provenance": "manual-local-review"
    }
  }
}
```

Ceci est un **fragment illustratif**, pas un workspace complet. Les notations UNESCO (comme `3`, `3.20`) doivent correspondre au profil épinglé, et chaque microthésaurus doit dépendre du domaine déclaré. Les vrais URI UNESCO, lorsqu’ils sont disponibles, sont à conserver. `reviewed` signifie **revu localement**, pas vérité certifiée ; `candidate` signifie **à revoir**, donc pas d’application automatique sur cette base. Une absence de classification reste `unmapped` : le nom du dossier, un ancien profil d’icône ou un code ISCED-F ne sont pas des preuves de correspondance.

## Icônes et dossiers Windows

`UT1` … `UT7` sont des **jetons de présentation propres au générateur d’icônes**, pas des codes ni des URI UNESCO. La génération utilise les domaines UNESCO explicitement déclarés et cohérents ; les microthésaurus donnent la granularité sémantique supplémentaire. Le Framework ne modifie **jamais** les icônes Windows. Dans Kristal-Manager, la personnalisation des icônes des dossiers sous `locals` est une action distincte, **désactivée par défaut**, exigeant une activation et une confirmation ; un scan ou un aperçu ne doit créer ni `.ico` ni `desktop.ini`.

## Validation, autorité, migration

- Référence : `spec/v7/UNESCO-Thesaurus-Alignment.md`, `spec/v7/reference-kos/unesco-thesaurus-profile.json` et baseline 7/88.
- Profil compagnon : `profiles/unesco/README.md` et `profiles/unesco/kristal-unesco-classification.schema.json`.
- Inspection facultative, en lecture seule : `python tools/v11/check_unesco_classification.py path/to/kristal.workspace.json --json`.
- Les engagements, la version des schémas/TCK historiques, les identités internes et les sources canoniques ne changent pas.
- Le **domaine 7** (« Countries and country groupings ») reste une facette géographique dans la navigation TOC par défaut, conformément à la référence v7.

Voir [[Reader-Discovery-and-Arketype-v10]], [[Semantic-Identity-v11]], [[Ecosystem-Integration]] et [[Version-Stack-v6-v7-v8-v9-v10-v11]].
