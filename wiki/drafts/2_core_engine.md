---
identity:
  node_id: "doc:wiki/drafts/2_core_engine.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-design.md", relation_type: "documents"}
---

Five components. Each is a vertical slice that delivers value independently.

## Details

Five components. Each is a vertical slice that delivers value independently.

### 2.1 Scanner & Graph Builder

Two-step pipeline: scan (parse tags) → build (resolve references).

- **Input:** Project root + `doc-router.yml`
- **Scan paths:** All directories listed in `doc_paths` for docs; all `src/` (or configured source roots) for code docstrings
- **Output:** `RouteGraph` — the core data model (see below)

**Scanning:**
- Parses YAML frontmatter from `.md` files
- Parses `:doc-*:` from Python docstrings, `@doc-*` from JSDoc
- Validates tags against vocabulary in `doc-router.yml`
- Produces a flat list of `TaggedEntity` records

**Building:**
- Resolves cross-references (`implements`, `doc-ref`, `depends_on`) into edges
- Detects broken links (tag points to nonexistent file/symbol)
- Computes connected components (isolated nodes = potential gaps)
- Caches result at `.doc-router/cache.json`

**Cache invalidation:** The cache stores a hash of each scanned file. On subsequent runs, only files with changed hashes are re-scanned. `doc-router scan --force` rebuilds from scratch.

#### RouteGraph Schema

```json
{
  "nodes": [
    {
      "id": "pipeline-match-design",
      "type": "doc",
      "path": "docs/product/match.md",
      "domain": "pipeline",
      "stage": "match",
      "nature": "philosophy",
      "version": "2026-03-22",
      "symbol": null,
      "tags": { "hitl_gate": null, "contract": null }
    },
    {
      "id": "pipeline-match-impl",
      "type": "code",
      "path": "src/nodes/match/logic.py",
      "domain": "pipeline",
      "stage": "match",
      "nature": "implementation",
      "version": null,
      "symbol": "MatchLogic",
      "tags": { "hitl_gate": "review_match", "contract": "src/nodes/match/contract.py::MatchInput" }
    }
  ],
  "edges": [
    {
      "source": "pipeline-match-design",
      "target": "pipeline-match-impl",
      "type": "implements"
    },
    {
      "source": "pipeline-match-impl",
      "target": "pipeline-match-design",
      "type": "doc-ref"
    }
  ]
}
```

**Node types:** `doc` (markdown file) or `code` (tagged symbol within a source file). A single file can produce multiple `code` nodes if it contains multiple tagged symbols.

**Edge types:** `implements` (doc → code), `doc-ref` (code → doc), `depends_on` (doc → doc), `contract` (any → schema definition).

### 2.2 Drift Detector

Compares tag state against filesystem state.

| Check | Severity | Description |
|-------|----------|-------------|
| **Staleness** | Warning | Content hash of linked code changed since last `doc-router verify` |
| **Broken links** | Error | `implements` or `doc-ref` target doesn't exist |
| **Orphans** | Info | Code with no tags, docs with no `implements` targets |
| **Vocabulary violations** | Error | Tags using domains/stages not in `doc-router.yml` |
| **Asymmetric links** | Warning | Doc declares `implements: X` but X has no `doc-ref` back (or vice versa) |

**Staleness model:** Uses content hashing, not mtime. The scanner stores a hash of each file's tagged symbols. `doc-router verify` marks a doc-to-code link as "verified" by recording the current hash. When the code's hash changes, the link becomes stale. This avoids false positives from formatting-only changes (the hash covers the symbol's signature and body, not whitespace).

**Asymmetric links:** Both `implements` and `doc-ref` are optional individually — you can link from either direction. But the drift detector warns when a link exists in only one direction, since bidirectional links are more robust. This is a warning, not an error — single-direction links are valid for lightweight tagging.

Output: drift report (JSON + human-readable) with severity levels.

### 2.3 Template Engine

Two functions:

**Scaffolding** — Generate new docs/code from templates:

```bash
doc-router new doc --domain pipeline --stage match --nature philosophy
doc-router new code --domain pipeline --stage match --lang python
```

Templates are Jinja2 in the project's `templates/` dir. Auto-populate tags from arguments.

**Runbook generation** — Produce "how to" instructions from tagged code:

```bash
doc-router runbook --domain api --stage match
```

Follows the graph from the target node, collects tagged content and assembles a runbook. The runbook extracts:
- CLI commands from docs tagged with `nature: development`
- API endpoints from docs tagged with `nature: implementation` in the `api` domain
- Config references from `doc-router.yml` and linked contracts
- Related docs from `depends_on` edges

This is what makes "you can always get the code and docs for things" work. The content comes from the tagged docs themselves — no new tag fields needed.

### 2.4 Packet Compiler

The prompt/task generator. Given a task description and explicit coordinates, resolves minimal context.

```bash
# Explicit routing (preferred — deterministic)
doc-router packet --domain pipeline --stage match --task "add confidence field" --type implement

# Keyword fallback (returns candidates for user to select)
doc-router packet --task "add confidence field to match output" --type implement
```

**Resolution strategy:** The compiler does NOT attempt NLP on the task description. Instead:

1. If `--domain` and `--stage` are provided → direct graph lookup (deterministic)
2. If omitted → keyword match against node IDs, tags, and file paths → return ranked candidates → user selects
3. Once the target nodes are identified → follow edges to include contracts, dependencies, HITL gates
4. Apply task-type template (`implement`, `test`, `fix`, `review`)

**Output** — structured packet:

- **Intent:** What to do (the task description)
- **Context:** Relevant files with content (docs) or references (code)
- **Constraints:** Writable paths (derived from `implements` targets) vs read-only (everything else)
- **Acceptance criteria:** How to verify success (from linked test docs and contract schemas)
- **Examples:** Similar past corrections (if correction history exists)

The packet is a markdown file — paste into any LLM, use as a skill prompt, or serve via MCP.

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-design.md`.