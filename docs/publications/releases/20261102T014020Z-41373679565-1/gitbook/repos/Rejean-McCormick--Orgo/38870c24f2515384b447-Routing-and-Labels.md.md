<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/wiki/Routing-and-Labels | commit: b89ca31f268c521cbd70ab1c736338a8c5039df7 | SHA-256: 2431441d5a285f0d5a0e27c122c512db75275e27c35eee4612acb51a9f594f8e -->

# Routing and Labels

Orgo uses **Labels** as a compact routing and classification language.

A label can express three things:

1. a vertical or organizational scope;
2. a category and subcategory;
3. an optional horizontal role.

The general form is:

```text
<BASE>.<CATEGORY><SUBCATEGORY>[.<HORIZONTAL_ROLE>]
```

Example:

```text
100.94.Operations.Safety
```

The precise codes are configured and documented technically, but public users mainly need to understand the idea: **a label is an address for operational context**.

## Labels are not permissions

A label can help determine where work belongs, but it does not replace authorization.

Seeing a routing label does not automatically grant access to the underlying Case or Task.

## One canonical routing label

Orgo keeps one canonical routing label on the work object rather than trying to encode every possible taxonomy dimension into one string.

Additional classification can live in metadata, tags or domain-specific structures.

## Broadcast labels

Some label bases represent broadcasts.

A broadcast is informational by default:

```text
broadcast
≠ mandatory Task
```

If the information requires action, a workflow must explicitly create or assign that work.

This prevents announcements from silently becoming obligations.
