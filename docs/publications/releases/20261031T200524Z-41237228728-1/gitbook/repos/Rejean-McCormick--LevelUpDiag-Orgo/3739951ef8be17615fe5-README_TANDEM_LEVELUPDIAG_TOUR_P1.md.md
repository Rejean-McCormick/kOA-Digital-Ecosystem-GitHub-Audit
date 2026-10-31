<!-- Frozen source: https://github.com/Rejean-McCormick/LevelUpDiag-Orgo/blob/79d495e637838784a1e137a7cf83722354f020f2/README_TANDEM_LEVELUPDIAG_TOUR_P1.md | commit: 79d495e637838784a1e137a7cf83722354f020f2 | SHA-256: 2e7f0e331c376459ed5ac6583036554c33f2e6a9e1f60f38455c5e4af2bdbef4 -->

# Installation — Tandem 1.0 — OrgoDiag / LevelUpDiag — Tour 7/8

**Racine du dépôt** : `C:\mycode\Orgo\LevelUpDiag-Orgo` (contenant `levelupdiag.py`).
Extraire toute cette archive **à la racine** du dépôt, puis sous Windows :

```powershell
cd 'C:\mycode\Orgo\LevelUpDiag-Orgo'
.\PREVIEW_LEVELUPDIAG_TOUR_P1.cmd
.\INSTALL_LEVELUPDIAG_TOUR_P1.cmd
.\VERIFY_LEVELUPDIAG_TOUR_P1.cmd
```

`ROLLBACK_LEVELUPDIAG_TOUR_P1.cmd` revient aux 8 fichiers de source ciblés
uniquement si leurs SHA-256 correspondent à la version installée. Les sauvegardes
sont conservées sous `C:\mycode\Orgo\Tandem_Local\levelupdiag_tour_p1\backups\`.
Le package contient une archive de **référence de code** pour les tests isolés :
elle n'est **pas déployée** dans le dépôt ou les données Orgo. L'archive ne contient
ni `.env` opérationnel ni base de données; les campagnes existantes ne sont pas
exécutées par l'installateur.

Le lot corrige `verify-run`, ajoute les liens SHA-256 des rapports Nxx, un contrôle
optionnel de l'empreinte du résumé épinglée **hors du lot**, et 17 tests adversariaux.
Il n'ajoute aucune preuve de réussite d'Orgo et ne contacte pas Orgo, Konfid, la DB,
Docker, un navigateur ou le VPS.

Après la tournée, la qualification intégrée exécutera des campagnes réelles Orgo
sur environnement de test, puis associera leurs empreintes au registre des preuves
kOA Digital Ecosystem. Les anciens rapports `verification/embedded` restent de
l'historique, **pas** des attestations de cette mise à jour.
