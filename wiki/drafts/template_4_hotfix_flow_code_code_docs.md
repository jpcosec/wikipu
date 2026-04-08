---
identity:
  node_id: "doc:wiki/drafts/template_4_hotfix_flow_code_code_docs.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md", relation_type: "documents"}
---

**Use when:** There's a bug, linting error, or you need AI to fix something quickly based on current business rules.

## Details

**Use when:** There's a bug, linting error, or you need AI to fix something quickly based on current business rules.

### ⚠️ CRITICAL FIX

**OLD (BROKEN) RULE**: "docs → UNCHANGED after hotfix"

This guaranteed documentation drift. After 5 hotfixes, Context Router breaks.

**NEW RULE**: Docs MUST be updated after every code change.

### Coordinates

- Domain: `[INSERT_DOMAIN]`
- Stage: `[INSERT_STAGE]`
- Problem: `[DESCRIBE_BUG, e.g. "span_resolver fails on multiline text offsets"]`

### Execution

1. `fetch_context(domain='[DOMINIO]', stage='[STAGE]', state='runtime', include_code=True)`
2. Read the documentation to understand the business contract the code MUST fulfill
3. Analyze source code to find the problem origin
4. Modify ONLY the source code strictly necessary to fix the issue
5. **Call the tool**: `hotfix(domain='[DOMINIO]', stage='[STAGE]', fixed_code={'src/file.py': 'fixed code'}, updated_docs={'docs/runtime/path.md': 'updated doc'})`

### Rules

- Modify ONLY the code strictly necessary to resolve the problem
- Ensure your fix doesn't violate rules in the documentation
- **ALWAYS update docs after code change** (no exceptions)
- Use `skip_docs=True` ONLY for critical production emergencies

### Postcondition

```
code → MODIFIED via hotfix()
docs/runtime/ → UPDATED via hotfix()
```

### Emergency Exception

If `skip_docs=True`, code is fixed but docs remain unchanged. This is a **debt**: must be resolved within 24 hours via `sync_code_to_docs()`.

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md`.