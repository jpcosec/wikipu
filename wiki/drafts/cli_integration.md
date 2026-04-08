---
identity:
  node_id: "doc:wiki/drafts/cli_integration.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md", relation_type: "documents"}
---

Package these templates into a simple command:

## Details

Package these templates into a simple command:

```bash
./agent.sh --mode implement --domain ui --stage match --target "B3_match_redesign.md"
```

### CLI Options

| Flag | Values | Description |
|------|--------|-------------|
| `--mode` | `sync`, `implement`, `design`, `hotfix` | Which template to use |
| `--domain` | `ui`, `api`, `pipeline`, `core`, `data`, `policy` | Technical domain |
| `--stage` | `scrape`, `translate`, `extract`, `match`, `strategy`, `drafting`, `render`, `package` | Pipeline stage |
| `--target` | filename | Plan file or problem description |
| `--include-code` | `true`, `false` | Include source code in context (default: true for sync/hotfix, false for design) |
| `--skip-docs` | flag | Skip doc update (hotfix only, creates 24h debt) |

### Example Commands

```bash
# Sync docs after manual code changes
./agent.sh --mode sync --domain ui --stage match

# Implement an existing plan
./agent.sh --mode implement --domain ui --stage extract --target "B2_extract_understand.md"

# Design a new feature
./agent.sh --mode design --domain ui --stage strategy --target "Add bulk regeneration"

# Fix a bug
./agent.sh --mode hotfix --domain pipeline --stage extract --target "span_resolver multiline"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md`.