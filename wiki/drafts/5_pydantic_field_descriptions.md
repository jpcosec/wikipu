---
identity:
  node_id: "doc:wiki/drafts/5_pydantic_field_descriptions.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/basic.md", relation_type: "documents"}
---

`Field(description=...)` is dual-purpose: read by humans and consumed by LLMs. Write it accordingly — semantic, specific, with examples for ambiguous values.

## Details

`Field(description=...)` is dual-purpose: read by humans and consumed by LLMs. Write it accordingly — semantic, specific, with examples for ambiguous values.

```python
responsibilities: list[str] = Field(
    description="Job responsibilities ('Deine Aufgaben', 'Your Impact'). Extract as short action phrases."
)
```

Mark MANDATORY vs OPTIONAL fields in class-level comments. For LLM-consumed schemas, keep descriptions accurate — stale descriptions cause silent extraction errors.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/basic.md`.