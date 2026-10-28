# Lanceur graphique Windows — OBSERVE

`kOA_GitHub_Audit_Launcher.pyw` est une interface **Tkinter** locale (Python 3.11+), incluse à la racine du dépôt. Aucune dépendance tierce n'est nécessaire. Le fichier `.pyw` ne lance pas de console sous Windows.

## Démarrage

1. Installer Python 3.11+ sous Windows, avec **Tcl/Tk et IDLE** (option par défaut de l'installateur Python standard).
2. Décompresser le dépôt et **double-cliquer sur `kOA_GitHub_Audit_Launcher.pyw`**. L'interface doit rester à la racine avec le dossier `koa_audit/`.
3. Dans **Audit GitHub**, choisir `bundled` et cliquer sur **Prévisualiser le périmètre** : l'inventaire de départ (49 dépôts) s'affiche hors ligne.
4. Pour un audit authentifié, définir `KOA_AUDIT_TOKEN` (ou `GH_TOKEN`) dans **l'environnement du processus avant le lancement**, avec les permissions de lecture décrites dans `DEPLOYMENT.md`. Le lanceur ne prend pas de mot de passe et ne conserve aucun jeton.
5. Choisir `github` pour le dernier inventaire de référence ou `bundled` pour la copie initiale, puis lancer **Lancer l'audit OBSERVE**. `0` signifie tous les dépôts de l'inventaire choisi. Les rapports sont générés dans `reports/` par défaut.
6. Dans **Rapports**, consulter `SUMMARY.md`, `audit.csv` et `audit.json`.

### Lancer depuis PowerShell avec un jeton temporaire

```powershell
$env:KOA_AUDIT_TOKEN = "<read-only-installation-token>"
& "C:\chemin\vers\Python\pythonw.exe" ".\kOA_GitHub_Audit_Launcher.pyw"
# Le jeton doit être retiré de la session une fois l'application fermée.
Remove-Item Env:KOA_AUDIT_TOKEN
```

Cette syntaxe est illustrative : utiliser les chemins correspondant à votre installation. **Ne jamais écrire un vrai jeton dans un fichier du dépôt ni dans une capture d'écran.** Préférer un jeton GitHub App éphémère à un PAT permanent.

## Import historique

1. Onglet **Import historique** : choisir la famille (KonnaxionDiag, KorDiag, KristalDiag ou LevelUpDiag), saisir **explicitement** le dépôt `owner/repo` ciblé et sélectionner le JSON ou ZIP source.
2. Pour un ZIP, saisir le chemin interne exact d'un résumé JSON (sans extraction) ; pour un JSON, laisser ce champ vide.
3. Cliquer **Importer les métadonnées** : un JSON normalisé et daté est créé dans `.legacy/` par défaut, sans écraser un ancien résultat.
4. L'option « Inclure les diagnostics historiques normalisés » devient disponible pour la prochaine campagne.

Les vérifications de schéma ont lieu dans la CLI. Un import historique est **non vérifié et non autoritatif** : il ne signifie jamais qu'un dépôt est actuellement sain.

## Fonctionnement et limites

- Le lanceur invoque localement `python -m koa_audit` par `subprocess` **sans shell** ; il n'exécute aucun programme provenant d'un dépôt cible.
- La prévisualisation `bundled` est hors ligne, mais `github` et l'audit font des appels à l'API GitHub. Une API inaccessible ou des permissions insuffisantes donnent des observations inconnues ou partielles.
- Le bouton **Annuler** termine la commande locale ; si l'opération écrivait un rapport, vérifier les fichiers éventuellement partiels avant de les réutiliser.
- Les dossiers `reports/` et `.legacy/` sont ignorés par Git. Les observations GitHub et les métadonnées d'incident peuvent être sensibles ; conserver les rapports privés.
- Aucun contrôle de protection de branches n'est ajouté, aucun scan distant n'est déclenché, aucune correction et aucun merge ne sont exécutés.
- L'interface utilise Windows et a été **vérifiée syntaxiquement et via des tests hors ligne**, mais son rendu graphique et le double-clic doivent être vérifiés sur une machine Windows avec Tkinter installé.
