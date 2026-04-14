---
identity:
  node_id: doc:wiki/drafts/2_domain_glossary.md
  node_type: concept
edges:
- target_id: raw:raw/unimplemented_from_sourcetalk.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/unimplemented_from_sourcetalk.md
  source_hash: 1a7f8c9ba485c0342c7bddb0d133479345f1edd3e7047103e0544db195914f61
  compiled_at: '2026-04-14T16:50:28.666214'
  compiled_from: wiki-compiler
---

**Idea:** A central file (e.g., `docs/domain_glossary.yaml`) that unifies synonyms across modules. If module A calls it "JobPosting" and module B calls it "Vacancy", the graph should know they're the same concept.

## Definition

**Idea:** A central file (e.

## Examples

- Idea:
- Current state:
- Reference (sourcetalk.txt line ~780):

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

**Idea:** A central file (e.g., `docs/domain_glossary.yaml`) that unifies synonyms across modules. If module A calls it "JobPosting" and module B calls it "Vacancy", the graph should know they're the same concept.

**Current state:** Not implemented. No glossary file exists. No "semantic collision" check in the validator.

**Reference (sourcetalk.txt line ~780):**
> "Todo sustantivo central debe estar registrado en `docs/domain_glossary.yaml`. El compilador fusionará conceptos semánticos basándose en este archivo."

---

Generated from `raw/unimplemented_from_sourcetalk.md`.
