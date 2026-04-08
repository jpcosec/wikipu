# Autoapply Runtime Hardening

**Why deferred:** The `src/apply/` module already has a usable structure, but its runtime path still depends on placeholder selectors, incomplete profile inputs, and a selector-validation flow that is not yet safe for real portal execution.
**Last reviewed:** 2026-03-30

## Problem / Motivation

The auto-application module under `src/apply/` looks structurally sound, but it is not yet hardened enough for real unattended execution.

Main gaps found during review:

1. Selector validation is disconnected from the real portal page state.
   - `src/apply/smart_adapter.py` validates selectors via `_validate_selectors()` using a fresh crawler session against `about:blank` instead of the already-open application page/modal.
   - This can raise false `portal_changed` errors even when the real page is healthy.
   - It also weakens the purpose of runtime validation, because the DOM being checked is not guaranteed to be the actual DOM where the form was opened.

2. Candidate profile data is not actually available to the fill scripts.
   - `_build_profile()` currently returns only job metadata (`job_title`, `company_name`, `application_url`).
   - Both portal adapters expect placeholders like `{{first_name}}`, `{{last_name}}`, `{{email}}`, and `{{phone}}`.
   - In practice, this means the generated fill script can leave unresolved placeholders or submit incomplete/invalid form data.

3. Error screenshots do not capture the failing browser state.
   - The exception path currently opens a new crawler on `about:blank` and stores `error_state.png` from there.
   - That artifact is unlikely to help when debugging selector drift, login redirects, validation failures, or modal timing issues.

4. Portal adapters still contain placeholder selectors.
   - Both XING and StepStone adapters explicitly note that selectors are placeholders pending DOM inspection.
   - The module therefore has the shape of a production adapter system, but not yet the validated selector contracts needed for real applications.

5. Snapshot-based selector tests are optional in practice right now.
   - The adapter tests skip if fixtures are absent.
   - That is reasonable for local development, but it means CI can report green while the most important selector assertions are not actually being exercised.

## Proposed Direction

### 1. Validate selectors on the active page state

Refactor `_validate_selectors()` so it runs against the same browser/page/session state used to open the apply modal.

Desired properties:
- no second detached crawler just for validation
- selector presence checked after modal open, on the real page
- failures distinguish better between login expiration, portal redesign, and timing issues

If crawl4ai hooks cannot reliably inspect the live state in-place, the base class should keep the page interaction and validation inside one execution boundary rather than bouncing through `about:blank`.

### 2. Introduce a real candidate-profile source for apply

Define one canonical source for candidate application fields required by portal forms.

Minimum expected fields:
- `first_name`
- `last_name`
- `email`
- `phone`

Possible implementations:
- load from a dedicated profile artifact under `data/profiles/`
- pass an explicit profile JSON path through the apply CLI
- reuse an existing normalized profile contract if one already exists elsewhere in the pipeline

The key requirement is that `src/apply/` should not rely on placeholders that are never populated at runtime.

### 3. Capture useful failure artifacts

On failure, preserve the actual browser state that failed.

Useful artifacts would include:
- screenshot from the active page/modal
- current URL at failure time
- short HTML excerpt or page title when available
- explicit classification for common failure modes (not logged in, selector missing, upload rejected, submit not confirmed)

### 4. Promote portal selectors from scaffold to contract

For each provider:
- capture fresh HTML fixtures from real portal flows
- replace placeholder selectors with validated selectors
- prefer stable attributes (`data-testid`, `data-at`, semantic names) over generated classes
- document known selector fragility points per portal

### 5. Tighten test guarantees

The current tests are useful, but they should evolve from optional smoke coverage to stronger contract coverage.

Recommended direction:
- keep pure unit tests for shared helper logic
- ensure portal fixtures are present in a reproducible way
- fail CI when selector-contract fixtures disappear or no longer match
- add at least one higher-level dry-run integration path per provider when feasible

## Suggested Execution Order

1. Fix active-page selector validation.
2. Wire real candidate profile loading into the apply flow.
3. Replace placeholder selectors with validated portal-specific selectors.
4. Improve failure artifacts and failure classification.
5. Strengthen CI expectations around provider fixtures and dry-run coverage.

## Linked TODOs

- `src/apply/smart_adapter.py` - `# TODO(future): validate selectors against the live apply page instead of a detached about:blank session`
- `src/apply/smart_adapter.py` - `# TODO(future): load a real candidate profile contract for apply-field placeholders`
- `src/apply/providers/xing/adapter.py` - `# TODO(future): replace placeholder selectors with fixture-validated XING selectors`
- `src/apply/providers/stepstone/adapter.py` - `# TODO(future): replace placeholder selectors with fixture-validated StepStone selectors`
