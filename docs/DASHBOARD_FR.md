# Tableau de bord GitHub Pages — guide kOA

## Ce que cette fonctionnalité fait

- Produit un site interactif en français dans `docs/` : graphiques, indicateurs, historique des campagnes et bascule **Audit local / GitHub OBSERVE**.
- **Ne relance aucun audit.** Les 3 rapports déjà communiqués sont inclus comme trois exemples réels **agrégés** : deux rapports locaux et une observation GitHub incomplète.
- N'utilise **aucun jeton personnel**, aucune API en ligne, aucune dépendance JavaScript externe.
- N'exporte jamais les JSON/CSV originaux, chemins Windows, noms de fichiers, noms de dépôts, commits, valeurs de secrets, extraits de code ou résultats par dépôt. On publie uniquement des chiffres et des statuts globaux autorisés.
- Le site affiche **la dernière publication** et rafraîchit ses données environ toutes les 3 minutes lorsque la page est ouverte. Une nouvelle campagne locale doit d'abord être agrégée puis ses fichiers publiés dans le dépôt de dashboard : aucune page web ne peut lire directement `C:\mycode`.

## Mettre à jour depuis le launcher

1. Ouvrir `kOA_GitHub_Audit_Launcher.pyw`.
2. Dans **Tableau de bord**, choisir le `audit.json` d'une campagne existante (**Audit local** ou **OBSERVE GitHub**); le second rapport est optionnel.
3. Cliquer **Mettre à jour le tableau de bord** : cela actualise `docs/data/dashboard.json` et conserve les campagnes précédentes, par date UTC et par mode.
4. Cliquer **Aperçu dans le navigateur** : ouvre un serveur uniquement sur `127.0.0.1`, sans publication sur Internet.
5. Vérifier les chiffres, puis publier les modifications du dossier `docs/` dans le dépôt **kOA-Digital-Ecosystem-GitHub-Audit**, sur la branche choisie pour Pages.

## Ligne de commande — sans interface graphique

```powershell
python -m koa_audit dashboard-publish `
  --audit-json "C:\mycode\mes-rapports\audit-local.json" `
  --audit-json "C:\mycode\mes-rapports\audit-github.json" `
  --out docs

# Aperçu local : ouvrir http://127.0.0.1:8765/
python -m http.server 8765 --bind 127.0.0.1 --directory docs
```

## Activer GitHub Pages (une seule fois)

1. Dans le dépôt `kOA-Digital-Ecosystem-GitHub-Audit`, aller dans **Settings → Pages**.
2. Choisir **Deploy from a branch**.
3. Choisir la branche **main** (ou la branche publiant le site), puis le dossier **/docs**.
4. Enregistrer. GitHub déploie le site lorsque des modifications dans `/docs` sont poussées par un utilisateur (selon les règles GitHub Pages).
5. Le site de projet sera normalement à l'adresse `https://<propriétaire>.github.io/kOA-Digital-Ecosystem-GitHub-Audit/`, si Pages est activé et si ce dépôt est le bon dépôt publié. Vérifier l'URL réelle dans **Settings → Pages**.

Aucune publication sur GitHub n'est déclenchée par notre application. Le dépôt peut être publié avec l'outil Git habituel. **Ne pas pousser le dossier `reports/` ni les JSON bruts.**

## Confidentialité et limites

**Attention : GitHub Pages est normalement public**, même si les fichiers originaux viennent d'un dépôt privé; certaines configurations Enterprise proposent une visibilité privée. Le JSON publié dans `docs/data/dashboard.json` a été conçu comme données publiques **agrégées**. Valider le contenu avant chaque première mise en ligne.

Les anciens rapports locaux 2026-10-28 ont utilisé une règle TLS trop large : leurs 6 alertes historiques sont **des motifs à requalifier**, pas 6 contournements HTTPS confirmés. Le correctif de règle date de la version 0.4.1; ce dashboard ne modifie pas rétroactivement les résultats antérieurs. Le problème `backend/.env` a été réglé plus tard : le dashboard ne constitue pas un suivi de corrections individuelles.

Le rapport `OBSERVE` du 2026-10-28 n'a pu observer que **15/49 dépôts**, et les alertes CodeQL/Dependabot/Secret Scanning sont **inconnues**. Aucun zéro d'alertes ne représente une attestation de sécurité.

## Publication automatisée (v0.6.0)

Le bouton **Publier sur GitHub (1 clic)** du launcher envoie le JSON agrégé et
le workflow Pages vers le **seul dépôt d'audit**, via les identifiants déjà
pris en charge par Git pour Windows. Aucun nouvel audit n'est lancé.
Cette étape est une écriture distante explicite, demandant confirmation dans l'interface.
Une activation initiale de GitHub Pages, source **GitHub Actions**, peut être requise.
La publication du workflow peut être refusée si le compte Git ne possède pas
les permissions correspondantes. Il n'existe aucun push forcé dans cette fonction.

## Dépannage aperçu Windows (v0.6.1)

Si Chrome affichait `ERR_EMPTY_RESPONSE` sur `127.0.0.1`, c'était causé
par les journaux HTTP tentant d'écrire dans la console absente de `pythonw.exe`.
Le serveur d'aperçu a été corrigé. Fermer l'ancienne application, décompresser
la v0.6.1 et relancer le launcher. Puis cliquer « Aperçu dans le navigateur ».
Le site d'aperçu est accessible uniquement tant que l'application reste ouverte.
Aucun nouveau scan ou `push` n'est nécessaire.
