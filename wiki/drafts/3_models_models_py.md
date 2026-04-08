---
identity:
  node_id: "doc:wiki/drafts/3_models_models_py.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md", relation_type: "documents"}
---

```python

## Details

```python
class FormSelectors(BaseModel):
    """All CSS selectors the adapter depends on. Validated against the live DOM before interaction."""

    # Mandatory — absence raises PortalStructureChangedError
    apply_button: str
    cv_upload: str
    submit_button: str
    success_indicator: str

    # Optional — absence is logged as warning, interaction skipped
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    phone: str | None = None
    letter_upload: str | None = None
    error_indicator: str | None = None
    cv_select_existing: str | None = None  # for portals that prefer selecting a saved CV over uploading


class ApplicationRecord(BaseModel):
    source: str
    job_id: str
    job_title: str
    company_name: str
    application_url: str
    cv_path: str
    letter_path: str | None
    fields_filled: list[str]
    dry_run: bool
    submitted_at: str | None
    confirmation_text: str | None


class ApplyMeta(BaseModel):
    status: Literal["submitted", "dry_run", "failed", "portal_changed"]
    timestamp: str
    error: str | None = None
```

---

Generated from `raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md`.