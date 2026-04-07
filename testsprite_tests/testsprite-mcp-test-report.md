## 1️⃣ Document Metadata
- **Project Name:** wikipu
- **Date:** 2026-04-07
- **Prepared by:** OpenCode + TestSprite MCP
- **Execution Mode:** TestSprite backend run against local `wikipu-server` on port `8765`
- **Source Artifacts:** `testsprite_tests/tmp/raw_report.md`, `logs/wikipu-server.log`

---

## 2️⃣ Requirement Validation Summary

### Requirement: Service Reachability

#### Test TC001 get_health_endpoint_reachable
- **Test Code:** [TC001_get_health_endpoint_reachable.py](./TC001_get_health_endpoint_reachable.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/e5be8a7b-6350-4c30-8105-63e65f252c65/e9d1be0f-6718-434c-b27e-575a77d6f336
- **Status:** ✅ Passed
- **Analysis / Findings:** The HTTP wrapper is reachable through the TestSprite tunnel and returns a valid readiness payload from `GET /health`.

---

### Requirement: Validation Endpoint Behavior

#### Test TC002 post_validate_with_valid_source
- **Test Code:** [TC002_post_validate_with_valid_source.py](./TC002_post_validate_with_valid_source.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/e5be8a7b-6350-4c30-8105-63e65f252c65/eccb94e5-2cbe-40df-a86f-fec7d90be0a2
- **Status:** ❌ Failed
- **Analysis / Findings:** The generated test posts a temporary source path created inside the remote TestSprite runner. That path does not exist on the local machine where `wikipu-server` is running, so the request cannot be validated successfully.

#### Test TC003 post_validate_with_invalid_source
- **Test Code:** [TC003_post_validate_with_invalid_source.py](./TC003_post_validate_with_invalid_source.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/e5be8a7b-6350-4c30-8105-63e65f252c65/9bed91d0-8f56-407b-983b-ba8fd5b7ffb3
- **Status:** ✅ Passed
- **Analysis / Findings:** The service correctly returns a structured `400` response for an invalid source path, including machine-readable error details.

#### Test TC004 post_validate_with_malformed_body
- **Test Code:** [TC004_post_validate_with_malformed_body.py](./TC004_post_validate_with_malformed_body.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/e5be8a7b-6350-4c30-8105-63e65f252c65/b41abb38-b78b-4a47-b9b2-8f96aca1cd5f
- **Status:** ❌ Failed
- **Analysis / Findings:** The endpoint returns a `400`, but the generated test expects the error text to explicitly mention schema or validation language. The current response is a plain domain error rather than a request-schema phrasing.

---

### Requirement: Build Endpoint Behavior

#### Test TC005 post_build_with_valid_source_and_render_true
- **Test Code:** [TC005_post_build_with_valid_source_and_render_true.py](./TC005_post_build_with_valid_source_and_render_true.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/e5be8a7b-6350-4c30-8105-63e65f252c65/273a4c1b-4b35-43b5-b439-10e661450d4d
- **Status:** ❌ Failed
- **Analysis / Findings:** Like TC002, this case relies on temporary filesystem paths created inside the remote runner. The local service cannot read or write those remote paths, so the test cannot validate the happy-path build flow end to end.

#### Test TC006 post_build_with_valid_source_and_render_false
- **Test Code:** [TC006_post_build_with_valid_source_and_render_false.py](./TC006_post_build_with_valid_source_and_render_false.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/e5be8a7b-6350-4c30-8105-63e65f252c65/c6ecdd00-17fc-4f23-9685-1a721ce0af50
- **Status:** ❌ Failed
- **Analysis / Findings:** This case uses the real repository source `src/wiki/nodes`, and the service correctly surfaces an actual data issue: `src/wiki/nodes/scraper/job_parser.md` references unknown target `dir:data/raw/jobs`. This is a genuine content-validation failure, not a harness artifact.

#### Test TC007 post_build_with_invalid_source
- **Test Code:** [TC007_post_build_with_invalid_source.py](./TC007_post_build_with_invalid_source.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/e5be8a7b-6350-4c30-8105-63e65f252c65/c5d4a167-622b-4574-aaac-d345ab0c996a
- **Status:** ✅ Passed
- **Analysis / Findings:** The build endpoint correctly rejects invalid source input with a `400` response.

---

### Requirement: Scaffolding Endpoint Behavior

#### Test TC008 post_scaffold_with_new_module
- **Test Code:** [TC008_post_scaffold_with_new_module.py](./TC008_post_scaffold_with_new_module.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/e5be8a7b-6350-4c30-8105-63e65f252c65/79f70f75-cd46-45eb-8a9e-06ffeeb42e12
- **Status:** ❌ Failed
- **Analysis / Findings:** The generated test expects the server to create files inside a temporary directory owned by the remote runner, but it only sends the relative module path `src/core/newmodule` to the local service. That mismatch makes the filesystem assertion invalid for this execution model.

#### Test TC009 post_scaffold_with_existing_module
- **Test Code:** [TC009_post_scaffold_with_existing_module.py](./TC009_post_scaffold_with_existing_module.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/e5be8a7b-6350-4c30-8105-63e65f252c65/b9bf07f1-24da-4fc8-a145-14d409f674fe
- **Status:** ❌ Failed
- **Analysis / Findings:** The generated test mixes a remote temporary directory with a local-service request, so the server sees a path that already exists only in the runner context, not necessarily on the local machine. The failure is due to environment mismatch rather than the scaffold implementation alone.

---

## 3️⃣ Coverage & Matching Metrics

- **Pass Rate:** `33.33%` (`3/9` passed)
- **Meaningful Product Coverage:** Reachability, invalid-path validation, and invalid build-path handling were exercised successfully.
- **Harness Mismatch Rate:** `4/6` failures are primarily caused by remote-runner vs local-filesystem path assumptions.

| Requirement | Total Tests | ✅ Passed | ❌ Failed |
|---|---:|---:|---:|
| Service Reachability | 1 | 1 | 0 |
| Validation Endpoint Behavior | 3 | 1 | 2 |
| Build Endpoint Behavior | 3 | 1 | 2 |
| Scaffolding Endpoint Behavior | 2 | 0 | 2 |

---

## 4️⃣ Key Gaps / Risks
- The main TestSprite limitation for this repo is environmental: generated tests create temporary files on the remote runner, but `wikipu-server` runs on the local machine and cannot access those runner-local paths.
- One real repository issue was confirmed: `src/wiki/nodes/scraper/job_parser.md` currently blocks a successful build because it references missing target `dir:data/raw/jobs`.
- The API error payload shape is acceptable for local tests, but wording could be made more schema-oriented if you want to satisfy stricter generated assertions like TC004.
- Scaffolding tests are not trustworthy in the current MCP tunnel setup unless the API is redesigned to accept file contents inline or return artifacts instead of relying on shared filesystem state.
- For high-confidence automation with TestSprite, the best next target is a self-contained HTTP contract that does not depend on caller-visible local paths; otherwise `pytest` remains the more accurate verification path for this repository.

---
