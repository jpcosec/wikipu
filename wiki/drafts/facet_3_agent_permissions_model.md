---
identity:
  node_id: "doc:wiki/drafts/facet_3_agent_permissions_model.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis.md"
  source_hash: "509baf32ca0ea70f59fdc2382e05095dde9fba07ad7092c46d49ecdca431bc34"
  compiled_at: "2026-04-10T17:47:33.732004"
  compiled_from: "wiki-compiler"
---

**Question:** What are agents explicitly allowed vs. forbidden? How is scope enforced?

## Details

**Question:** What are agents explicitly allowed vs. forbidden? How is scope enforced?

**Most sophisticated (doc_methodology) — 4 intervention templates:**

| Mode | Can write code? | Can write docs/runtime? | Can write plan/? | Notes |
|---|---|---|---|---|
| design | NO | NO | YES | Proposes architecture only |
| implement | YES | YES (promote) | NO (auto-delete) | Executes existing plan |
| sync | NO | YES (overwrite) | NO | Docs drifted behind code |
| hotfix | YES | YES (update) | NO | Bug fix, docs update mandatory |

`skip_docs=True` in hotfix creates an explicit 24-hour debt — never a silent escape.

**Lighter enforcement (cotizador):** Per-task agent_guideline files list explicit "What NOT to do" sections. Less mechanical enforcement, same intent.

**AGENTS.md approach (postulador_v2):** Convention-based: prefer small changes, follow module boundaries, update changelog for major changes, don't revive deleted legacy modules.

**Finding:** All projects enforce some version of "agents have a current mode with bounded permissions." The difference is how mechanically it's enforced. Doc_methodology's 4-template system is the most explicit and least ambiguous. The core principle is identical: **an agent always knows what it's currently allowed to touch.**

---

Generated from `raw/methodology_synthesis.md`.