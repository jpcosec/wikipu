---
identity:
  node_id: "doc:wiki/drafts/stepstone_autoapply_track.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/post_key_validation_and_stepstone_autoapply_plan.md", relation_type: "documents"}
---

Use `src/cli/run_stepstone_autoapply.py` (added in this change) with safe defaults.

## Details

Use `src/cli/run_stepstone_autoapply.py` (added in this change) with safe defaults.

### Dry-run (default recommended)

```bash
python -m src.cli.run_stepstone_autoapply \
  --job-id 13722751 \
  --source-url "https://www.stepstone.de/stellenangebote--Data-Science-Trainee-w-m-d-Guetersloh-Bertelsmann-SE-Co-KGaA--13722751-inline.html"
```

### Attempt mode

```bash
python -m src.cli.run_stepstone_autoapply \
  --job-id 13722751 \
  --source-url "https://www.stepstone.de/stellenangebote--Data-Science-Trainee-w-m-d-Guetersloh-Bertelsmann-SE-Co-KGaA--13722751-inline.html" \
  --apply
```

Attempt mode intentionally fail-stops on login/captcha/manual-only states and records evidence artifacts.

Generated from `raw/docs_postulador_langgraph/docs/operations/post_key_validation_and_stepstone_autoapply_plan.md`.