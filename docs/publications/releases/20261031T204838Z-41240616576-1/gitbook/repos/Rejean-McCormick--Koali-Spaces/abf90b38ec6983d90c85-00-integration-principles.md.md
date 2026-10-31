<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/11-integrations/00-integration-principles.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 79dcacb15bcc4f400f0cc21582c8c3ca99846ec55f9381b0409322fa31a67e4e -->

# Principes d’intégration

**Classe : Normatif**

Une intégration Koali Spaces décrit comment présenter un owner, pas comment absorber son architecture.

Avant onboarding : lire le contract/boundary kOA applicable, la documentation officielle du propriétaire et la Surface Layer.

Chaque application complète doit posséder un Application Conformance Profile décrivant transport, readiness, base path, frame policy, auth, offline behavior, browser permissions et route ownership.


## Standalone + integrated

Un owner peut rester une application standalone et publier simultanément une contribution Koali intégrée. Une intégration ne doit pas créer de dépendance UI privée entre deux produits. Les comportements génériques de shell viennent du contrat/primitives Koali ; les objets, pages et actions métier restent dans le produit propriétaire.

Le retrait d’un produit est un cas nominal : son manifest disparaît du registre et les autres produits restent fonctionnels.
