---
identity:
  node_id: "doc:wiki/drafts/2_orthogonalize_dimensions_conceptual_decoupling.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/standards/feature_creation_methodology.md", relation_type: "documents"}
---

**Definition:** Identifying the independent axes of the feature and drawing "hard boundaries" between them.

## Details

**Definition:** Identifying the independent axes of the feature and drawing "hard boundaries" between them.

### Requirements:
- **Separate Concerns:** Identify the distinct dimensions of the problem. Typical dimensions include:
    - **Mechanisms (The "How"):** Execution engines, third-party libraries, transport layers.
    - **Domain Knowledge (The "Where/Who"):** Site-specific logic, source definitions, portal-level intent.
    - **State & Knowledge (The "What"):** Playbooks, schemas, traces, persistent history.
    - **Orchestration (The "When"):** The high-level workflow or graph that coordinates the other dimensions.
- **Enforce Boundaries:** Define a rule that Dimensions must remain decoupled. A change in "The How" (e.g., switching a library) should never require a change in "The Where" (site-specific logic).

**Goal:** To create a system where independent parts can evolve at different speeds without side effects.

---

Generated from `raw/docs_postulador_v2/docs/standards/feature_creation_methodology.md`.