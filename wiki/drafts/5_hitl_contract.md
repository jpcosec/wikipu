---
identity:
  node_id: "doc:wiki/drafts/5_hitl_contract.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_components.md", relation_type: "documents"}
---

Human-in-the-loop review is payload-driven, not acknowledgement-driven.

## Details

Human-in-the-loop review is payload-driven, not acknowledgement-driven.

**System responsibilities:**
- Pause at the right moment (`interrupt_before` the review node)
- Persist the review surface before pausing
- Validate payload shape and hash on resume
- Reject stale payloads (hash mismatch)
- Route deterministically from the payload — never guess intent
- Treat a bare resume with no payload as a safe no-op (return to pending state)

**Human responsibilities:**
- Inspect the review surface (`review/current.json`)
- Make an explicit semantic decision per row (approve / request_regeneration / reject)
- Provide patch evidence when requesting regeneration
- Submit a typed `ReviewPayload` — not just pressing Continue

The bare-Continue case must be handled safely: if `review_payload` is absent on resume, return to `pending_review` without crashing. This is not optional — Studio will trigger this case.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_components.md`.