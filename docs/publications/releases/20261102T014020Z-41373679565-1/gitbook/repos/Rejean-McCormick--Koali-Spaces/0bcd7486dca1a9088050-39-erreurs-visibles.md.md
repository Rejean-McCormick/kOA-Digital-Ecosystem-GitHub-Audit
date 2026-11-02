<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/04-runtime-and-security/39-erreurs-visibles.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 78635a53e9a96e3f7665ffc6de82c88bbedaa5f91676dbda892d93911c3eacd7 -->

# 39. Erreurs visibles

Exemples de codes techniques Koali :

```text
KS_SURFACE_MODULE_UNKNOWN
KS_SURFACE_ROUTE_UNKNOWN
KS_SURFACE_CAPABILITY_DENIED
KS_SURFACE_REGISTRATION_MISSING
KS_SURFACE_TARGET_REJECTED
KS_SURFACE_RUNTIME_UNAVAILABLE
KS_SURFACE_HEALTH_NOT_READY
KS_SURFACE_EMBED_BLOCKED
KS_SURFACE_RUNTIME_ERROR
```

Les codes doivent être stables et testables.

`LOCK-KS-SURF-121` — **Les erreurs de surface ne doivent pas être remplacées par une page business fictive.**

`LOCK-KS-SURF-122` — **Une erreur de sécurité/politique ne propose pas “ouvrir quand même”.**

---
