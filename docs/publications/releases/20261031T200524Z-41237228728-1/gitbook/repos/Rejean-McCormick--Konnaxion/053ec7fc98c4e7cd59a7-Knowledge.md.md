<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion/wiki/Knowledge | commit: 62c3bb451bacb4cfbbeb68181c1edfc7ba47a8f9 | SHA-256: 0730dd4e36baeb03c2a17b1810d1f0cbca7e75773c72c51ae52ef2d92d800cc3 -->

# Knowledge — KonnectED Learning Resources

Knowledge is a **capability inside KonnectED**, not an independent ecosystem system.

Canonical backend:

```text
backend/konnaxion/konnected/
```

## Current models

- `KnowledgeResource`;
- `KnowledgeRecommendation`;
- `LearningProgress`;
- `OfflinePackage`.

KonnectED also contains certification, portfolio, mentorship, co-creation and forum capabilities.

## Current UI

Current route families include:

```text
/konnected/knowledge/contribute
/konnected/learning-library/*
/konnected/learning-paths/*
```

## Offline packages

A KonnectED `OfflinePackage` is a Konnaxion learning/content package. It must not be called a Kristal Runtime Pack unless an explicit Kristal integration contract adopts that semantics.

## Ownership

KonnectED owns the learning-resource/progress state. Search or recommendation surfaces are projections/capabilities over that state, not alternate sources of truth.
