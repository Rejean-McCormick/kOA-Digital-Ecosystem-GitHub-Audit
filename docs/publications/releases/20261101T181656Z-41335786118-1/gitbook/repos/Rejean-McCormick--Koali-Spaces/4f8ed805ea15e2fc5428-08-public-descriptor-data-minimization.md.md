<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/01-core-architecture/08-public-descriptor-data-minimization.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: f5fb117d0455464f8d8b6d47605f7ca8a8ad9d827a62a05ee3e44258ae541afd -->

# 8. Minimisation du descriptor public

Le fait qu’un champ existe dans le control side ne justifie pas son exposition au navigateur.

## 8.1 Informations typiquement server-only

```text
runtimeRef
agent/control endpoint
local service-manager identity
artifact staging path
socket path
operator filesystem path
secret-store reference
privileged lifecycle operation
raw capability evidence
```

## 8.2 Informations nécessaires au navigateur

```text
surfaceId
moduleId
routeId
kind
public status
label/accent token
immersiveAllowed + default display mode
safe embedSrc
iframeTitle
sandbox tokens
browser permissions
optional bridgeProtocolRef
```

`LOCK-KS-SURF-154` — **Une target navigateur peut exposer uniquement l'adresse nécessaire au rendu admis ; elle ne peut pas exposer l'endpoint de contrôle/lifecycle ni des détails internes sans nécessité de présentation explicite.**
