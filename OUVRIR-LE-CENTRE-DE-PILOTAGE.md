# Ouvrir le centre de pilotage kOA

1. **Décompresse** complètement le ZIP et double-clique sur `kOA_GitHub_Audit_Launcher.pyw`.
2. Dans **Pilotage**, clique sur **Ouvrir les validations et les fiches d’applications**.
3. Le navigateur s’ouvre sur **Validations** : les dossiers ayant des jalons étayés sont présentés en premier, sans classement de qualité. Choisis une application, puis **Tests**, **Sécurité**, **Architecture**, **Implémentation**, **Intégration** ou **Production**.
4. Clique sur une source vérifiée pour consulter sa portée, sa date et la pièce d’origine.
5. Va dans **Applications** pour les Engineering Profiles et la carte Kristal (sous-vue **Voir la carte**). Ouvre **Campagnes** pour comparer l’état du registre et les captures figées.

La fenêtre Windows comporte quatre espaces : **Pilotage**, **Dossiers des systèmes** (Registre des 49, Preuves et sources, Qualification et profils), **Campagnes datées**, **Outils avancés** (sources, publication, audit local, GitHub, historiques).

**Rien à scanner ou publier pour consulter les dossiers existants.** Les profils mesurés disponibles dans l'archive sont déjà intégrés. Les tests CI historiques ne prouvent pas une certification globale. L'absence de coche verte n'est pas un échec.

Les campagnes privées et les registres restent dans `%LOCALAPPDATA%\kOA-GitHub-Audit` et ne sont pas publiés sur GitHub Pages. Pour configurer la source Kristal locale ou publier explicitement la page publique : **Outils avancés → Sources et publication**. Si le lanceur ne s’ouvre pas, exécute `DIAGNOSTIC_LAUNCHER.cmd`.

## Mesurer et figer des preuves — v0.11.0

Dans **Campagnes datées**, sélectionne ton ancien `audit.json` ou le dossier d'un clone Git précis. Clique sur **Mesurer clones de l'audit** ou **Mesurer ce clone**. Par défaut, seul Git est lu (aucun test ni scan complet). L'option `scc/Lizard/Universal Ctags` est facultative. Les rapports privés sont joints à la prochaine campagne, puis consultables dans ton navigateur via **campagne → dépôt → preuve**. Utilise **Comparer à la campagne précédente** pour consulter les graphiques de progression documentaire.

## Barres de progression sans fenêtres qui clignotent — v0.11.1

- Ouvre l'onglet **Campagnes datées** : une barre fixe indique les dépôts mesurés (`3/49 · 6 %`, par exemple).
- Pendant **Créer une campagne figée**, la barre avance lors de la capture des fiches puis aux étapes d'archivage, vérification SHA-256 et publication locale.
- Aucune fenêtre de console Git, `scc`, Lizard ou Ctags ne doit s'ouvrir puis disparaître pendant ces opérations sur Windows. Les outils facultatifs nécessitent toujours ton accord.
- Pour les opérations qui ne donnent pas de décompte fiable, la barre n'invente pas de pourcentage et reste stable jusqu'au résultat.
- Les confirmations demandées par l'application ou un gestionnaire d'identifiants Git restent possibles : ce ne sont pas des fenêtres de console.

## Découvrir les preuves et voir la progression — v0.12.0

1. Dans **Campagnes datées**, choisis le clone local d’une application ou un ancien `audit.json` avec les chemins des clones.
2. Clique sur **Trouver rapports de ce clone** ou **Trouver rapports des clones de l’audit**. La barre de progression indique les dépôts examinés.
3. Examine les noms trouvés, puis **confirme** si tu veux joindre ces rapports JUnit, couverture ou SARIF à la prochaine campagne. Aucun test n’est exécuté.
4. Crée ta **campagne figée** : si un document a changé après la découverte, relance la découverte pour le revoir.
5. Ouvre le dashboard **Écosystème** : la section privée des campagnes affiche les profils, les rapports et les cinq jalons à cette date. Clique **Fiche figée · dernière campagne** depuis une application, ou **Comparer les deux dernières campagnes**.

Cette fonction utilise exclusivement l’aperçu **local**. Elle n’envoie pas les pièces sur GitHub; un rapport importé ne prouve pas à lui seul sa concordance avec le commit Git.

## Revue des 245 dossiers (v0.13.0)

