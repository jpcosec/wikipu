---
identity:
  node_id: "doc:wiki/drafts/critical_always_use_docmutator_tools.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md", relation_type: "documents"}
---

LLMs are literal. You MUST explicitly call the DocMutator methods — do NOT use generic OS tools (bash, echo, etc.) to write files.

## Details

LLMs are literal. You MUST explicitly call the DocMutator methods — do NOT use generic OS tools (bash, echo, etc.) to write files.

**Why?** DocMutator tools have:
- Atomic lock protection (prevents race conditions)
- Automatic path resolution
- Audit trails

**Available Tools (from `src/tools/doc_mutator.py`):**

| Tool | When to Use |
|------|-------------|
| `sync_code_to_docs(domain, stage, generated_docs)` | Template 1 |
| `implement_plan(domain, stage, plan_doc, generated_code, generated_docs)` | Template 2 |
| `draft_plan(domain, stage, plan_filename, plan_content)` | Template 3 |
| `hotfix(domain, stage, fixed_code, updated_docs, skip_docs)` | Template 4 |

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md`.