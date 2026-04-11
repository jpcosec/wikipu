---
identity:
  node_id: "doc:wiki/drafts/facet_1_plan_anatomy.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis.md"
  source_hash: "509baf32ca0ea70f59fdc2382e05095dde9fba07ad7092c46d49ecdca431bc34"
  compiled_at: "2026-04-10T17:47:33.731916"
  compiled_from: "wiki-compiler"
---

**Question:** What sections does a well-formed plan always contain?

## Details

**Question:** What sections does a well-formed plan always contain?

**What the projects show:**

- **postulador_langgraph** has the most complete format: TL;DR, Context, Objectives, Must have / Must not have, Verification strategy, Execution waves, Dependency matrix, Task checklist, Final verification wave.
- **doc_methodology** planning templates (UI and backend) use: Problem Statement, State Contract, Core Functions, Node Implementation, HITL Requirements, File Changes Summary, Dependencies, Testing Strategy, Rollback Plan.
- **cotizador** uses lighter agent_guideline files: Context, numbered steps, "What NOT to do".
- **postulador_refactor** documentation guide says: goal, constraints, ordered steps, open questions.

**Common core across all:**

Every well-formed plan always contains:
1. **What problem this solves** (one paragraph, mandatory)
2. **What is out of scope / must not happen** (explicit negative constraints)
3. **Ordered steps**, each narrow enough to verify independently
4. **File changes map** (what gets created, modified, deleted)
5. **Verification** — per-step or at the end, never absent

**What varies:** depth of state contracts, rollback plans, HITL gates. These are domain-specific extensions, not universal.

**Finding:** The lightest valid plan is: problem, constraints, steps, file map, verification. Everything else is specialization.

---

Generated from `raw/methodology_synthesis.md`.