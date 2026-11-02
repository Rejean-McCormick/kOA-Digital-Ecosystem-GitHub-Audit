<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/blob/381ab137d087794ffcb381532c7d2eabcdd60bb5/docs/Technical-Reference/HowToStartAndEnter.txt | commit: 381ab137d087794ffcb381532c7d2eabcdd60bb5 | SHA-256: 6ee6b34a37c4cf697a7b5b4279e97920fa2a2255dd31f300d0629bbd1728ecb4 -->

Orgo current local startup (2026-09-15)

Requirements:
- Node.js 22+
- npm
- PostgreSQL 16 when exercising database-backed behavior

1. From the repository root:

   npm ci

2. Start the API in terminal A:

   npm run dev:api

   Default API port: 4000
   API base: http://localhost:4000/api/v3
   Readiness: http://localhost:4000/health/ready

3. Start the web application in terminal B:

   npm run dev:web

   Web UI: http://localhost:3000/

   When needed, set ORGO_API_URL=http://127.0.0.1:4000 for the web runtime before starting it.

4. There is no active root `npm run dev` script in the current workspace. Use `dev:api` and `dev:web`, or run `npm run dev -w api` / `npm run dev -w web` directly.

5. The active API does not currently expose Swagger at `/docs`. Use `docs/Technical-Reference/API_IMPLEMENTED.md` for the implemented route inventory.

6. Validation:

   Repository-local: npm run validate:local
   Comprehensive external diagnostic: LevelUpDiag-Orgo `deep`, plus `browser` for Chromium acceptance.

Historical Yarn Classic / Turborepo / NPS / port-5002 instructions do not describe the active Orgo workspace.
