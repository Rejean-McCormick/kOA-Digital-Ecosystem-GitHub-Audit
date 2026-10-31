<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/11-integrations/09-linked-snapshot-components.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 4f78d14cc5942afc48480e03b65af2ca51fa435b16effdfd8f251081c3179d05 -->

# Composants intégrés du snapshot

**Classe : Boundary d'intégration**

Koali intègre les composants fournis par **contrats propriétaires, supervision locale et qualification explicite**, sans copier leur état métier ni transférer leur autorité interne au shell.

## Exclusions

Les composants de diagnostic autonomes (`LevelUpDiag-*`, `KorDiag` et autres produits `*Diag*`) ne sont pas onboardés. Le **Kristal Framework** est `reference_only` : ses diagrammes et sa théorie ne sont pas importés dans Koali et sa présence n'est pas une condition de bootstrap.

## Topologie retenue

| Composant | Rôle Koali | Mode final |
|---|---|---|
| Orgo | application propriétaire principale | surface web supervisée + API/worker + PGlite local |
| Orgo Worlds | application propriétaire complémentaire | surface web supervisée + API, lancée en parallèle d'Orgo |
| SemantiK Architect | capacité sémantique | service headless supervisé |
| Konfid | plan de contrôle sécurité | API + worker headless supervisés |
| Kor | boundary humain/mobile | service headless supervisé; UI Android conservée propriétaire |
| Interaction Kernel | protocole d'interopérabilité | runtime Python + runtime TypeScript + adaptateur Orgo qualifiés |
| SemantiK Runtime Orchestrator | release/activation de RuntimeSets | CLI qualifié, pas de faux serveur |
| kOA-Linux | autorité plateforme | CLI qualifié |
| kOA Digital Ecosystem | carte système / inventaire | source opérationnelle qualifiée |
| Koali Control Panel | orchestration de développement | self-test qualifié |
| Kristal Framework | référence | référence seulement, non requise |

## Readiness

Le profil complet est fail-closed. Tous les produits et sources opérationnels fournis sont `requiredForBootstrap`. Le shell ne démarre qu'après qualification des sources et readiness de toutes les applications/services supervisés. Kristal est explicitement exclu de cette condition.

## Invariants

- Une source sans UI officielle n'est pas transformée artificiellement en module browser.
- Orgo et Orgo Worlds sont deux surfaces distinctes; Worlds ne remplace plus Orgo.
- Kor se lie à Orgo local au démarrage via le profil IK épinglé par Kor.
- Interaction Kernel conserve son autorité de protocole et ses locks propres.
- Les chemins locaux, tokens et commandes de processus ne sont pas projetés vers le navigateur.
- Les composants diagnostiques ne deviennent pas des produits Koali.
- La théorie Kristal ne devient ni logique métier, ni modèle d'autorité, ni dépendance de démarrage de Koali.
