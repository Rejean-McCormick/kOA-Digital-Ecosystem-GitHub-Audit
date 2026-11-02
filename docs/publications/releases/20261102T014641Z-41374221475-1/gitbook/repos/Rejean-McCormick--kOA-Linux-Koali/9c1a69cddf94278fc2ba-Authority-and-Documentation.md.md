<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Authority-and-Documentation | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: 780fadb0b7d9e03f2c7d032a7ff6af5e46d7f124bdf648015c505fecb47c8187 -->

<!-- Navigational projection. Normative authority remains in the repository docs/ corpus. -->

# Authority and Documentation

> **Authority notice:** This wiki is a readable navigation layer. Source contracts, accepted ADRs, normative documents, and executable validators in the repository remain authoritative.

## Contract-first architecture

The documentation system is contract-first. Source contracts and focused explanatory documents own facts. Catalogs, indexes, matrices, manifests, and AI context packages are generated projections.

## Authority order

| Layer | Responsibility |
| --- | --- |
| Accepted decisions | Close significant architectural choices |
| Source contracts | Own machine-readable system, component, profile, subsystem-boundary, integration, toolchain, and artifact facts |
| Normative source documents | Explain requirements and procedures within their declared scope |
| Executable validators | Enforce identities, schemas, references, boundaries, generated consistency, and release gates |
| Generated outputs | Support discovery only; never override a source |
| Recipes and examples | Provide bounded non-authoritative implementation guidance |

## Scope discipline

Authority remains explicit across global, profile, component, subsystem-boundary, integration, artifact, and recipe scopes. A narrower source cannot silently become global.

## Subsystem authority

Mounted subsystem documentation owns internal product behavior. kOA boundary contracts own deployment, resources, lifecycle, trust, health, storage exposure, artifact admission, and cross-subsystem interactions.

Missing, conflicting, or unresolved authority blocks the affected activation. No undeclared replacement is selected.

## Generated navigation

Generated files under `docs/generated/` are disposable and rebuildable. Do not edit them manually.

```bash
python docs/tools/build_indexes.py
python docs/tools/build_ai_context.py
python docs/tools/check_generated_content.py
```

## AI reading order

1. [`docs/AI_CONTEXT.md`](../blob/main/docs/AI_CONTEXT.md)
2. [`docs/contracts/ai-navigation.contract.json`](../blob/main/docs/contracts/ai-navigation.contract.json)
3. applicable source contract;
4. applicable kOA boundary page;
5. mounted subsystem documentation when internal behavior is needed;
6. generated indexes for discovery only.

## Sources

- [`docs/00-governance/00-documentation-architecture.md`](../blob/main/docs/00-governance/00-documentation-architecture.md)
- [`docs/00-governance/01-authority.md`](../blob/main/docs/00-governance/01-authority.md)
- [`docs/00-governance/08-generated-content-policy.md`](../blob/main/docs/00-governance/08-generated-content-policy.md)
- [`docs/00-governance/09-canonical-ownership.md`](../blob/main/docs/00-governance/09-canonical-ownership.md)
- [`docs/00-governance/13-validation-pipeline.md`](../blob/main/docs/00-governance/13-validation-pipeline.md)
- [`docs/contracts/ai-navigation.contract.json`](../blob/main/docs/contracts/ai-navigation.contract.json)
