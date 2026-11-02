<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo-Worlds/blob/c2445db8abf78afcb647f22615ad3b9dd132bde8/docs/Technical-Reference/Worlds/10_CONTROL_PLANE_API.md | commit: c2445db8abf78afcb647f22615ad3b9dd132bde8 | SHA-256: a9ac8c0d93c0a984734a235fc7d5ac9e175cffdb084d32133982894495bc8992 -->

# Control plane API

```text
GET    /api/v3/control/worlds
POST   /api/v3/control/worlds
GET    /api/v3/control/worlds/{key}
GET    /api/v3/control/worlds/{key}/releases
POST   /api/v3/control/worlds/{key}/releases
POST   /api/v3/control/worlds/{key}/releases/{id}/promote
GET    /api/v3/control/worlds/{key}/memberships
PUT    /api/v3/control/worlds/{key}/memberships/{userId}
POST   /api/v3/control/worlds/{key}/archive
```

Toutes les mutations sont authentifiées, validées par Zod, idempotentes au niveau HTTP/Commands lorsque pertinent, et les événements de control plane sont écrits dans `world_audit_events`.
