---
identity:
  node_id: "doc:wiki/concepts/q5_is_the_human_considered_in_the_overall_loop.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis_extended.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis_extended.md"
  source_hash: "0eaf49dde8b77f6999c8e390207549968bc290d82d4774999f7136fecc61fb30"
  compiled_at: "2026-04-14T16:50:28.663672"
  compiled_from: "wiki-compiler"
---

Yes, and it's a core design assumption, not an afterthought.

## Details

Yes, and it's a core design assumption, not an afterthought.

**postulador / PhD 2.0** has the most explicit human model:

HITL (Human-in-the-Loop) is payload-driven, not acknowledgement-driven. The human makes an **explicit semantic decision per row** (approve / request_regeneration / reject) and submits a typed `ReviewPayload`. Pressing "Continue" without a payload is a safe no-op — the system handles it explicitly, not as an error.

Human responsibilities (from `llm_langgraph_components.md`):
- Inspect the review surface (`review/current.json`)
- Make an explicit semantic decision per row
- Provide patch evidence when requesting regeneration
- Submit a typed ReviewPayload, not just pressing Continue

System responsibilities:
- Pause at the right moment (`interrupt_before` the review node)
- Persist the review surface before pausing
- Validate payload shape and hash on resume
- Reject stale payloads (hash mismatch)
- Route deterministically from the payload — never guess intent
- Handle bare-Continue as a safe no-op

**Git hooks put the human at the merge gate:**
- Requires 1+ human approval on every PR before merge
- Even admins must follow branch protection rules
- CI must pass before human review is triggered

**The human review surface is the UI:**
The Review Workbench product brief states: "This product assumes model output is useful but not final." The UI exists for inspection, correction, confidence building, and provenance visibility. It is not a display tool — it is a semantic review and correction tool.

**cotizador** has the same principle at the component level: `@wiki_exempt` is a human-authored override. Agent guidelines include explicit "What NOT to do" sections, written by the human for the agent before each task.

**Finding:** The human is not at the end of the loop as a final reviewer. The human is at multiple points: writing plans (before agent acts), reviewing semantic outputs (during pipeline execution), approving merges (before code lands), and auditing documentation drift. The methodology assumes the human operates on artifacts, not on code directly.

---

Generated from `raw/methodology_synthesis_extended.md`.