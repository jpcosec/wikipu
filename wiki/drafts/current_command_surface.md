---
identity:
  node_id: "doc:wiki/drafts/current_command_surface.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md", relation_type: "documents"}
---

The runnable operator commands in this workspace are Python module entrypoints, not `phd2 ...` aliases.

## Details

The runnable operator commands in this workspace are Python module entrypoints, not `phd2 ...` aliases.

Primary flow:

- `python -m src.cli.run_prep_match --source <source> --job-id <id> --source-url <url> --profile-evidence <json-path>`
- `python -m src.cli.run_prep_match --source <source> --job-id <id> --resume`

Supporting tools:

- `python -m src.cli.run_scrape_probe --source <source> --url <url> --mode detail`
- `python -m src.cli.run_scrape_probe --source <source> --url <listing_url> --mode listing --max-pages <n>`
- `python -m src.cli.run_stepstone_autoapply --job-url <url> [--apply]`

Do not assume `phd2 run`, `phd2 review-validate`, `phd2 graph-status`, or other alias commands exist in this repo unless they are added explicitly.

Generated from `raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md`.