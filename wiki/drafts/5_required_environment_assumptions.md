---
identity:
  node_id: "doc:wiki/drafts/5_required_environment_assumptions.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md", relation_type: "documents"}
---

- Use conda environment `phd-cv`:

## Details

- Use conda environment `phd-cv`:
  - `conda activate phd-cv`
- Export repository `.env` into the shell before any run/resume command:
  - `set -a; source .env; set +a`
- Python dependencies are expected to be installed in that environment.
- `langgraph` available (graph compile + sqlite checkpointing).
- `google-generativeai` available for LLM nodes.
- Valid API credentials for Gemini in environment.
- Optional model override:
  - `PHD2_GEMINI_MODEL` (default in code: `gemini-2.5-flash`).

Generated from `raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md`.