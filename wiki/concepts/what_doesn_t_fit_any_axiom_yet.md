---
identity:
  node_id: doc:wiki/concepts/what_doesn_t_fit_any_axiom_yet.md
  node_type: concept
edges:
- target_id: raw:raw/methodology_synthesis.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/methodology_synthesis.md
  source_hash: 509baf32ca0ea70f59fdc2382e05095dde9fba07ad7092c46d49ecdca431bc34
  compiled_at: '2026-04-14T16:50:28.662075'
  compiled_from: wiki-compiler
---

**The critique pattern (cotizador mixin-arch/03_critique.md):** The codebase has a practice of writing explicit architectural critiques — documents that identify the failure modes, hidden coupling, and scalability cliffs of current patterns BEFORE they become problems. This is distinct from future_docs/ (which tracks known deferred work) and ADRs (which record decisions). It's a structural risk register.

## Definition

**The critique pattern (cotizador mixin-arch/03_critique.

## Examples

- The critique pattern (cotizador mixin-arch/03_critique.md):
- Proposed Axiom 6: Known architectural risks are documented explicitly.

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

**The critique pattern (cotizador mixin-arch/03_critique.md):** The codebase has a practice of writing explicit architectural critiques — documents that identify the failure modes, hidden coupling, and scalability cliffs of current patterns BEFORE they become problems. This is distinct from future_docs/ (which tracks known deferred work) and ADRs (which record decisions). It's a structural risk register. No other project does this explicitly, but it may be the most valuable artifact in the cotizador docs. Worth considering as Axiom 6.

**Proposed Axiom 6: Known architectural risks are documented explicitly.**
Every non-trivial architectural decision has a companion critique: what it correctly solves, what its hidden costs are, what a better implementation would look like. This is not pessimism — it's the precondition for evolving architecture without losing institutional memory.

Generated from `raw/methodology_synthesis.md`.
