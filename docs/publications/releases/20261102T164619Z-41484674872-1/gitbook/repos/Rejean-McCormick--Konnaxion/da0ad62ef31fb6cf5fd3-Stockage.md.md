<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion/wiki/Stockage | commit: 62c3bb451bacb4cfbbeb68181c1edfc7ba47a8f9 | SHA-256: b871781be7f0c120748524bf83997bf0ce327125428f76b2d1f7e3dac62235e0 -->

# Stockage — keenKonnect Knowledge and Project Resources

Stockage is the project/document repository capability inside **keenKonnect**. It is not a separate system or database owner.

Current physical owner:

```text
backend/konnaxion/keenkonnect/
```

## Current core objects

- `ProjectResource` — resource/document reference attached to a project;
- `Project` — project/workspace context;
- `ProjectTeam` — membership/role context;
- `Tag` — classification.

## Current UI

The current product exposes knowledge/document surfaces under:

```text
/keenkonnect/knowledge/browse-repository
/keenkonnect/knowledge/document-management
/keenkonnect/knowledge/search-filter-documents
/keenkonnect/knowledge/upload-new-document
```

## Ownership

A search index, preview, cache or document browser remains a projection over the resource owner. It does not become a second source of project/document truth.

Do not invent versioning/ACL persistence tables unless they exist in the code/schema being updated.
