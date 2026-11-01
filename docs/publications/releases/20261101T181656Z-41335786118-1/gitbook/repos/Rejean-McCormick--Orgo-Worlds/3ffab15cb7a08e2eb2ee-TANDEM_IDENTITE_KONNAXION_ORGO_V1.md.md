<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo-Worlds/blob/c2445db8abf78afcb647f22615ad3b9dd132bde8/docs/TANDEM_IDENTITE_KONNAXION_ORGO_V1.md | commit: c2445db8abf78afcb647f22615ad3b9dd132bde8 | SHA-256: bc11fc3469949cebda6bd588fb68ca64b54278b527a21e237e99455228d25c06 -->

# Contrat FakePlant / Konnaxion / Orgo — identités

Le World Pack FakePlant utilise `world-packs/fakeplant/identity/koa-identity.json` pour documenter la source commune des **900 personnes synthétiques**. Ce fichier ne fournit aucun compte de connexion.

- Le `id` de chaque employé est une référence synthétique stable partagée, vérifiée via SHA-256.
- Orgo conserve son `UserAccount.id` (UUID applicatif), `PersonProfile.external_reference` pointe au `id` synthétique de la fixture.
- Konnaxion gère ses membres et son propre utilisateur Django; aucune égalité des UUID internes n'est imposée.
- Les véritables utilisateurs humains utilisent une identité OIDC `issuer + subject`, avec deux clients OIDC et autorisations distinctes.
- Le tenant Orgo `fakeplant` exige la création/vérification explicite de `Organization.id` ; ce dépôt ne crée pas d'organisation en base.
- Le scénario FakePlant reste à `world-packs/fakeplant` et la fixture historique non dupliquée à `fakeplant/fixture`, pour conserver les scripts existants; cela n'est pas un Universe imbriqué Konnaxion et ne remplace pas le catalogue canonique `Konnaxion_Worlds/universes`.

**Validation :** `node tools/fakeplant/validate.mjs` (lecture seule). Aucun accès réseau, aucun seed appliqué.
