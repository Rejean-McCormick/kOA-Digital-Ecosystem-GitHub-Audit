# Profils et conformité — guide rapide

Dans le launcher `kOA_GitHub_Audit_Launcher.pyw`, ouvrir **Profils & conformité**.

1. Choisir le dépôt dans la liste des 49 projets.
2. Filtrer la checklist par **Architecture** ou **Sécurité**.
3. Cliquer une pratique pour lire sa fiche originale dans le volet de droite.
4. Choisir **Non évalué**, **Pas applicable**, **À améliorer** ou **Appliqué** et, idéalement, noter pourquoi.
5. Cliquer **Enregistrer**. La progression se met à jour pour ce dépôt seulement.
6. Choisir `ENGINEERING_PROFILE.md` ou `SECURITY_PROFILE.md` pour consulter le rapport Markdown local.
7. Quand un nouveau rapport est prêt, cliquer **Importer .md** pour le lier au dépôt sélectionné. L'import modifie seulement le dossier de cette application.

Le lien avec l'audit se fait par le fichier `audit.json` sélectionné dans l'onglet Tableau de bord. L'outil affiche son statut, fichiers inspectés et nombre d'observations pour le dépôt choisi; il ne lance aucun nouveau scan.

L'état d'une pratique n'est pas une certification; ne considérer **Appliqué** comme une validation technique qu'après examen des preuves. Tous les profils manquants et tous les statuts non fournis restent **Non évalué**.

Les évaluations sont stockées dans `%LOCALAPPDATA%\kOA-GitHub-Audit\profiles\assessments.json` et ne sont jamais envoyées par le bouton du dashboard GitHub Pages. Les fichiers des rapports sont dans `profiles/repositories/<nom>`. Ne pas inclure de secrets dans les notes.

**Provenance :** les 33 patterns d'architecture et les 53 de sécurité proviennent des archives fournies par l'utilisateur. Le profil Konnaxion fourni date du 16 septembre 2026; son rattachement au dépôt est présumé. Pour Orgo et kOA-Linux-Koali, les premiers rapports sont provisoires et n'affirment pas posséder des mesures de complexité ni des tests exécutés.
