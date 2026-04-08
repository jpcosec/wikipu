---
identity:
  node_id: "doc:wiki/drafts/environment_and_setup.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/AGENTS.md", relation_type: "documents"}
---

- Python package metadata is in `pyproject.toml`.

## Details

- Python package metadata is in `pyproject.toml`.
- Direct dependencies are pinned in `requirements.txt`.
- Typical setup:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

- Required env vars for LLM-backed flows:

```bash
export GOOGLE_API_KEY=...
export GEMINI_API_KEY=...
export LOG_DIR=logs
```

- Rendering PDF output also requires external tools such as `pandoc` and a TeX distribution.

Generated from `raw/docs_postulador_v2/AGENTS.md`.