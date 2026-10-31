<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion-Capsule-Manager/blob/a137f3c1ab5e7a79887074560b11a2a6b0a70518/README_TANDEM_IK_E2E_LOCAL_V1.md | commit: a137f3c1ab5e7a79887074560b11a2a6b0a70518 | SHA-256: a9c2c14d16c113f4efb7a6d0b5d8fe90e51a7d55945e04a3bdb6ee00b600883a -->

# FakePlant — premier aller-retour IK local

Cible : Capsule Manager `C:\mycode\Konnaxion\Konnaxion_Capsule_Manager`.

Prerequis deja verifies : backend Uvicorn actif Windows, Celery `--pool=solo`, Redis `konnaxion_ik_redis`, Orgo API/Worker/PostgreSQL Docker, Workflow `konnaxion_decision_v1` version 2 publiee, jeton IK encore valide, tenant UUID `0c2d7244-a0c0-4a10-8f11-0389f275f133`.

Avant de tester, sauvegardes Neon et Orgo recommandees. Lancement ecriture sans confirmation a recopier : `TEST_TANDEM_IK_E2E_FAKEPLANT.cmd`. Le lanceur repasse le preflight en lecture seule, cree UNE decision synthetique fermee puis publiee sous le World `fp-electromecanique-informatique`, release ID `132`, et enfile son emission pour Celery. L'API Orgo doit recevoir un Signal, appliquer le workflow V2, creer un Case et une Task et retourner un impact a Konnaxion.

Lancer `STATUT_TANDEM_IK_E2E_FAKEPLANT.cmd` pour controler l'etat sans nouvelle ecriture dans les bases. Le rapport local, ecrit par les deux lanceurs, est `C:\mycode\Konnaxion\Tandem_Local\fakeplant-IK-E2E-LIVE.LOCAL.json`. Aucun jeton n'est affiche.

Ce test reutilise la decision existante si le lanceur est relance et ne cree pas de nouvel envoi. **Ne pas relancer l'execution si le resultat reste en attente : verifier les logs Celery, Orgo Worker et le rapport.**

Le test confirme un parcours fonctionnel synthetique, **pas** les ACL humaines, le SSO, la securite production, ni le GO LIVE. Il cree des lignes persistantes dans Neon et Orgo. Il n'importe pas les 900 employes et ne touche pas aux autres tenants.
