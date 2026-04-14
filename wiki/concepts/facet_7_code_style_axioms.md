---
identity:
  node_id: doc:wiki/concepts/facet_7_code_style_axioms.md
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
  compiled_at: '2026-04-14T16:50:28.661943'
  compiled_from: wiki-compiler
---

**Question:** What conventions appear in every project without being discussed — the assumed rules?

## Definition

**Question:** What conventions appear in every project without being discussed — the assumed rules?.

## Examples

- `from __future__ import annotations` at the top of every module
- Module docstring: one paragraph, executive summary of the module's role
- Every public class, method, function has a structured docstring
- `contracts.py` / Pydantic models are the only legitimate way to pass data between modules
- `Field(description=...)` is dual-purpose: human + LLM readable, always semantic and specific

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

**Question:** What conventions appear in every project without being discussed — the assumed rules?

Across all Python projects:
- `from __future__ import annotations` at the top of every module
- Module docstring: one paragraph, executive summary of the module's role
- Every public class, method, function has a structured docstring
- `contracts.py` / Pydantic models are the only legitimate way to pass data between modules
- `Field(description=...)` is dual-purpose: human + LLM readable, always semantic and specific
- Domain-specific exceptions defined at the top of the relevant file. Never bare `Exception` for flow control.
- Never swallow errors silently. Log with context, re-raise with `from e`.
- `LogTag` shared vocabulary — never hardcoded emoji strings
- `changelog.md` updated on every significant change
- Comments only for non-obvious invariants or workflow decisions

**Finding:** These are assumed so deeply that they rarely appear in explicit rules documents — they show up in code examples and templates. They need to be stated explicitly in the seed rules because they're invisible to a newcomer.

---

Generated from `raw/methodology_synthesis.md`.
