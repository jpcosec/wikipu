---
identity:
  node_id: "doc:wiki/standards/checklists.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

Verification checklists provide a machine-readable set of binary (pass/fail) checks for core operations in the Wikipu ecosystem. These checklists ensure that "Done" is objective and that all required protocols (OP-4, OP-5, MA-5) are strictly followed before an operation is considered complete.

# ✅ Verification Checklists

## Rule Schema

Each checklist consists of a set of items, where each item includes a description, the `rule_id` it enforces from the `[[house_rules]]`, and the verification method (command or query).

### 1. Issue Resolution Checklist (`issue-resolution`)
*Enforces the OP-4 Protocol.*

1. **Existing Tests Valid?** (OP-4.1) — All existing tests relevant to the changed area still pass.
   `Verification:` `pytest <relevant_tests>`
2. **New Tests Added?** (OP-4.2, MA-5) — Automated tests covering the new behavior or fix are present.
   `Verification:` `ls tests/` or AST scan for new test functions.
3. **Tests Pass?** (OP-4.3, MA-5) — All new and existing tests pass with 100% success.
   `Verification:` `pytest`
4. **Changelog Updated?** (OP-4.4, CS-9) — `changelog.md` contains a concise entry for the change.
   `Verification:` `grep` last change in `changelog.md`.
5. **Issue File Deleted?** (OP-4.5, MA-3) — The issue file in `desk/issues/` has been removed.
   `Verification:` `ls desk/issues/`
6. **Board Updated?** (OP-4.5) — The issue has been removed from `desk/issues/Board.md`.
7. **Committed?** (OP-4.6) — Changes are committed with a clear, imperative message.
   `Verification:` `git status` (should be clean).

### 2. New Wiki Node Checklist (`new-wiki-node`)
*Enforces WK and NAV rules.*

1. **Frontmatter Present?** (WK-5) — Node has valid YAML frontmatter with `identity` and `edges`.
   `Verification:` `wiki-compiler build` (schema check).
2. **Mandatory Abstract?** (WK-2, WK-4) — Node starts with a 1–3 sentence intent summary.
   `Verification:` `wiki-compiler audit` (MissingAbstractCheck).
3. **Required Sections?** (WK-4) — Node contains all sections required for its `node_type`.
   `Verification:` `wiki-compiler audit` (TemplateViolationCheck).
4. **Edges Registered?** (NAV-1) — Relationships to other nodes are explicitly defined in the frontmatter.
   `Verification:` `wiki-compiler query` for outgoing edges.
5. **Status Set?** (NAV-2, WK-5) — `compliance.status` accurately reflects implementation state.
   `Verification:` Manual check or `wiki-compiler audit`.

### 3. New Module Checklist (`new-module`)
*Enforces MA and CS rules.*

1. **Topology Approved?** (ID-1, ID-5) — A `TopologyProposal` was validated and approved.
   `Verification:` `wiki-compiler validate` on the proposal file.
2. **Contracts Defined?** (ID-3, MA-2, CS-4) — `contracts.py` contains Pydantic models for all I/O.
   `Verification:` `ls <module>/contracts.py`
3. **Descriptions Mandatory?** (ID-3, CS-5) — All Pydantic fields have `Field(description=...)`.
   `Verification:` `wiki-compiler audit`.
4. **Docstrings Present?** (CS-2, CS-3) — Module, classes, and public functions have structured docstrings.
   `Verification:` `wiki-compiler audit` (undocumented_code).
5. **Reference Node Created?** (WK-6) — A corresponding node exists in `wiki/reference/`.
   `Verification:` `ls wiki/reference/`
6. **Tests Added?** (MA-5) — Unit and integration tests cover the module's core logic.
   `Verification:` `ls tests/`

### 4. Structural Change Checklist (`structural-change`)
*Enforces ID rules.*

1. **Orthogonality Check?** (ID-1) — Change does not introduce redundancy or overlap.
   `Verification:` `wiki-compiler validate`.
2. **No Orphans?** (ID-6) — No nodes are left without incoming or outgoing edges (unless root).
   `Verification:` `wiki-compiler audit`.
3. **Zone Integrity?** (ID-4) — No cross-zone references (e.g., `wiki/` referencing `plan_docs/`).
   `Verification:` `wiki-compiler build` (edge validation).
4. **Build Passes?** — `wiki-compiler build` runs without errors and compliance is at or above baseline.
   `Verification:` `wiki-compiler build`.

### 5. Session Closure Checklist (`session-close`)
*Enforces OP-5 and MA-6.*

1. **Issue Status Clear?** (OP-1) — All issues worked on are either resolved (deleted) or updated.
   `Verification:` `git status` + `ls desk/issues/`.
2. **Changelog Reflects Work?** (CS-9) — All significant session changes are recorded.
   `Verification:` `cat changelog.md`.
3. **Clean Worktree?** (OP-4.6) — All intended changes are committed.
   `Verification:` `git status`.
4. **Trail Collect Done?** (MA-6) — Friction or rule improvements discovered are encoded.
   `Verification:` Check for updates to `wiki/standards/` or `wiki/concepts/`.

## Fields

| Field | Description |
|---|---|
| Checklist Name | Unique identifier for the operation class. |
| Item | A specific, binary check to perform. |
| rule_id | The ID of the rule from `[[house_rules]]` being enforced. |
| Verification | The suggested command or query to verify the check. |

## Usage Examples

### Example: Verifying an Issue Resolution
An agent resolving `fix-auth-bug` would run through the `issue-resolution` checklist:
1. `pytest tests/test_auth.py` -> PASS
2. `ls tests/test_auth_bug_fix.py` -> PASS
3. `pytest` -> PASS
4. `grep "fix auth bug" changelog.md` -> PASS
5. `ls desk/issues/fix-auth-bug.md` -> FILE NOT FOUND (PASS)
6. `grep "fix-auth-bug" desk/issues/Board.md` -> NOT FOUND (PASS)
7. `git status` -> "nothing to commit, working tree clean" (PASS)
