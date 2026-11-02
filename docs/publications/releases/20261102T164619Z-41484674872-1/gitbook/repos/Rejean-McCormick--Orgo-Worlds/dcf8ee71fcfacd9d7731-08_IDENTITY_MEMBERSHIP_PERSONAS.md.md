<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo-Worlds/blob/c2445db8abf78afcb647f22615ad3b9dd132bde8/docs/Technical-Reference/Worlds/08_IDENTITY_MEMBERSHIP_PERSONAS.md | commit: c2445db8abf78afcb647f22615ad3b9dd132bde8 | SHA-256: 96588b87e2911d4a6137237f9a30cd2f8f8ea2142e9d5050e3f3f8c32cd39f21 -->

# Identity, memberships and personas

L'identité est organisationnelle. Le Common Login utilise le compte local ou OIDC avec clé `(issuer, subject)`. Un World ne crée jamais un second login pour une personne réelle.

`WorldMembership` ajoute un rôle local : owner/maintainer/member/viewer. Sur les routes runtime explicites, `viewer` est strictement lecture seule; `member` utilise ensuite les permissions RBAC normales. Les rôles `owner`/`maintainer` permettent la gestion de ce World sans accorder de permission globale. La création d’un nouveau World reste une capacité d’organisation (`worlds:manage` ou `*`). Un World `organization` est lisible par les acteurs autorisés de l'organisation; un World `private` exige membership active sauf administrateur global.

Les personas synthétiques, lorsqu'ils seront utilisés, restent distincts des comptes de connexion (`create_login=false`).
