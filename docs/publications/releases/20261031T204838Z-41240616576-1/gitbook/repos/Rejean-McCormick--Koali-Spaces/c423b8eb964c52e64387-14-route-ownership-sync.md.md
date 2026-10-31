<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/03-routing-and-registry/14-route-ownership-sync.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: dab05d547c9caf19b27e13529966ce20cab8066784fc4304c6c5f3f12d3ddabc -->

# 14. Propriété du routing et synchronisation

Koali possède :

```text
module selection
outer namespace
route contribution admission
initial deep-link mapping
return to Koali
```

L'application enfant possède ensuite son router interne.

MVP :

```text
/apps/konnaxion/<declared-deep-link>
    -> initial path transmis à Konnaxion
    -> navigation interne ultérieure gérée par Konnaxion
```

Une synchronisation plus riche peut exister plus tard uniquement par protocole versionné et opt-in.

`LOCK-KS-SURF-146` — **Après le deep link initial, le router interne de l'application propriétaire reste son autorité de navigation sauf bridge versionné explicitement négocié.**

`LOCK-KS-SURF-147` — **Koali ne synchronise pas silencieusement son URL avec le router enfant par inspection DOM, interception non déclarée ou heuristique de navigation.**
