---
identity:
  node_id: "doc:wiki/adrs/002_documentation_consolidation.md"
  node_type: "adr"
adr:
  decision_id: "002"
  status: "accepted"
  context_summary: "Duplicate documentation drafts in raw/ were causing context drift. We decided to treat wiki/ as the single source of truth and raw/ as historical ore."
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

This ADR consolidates all documentation sources by designating `wiki/` as the single source of truth, deprecating duplicate drafts in `raw/` and `agents/`, and establishing the Librarian Agent's canonical protocol location.

# ADR 002: Documentation Consolidation

## Context
There were multiple versions of "House Rules" and "Agent Intros" in `wiki/`, `agents/`, and `raw/sourcetalk_artifacts/`. This led to confusion about which rules to follow. Specifically, the Spanish drafts in `raw/` contained some rules (like Law 13: Maps of Content) that were not yet in the English canonical versions.

## Decision
1. **Wiki is Truth:** All active standards and concepts must reside in `wiki/`.
2. **Refine Spanish Drafts:** Incorporate relevant laws from `raw/sourcetalk_artifacts/00_hausordnung_draft.md` into `wiki/standards/house_rules.md`.
3. **Deprecate raw/ artifacts:** The contents of `raw/sourcetalk_artifacts/` are now formally considered "historical ore" and are superseded by the `wiki/` versions.
4. **Librarian canonical home:** The Librarian Agent's canonical protocol is `agents/librarian/intro.md`, which points to `wiki/standards/house_rules.md`.

## Rationale
Following the "Sanctuary" law, `raw/` remains immutable, but our operational protocol must prioritize the "Refined metal" in `wiki/`. This prevents context drift and ensures all agents follow the same English canonical rules.

## Consequences
- Agents must ignore `raw/sourcetalk_artifacts/` when looking for active rules.
- The `wiki/standards/house_rules.md` is now the sole authority for ecosystem laws.
