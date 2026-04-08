---
identity:
  node_id: "doc:wiki/drafts/build_run_and_test_commands.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/AGENTS.md", relation_type: "documents"}
---

### Install / package

## Details

### Install / package

```bash
pip install -r requirements.txt
pip install -e .
```

### Main runtime commands

```bash
python -m src.cli.main api start
python -m src.cli.main run-batch --sources xing stepstone --limit 5 --profile-evidence path/to/profile.json
python -m src.cli.main review
python -m src.cli.main review --source xing --job-id 12345
python -m src.cli.main generate --source stepstone --job-id <ID> --language en --render
python -m src.core.tools.render.main cv --source stepstone --job-id <ID> --language en
python -m src.core.tools.translator.main --source stepstone
```

### Test commands

- Full suite currently includes stale legacy coverage and is not fully green.
- Active suite that passes in the current repo:

```bash
python -m pytest tests/unit tests/test_generate_documents_v2 -q
```

- Full suite:

```bash
python -m pytest tests/ -q
```

- Single test file:

```bash
python -m pytest tests/unit/cli/test_main.py -q
python -m pytest tests/unit/core/ai/generate_documents_v2/test_profile_updater.py -q
```

- Single test function:

```bash
python -m pytest tests/unit/cli/test_main.py::test_main_without_command_prints_help -q
python -m pytest tests/unit/core/ai/generate_documents_v2/test_profile_updater.py::test_profile_updater_writes_to_disk_and_clears_list -q
```

- Test subtree:

```bash
python -m pytest tests/unit/core/ai/generate_documents_v2 -q
```

### Lint / static checks

- No dedicated repo-wide linter or type-checker configuration was found in `pyproject.toml`.
- No confirmed canonical `ruff`, `black`, `mypy`, `pyright`, `tox`, or `nox` command is checked in.
- Treat `pytest` as the mandatory verification baseline.
- If you need a lightweight syntax smoke check, use:

```bash
python -m compileall src tests
```

Generated from `raw/docs_postulador_v2/AGENTS.md`.