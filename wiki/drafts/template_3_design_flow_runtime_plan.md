---
identity:
  node_id: "doc:wiki/drafts/template_3_design_flow_runtime_plan.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md", relation_type: "documents"}
---

**Use when:** You want the agent to propose architecture, refactor, or UI design WITHOUT touching working code.

## Details

**Use when:** You want the agent to propose architecture, refactor, or UI design WITHOUT touching working code.

### Coordinates

- Domain: `[INSERT_DOMAIN]`
- Stage: `[INSERT_STAGE]`
- Design requirement: `[DESCRIBE_WHAT_YOU_WANT, e.g. "Add bulk regeneration button"]`

### Execution

1. `fetch_context(domain='[DOMINIO]', stage='[STAGE]', state='runtime', include_code=True)` — understand current system
2. Create a detailed technical proposal solving the "Design requirement"
3. **Call the tool**: `draft_plan(domain='[DOMINIO]', stage='[STAGE]', plan_filename='proposal_name.md', plan_content='# Proposal\n...')`

### Rules

- Write to `plan/[DOMAIN]/` ONLY
- NEVER modify source code (`.py`, `.tsx`)
- NEVER modify files in `docs/runtime/` or `docs/ui/`

### Postcondition

```
plan/[DOMAIN]/[PROPOSAL].md → CREATED via draft_plan()
code → UNCHANGED
docs/runtime/ → UNCHANGED
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md`.