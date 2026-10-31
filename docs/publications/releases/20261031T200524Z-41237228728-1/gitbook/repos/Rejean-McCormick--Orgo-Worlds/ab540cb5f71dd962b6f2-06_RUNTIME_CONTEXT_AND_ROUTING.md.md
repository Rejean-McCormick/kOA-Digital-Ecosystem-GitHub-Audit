<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo-Worlds/blob/c2445db8abf78afcb647f22615ad3b9dd132bde8/docs/Technical-Reference/Worlds/06_RUNTIME_CONTEXT_AND_ROUTING.md | commit: c2445db8abf78afcb647f22615ad3b9dd132bde8 | SHA-256: 44e46df58e3ce50eefbab7a581e1b462c82edb98a8cdf4488a395c7cd2df3aea -->

# Runtime context and routing

The standalone API exposes World control/routing operations only. With the current bootstrap (`app.setGlobalPrefix("api")`), the canonical local endpoints include:

```text
GET  /api/control/worlds
POST /api/control/worlds
GET  /api/control/worlds/{world_key}
GET  /api/control/worlds/{world_key}/releases
POST /api/control/worlds/{world_key}/releases
POST /api/control/worlds/{world_key}/releases/{release_id}/promote
GET  /api/control/worlds/{world_key}/memberships
PUT  /api/control/worlds/{world_key}/memberships/{user_id}
POST /api/control/worlds/{world_key}/archive
GET  /api/runtime
```

The request context can carry organization, user, permission, World and release identifiers through the standalone header contract. It is control/routing context; it does not activate a local Signal/Case/Task engine.

Operational routes such as `/tasks`, `/cases`, `/signals` and `/workflows`, plus the Interaction Kernel endpoint, belong to the main `Orgo` product.
