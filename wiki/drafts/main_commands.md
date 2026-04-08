---
identity:
  node_id: "doc:wiki/drafts/main_commands.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/cli/README.md", relation_type: "documents"}
---

### Pipeline Execution

## Details

### Pipeline Execution

#### `run_prep_match`

Main pipeline entrypoint for the prep-match flow.

```bash
python -m src.cli.run_prep_match \
  --source <source> \
  --job-id <job_id> \
  --source-url <url> \
  --profile-evidence <path>
```

**Options:**

| Flag | Description |
|------|-------------|
| `--source` | Job source (e.g., `tu_berlin`) |
| `--job-id` | Unique job identifier |
| `--source-url` | URL to scrape |
| `--profile-evidence` | Path to profile evidence file |
| `--resume` | Resume from checkpoint |
| `--resume-from` | Resume from specific node |

**Example:**

```bash
# Start new job
python -m src.cli.run_prep_match \
  --source tu_berlin \
  --job-id 201397 \
  --source-url "https://jobs.tu-berlin.de/jobposting/..." \
  --profile-evidence data/master/profile.json

# Resume interrupted job
python -m src.cli.run_prep_match --source tu_berlin --job-id 201397 --resume
```

### API Server

#### `run_review_api`

Start the FastAPI review server.

```bash
python -m src.cli.run_review_api
```

Runs on `http://localhost:8000` by default.

### Scraping Utilities

#### `run_scrape_probe`

Probe scraping for a URL or listing.

```bash
python -m src.cli.run_scrape_probe --url <url> --mode <listing|detail>
```

**Options:**

| Flag | Description |
|------|-------------|
| `--url` | URL to probe |
| `--mode` | `listing` or `detail` |
| `--adapter` | Source adapter (e.g., `tu_berlin`, `stepstone`) |

#### `run_stepstone_autoapply`

StepStone autoapply prototype (dry-run by default).

```bash
python -m src.cli.run_stepstone_autoapply --url <url> [--dry-run false]
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/cli/README.md`.