<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Toolchain-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: bab5220b2ebd02f923a44a4b470cc59810e6dcf2fc039957af426673b9234077 -->

# Toolchain Responsibilities — v10 / draft.3

| Component (snapshot) | Responsibility | Boundary |
| --- | --- | --- |
| **Kristal Framework** `10.0.0-draft.3.2` | Normative contracts, reference JS, v10 GitHub profile, Reader Discovery companion | Does not make hosting part of semantic state |
| **Local/Authoring Kit** `3.3.0` | Workspace, canon, sources, validation, v9 builds, optional AI capsule and exact `read-surface` output and noncanonical reader discovery/size profiles | Does not own GitHub node publication/activation |
| **Kristal Manager** `0.1.0-alpha.11` | Local inventory/validation and exact GitHub reader Sync; derived collection index | `SYNC != PUBLICATION` |
| **GitHub Bootstrap / Setup** `1.1.0-alpha.10` | Declarative node/collection infrastructure, qualify, immutable publish, activate | Does not define v9 logical commitments |
| **KristalDiag** (v10 examiner snapshot) | Independent read-only conformance and release qualification | PASS is evidence only; snapshot README pinned to draft.2 |
| **Kompiler** (optional) | Read/query/context compilation | No semantic authoring or canonical lifecycle authority |

## One workflow, different authorities

```text
sources → Local Kit [canon, state, local validation]
                       │
               Manager [GitHub read sync]
                       │
         Bootstrap/Setup [qualify / publish / activate]
                       │
           Reader/Kompiler [read/query/context]

KristalDiag independently examines contracts/evidence.
```

Source adoption is explicit: a source repository or library is not automatically canonical knowledge.

**Snapshot caution:** documentation and pinned tool builds can lag the Framework proposed standard. Confirm actual profile coverage for your target version; do not infer full draft.3 conformance from a draft.2 lock.

See [[Workflow-GitHub-v10]], [[Conformance-v10]] and [[Status-v10]].

Additional reader-discovery path: Arketype 1.4 -> Local Kit 3.3.0 -> Framework 10.0.0-draft.3.2 -> external parser adapter. See [[Reader-Discovery-and-Arketype-v10]].
