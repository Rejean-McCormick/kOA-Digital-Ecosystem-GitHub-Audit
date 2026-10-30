# Ouvrir le centre de pilotage kOA

1. **Décompresse** toute l'archive ZIP dans un dossier ordinaire sur Windows.
2. **Double-clique** `kOA_GitHub_Audit_Launcher.pyw`.
3. Le premier onglet est **Écosystème**. Clique sur **Ouvrir le centre de pilotage (carte + profils)**.
4. Dans le navigateur, explore la **Carte des contrats (12 systèmes)** ou la **Constellation (49 dépôts)**.
5. Clique une application, puis **Lire l'Engineering Profile original** pour consulter le Markdown complet. Tu peux aussi voir les cinq jalons de qualification dans la fiche.

**Rien à scanner et rien à publier pour consulter ces résultats.** Les 12 profils mesurés de l'inventaire sont déjà présents. Le 13e profil complémentaire reste disponible dans l'onglet Windows « Certification & profils ».

- Pour enregistrer des preuves et des statuts : onglet **Certification & profils** de l'application Windows.
- Pour vérifier les 49 dépôts en tableau : **Registre des 49**.
- Pour publier le site : bouton **Publier sur GitHub**, seulement si tu le décides. La version publique montre la carte et des rapports d'ingénierie expurgés; tes preuves et notes locales ne sont pas exportées.
- Si l'aperçu ne s'ouvre pas : exécute `DIAGNOSTIC_LAUNCHER.cmd` et consulte le message affiché.

Le tableau de bord ne classe pas les noms de fichiers similaires, les copies de dépôts ou l'absence de certains outils comme des défauts de qualité.

## Mesurer et figer des preuves — v0.11.0

Dans **Campagnes datées**, sélectionne ton ancien `audit.json` ou le dossier d'un clone Git précis. Clique sur **Mesurer clones de l'audit** ou **Mesurer ce clone**. Par défaut, seul Git est lu (aucun test ni scan complet). L'option `scc/Lizard/Universal Ctags` est facultative. Les rapports privés sont joints à la prochaine campagne, puis consultables dans ton navigateur via **campagne → dépôt → preuve**. Utilise **Comparer à la campagne précédente** pour consulter les graphiques de progression documentaire.
