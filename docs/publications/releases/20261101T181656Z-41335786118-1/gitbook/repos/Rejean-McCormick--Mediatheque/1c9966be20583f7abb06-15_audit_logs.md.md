<!-- Frozen source: https://github.com/Rejean-McCormick/Mediatheque/blob/21e8d732e6690ab15ced87179eb5b152386fe716/docs/15_audit_logs.md | commit: 21e8d732e6690ab15ced87179eb5b152386fe716 | SHA-256: 7ab708ad76ac3c72b4a133c1dd5bd8c62e5574e961b12c68a06e34d5357f2955 -->

# 15 — Audit Logs

**Project:** Médiathèque kOA  
**Technical name:** `koa-mediatheque`  
**Status:** AI-only final target specification  
**Audience:** AI coding conversations only  
**Rule:** All implementation conversations must start from `01_alignment_variables.md`.

---

## 1. Purpose

The app is local and simple, but it must preserve enough traceability to undo mistakes and understand AI-assisted classification.

---

## 2. Events to log

```text
DB initialized
row inserted
row updated
row archived
file copied
file hash calculated
ChatGPT template copied
ChatGPT response pasted
ChatGPT response validated
ChatGPT response rejected
XLSX exported
XLSX import previewed
XLSX import applied
manifest exported
backup created
```

---

## 3. Audit entry format

```text
actor
action
entity_type
entity_uuid
before_json
after_json
note
created_at
```

---

## 4. Backup rule

Before destructive or bulk operations:

```text
copy koa_mediatheque.sqlite to 07_BACKUPS with timestamp
```
