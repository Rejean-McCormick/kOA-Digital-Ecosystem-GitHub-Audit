<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Query-Algebra-and-Planning | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: aa1a88ade57a84518e46bd188b0e156a875fdc3a0018f271cb234b9b87c4889c -->

# Query Algebra and Planning

KQP uses a typed algebra so different engines can execute the same semantic request without interpreting arbitrary JSON differently.

## Core operators

A conforming engine should normalize supported requests into operations equivalent to:

```text
RESOLVE(roots)
SCOPE(namespaces, kristals, shards, sources)
TRAVERSE(direction, properties, depth, limits)
FILTER(status, role, time, source, property)
EVIDENCE(closure, depth)
PROJECT(fields, encoding)
PAGE(cursor, size)
```

Mode names are conveniences over this algebra. Engines may optimize execution order but must preserve declared semantics.

## Cost-based planning

Implementations may choose indexes or shard order based on estimated cost. Planning metadata should expose indexes used, shards contacted and limits applied. Optimization must not silently broaden filters or change semantic meaning.

## Validation pipeline

```text
parse
 ↓
schema validation
 ↓
semantic validation
 ↓
capability / scope validation
 ↓
budget normalization
 ↓
plan
 ↓
execute
```

Schema validity alone does not prove semantic validity, authorization or capability support.