Dans l'onglet **Revue des 245**, sélectionne un des 49 dépôts, puis un des cinq jalons. Double-clique une source disponible pour lire le document original dans le navigateur local. Clique sur **Préparer une qualification à examiner** pour remplir le formulaire **Certification & profils** sans attribuer de verdict automatiquement. Après lecture et validation de la portée, enregistre manuellement ton statut et crée une nouvelle campagne datée. Les campagnes anciennes restent inchangées. La bibliothèque historique se trouve dans `private_evidence/` et n'est jamais publiée sur GitHub.

## Qualification documentaire v0.14.0

Au premier démarrage, l'application inscrit la revue fondée sur les sources du 30 octobre 2026 : **10 jalons étayés pour des périmètres restreints** et **235 à documenter**, à condition qu'aucune décision ne soit déjà enregistrée pour ces jalons. Les anciennes décisions sont conservées.

Dans **Preuves 245**, choisis une application et son jalon pour consulter la décision, la portée, les limites et le **document primaire original**. Les 10 cas étayés ne constituent ni 10 tests indépendants, ni une preuve de production, ni une attestation du SHA Git des clones.

Une campagne déjà créée ne sera jamais modifiée. Après ouverture de cette version, crée une **nouvelle campagne datée** pour conserver le nouvel état.

## Compteur de qualification et campagnes figées — v0.14.1

Le chiffre principal du dashboard local mesure **uniquement les jalons « Étayé par preuve »** sur les 245 possibles. Il n'inclut pas les dossiers « À documenter », bien que ces derniers aient été examinés. Par exemple, si le registre local contient les décisions de la revue du 30 octobre, il indique **10/245 étayés, 235 à documenter, 245/245 dossiers examinés**. Ce n'est pas 10 applications globalement certifiées : les 10 preuves portent sur des périmètres historiques limités.

La section **Campagne figée** montre l'état immuable de la campagne à sa date, indépendamment du **registre actuel**. Une ancienne campagne peut donc rester à **0/245** alors que le registre actuel indique **10/245**; pour conserver le nouvel état, il faut créer une nouvelle campagne datée. Les campagnes existantes ne sont jamais modifiées par l'affichage.

## v0.15.0 · Premier écran : Validations

La première section du navigateur présente les 49 applications et leurs catégories :
**Tests, Sécurité, Architecture, Implémentation, Intégration, Production et Composants Kristal**.
Cliquer une application, puis un domaine, pour consulter les contrôles et ouvrir les preuves quand elles sont réellement dans l'archive.
Le symbole vert est toujours limité à une pièce ou à un résultat CI historique précisément identifié.
La sécurité ne reçoit aucune validation implicite à partir de noms ou de profils.
La carte et les Engineering Profiles se trouvent dans l’espace distinct « Applications ».

Pour disposer de plus de validations vérifiables, utiliser l'onglet **Campagnes datées** pour importer les sorties JUnit, couverture et SARIF déjà disponibles; leur date et leur SHA doivent correspondre au périmètre revendiqué.

## v0.16.0 · Refonte selon le guide d’architecture d’interfaces IA v2

Les trois espaces du navigateur sont **Validations**, **Applications** et **Campagnes**. Le parcours dominant reste au même endroit : application → catégorie → source → portée. Les autres informations ne sont pas empilées sur la page d’accueil. Les 86 critères d’architecture et de sécurité se déplient seulement à la demande. Dans Windows, les outils rares passent sous « Outils avancés » sans perdre leurs fonctionnalités. Voir `docs/UX_REFACTOR_GUIDE_V2.md` pour la correspondance des anciens onglets et les scénarios de validation.


## v0.17.0 · Fonctionnalités et fiche technique par système

À l'ouverture du dashboard local, sélectionne une application dans **Validations** :

1. **Fonctionnalités** : actions concrètes et composants, avec l’état « code observé » ou « scénario spécifié ».
2. **Technologies** : Python, FastAPI, Django, API, PostgreSQL, authentification, etc., selon les fichiers réellement observés.
3. **Tests** : journaux JUnit cliquables des tests ciblés exécutés sur copies de snapshots (3/3 KonnaxionDiag, 42/42 Security Gate Capsule Manager).
4. **Sécurité** : ces résultats restent distincts des 53 critères du référentiel. Aucun des 53 n’est déclaré automatiquement validé.

Choisis le filtre « **Avec fiche technique issue d’un snapshot** » pour voir les trois dossiers détaillés. Les 46 autres n’ont pas encore de spécification fonctionnelle extraite, ce qui n’est pas une non-conformité.

La carte, les Engineering Profiles et les campagnes continuent de fonctionner. Les anciens ZIP de campagne ne changent pas; une nouvelle campagne conserve aussi les fiches et rapports JUnit source.
