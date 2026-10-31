# kOA Graph — Publications datées / Frozen documentation releases

## Ce que ça fait / What it does

Le site GitHub Pages ne s'actualise plus directement lors de chaque `push` dans les dépôts. La publication est **manuelle et datée**, déclenchée par `Actions → kOA Graph - publication datee FR EN → Run workflow`. Aucune création de dépôt GitHub supplémentaire n'est requise.

The public site no longer redeploys automatically on regular repository pushes. Publishing is **manual, dated, and gated**. No third GitHub repository is required.

1. **Prévisualiser / Preview** — mode `selected` ou `all`, `preview_only=true`. Produit un artefact téléchargable (`koa-graph-publication-candidate`) pendant 30 jours, sans modifier GitHub Pages ni le dépôt.
2. **Publier / Publish** — même choix, `preview_only=false`, depuis `main`. Le job `publish` est soumis aux règles de protection de l'environnement `github-pages`, s'il y en a. Après approbation, le job commit la version datée et l'envoie à GitHub Pages. **Important :** une exécution séparée de prévisualisation peut différer d'une publication ultérieure si les sources ont évolué. Pour approuver **exactement** la version à publier, télécharger l'artefact candidat **dans l'exécution de publication en attente d'approbation**, puis approuver cette même exécution.
3. **Revenir en arrière / Rollback** — mode `rollback` et identifiant d'une publication antérieure, `preview_only=false`. Le contenu publié redevient cette version, sans toucher à son historique.

### Tous les dépôts / All

`mode=all` collecte tous les dépôts de la liste publique `data/initial_inventory.json` et les ajouts explicitement approuvés dans `config/publication_repositories.json` (actuellement Kolor et Karacter). Les noms de dossiers locaux ne deviennent **jamais** des URL GitHub présumées.

### Sélection / Selected

`mode=selected` avec `repositories=Kolor,Karacter` collecte seulement ces deux dépôts. Les copies datées des autres dépôts **restent identiques**, même si leur branche `main` a évolué ou ne construit plus. Un dépôt sélectionné inaccessible conserve sa dernière copie disponible; si aucune sélection n'a pu être collectée, **la publication est refusée**.

### Ce qui est figé / What's frozen

- Les README, fichiers textuels de `docs/`, `doc/`, `documentation/`, `wiki/`, et pages du GitHub Wiki (`*.wiki.git`) lorsqu'ils sont publiquement accessibles.
- Identifiant de publication, date UTC, commit SHA du dépôt, commit du wiki s'il existe, SHA-256 de chaque copie et liens vers les sources.
- `docs/publications/releases/<version>/` conserve l'historique en Git et expose les anciennes versions publiées. `docs/publications/index.html` affiche la version publique actuelle; `docs/data/publication-current.json` contient son pointeur.
- Les pages publiées montrent une **copie HTML échappée et sûre** des fichiers texte. Les liens GitHub originaux restent accessibles à titre de référence, mais la lecture de l'archive ne dépend plus de leur état actuel.
- `releases/<version>/gitbook/` contient une sortie Markdown (`README.md`, `SUMMARY.md`, pages) destinée à un éventuel Git Sync **sur une branche dédiée aux versions approuvées**, et non sur `main` d'une application. **Aucun envoi automatique vers GitBook n'est configuré**.

Ces copies sont des **documents**, pas des tests validés ni des preuves de production. Les rapports privés, décisions de conformité, dossiers locaux et secrets ne sont pas copiés. Chaque collecte est bornée (nombre et taille de fichiers). Si un dépôt n'a ni README ni docs ni wiki dans les chemins admis, il est marqué indisponible, pas certifié absent.

## Configuration GitHub — une fois

1. `Settings → Pages → Source : GitHub Actions`.
2. `Settings → Environments → github-pages` : configurer si possible les **required reviewers** pour approuver chaque publication; limiter les branches de déploiement à `main`. La disponibilité des protections d'environnement dépend du plan GitHub et de la visibilité du dépôt.
3. `Settings → Actions → General → Workflow permissions` : permettre au `GITHUB_TOKEN` du workflow d'écrire dans le dépôt pour archiver les snapshots (`contents: write`). Si des règles de protection de `main` bloquent `github-actions[bot]`, adapter la stratégie d'écriture ou utiliser une branche de publication avec les permissions adéquates. **Ne pas supprimer les protections sans examen.**
4. Démarrer avec `mode=selected`, `repositories=Kolor,Karacter`, `preview_only=true`, inspecter l'artefact. Ensuite démarrer une exécution `preview_only=false` et, si les règles d'environnement sont actives, vérifier **l'artefact candidat de cette exécution précise** avant d'approuver la publication.

GitHub Pages publie uniquement la sortie de `deploy-pages` du workflow manuel. Le précédent déclencheur automatique `push` est supprimé; les pushes de code ou de docs seuls ne modifient pas le site en ligne. `dashboard-sync` peut continuer à préparer des données, mais la publication n'a lieu qu'à la prochaine action approuvée.

## GitBook ?

GitBook offre Git Sync avec une branche GitHub; Git Sync est bidirectionnel. Le brancher directement sur un dépôt applicatif **réintroduirait une synchronisation du travail en cours**. On peut ultérieurement synchroniser une branche stable dédiée aux exports `gitbook/` de versions approuvées, ou préférer GitHub Pages, déjà présent et plus simple pour le graphe HTML. [Documentation GitBook Git Sync](https://gitbook.com/docs/guides/editing-and-publishing-documentation/import-or-migrate-your-content-to-gitbook-with-git-sync).

### Limites / Limits

- Les dépôts doivent être publics et explicitement autorisés. Le workflow n'a **pas** vocation à cloner des dépôts privés.
- La collecte nécessite Git et l'accès réseau dans GitHub Actions; le test local injecte des captures fictives et n'atteste pas la réussite des clones à distance.
- Les versions sont conservées dans le dépôt; leur taille cumulée doit être surveillée.
- Les versions antérieures survivent aux nouvelles publications **tant qu'elles ne sont pas supprimées du Git**. Les protections de branche et revues sont recommandées.
- Chaque publication reprend aussi le code et les JSON du site présents dans `docs/` à l'instant du workflow; les dépôts applicatifs ne sont jamais modifiés.

## Graphe architecturé / Source-owned public graph (v1)

La description architecturale de kOA Graph provient de `kOA-Digital-Ecosystem/docs/inventory/graph-registry.v1.json`. Le collecteur ne la lit que lors d'une **publication explicite** incluant le dépôt `kOA-Digital-Ecosystem`. Les deux sources `graph-registry.v1.json` et `repositories.json` sont extraites du **même commit Git**. Le modèle public figé se trouve dans `docs/data/graph-public.json` et dans l'archive de cette version.

- **49 dépôts de référence** : statut d'inventaire conservé, sans en déduire une qualification technique.
- **Kolor et Karacter** : dépôts supplémentaires connus, mais `discovered_not_admitted` tant que leur rôle n'est pas formellement établi.
- **12 systèmes / 7 passages** : rôles et liens du modèle documentaire déjà connus; les relations ne sont pas des intégrations qualifiées.
- `mode=selected` sans le dépôt architectural conserve le dernier graphe public approuvé.
- `mode=republish` change uniquement la présentation, sans nouvelle collecte.
- Le portail Pages affiche les applications et les documents de la version figée. L'outil Windows conserve seul les preuves et décisions privées.

**Note :** le manifeste de documentation et le graphe public sont des sorties distinctes de la même publication. Pour mettre à jour une responsabilité architecturale, réviser d'abord le dépôt `kOA-Digital-Ecosystem`, puis publier dans GitHub Audit.
