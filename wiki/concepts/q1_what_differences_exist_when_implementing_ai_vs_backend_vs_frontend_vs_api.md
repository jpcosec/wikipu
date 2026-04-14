---
identity:
  node_id: doc:wiki/concepts/q1_what_differences_exist_when_implementing_ai_vs_backend_vs_frontend_vs_api.md
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
  compiled_at: '2026-04-14T16:50:28.663320'
  compiled_from: wiki-compiler
---

Each domain has its own file layout, build sequence, and validation gate. They are not unified in any project — each extends a shared `basic.md` but defines its own rules on top.

## Definition

Each domain has its own file layout, build sequence, and validation gate.

## Examples

- Finding:

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

Each domain has its own file layout, build sequence, and validation gate. They are not unified in any project — each extends a shared `basic.md` but defines its own rules on top.

### AI / LangGraph modules

File layout:
```
contracts.py   ← schema backbone (input, output, review, persistence models)
prompt.py      ← prompt templates and variable construction only
storage.py     ← artifact paths, round management, JSON I/O only
graph.py       ← state, nodes, edges, chain wiring, Studio factory
main.py        ← CLI entry point only
```

Build sequence (order is mandatory):
1. contracts → 2. storage → 3. prompt → 4. graph (demo chain) → 5. CLI → 6. Studio → 7. real model → 8. harden

The **demo chain** is the key structural enabler — the graph must be exercisable at every step before credentials exist. Without it, testing graph topology requires live API calls.

Node taxonomy by responsibility: `load_*` (validate inputs), `run_*_llm` (only place that calls the model), `persist_*` (no logic, delegates to storage), `*_review_node` (thin breakpoint anchor), `apply_*` (validate payload, hash-check, route), `prepare_*` (context prep for regeneration).

GraphState carries only routing signals and artifact refs — never full payloads. Heavy data is on disk.

### Backend / pipeline modules (deterministic)

File layout mirrors AI but without `prompt.py`. The key distinction: deterministic functions live in `src/core/`, AI nodes live in `src/nodes/`. They never mix.

Build sequence is simpler: contracts → implementation → tests → CLI. No demo chain needed. Fail-closed is mandatory — no fallback that silently converts failure into success.

Ingestion modules (system boundary) have their own layout:
```
models.py      ← output Pydantic model (internal contract)
adapter.py     ← abstract base defining extraction contract
providers/     ← source-specific adapters
main.py        ← discovery, dispatch, idempotency check
storage.py     ← artifact paths, meta.json, idempotency state
```

Ingestion has one job: receive uncontrolled external input, validate it, produce a typed internal model. All validation at the boundary. Downstream modules never see raw input.

### Frontend / UI

Plan template structure (PhD 2.0 UI template): Spec ID + view name, Feature path, Libraries, Phase, Migration Notes, Operator Objective, Data Contract (API I/O), UI Composition and Layout (grid description with ASCII art), Styles, Files to Create, Definition of Done (checkbox list), E2E tests (TestSprite steps), Git Workflow (mandatory commit format + changelog entry + checklist update).

The UI is explicitly a **projection layer** over disk artifacts, never the source of truth. The data contract points to TypeScript types — it does not restate them. Missing data must degrade gracefully.

API endpoints follow FastAPI. They act as a data bridge to the filesystem, never as business logic. Rule from doc_methodology: "the API acts exclusively as a data bridge."

### Key cross-domain rule

Every domain follows the same contract principle: a typed Pydantic/TypeScript schema defines every boundary. The schema is the documentation. But the file layout, build sequence, and validation gates are domain-specific — not universal.

**Finding:** The methodology has a universal contract layer (schemas define all boundaries) and domain-specific implementation layer (each domain has its own file structure and build sequence). Mixing the two produces the most common drift.

---

Generated from `raw/methodology_synthesis_extended.md`.
