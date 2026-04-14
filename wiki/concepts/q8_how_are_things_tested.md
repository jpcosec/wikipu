---
identity:
  node_id: "doc:wiki/concepts/q8_how_are_things_tested.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis_extended.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis_extended.md"
  source_hash: "0eaf49dde8b77f6999c8e390207549968bc290d82d4774999f7136fecc61fb30"
  compiled_at: "2026-04-14T16:50:28.663823"
  compiled_from: "wiki-compiler"
---

**Per domain:**

## Details

**Per domain:**

**Deterministic (backend/core):** Standard pytest unit tests. Each function tested in isolation. No real DB, no real LLM. Domain functions are pure — inputs in, outputs out, no side effects. Tests verify behavior against contracts, not implementation details.

**LangGraph / AI modules:** 
Minimum required test cases per module:
1. Approve flow (run → persist → pause → resume with approval → complete)
2. Regeneration flow (review requests regen → context prepared → second round runs)
3. Rejection flow (review rejects → graph ends cleanly)
4. Stale hash rejection (resume with hash mismatch → rejected)
5. Bare-Continue safety (resume with no payload → returns to pending state without crash)

Tests use `InMemorySaver` and injected fake chains — never the real model. CLI tests patch `build_graph` to inject the fake app. Demo chain must produce structurally valid output (passes `with_structured_output` validation).

**Ingestion:**
- Each ingestion run is idempotent — tests verify that re-running produces the same output, not a duplicate
- Partial failure handling: tests verify that one failed record doesn't abort the batch
- LLM rescue path: rescue is only triggered on explicit failure, never speculatively
- Validation at boundary: missing mandatory fields raise domain exceptions, not generic errors

**UI / Frontend:**
Two layers:
1. Type checking (`npm run typecheck`) — TypeScript validates all contracts at compile time
2. E2E tests via TestSprite — real browser flows verifying specific user actions and expected outcomes

The UI testing philosophy is: if a behavior can only be verified in a real browser, verify it in a real browser. No synthetic assertions for UI rendering behavior. TestSprite evidence is required in the commit message — testing is not optional or separable from shipping.

**Documentation quality testing:**
`scripts/validate_doc_links.py` validates that all file references in READMEs point to existing files. Broken links are a CI failure. This is the only automated documentation test found across projects.

**Integration / cross-layer:**
Not explicitly defined as a test category in any project. The closest equivalent is the Studio verification checklist (can the graph load without credentials? does it pause at the right node? does resume route correctly?) — but this is manual, not automated.

**Test pyramid shape implied across projects:**
- Many unit tests (contracts, pure functions, storage round-trips)
- Some graph topology tests (demo chain, approve/reject/regen flows)
- Some E2E tests (TestSprite for UI flows)
- No dedicated integration tests between backend and UI layers

**Finding:** Testing is domain-specific and has explicit minimum coverage contracts per domain. The weakest layer is cross-domain integration — no project has a stated policy for testing the full pipeline from ingestion through AI through UI through human review as a single flow. Studio verification partially fills this gap but it's manual and not tracked as a test artifact.

Generated from `raw/methodology_synthesis_extended.md`.