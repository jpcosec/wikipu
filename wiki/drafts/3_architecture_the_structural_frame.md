---
identity:
  node_id: "doc:wiki/drafts/3_architecture_the_structural_frame.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/standards/feature_creation_methodology.md", relation_type: "documents"}
---

**Definition:** Translating the conceptual dimensions into a physical directory and module hierarchy.

## Details

**Definition:** Translating the conceptual dimensions into a physical directory and module hierarchy.

### Requirements:
- **Map Dimensions to Folders:** Create a directory structure that reflects the orthogonalized dimensions.
- **Establish Legal Ownership:** Define exactly what type of logic is allowed in each directory.
- **Create Scaffolding:** Build the package root and the primary sub-packages (e.g., `motors/`, `portals/`, `ariadne/`).
- **Define Entrypoints:** Establish the main CLI or API surface that orchestrates the internal modules.

**Goal:** To eliminate ambiguity about where a piece of code belongs and to prevent "logic leakage" between layers.

---

Generated from `raw/docs_postulador_v2/docs/standards/feature_creation_methodology.md`.