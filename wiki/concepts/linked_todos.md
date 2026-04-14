---
identity:
  node_id: doc:wiki/concepts/linked_todos.md
  node_type: concept
edges:
- target_id: raw:raw/methodology_synthesis_extended.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/methodology_synthesis_extended.md
  source_hash: 0eaf49dde8b77f6999c8e390207549968bc290d82d4774999f7136fecc61fb30
  compiled_at: '2026-04-14T16:50:28.663514'
  compiled_from: wiki-compiler
---

- `src/path/to/file.py` — `# TODO(future): description`

## Definition

- `src/path/to/file.

## Examples

- `src/path/to/file.py` — `# TODO(future): description`
- **Hardening roadmap** — known fragility in a module, not urgent enough to plan now
- **New feature** — wanted capability, not yet scheduled
- **Issues / conflicts** — known system inconsistencies (logging conflicts, overlapping responsibilities)
- **Product standards** — expected future policies that haven't been formalized

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

- `src/path/to/file.py` — `# TODO(future): description`
```

Types found in practice:
- **Hardening roadmap** — known fragility in a module, not urgent enough to plan now
- **New feature** — wanted capability, not yet scheduled
- **Issues / conflicts** — known system inconsistencies (logging conflicts, overlapping responsibilities)
- **Product standards** — expected future policies that haven't been formalized

Stale threshold: 6 months. A future_docs entry is either promoted, deleted, or re-dated. No exceptions.

### plan_docs/ — Active execution

Two templates coexist (backend and UI):

**Backend plan mandatory sections:** Problem Statement, State Contract (current + required state.json), Core Functions affected, Node Implementation (affected nodes + edge transitions), HITL Requirements, API Endpoints (if any), File Changes Summary, Dependencies, Testing Strategy, Rollback Plan.

**UI plan mandatory sections:** Spec ID + coordinates, Migration Notes (legacy source to extract), Operator Objective, Data Contract (API I/O), UI Composition + Layout (ASCII grid), Styles, Files to Create, Definition of Done (checkbox), E2E (TestSprite steps), Git Workflow (commit format + changelog + checklist update).

**Lightweight plan (cotizador agent_guideline):** Context, numbered steps, "What NOT to do". Used for small feature-scoped tasks where the full template is overhead.

Common to all plan types:
- What this solves
- Explicit negative constraints ("What NOT to do")
- Ordered steps
- File changes map
- Verification criteria

Plans are ephemeral — deleted when work is done.

### docs/ — Persistent reference

Types found across projects:

| Type | Content | Examples |
|---|---|---|
| **standards/code/** | Universal and domain-specific code rules | `basic.md`, `llm_langgraph_components.md`, `ingestion_layer.md` |
| **standards/docs/** | Documentation conventions, checklists, lifecycle rules | `documentation_and_planning_guide.md`, `documentation_quality_checklist.md`, `future_docs_guide.md` |
| **runtime/** | Current technical truth for each domain/stage | `graph_flow.md`, `data_management.md`, `pipeline_overview.md` |
| **reference/** | Schemas, contracts, node matrices, artifact specs | `graph_state_contract.md`, `artifact_schemas.md`, `node_io_target_matrix.md` |
| **operations/** | Runbooks, known issues, diagnostic patterns | `agent_planning_and_verification_pattern.md`, `tool_interaction_and_known_issues.md` |
| **index/** | Navigation maps, conceptual trees, canonical paths | `canonical_map.md`, `conceptual_tree.md` |
| **adrs/** | Architecture decision records | `002_documentation_consolidation.md` |

Rule from doc_methodology: `docs/runtime/` can be referenced by `plan/` but NEVER the reverse. Current truth must not point forward to uncommitted future.

---

Generated from `raw/methodology_synthesis_extended.md`.
