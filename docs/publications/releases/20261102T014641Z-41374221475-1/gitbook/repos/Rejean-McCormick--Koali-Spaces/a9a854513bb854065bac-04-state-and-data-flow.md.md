<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/02-architecture/04-state-and-data-flow.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 7d9475e4a26eacafc2e93b366b529d949ace64e915bea6194f48bdb96894c6ce -->

# Flux d’état et de données

**Classe : Normatif**

Flux de shell :

```text
kOA -> control socket -> active-state.json -> /api/shell-state -> ShellProvider
                                                   |
                                                   v
                           registry/capability filters -> shell UI
```

Le state public contient :

- état de présentation ;
- network state ;
- Space actif ;
- thème actif ;
- manifests actifs ;
- module/route actifs ;
- capabilities projetées ;
- raison de dégradation.

Les champs internes précédés de `_` servent aux receipts/rollback et ne sont pas exposés au browser.

Le client actuel rafraîchit le shell state périodiquement. Une stratégie événementielle future peut remplacer le polling sans changer le modèle de propriété.
