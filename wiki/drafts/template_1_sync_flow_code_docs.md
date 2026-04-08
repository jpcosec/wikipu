---
identity:
  node_id: "doc:wiki/drafts/template_1_sync_flow_code_docs.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md", relation_type: "documents"}
---

**Use when:** You wrote code manually or AI generated code, and runtime documentation is outdated.

## Details

**Use when:** You wrote code manually or AI generated code, and runtime documentation is outdated.

### Coordinates

- Domain: `[INSERT_DOMAIN, e.g. ui]`
- Stage: `[INSERT_STAGE, e.g. match]`

### Execution

1. `fetch_context(domain='[DOMINIO]', stage='[STAGE]', state='runtime', include_code=True)`
2. Analyze the source code provided in context
3. Analyze the corresponding Markdown doc in `docs/runtime/` or `docs/ui/`
4. Rewrite the Markdown to reflect STRICTLY the code reality
5. **Call the tool**: `sync_code_to_docs(domain='[DOMINIO]', stage='[STAGE]', generated_docs={'docs/path.md': 'rewritten content'})`

### Rules

- Do NOT speculate about future features
- Remove any mention of features that no longer exist in code
- Do NOT modify source code (only docs)

### Postcondition

```
docs/runtime/[DOMAIN]/[STAGE].md → UPDATED via sync_code_to_docs()
code → UNCHANGED
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md`.