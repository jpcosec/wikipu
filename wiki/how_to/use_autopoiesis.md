---
identity:
  node_id: "doc:wiki/how_to/use_autopoiesis.md"
  node_type: "how_to"
compliance:
  status: "implemented"
  failing_standards: []
---

The autopoietic cycle is the mechanism by which Wikipu maintains and reproduces itself — feeding its own state back through the pipeline as source material for a new generation of the system. Trigger the cycle after each significant development phase when the system has drifted from its own description or when accumulated ore in `raw/` is ready to be processed.

# How to Use Autopoiesis

The autopoietic cycle is the mechanism by which Wikipu maintains and reproduces itself — feeding its own state back through the pipeline as source material for a new generation of the system. Borrowed from systems biology (Maturana and Varela, 1972), autopoiesis in this context means the system's operation continuously regenerates the components that constitute it: the wiki, the graph, the rules, and the CLI are all inputs as well as outputs of the cycle. Trigger the cycle after each significant development phase — when the system has drifted from its own description, when accumulated ore in `raw/` is ready to be processed, or when the rules need revision based on friction discovered in operation. The steps are defined in OP-8 of `wiki/standards/house_rules.md`. 

## Prerequisites

- The current development phase is complete: all active issues in `desk/` are resolved, tests pass, and `changelog.md` is updated.
- `wiki-compiler` is installed and `wiki-compiler build` runs without errors on the current state.
- Familiarity with OP-8 in `wiki/standards/house_rules.md` — the eight-step cycle definition.

## Steps

1. Run `git tag v<n>` to snapshot the current state before the cycle begins. This creates a recoverable baseline.
2. Clear processed ore from `raw/`: delete external project docs, obsolete seeds, or any raw material that has already been fully promoted to `wiki/` and no longer serves as new input. Do not delete raw material that has not been ingested yet.
3. Evaluate the system against its own rules: what is redundant (two nodes covering the same concept), lacking (a rule that references an unimplemented mechanism), or upgradeable (a rule whose enforcement is weak or undefined)?
4. Research new sources if the evaluation reveals gaps that require external input — papers, analogous systems, or updated documentation. Ingest them via `wiki/how_to/research.md`.
5. Put the current system's own state back into `raw/` as ore: export or copy the current `wiki/` content, `house_rules.md`, and relevant agent protocol descriptions as raw seed files.
6. Run `wiki-compiler ingest` on the new and re-seeded raw files, then `wiki-compiler build` to regenerate `knowledge_graph.json` from the updated `wiki/`.
7. Write a new version of `house_rules.md` incorporating what the cycle revealed: rules that caused friction should be tightened or removed; gaps in enforcement should be closed.
8. Commit. The commit message should name the cycle version and summarize what changed. Example: `autopoiesis v3: encode constraint-closure rule, remove obsolete MA-6 note`.

## Verification

- [ ] A `git tag v<n>` exists marking the pre-cycle snapshot.
- [ ] `raw/` contains only unprocessed or re-seeded material — no stale processed ore.
- [ ] `wiki-compiler build` runs without errors after the cycle.
- [ ] `house_rules.md` has been revised to reflect what the cycle revealed — it is not identical to the pre-cycle version.
- [ ] `changelog.md` records the cycle completion with the version tag.
- [ ] All active `desk/` items were resolved before the cycle began — the cycle is a phase boundary, not an escape from unfinished work.
