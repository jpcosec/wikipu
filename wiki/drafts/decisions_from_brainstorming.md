---
identity:
  node_id: "doc:wiki/drafts/decisions_from_brainstorming.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

- **CvGraphEditor is eliminated.** Its capabilities are requirements for the NodeEditor. Step 00b maps every feature to its new home.

## Details

- **CvGraphEditor is eliminated.** Its capabilities are requirements for the NodeEditor. Step 00b maps every feature to its new home.
- **elkjs from the start.** No dagre. Compound/nested layout natively.
- **Library-first, no speculative abstraction.** Use React Flow, elkjs, zustand, FlexLayout, RJSF directly. No wrapper modules for hypothetical portability.
- **Representation Schema** — per-project YAML/JSON config that maps neo4j graph structure to editor behavior (node types, containment, relations, visual mappings, views). The editor is domain-agnostic by configuration.
- **CSS Theme** — Obsidian-style overridable CSS. Schema sets `data-*` attributes, CSS targets them. MD3 token system as default theme (Manrope + Inter, glass panels, dot grid).
- **Color scales** — schema declares scales as defaults, CSS overrides win.
- **Extension Model** — one `registry.register()` pattern for every extension type. Built-in features use the same API. 10 extension types.
- **Panel docking** — user-configurable via FlexLayout-react. Left/right/float, saved per view preset.
- **Schema-driven inspector** — RJSF renders forms from representation schema attributes compiled to JSON Schema.
- **Performance** — render tiers (only focused node gets expensive renderer), prerender cache, background precomputation, compiled registry lookup tables (O(1) at render time).
- **Testing** — ideal approach: Vitest (unit), @testing-library/react (component), Playwright (integration). Bootstrap from scratch.
- **Gap analysis** — inline per step + consolidated gap matrix.
- **Library decisions** — decision matrix per choice point with recommendation + switch trigger.

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.