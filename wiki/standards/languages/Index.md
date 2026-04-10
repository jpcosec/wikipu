---
identity:
  node_id: "doc:wiki/standards/languages/Index.md"
  node_type: "index"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

Per-language style guides that translate the language-agnostic CS-1 through CS-9 rules from `wiki/standards/house_rules.md` (Layer 5) into each language's idioms, toolchain, and enforcement mechanisms. Every guide covers rule mapping, recommended toolchain configuration, and a breakdown of automated versus manual enforcement.

| Language | File | Summary |
|---|---|---|
| Python | `python.md` | Pydantic contracts, ruff, docstring-coverage audit, ASTFacet scanning |
| TypeScript | `typescript.md` | Zod/typed interfaces, tsc --strict, ESLint, JSDoc on every export |
