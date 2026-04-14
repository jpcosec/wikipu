---
identity:
  node_id: doc:wiki/concepts/facet_8_inter_project_divergence.md
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
  compiled_at: '2026-04-14T16:50:28.661988'
  compiled_from: wiki-compiler
---

**Question:** Where do projects contradict each other? Which version is better?

## Definition

**Question:** Where do projects contradict each other? Which version is better?.

## Examples

- Doc_methodology: mechanical enforcement via git hooks + 4-template system with tooling (DocMutator auto-manages file lifecycles, TestSprite required in commits)
- Postulador: AGENTS.md + convention, no hard enforcement
- Cotizador: per-task agent_guideline, enforcement by human review only
- Cotizador: atomic feature-scoped plans (`plan/<feature>/` folder with phases as separate files). One feature = one plan.
- Postulador: larger multi-phase plans with dependency matrices in single documents.

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

**Question:** Where do projects contradict each other? Which version is better?

**Divergence 1: Agent control granularity**
- Doc_methodology: mechanical enforcement via git hooks + 4-template system with tooling (DocMutator auto-manages file lifecycles, TestSprite required in commits)
- Postulador: AGENTS.md + convention, no hard enforcement
- Cotizador: per-task agent_guideline, enforcement by human review only

**Verdict:** Doc_methodology is the most explicit and least ambiguous. The 4-template model eliminates the question "am I allowed to touch this?" at every moment. However, it requires tooling (DocMutator, TestSprite) that adds overhead. The minimal viable version is the 4-mode permission model without requiring the exact tooling.

**Divergence 2: Plan scope**
- Cotizador: atomic feature-scoped plans (`plan/<feature>/` folder with phases as separate files). One feature = one plan.
- Postulador: larger multi-phase plans with dependency matrices in single documents.
- Doc_methodology: domain + stage coordinates every piece of work.

**Verdict:** Cotizador's atomic feature folders are the most agent-friendly. A single plan document that runs 200+ lines becomes a context problem. Phases-as-files allows parallel execution and incremental completion. The postulador wave model is good for dependency tracking but creates large monolithic documents.

**Divergence 3: How docs point to code**
- Postulador_refactor: docs point to file paths, links are validated by CI
- Cotizador: docs describe behavior, code is the authority, no link validation
- Doc_methodology: strict temporal unidirectionality (docs/runtime/ never references plan/)

**Verdict:** Doc_methodology's unidirectionality rule is the clearest. The postulador's link validation is good engineering but adds CI overhead. The minimum viable version: docs/runtime/ references code, never plan/. Plan references docs/runtime/. This is unambiguous and requires no tooling.

---

Generated from `raw/methodology_synthesis.md`.
