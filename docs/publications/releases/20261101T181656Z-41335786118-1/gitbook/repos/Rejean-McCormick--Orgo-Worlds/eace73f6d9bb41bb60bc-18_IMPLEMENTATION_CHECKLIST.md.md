<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo-Worlds/blob/c2445db8abf78afcb647f22615ad3b9dd132bde8/docs/Technical-Reference/Worlds/18_IMPLEMENTATION_CHECKLIST.md | commit: c2445db8abf78afcb647f22615ad3b9dd132bde8 | SHA-256: 837044a29782ba59f7d19f91221f99abf69d34a67dacad78c1e7c7df5cd1517a -->

# Implementation checklist

- [x] Standalone World registry
- [x] WorldRelease lifecycle
- [x] WorldMembership and permissions
- [x] Standalone API/UI tooling
- [x] Main Orgo operational engine removed
- [x] Interaction Kernel operational boundary removed from Orgo_Worlds
- [x] Static anti-drift validation
- [ ] Replace JSON control-plane store only if a dedicated Worlds persistence decision is made

`Signal`, `WorkflowVersion`, `Case`, `Task`, `IntegrationOperation` and the Orgo
outbox are deliberately outside this checklist because they are owned by `Orgo`.
