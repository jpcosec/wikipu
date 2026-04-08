---
identity:
  node_id: "doc:wiki/drafts/cycle_walkthrough.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/match_review_cycle.md", relation_type: "documents"}
---

### 1) `match` generates assessment and persists round

## Details

### 1) `match` generates assessment and persists round

`match` calls the LLM with:

- `<job_requirements>` and `<profile_evidence>` always,
- optional `<round_feedback>` when regeneration feedback exists.

Then it persists:

1. `nodes/match/approved/state.json` (current canonical persisted match payload)
2. `nodes/match/review/rounds/round_<NNN>/decision.md`
3. mirrored `nodes/match/review/decision.md`

`decision.md` includes front matter:

- `source_state_hash: "sha256:<...>"`
- `node: "match"`
- `job_id`
- `round`

and a review table with per-requirement action checkboxes:

`[ ] Proceed / [ ] Regen / [ ] Reject`

The actionable table now includes a `Req ID` column so parser routing can remain stable even when only a subset of requirements is reviewed.

If regeneration context exists, the markdown also includes a "Feedback Applied from Round X" section.

### 2) Graph pauses at `review_match`

The graph is configured to interrupt before `review_match` in CLI runs.

Operator edits:

- `data/jobs/<source>/<job_id>/nodes/match/review/decision.md`

### 3) `review_match` validates and parses decisions

On resume, `review_match`:

1. Computes expected hash from `nodes/match/approved/state.json`.
2. Validates `source_state_hash` in `decision.md`.
3. Parses checkbox decisions deterministically.

Parsing order:

1. table format (`Action` and `Comments` columns),
2. per-block lines (`Decision [REQ_ID]: ...`),
3. global fallback (`Decision: ...` or `Decision [global]: ...`).

Accepted checkbox marks are strict but tolerant to spacing (for example `[]` and `[ x]`).

### 4) `review_match` writes machine artifacts

When decisions are valid and complete, it writes:

- `nodes/match/review/decision.json`
- `nodes/match/review/rounds/round_<NNN>/decision.json`
- `nodes/match/review/rounds/round_<NNN>/feedback.json`

`feedback.json` maps parsed decisions to actions:

- `approve` -> `proceed`
- `request_regeneration` -> `patch`
- `reject` -> `reject`

Route aggregation rule:

- any `reject` => route `reject`
- else any `request_regeneration` => route `request_regeneration`
- else all `approve` => route `approve`

### 5) Regeneration loop (`request_regeneration`)

When route is `request_regeneration`, graph returns to `match`.

`match` then:

1. loads latest round feedback,
2. appends valid `patch_evidence` items to effective evidence set,
3. derives regeneration scope from feedback entries with `action == "patch"`,
4. includes normalized feedback plus scope in prompt context,
5. generates a new match payload,
6. creates next immutable round (`round_<NNN+1>`).

During regeneration rounds, `decision.md` is split into:

- context section (non-scoped requirements, read-only),
- regeneration scope section (actionable rows only, revalidation loop input).

This avoids revalidating already approved requirements while still keeping full visibility in the review file.

Generated from `raw/docs_postulador_langgraph/docs/runtime/match_review_cycle.md`.