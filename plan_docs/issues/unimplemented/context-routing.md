# Context Routing Mechanism

**Explanation:** Before starting any operation (plan, implement, debug, document), an agent needs the relevant wiki nodes, graph edges, and checklists loaded into context. Currently this requires manual graph queries or reading multiple files. A routing mechanism would let a single CLI call (`wiki-compiler context --task "implement cleanser"`) resolve the relevant nodes, return them ranked by relevance, and pre-load the applicable verification checklist — all in one shot.

**Reference:** `wiki/standards/00_house_rules.md` (NAV-1, NAV-3), `plan_docs/issues/unimplemented/query-server-runtime.md`

**What to fix:** Add a `wiki-compiler context` command that:
1. Accepts a natural-language task description or a structured query (`--node`, `--tag`, `--operation-type`).
2. Queries the graph for nodes relevant to the task: direct matches, ancestors, dependents, and related how-to nodes.
3. Returns a ranked context bundle: relevant wiki nodes (prose), applicable verification checklist, open desk items that intersect, and the rule_ids that govern the operation.
4. Output modes: `--print` (markdown to stdout for LLM injection), `--json` (structured for programmatic use).

**Example invocations:**
```
wiki-compiler context --task "add a new module"
wiki-compiler context --node "wiki/how_to/design.md" --operation-type implement
wiki-compiler context --tag cleanser --operation-type debug
```

**Why this matters:** Reduces the cold-start cost of every agent session from "read 10 files" to "run 1 command." Enables consistent, graph-driven context loading rather than ad-hoc file reading.

**Depends on:** `unimplemented/query-server-runtime.md` (graph query layer must exist), `unimplemented/how-to-wiki-section.md` (how-to nodes must exist to be routable), `unimplemented/verification-checklists.md` (checklists must exist to be returned)
