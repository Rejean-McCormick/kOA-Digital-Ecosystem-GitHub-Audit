<!-- Frozen source: https://github.com/Rejean-McCormick/Kompiler/blob/cf4836ccf2741b609c562254d09ba47d7e9a6187/docs/09-reference/adapter-manifests.md | commit: cf4836ccf2741b609c562254d09ba47d7e9a6187 | SHA-256: f1c3b2c5dd0ed76e49df2d2702aef980050d4e6df543636f01cc1d9f197fb0c5 -->

# Adapter Manifest Reference

A manifest is administrator-controlled configuration. Query Plans cannot modify it.

```toml
id = "kristal-humanbody"
version = "1.0.0"
target_id = "HumanBody"
kind = "kristal"

[source]
root = "/absolute/path/to/Kristal-HumanBody/knowledge-base"

[implementation]
type = "kristal-humanbody"
```

Register manifests from `kompiler.toml`:

```toml
[adapters.humanbody]
manifest = "~/.config/kompiler/adapters/humanbody.toml"
```

For temporary explicit development roots, `KOMPILER_KRISTAL_ROOTS` may contain an OS-path-separator-delimited list. Those roots are signature-detected but source scripts are not executed during discovery.

## Kristall v7 manifest

A v7 meta-plane target uses `kind = "kristall"` and the built-in `kristall-v7` implementation:

```toml
id = "kristall-v7"
version = "1.0.0"
target_id = "Kristall:kristall-main"
kind = "kristall"

[source]
root = "/absolute/path/to/Kristall-v7-deployment"

[implementation]
type = "kristall-v7"
```

The source root must contain or resolve a v7 `kristall_manifest`. Discovery may expose both this meta-plane target and nested source Kristals.
