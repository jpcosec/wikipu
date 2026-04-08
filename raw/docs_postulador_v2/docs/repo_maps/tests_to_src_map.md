# Tests To Src Map

Current test inventory mapped to the closest source area, grouped in roughly the same shape as `src/`.

Status labels:

- `current` - maps cleanly to active code
- `review` - still maps to active code, but needs follow-up or replacement under the newer testing plan
- `outdated` - targets removed architecture or old behavior

## `src/cli/`

### `tests/unit/cli/test_main.py`

- status: `current`
- maps to:
  - `src/cli/main.py`
  - `src/core/api_client.py`
  - `src/core/data_manager.py`

## `src/core/data_manager.py`

### `tests/unit/core/data_manager/test_data_manager.py`

- status: `current`
- maps to:
  - `src/core/data_manager.py`

## `src/core/io/`

### `tests/unit/core/io/test_workspace_manager.py`

- status: `current`
- maps to:
  - `src/core/io/workspace_manager.py`

### `tests/legacy/guardrails/test_file_management_guardrails.py`

- status: `outdated`
- maps to:
  - `src/core/data_manager.py`
  - `src/core/io/`
  - `src/core/ai/generate_documents_v2/`
- reason:
  - encodes an older “DataManager-only filesystem access” rule and still assumes legacy graph boundaries

## `src/scraper/`

### `tests/unit/scraper/test_smart_adapter.py`

- status: `current`
- maps to:
  - `src/scraper/smart_adapter.py`
  - `src/core/data_manager.py`

## `src/apply/`

### `tests/unit/apply/test_models.py`

- status: `current`
- maps to:
  - `src/apply/models.py`
  - `src/apply/main.py`

### `tests/unit/apply/test_smart_adapter.py`

- status: `current`
- maps to:
  - `src/apply/smart_adapter.py`
  - `src/apply/models.py`

### `tests/unit/apply/browseros/test_models.py`

- status: `current`
- maps to:
  - `src/apply/browseros_models.py`
  - `src/apply/playbooks/linkedin_easy_apply_v1.json`

### `tests/unit/apply/browseros/test_client.py`

- status: `current`
- maps to:
  - `src/apply/browseros_client.py`

### `tests/unit/apply/browseros/test_executor.py`

- status: `current`
- maps to:
  - `src/apply/browseros_executor.py`
  - `src/apply/playbooks/linkedin_easy_apply_v1.json`

## `src/core/ai/generate_documents_v2/`

### `tests/unit/core/ai/generate_documents_v2/nodes/test_ingestion.py`

- status: `current`
- maps to:
  - `src/core/ai/generate_documents_v2/nodes/ingestion.py`

### `tests/unit/core/ai/generate_documents_v2/nodes/test_requirement_filter.py`

- status: `current`
- maps to:
  - `src/core/ai/generate_documents_v2/nodes/requirement_filter.py`

### `tests/unit/core/ai/generate_documents_v2/nodes/test_alignment.py`

- status: `current`
- maps to:
  - `src/core/ai/generate_documents_v2/nodes/alignment.py`

### `tests/unit/core/ai/generate_documents_v2/nodes/test_blueprint.py`

- status: `current`
- maps to:
  - `src/core/ai/generate_documents_v2/nodes/blueprint.py`

### `tests/unit/core/ai/generate_documents_v2/nodes/test_drafting.py`

- status: `current`
- maps to:
  - `src/core/ai/generate_documents_v2/nodes/drafting.py`

### `tests/unit/core/ai/generate_documents_v2/nodes/test_assembly.py`

- status: `current`
- maps to:
  - `src/core/ai/generate_documents_v2/nodes/assembly.py`

### `tests/unit/core/ai/generate_documents_v2/nodes/test_localization.py`

- status: `current`
- maps to:
  - `src/core/ai/generate_documents_v2/nodes/localization.py`

### `tests/unit/core/ai/generate_documents_v2/test_profile_loader.py`

- status: `current`
- maps to:
  - `src/core/ai/generate_documents_v2/profile_loader.py`

### `tests/unit/core/ai/generate_documents_v2/test_storage.py`

- status: `current`
- maps to:
  - `src/core/ai/generate_documents_v2/storage.py`

### `tests/unit/core/ai/generate_documents_v2/contracts/test_contracts.py`

- status: `current`
- maps to:
  - `src/core/ai/generate_documents_v2/contracts/`

### `tests/unit/core/ai/generate_documents_v2/test_pipeline.py`

- status: `current`
- maps to:
  - `src/core/ai/generate_documents_v2/pipeline.py`

## Legacy / e2e bucket

### `tests/legacy/e2e/test_pipeline.py`

- status: `outdated`
- maps to:
  - legacy pipeline / removed `match_skill` flow
- reason:
  - imports removed modules and expects old artifacts like `pipeline_inputs/` and legacy final package manifests

### `tests/legacy/e2e/fixtures/stub_profile.json`

- status: `review`
- maps to:
  - legacy e2e support data
- reason:
  - fixture may still be useful, but its owning test is currently outdated

## Quick cleanup targets

Highest-confidence cleanup candidates:

1. `tests/legacy/e2e/test_pipeline.py`
2. `tests/legacy/guardrails/test_file_management_guardrails.py`
3. recreate portal-adapter DOM/fixture tests under the newer testing plan if selector validation becomes important again
