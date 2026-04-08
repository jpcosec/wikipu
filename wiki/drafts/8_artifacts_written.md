---
identity:
  node_id: "doc:wiki/drafts/8_artifacts_written.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md", relation_type: "documents"}
---

```

## Details

```
data/jobs/<source>/<job_id>/nodes/apply/
  proposed/
    application_record.json   # filled fields, cv path, submitted_at, confirmation text
    screenshot.png            # state just before submit (dry-run and auto)
    error_state.png           # written only on exception — for debugging
  meta/
    apply_meta.json           # status, timestamp, error
```

Running in auto mode after a dry-run overwrites all artifacts — the dry-run state is not preserved. This is intentional: `status=dry_run` in `apply_meta.json` does not block re-execution (see idempotency rules in Section 5). If a dry-run reference needs to be kept, copy the artifacts manually before running in auto mode.

---

Generated from `raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md`.