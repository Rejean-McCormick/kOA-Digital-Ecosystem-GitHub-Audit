<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/blob/9d4f7e74ed87b5a4c8d284dad891029d834911e4/docs/runbooks/README.md | commit: 9d4f7e74ed87b5a4c8d284dad891029d834911e4 | SHA-256: 9ee07c296e06d1067245d9b16b8fc51b73c4812487dd86bb4f9d05f14c85d429 -->

# Runbooks Konstellation

- [Startup / readiness](STARTUP.md)
- [Rollback](ROLLBACK.md)
- [Backup / restore](BACKUP-RESTORE.md)
- [Threat model](THREAT-MODEL.md)
- [Incident](INCIDENT.md)
- [Upgrade](UPGRADE.md)

Ces runbooks complètent [OPERATIONS.md](../OPERATIONS.md). Toute instance partagée/publique doit adapter les commandes à son orchestrateur, son reverse proxy, son stockage canonique et sa gestion de secrets. Les projections et caches Konstellation sont reconstructibles et ne remplacent jamais le Kristal canonique dans un plan de reprise.
