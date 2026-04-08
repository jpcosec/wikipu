---
identity:
  node_id: "doc:wiki/drafts/1_readme_completeness.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/docs/documentation_quality_checklist.md", relation_type: "documents"}
---

- [ ] A `README.md` exists in the component's root directory.

## Details

- [ ] A `README.md` exists in the component's root directory.
- [ ] `## 🏗️ Architecture & Features` — describes shape and rationale, links to the authoritative source files.
- [ ] `## ⚙️ Configuration` — all required env vars and setup instructions in code blocks.
- [ ] `## 🚀 CLI / UI / Usage` — describes intent and entry points; points to the argparse/Settings definition in code, not a duplicated argument table.
- [ ] `## 📝 Data Contract` — points to the Pydantic model file; does not restate field names or types.
- [ ] `## 🛠️ How to Add / Extend` — numbered, algorithmic steps for adding new modules or providers.
- [ ] `## 💻 How to Use` — copy-pasteable quickstart.
- [ ] `## 🚑 Troubleshooting` — common errors mapped as "Symptom → Diagnosis → Solution".
- [ ] Emojis are used consistently as structural markers on section headers.
- [ ] `scripts/validate_doc_links.py` passes — no broken file references.

---

Generated from `raw/docs_postulador_refactor/docs/standards/docs/documentation_quality_checklist.md`.