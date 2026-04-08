---
identity:
  node_id: "doc:wiki/drafts/template_2_implement_flow_plan_code_docs.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md", relation_type: "documents"}
---

**Use when:** An existing design document lives in `plan/` and you want the agent to write real code.

## Details

**Use when:** An existing design document lives in `plan/` and you want the agent to write real code.

### Coordinates

- Domain: `[INSERT_DOMAIN]`
- Stage: `[INSERT_STAGE]`
- Plan to implement: `[PLAN_FILENAME, e.g. B2_extract_understand.md]`

### Execution

1. `fetch_context(domain='[DOMINIO]', stage='[STAGE]', state='plan')` — read target design
2. `fetch_context(domain='[DOMINIO]', stage='[STAGE]', state='runtime', include_code=True)` — understand base state
3. Write code to fulfill EXACTLY what the plan demands
4. **Call the tool**: `implement_plan(domain='[DOMINIO]', stage='[STAGE]', plan_doc='plan/[DOMAIN]/[FILENAME]', generated_code={'src/file.tsx': 'code'}, generated_docs={'docs/runtime/path.md': 'doc'})`

### Rules

- Code MUST match plan specifications exactly
- **Use implement_plan tool** — it automatically deletes the plan after success
- Do NOT manually delete files

### Postcondition

```
plan/[DOMAIN]/[PLAN] → DELETED automatically by implement_plan()
code → CREATED/MODIFIED
docs/runtime/ → PROMOTED automatically by implement_plan()
```

### ⚠️ Permission Fix

The phrase "recommend (or execute) deletion" is **broken**. Use `implement_plan()` — it handles deletion automatically.

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md`.