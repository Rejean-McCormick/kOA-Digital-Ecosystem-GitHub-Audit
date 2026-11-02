<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Ekole-Integration | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: 38d68200c0abe919dcb3f9f511248b9b50d4c491b50ff86a1a9bb269f905b593 -->

# Ekole Integration

Ekole remains the owner of curriculum, source selections, editorial review, and student-readable releases. Spek can import **only a deliberately filtered exported projection**, not an Ekole repository or teacher workspace.

```
python -m spek import-educational --adapter ekole --input examples/education/ekole-curated-preview.json --out-dir education-ekole
python -m spek build --source education-ekole/article.json --realizations education-ekole/realizations.json --out dist-education
python -m spek verify-site dist-education
```

The example is invented and trilingual, not approved educational material. The export records audience, classification, dataset, reader policy and upstream review. Spek never upgrades these claims to publication permission. Refer to [[Educational Privacy]] and [[Educational Layout Pack]].
