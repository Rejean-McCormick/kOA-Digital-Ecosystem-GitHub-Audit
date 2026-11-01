<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/UCKK | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: 83e19a488ebf70d97112580fa6c990f591f30e5c71cffd18c22173bdaa0084d7 -->

<!-- Explanatory wiki projection. Normative authority remains in the repository and subsystem documentation. -->

# UCKK

> **Reading model:** The main path explains what the kOA ecosystem enables. The technical reference explains how kOA-Linux hosts, isolates, verifies, and operates those capabilities. Product-specific details remain in each subsystem's own documentation.

UCKK is an external Moodle platform for online learning, courses, pathways, activities, resources, and learning communities.

It is not an internal kOA-Linux subsystem and does not define the kOA ecosystem. Its own Mediatheque is distinct from the local kOA Mediatheque.

Where enabled, kOA-Linux can support two explicit operations:

- `publish_to_uckk` — publish an authorized local representation as a distinct UCKK object;
- `import_from_uckk` — import a selected UCKK resource as a distinct local offline copy.

There is no implicit database merge or generic `sync_mediatheques` operation.
