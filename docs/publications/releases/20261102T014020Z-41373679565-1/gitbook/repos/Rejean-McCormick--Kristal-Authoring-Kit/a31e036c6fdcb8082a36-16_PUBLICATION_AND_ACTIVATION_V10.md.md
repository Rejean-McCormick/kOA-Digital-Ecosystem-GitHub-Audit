<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Authoring-Kit/blob/2a20971ca69828a5168c7a086a14accbbb5cee6f/docs/16_PUBLICATION_AND_ACTIVATION_V10.md | commit: 2a20971ca69828a5168c7a086a14accbbb5cee6f | SHA-256: 1cee1dbea5c67a8c2acbfe921067451f2a12ae3abb65cb7dd769d4ea4340e1b3 -->

# 16 — V10 publication and activation boundaries

A qualified network release contains, at minimum, an exact `state-snapshot.json`, a `bundle-manifest.json` and a `publication.json`. The independently verified bundle must refer to the exact authorized Git commit and source state. C1 qualification, C2 authorization, C3 collection integrity, GitHub synchronization, immutable release, and activation have **different responsible owners and checks**.

The Authoring Kit's ordinary offline pipeline neither synchronizes a GitHub collection nor activates a hosted channel. The `publish-v9` and `activate-v9` commands belong to a **local v9 lifecycle** and must not be presented as hosted network publication.

**A public sync is already a disclosure operation.** A GitHub release is not the first point of exposure. Never bypass authorization or attempt to repair a blocked C3 collection by fabricating a sync index or qualification receipt.
