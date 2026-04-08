---
identity:
  node_id: "doc:wiki/drafts/4_specifications_the_formal_contracts.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/standards/feature_creation_methodology.md", relation_type: "documents"}
---

**Definition:** Defining the Pydantic models, Abstract Base Classes (ABCs), and Protocols that act as the system's internal API.

## Details

**Definition:** Defining the Pydantic models, Abstract Base Classes (ABCs), and Protocols that act as the system's internal API.

### Requirements:
- **Data Contracts:** Use Pydantic V2 models to define every data structure that passes between dimensions.
- **Interfaces:** Use ABCs or Protocols to define the "Motor" or "Provider" interfaces. 
- **Validation:** Ensure the specs handle validation and normalization (e.g., converting relative dates to ISO-8601).
- **Documentation:** The Spec *is* the documentation. Field descriptions and type hints are the authoritative source of truth.

**Goal:** To create a "lingua franca" that allows different modules to work together safely without knowing each other's internal details.

---

Generated from `raw/docs_postulador_v2/docs/standards/feature_creation_methodology.md`.