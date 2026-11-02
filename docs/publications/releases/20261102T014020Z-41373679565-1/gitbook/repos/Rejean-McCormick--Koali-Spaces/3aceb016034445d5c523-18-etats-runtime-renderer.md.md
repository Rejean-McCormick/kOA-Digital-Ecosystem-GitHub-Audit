<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/04-runtime-and-security/18-etats-runtime-renderer.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 0d02e8d380104cbb976d050bc97ec7e0088a6723fc4da6723fad7de942edb2d5 -->

# 18. État de surface : quatre axes orthogonaux

La v1.1 remplace l'enum unique `SurfaceRuntimeState` par quatre axes indépendants.

```ts
interface SurfaceStatus {
  access:
    | "allowed"
    | "blocked";

  runtime:
    | "inactive"
    | "starting"
    | "ready"
    | "degraded"
    | "failed"
    | "missing";

  connectivity:
    | "online"
    | "offline"
    | "unknown";

  render:
    | "idle"
    | "resolving"
    | "loading"
    | "ready"
    | "error";
}
```

Exemple valide :

```text
access       = allowed
runtime      = ready
connectivity = offline
render       = ready
```

Il décrit une application locale prête et utilisable hors ligne.

Autre exemple :

```text
access       = blocked
runtime      = ready
connectivity = online
render       = idle
```

Le runtime existe, mais Koali ne doit pas le monter.

`LOCK-KS-SURF-067` — **Un état de panne ne peut pas être converti en succès autoritatif.**

`LOCK-KS-SURF-068` — **L'état `blocked` doit rester distinct de `unavailable`.** Le premier représente une décision de politique/contrat ; le second une indisponibilité technique.

`LOCK-KS-SURF-069` — **Les messages d'erreur du host ne doivent pas prétendre connaître l'état métier interne de l'application.**

`LOCK-KS-SURF-137` — **Access, runtime, connectivity et render sont des axes distincts ; le code ne doit pas les réduire à un enum unique qui perd les combinaisons valides.**

`LOCK-KS-SURF-138` — **`access=blocked` interdit le montage de la surface même si `runtime=ready` et le health check réussit.**
