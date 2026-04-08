---
identity:
  node_id: "doc:wiki/drafts/3_validation_gates.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_methodology.md", relation_type: "documents"}
---

After each phase, verify before proceeding:

## Details

After each phase, verify before proceeding:

| Phase | Verification |
|---|---|
| Contracts | Pydantic models instantiate correctly. `model_json_schema()` produces expected shapes. |
| Storage | Artifact files are written and reloaded correctly. Hashes are stable. |
| Graph (demo chain) | Automated tests cover: approve, regenerate, reject, stale hash, bare-Continue. |
| CLI | `--help` works. Run/resume cycle completes with demo chain. |
| Studio | Graph topology visible. Pause at review node confirmed. Thread history visible. |
| Real model | End-to-end run produces valid artifacts. Review surface is human-readable. |

Do not proceed to the next phase if the current phase's gate fails.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_methodology.md`.