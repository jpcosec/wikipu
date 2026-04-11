---
identity:
  node_id: "doc:wiki/drafts/q3_what_standards_rules_documents_exist_is_there_a_consistent_structure.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/methodology_synthesis_extended.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis_extended.md"
  source_hash: "0eaf49dde8b77f6999c8e390207549968bc290d82d4774999f7136fecc61fb30"
  compiled_at: "2026-04-10T17:47:33.733201"
  compiled_from: "wiki-compiler"
---

**Standards documents across projects follow this structure:**

## Details

**Standards documents across projects follow this structure:**

1. **Title** — domain + what this governs
2. **Extension declaration** — "Extends basic.md" or "Extends llm_langgraph_components.md" — explicit layering, not self-contained
3. **Numbered sections**, each with: rule statement + code example + rationale
4. **Reference implementation** pointer — a real module that exemplifies the standard

**Hierarchy observed:**

```
basic.md                         ← universal (all Python modules)
  ├── llm_langgraph_components.md    ← AI/LangGraph specific
  │     └── llm_langgraph_methodology.md  ← process guide for the above
  ├── ingestion_layer.md             ← boundary components
  └── deterministic_tools.md        ← (referenced, not read)
```

UI standards follow the same layering pattern but in TypeScript. Architecture principle docs (cotizador's `design-principles.md`) have a different structure: numbered principles, each with a statement + elaboration + "no layer should X" negative constraint.

**Consistent elements across all standards:**
- Rule statements are declarative, not procedural ("the output model is the boundary" not "you should try to make the output model the boundary")
- Every rule has an anti-pattern shown or implied
- Code examples are specific and copy-pasteable
- Rules are organized from most universal to most specific

**Missing from every project:** A single index of all standards documents. Each project has a `practices/README.md` pointing to the files, but no cross-project or cross-domain standards map. The relationships between standards (what extends what) are declared in-file, not in a registry.

---

Generated from `raw/methodology_synthesis_extended.md`.