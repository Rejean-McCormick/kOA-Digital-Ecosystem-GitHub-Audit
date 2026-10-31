<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Host-Bindings-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: e933ec65a34cd9745e4d6bf1904a7aa9661f1ce0fb5570e2c006d1bae8fe3e79 -->

# Host Bindings — v10

A `kristal_host_binding` connects a stable Kristal `node_id` to a concrete host. Hosting metadata is replaceable and must not redefine the v9 state.

The generic binding carries a stable `binding_id`, host profile/version, account scope, primary host resource and optional source, publication, activation, materialization, attestation, automation and discovery surfaces.

```text
node_id ─── binding A → GitHub repository
       ├── binding B → object-storage mirror
       └── binding C → offline archive
```

## Rules

- **No reusable credentials** (tokens, keys or passwords) inside a Host Binding.
- Host-specific repository paths, URLs, branch names and release IDs are not included in v9 logical/state commitments unless a domain contract explicitly defines them as logical data.
- Rehosting or mirroring alone does not create a logical revision.
- `kristal.host/github/1.0` is an **optional** reference profile, not the only conforming host.

See [[GitHub-Reference-Profile-v10]], [[Security-and-Confidentiality-v10]] and [[Compatibility-v9-v10]].

*Normative source: Framework `spec/v10/Host-Bindings.md`.*
