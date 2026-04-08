---
identity:
  node_id: "doc:wiki/drafts/9_product_logic_the_designer_must_understand.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/review_workbench_product_brief.md", relation_type: "documents"}
---

### A. This is not a generic graph app

## Details

### A. This is not a generic graph app

The graph is not decorative. It is a human-review representation of machine-generated application logic.

There are three semantic spaces:

1. source document understanding
2. requirement-to-evidence matching
3. graph-to-document grounding

The UI should help the user move between those spaces.

### B. Human review is mandatory, not optional

This product assumes model output is useful but not final.

Therefore the UX should support:

1. inspection
2. correction
3. confidence building
4. provenance visibility

### C. Local artifact visibility is a feature, not a hack

Being able to see:

- the source text
- the extracted state
- the match state
- generated markdown
- scrape screenshots

is part of the product value because it keeps the system auditable.

### D. Deterministic evidence linking matters

The designer should assume the product wants a reliable link between source text and structured evidence.

Important principle:

- the system should not invent text coordinates
- it should link evidence by matching real text fragments in the stored source text

In design terms, this means the UI needs room for:

1. source text highlighting
2. evidence snippets
3. visible grounding relationships
4. graceful handling when a quote cannot be resolved

Generated from `raw/docs_postulador_langgraph/docs/ui/review_workbench_product_brief.md`.