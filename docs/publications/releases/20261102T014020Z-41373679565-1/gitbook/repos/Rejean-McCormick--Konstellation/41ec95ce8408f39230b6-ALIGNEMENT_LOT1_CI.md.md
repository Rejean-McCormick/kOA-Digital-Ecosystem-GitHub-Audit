<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/blob/9d4f7e74ed87b5a4c8d284dad891029d834911e4/docs/ALIGNEMENT_LOT1_CI.md | commit: 9d4f7e74ed87b5a4c8d284dad891029d834911e4 | SHA-256: b3bb9c5deff9738170ce2094ef6f689dee6739f042a6e655ac3b5cd414dfd68a -->

# Lot 1 — Reproducible CI install (2026-10-27)

The CI `fast` job now **always** runs `npm ci`. Missing or drifting `package-lock.json` is a hard failure, never a fallback to mutable `npm install`.

The locked dependency graph and Node >=24.15.0 requirement are preserved. No runtime server, renderer, access-policy, public profile, or publication code changed.

Run under Node.js >=24.15.0:

```sh
npm ci
npm test
npm run test:ui
npm run build
npm run test:e2e:smoke
```

This patch is not a release-qualification result; E2E and production deployment remain separate gates.
