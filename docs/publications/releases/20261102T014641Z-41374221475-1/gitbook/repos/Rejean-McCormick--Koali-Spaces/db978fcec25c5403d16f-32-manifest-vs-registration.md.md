<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/03-routing-and-registry/32-manifest-vs-registration.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 51e336023e5971499bd07501b8a0eee5c1b53b9c21642128b21ec248eb389a31 -->

# 32. Séparation des contrats : manifest vs registration

## 32.1 Module interface manifest

Rôle : présentation déclarative du module.

Il peut décrire, selon le contrat canonique applicable :

- routes ;
- sidebar ;
- top-bar widgets ;
- labels ;
- capability requirements ;
- offline presentation behavior.

Il ne doit pas contenir de secret ni devenir une configuration privilégiée de runtime.

## 32.2 Local surface registration

Rôle Koali local : relier une identité de module validée à un runtime local explicitement admis.

Exemple cible non canonique kOA :

```json
{
  "schema_version": 1,
  "module_id": "konnaxion",
  "surface_kind": "local_module_surface",
  "runtime_ref": "service:konnaxion-web",
  "health_ref": "service:konnaxion-health",
  "presentation": {
    "default_mode": "framed",
    "immersive_allowed": true,
    "context_accent_token": "module.konnaxion"
  }
}
```

`runtime_ref` doit être résolu côté serveur à partir d'une configuration admise. Le navigateur ne reçoit pas de secret.

`LOCK-KS-SURF-107` — **`runtime_ref` n'est pas une capability et n'accorde pas d'autorisation.**

`LOCK-KS-SURF-108` — **Un module manifest et une local surface registration doivent correspondre au même `module_id` stable avant activation.**

---
