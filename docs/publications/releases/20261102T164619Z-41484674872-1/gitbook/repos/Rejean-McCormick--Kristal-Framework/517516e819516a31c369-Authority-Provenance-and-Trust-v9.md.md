<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Authority-Provenance-and-Trust-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 3409c1733c1b687ccd00349e51116b8bbcbfd14eff56a0be87ed69d26726d07c -->

# Authority, Provenance and Trust — v9

V9 introduces more derived and physical artifacts, so authority boundaries must remain explicit.

## Four separate questions

```text
INTEGRITY != AUTHENTICITY != AUTHORITY != FACTUAL CORRECTNESS
```

- **Integrity**: do bytes/logical content match a declared digest?
- **Authenticity**: did a particular key sign an object?
- **Authority**: is that signer/source recognized for this scope?
- **Factual correctness**: is the knowledge actually correct?

No one layer automatically proves the others.

## Epistemic provenance

Explains where knowledge came from, what evidence supports it and how it should be interpreted.

## Build provenance

Explains how software produced an artifact:

```text
source commitments
transform
configuration
policies
toolchain
```

A builder does not become an epistemic authority merely by computing an artifact.

## Publication/activation provenance

Publishing or activating a State Snapshot can be recorded independently from the state content itself.

## Composition

```text
STATE COMPOSITION != AUTHORITY MERGE
```

This matters in systems such as HospitalOps where commons, practice facts, identity vaults and audit systems deliberately retain separate authority and security domains.
