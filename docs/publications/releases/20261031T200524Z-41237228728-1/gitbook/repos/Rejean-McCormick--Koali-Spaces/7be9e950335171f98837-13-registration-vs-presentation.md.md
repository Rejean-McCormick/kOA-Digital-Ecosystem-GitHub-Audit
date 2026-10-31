<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/03-routing-and-registry/13-registration-vs-presentation.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 65fac8f4ce1f797ef9ccd9389c00f505636b2c7cf32a790c49ead912d078f4c5 -->

# 13. RuntimeRegistration vs SurfacePresentationPolicy

Ces deux objets ne doivent pas être fusionnés.

## RuntimeRegistration

Possède les faits techniques nécessaires au control side :

```text
module/runtime identity
artifact reference
runtime reference
health/readiness reference
lifecycle profile reference
transport profile reference
offline class
embed compatibility
```

## SurfacePresentationPolicy

Possède seulement l'expérience Koali :

```text
moduleId
label source
accentTokenRef
allowed display modes
default display mode
chrome profile
```

`LOCK-KS-SURF-145` — **Les informations de runtime/lifecycle/transport et les préférences de présentation Koali sont des structures distinctes ; une couleur ou un mode d'affichage ne peut pas devenir une propriété d'autorité runtime.**
