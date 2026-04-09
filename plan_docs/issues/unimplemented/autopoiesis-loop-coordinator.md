# Autopoiesis Loop Coordinator

**Explanation:** The individual processes (build, ingest, cleanse, curate, socratic, trail collect) exist or are planned as independent commands. What does not exist is the coordinator that ties them into a continuous, self-correcting cycle. Without the coordinator, the system is a toolbox — useful but inert. With it, the system becomes a network that responds to perturbations, maintains its own coherence, and improves across sessions. The coordinator is the operational form of autopoiesis for this system.

**Reference:** `raw/autopoiesis_system.md`, `raw/trail_collect.md`, `raw/socratic_protocol.md`

**The cycle:**
```
status (detect perturbations)
    ↓
classify perturbations → response plan
    ↓
execute non-structural responses autonomously (ingest new raw/, rebuild graph)
    ↓
generate proposals for structural responses (CleansingProposal, TopologyProposal, Socratic questions)
    ↓
write open gates to desk/Gates.md
    ↓
wait for human gate resolution
    ↓
apply approved proposals (cleanse --apply, scaffold, doc patch)
    ↓
trail collect → encode session artifacts
    ↓
rebuild graph
    ↓
write session log
    ↓
repeat
```

**What to fix:**
1. Implement `wiki-compiler run` command — the coordinator entry point. Runs one full cycle: status → classify → execute → propose → gate → (pause for human) → apply → collect → rebuild → log.
2. Implement the perturbation classifier (maps `status` output to response categories: auto-executable vs. gate-required).
3. Implement trail collect as a subprocess within `run`: at cycle close, scan desk/ for resolved gates and newly created artifacts, classify by type, route each to its destination (doc update, new issue, raw seed, changelog entry).
4. Implement the minimal energy check: before any proposal is generated, ask whether the same requirement can be satisfied by extending an existing node rather than creating a new one. This is a query against the graph, not a heuristic.
5. Write cycle output to `desk/autopoiesis/cycles/<timestamp>.json` for `wiki-compiler history` to consume.

**How to do it:**
- `wiki-compiler run` is a sequential orchestrator — it calls the other commands as library functions, not subprocess shells.
- The pause-for-human step is explicit: after writing to `desk/Gates.md`, `run` prints "Gates opened. Resolve them and run again to continue." It does not block indefinitely.
- On re-invocation, `run` checks `desk/Gates.md` first: if open gates exist, it checks which ones are resolved (file deleted or marked approved) before continuing.
- Minimal energy check: `StructuredQuery` against the graph for nodes with overlapping `SemanticFacet.intent` or `IOFacet` before any `TopologyProposal` is submitted.

**Identity rule enforcement:**
The coordinator is also the enforcement point for identity rules declared in the hausordnung. Before executing any response, it checks the proposed action against the identity rules. A response that would violate orthogonality, zone separation, or the minimal energy principle is rejected and converted into a Socratic question instead.

**Depends on:**
- `unimplemented/perception-layer.md` (status command must exist)
- `unimplemented/cleansing-protocol.md` (cleanse --apply must be callable)
- `unimplemented/query-server-runtime.md` (minimal energy check requires graph queries)
- `gaps/duplicate-docs-cleanup.md` (identity rules must be declared before they can be enforced)
