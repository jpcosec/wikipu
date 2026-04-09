# Artifact Schema Validation

**Explanation:** `wiki/standards/artifacts/` defines the schema for every artifact type as human-readable documents. There is no code that actually validates artifacts against these schemas. An agent can produce a malformed issue file or a wiki node with a missing abstract and nothing catches it. The artifact definitions are currently aspirational — they need Pydantic models and a `wiki-compiler validate` command to become enforced contracts.

**Scope:** This issue covers validation of *operational and wiki artifacts* (markdown + YAML frontmatter files: wiki nodes, ADRs, proposals, boards, issues, gates, backlog items). It does NOT cover source code node extraction — that is handled by the scanner plugin interface (see `unimplemented/scanner-plugin-interface.md`). The wiki-compiler is a Python CI/build tool; the language of the source code it describes is irrelevant to artifact validation.

**Reference:** `wiki/standards/artifacts/` (all files), `wiki/standards/00_house_rules.md` (ID-3, MA-5)

**What to fix:** Implement Pydantic models for frontmatter-bearing artifacts and structural validators for body-only artifacts. Expose via `wiki-compiler validate`.

**How to do it:**
1. Create `ArtifactSchema` base Pydantic model with shared fields (`node_id`, `node_type`, `compliance`).
2. Create subclasses: `WikiNodeSchema`, `ADRSchema`, `ProposalSchema` — each maps to the frontmatter schema in `wiki/standards/artifacts/`.
3. Create structural validators (markdown section parsers) for: `BoardValidator`, `IssueValidator`, `BacklogItemValidator`, `GateRowValidator`.
4. Add `wiki-compiler validate <path>` and `wiki-compiler validate --all` CLI commands — report pass/fail per rule_id.
5. Add validation as a step in the pre-push hook and in the issue resolution checklist.

**Depends on:** `unimplemented/query-server-runtime.md` (edge validation requires graph queries)
