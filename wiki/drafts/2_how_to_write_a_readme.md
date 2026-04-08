---
identity:
  node_id: "doc:wiki/drafts/2_how_to_write_a_readme.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/docs/documentation_and_planning_guide.md", relation_type: "documents"}
---

READMEs explain **why the module exists**, **what it does**, and **where the important pieces are**. They do not re-document what the code already makes explicit.

## Details

READMEs explain **why the module exists**, **what it does**, and **where the important pieces are**. They do not re-document what the code already makes explicit.

### Mandatory sections

Every module README must contain these sections, in order, with emoji markers:

| Section | Emoji | Purpose |
|---|---|---|
| Architecture & Features | 🏗️ | Shape of the system and its design rationale |
| Configuration | ⚙️ | Required env vars and setup, in code blocks |
| CLI / UI / Usage | 🚀 | Intent and entry points — not argument tables |
| Data Contract | 📝 | What flows in and out — points to the model files |
| How to Add / Extend | 🛠️ | Numbered steps for extending the module |
| How to Use | 💻 | Copy-pasteable quickstart |
| Troubleshooting | 🚑 | Symptom → Diagnosis → Solution |

### Architecture section rules

Describe the structural shape, then **link to the exact file**. The file is authoritative. File links are validated by `scripts/validate_doc_links.py` — a broken link is a CI failure.

```markdown

Generated from `raw/docs_postulador_refactor/docs/standards/docs/documentation_and_planning_guide.md`.