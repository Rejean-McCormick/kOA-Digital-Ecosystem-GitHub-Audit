<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Subsystem-Documentation-Mounts | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: e037cd9c5ac891f0c88b97ebbc044e33d1655b814796442dce4db15b0c072d70 -->

<!-- Explanatory wiki projection. Normative authority remains in the repository and subsystem documentation. -->

# Subsystem Documentation Mounts

> **Reading model:** The main path explains what the kOA ecosystem enables. The technical reference explains how kOA-Linux hosts, isolates, verifies, and operates those capabilities. Product-specific details remain in each subsystem's own documentation.

The repository reserves documentation mount points for independently maintained systems:

```text
docs/subsystems/ariane
docs/subsystems/konnaxion
docs/subsystems/orgo
docs/subsystems/sentient
docs/subsystems/semantik-architect
```

These paths may be directory junctions or symbolic links to pinned official documentation repositories. They are not copied into kOA-Linux as a second authority.

There is no UCKK subsystem mount because UCKK is an external Moodle platform. Product readers should normally use the public Wikis listed in [Related Wikis](Related-Wikis).
