---
identity:
  node_id: "doc:wiki/drafts/7_runtime_validation_two_layers.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md", relation_type: "documents"}
---

### Layer 1 — `_validate_selectors(selectors)` (after Step 1, before file upload)

## Details

### Layer 1 — `_validate_selectors(selectors)` (after Step 1, before file upload)

Runs a dedicated `arun()` call with `js_only=True` and a `js_code` snippet that queries every non-None selector and returns a presence map:

```javascript
JSON.stringify({
    apply_button: !!document.querySelector('...'),
    cv_upload: !!document.querySelector('...'),
    submit_button: !!document.querySelector('...'),
    // ... all selectors
})
```

The base class parses `result.extracted_content`, checks the map:
- **Mandatory selector absent** → `PortalStructureChangedError` with full list of missing selectors → error screenshot → `apply_meta.json` with `status=portal_changed`
- **Optional selector absent** → `LogTag.WARN`, field skipped, execution continues

### Layer 2 — `_validate_success_text(result)` (after submit)

Checks `result.markdown` or `result.cleaned_html` for the `get_success_text()` fragment:
- Not found → `LogTag.WARN` only (copy changes are common, not structural failures)
- Found → confirms submission is complete

Both results are persisted in `apply_meta.json` and visible in logs with structured tags.

---

Generated from `raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md`.