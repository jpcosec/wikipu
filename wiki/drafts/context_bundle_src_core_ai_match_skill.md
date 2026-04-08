---
identity:
  node_id: "doc:wiki/drafts/context_bundle_src_core_ai_match_skill.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/new_feature/dev machine/expand_context_navigation_skill.md", relation_type: "documents"}
---

Generated: <timestamp>

## Details

Generated: <timestamp>

### [1/3] README
<content of src/core/ai/match_skill/README.md>

### [2/3] Architecture Files
#### src/core/ai/match_skill/graph.py
<content>

#### src/core/ai/match_skill/storage.py
<content>

### [3/3] Data Contracts (JSON Schema)
#### MatchEnvelope
<json schema>

#### ReviewPayload
<json schema>
```

### Parsing strategy

- Extract Architecture file links using the same regex as `scripts/validate_doc_links.py` (backtick paths + markdown links), scoped to lines between the `## 🏗️ Architecture` header and the next `##`.
- Extract Pydantic model names from the Data Contract section, import them dynamically from the module's `contracts.py`, and call `.model_json_schema()`.
- Fail explicitly if a linked file does not exist (do not silently skip).

### CLAUDE.md navigation rules

These rules belong in CLAUDE.md regardless of whether the script exists — they encode the navigation protocol for any agent working in this codebase:

**Rule 1 — Read the article before the source:**
When starting work on a module, read `src/<module>/README.md` before reading any source file. The Architecture section tells you which files matter. The Data Contract section tells you what data flows in and out.

**Rule 2 — Contracts before logic:**
Never read `logic.py` or `graph.py` to understand a module's data shape. Read the linked `contracts.py` first. The contract is the module's interface; the logic is the implementation.

**Rule 3 — Anti-drift check:**
After modifying a file, check whether the module README's Architecture section links to it. If it does, verify the description is still accurate. If the file was renamed or moved, update the link.

**Rule 4 — Quality gate:**
Before marking a task complete, run through `docs/standards/docs/documentation_quality_checklist.md`.

---

Generated from `raw/docs_postulador_refactor/future_docs/new_feature/dev machine/expand_context_navigation_skill.md`.