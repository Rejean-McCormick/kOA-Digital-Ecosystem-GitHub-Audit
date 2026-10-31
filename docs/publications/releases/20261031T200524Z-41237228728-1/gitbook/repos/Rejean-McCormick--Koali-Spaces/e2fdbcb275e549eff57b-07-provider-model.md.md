<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/07-global-surfaces/07-provider-model.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: b06788fbfd7845036876719644e9ce9a458bd179b6deaa71414cad521b91b98d -->

# Provider model global

**Classe : Architecture cible**

Providers recommandés :

- SearchProvider ;
- TaskProvider ;
- StatusProvider ;
- CounterProvider ;
- ResumeProvider.

Chaque provider : identité stable, owner, capability requirements, offline behavior, staleness, bounded timeout et target routes déclarées.

Un provider de vue est non autoritatif. Il ne doit ni exécuter une transaction cross-owner ni cacher sa staleness.
