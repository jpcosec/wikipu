---
identity:
  node_id: "doc:wiki/concepts/what_the_system_needs_to_be_truly_autopoietic.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/autopoiesis_system.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/autopoiesis_system.md"
  source_hash: "708ee8f8d07379bae69e1774c1cba81002bcbb923d90699210e3c3a09ebf5ea0"
  compiled_at: "2026-04-14T16:50:28.656613"
  compiled_from: "wiki-compiler"
---

The Spanish Wikipedia definition is the most precise:

## Details

The Spanish Wikipedia definition is the most precise:

> "Sistemas que presentan una red de procesos u operaciones (que los definen como tales y los hacen distinguibles de los demás sistemas), y que pueden crear o destruir elementos del mismo sistema, como respuesta a las perturbaciones del medio. Aunque el sistema cambie estructuralmente, dicha red permanece invariante durante toda su existencia, manteniendo la identidad de este."

Mapped to wikipu:

- **Network of processes (invariant):** `build`, `ingest`, `query`, `cleanse`, `curate`, `scaffold`, the Socratic protocol, the gate loop, trail collect. These define what the system *is*. They do not change as content changes.
- **Elements (mutable):** wiki nodes, plans, the graph, docs, the CLI modules themselves, the hausordnung. Created and destroyed in response to perturbations.
- **Perturbations from the medium:** human interactions through gates, files dropped in `raw/`, test failures, execution logs, agent memory, outputs of `src/`.

### The Identity Layer

The invariant network must be governed by declared identity rules — constraints on how processes operate, not on what content exists. These rules define the system's identity. Violating them means the system is no longer itself.

Current identity rules (to be formalized in `wiki/standards/00_house_rules.md`):
- **Orthogonality** — no two elements do the same thing
- **Minimal energy** — prefer the simplest structure that satisfies the requirement; minimize LLM consumption, uncertainty, and topology complexity
- **Typed contracts** — all inter-process data crosses boundaries as Pydantic models
- **Zone separation** — raw / wiki / desk / backlog zones cannot contaminate each other
- **Human gate for structural changes** — the system proposes; humans authorize destruction or restructuring
- **Traceable causality** — every element's existence traces to a perturbation that created it

The hausordnung is not a document *describing* the system — it is a declaration of identity rules *for* the network. Its existence as a graph node, with edges to the processes that enforce each rule, is the precondition for operational closure.

### The Three Missing Layers

**1. Identity layer** — machine-readable, enforced identity rules + self-inclusion in graph
The system currently does not model its own processes as nodes. The CLI commands, agent protocols, and the hausordnung are not in the graph they govern. A system that cannot model itself cannot maintain itself. Self-inclusion is the structural precondition for operational closure.

**2. Perception layer** — drift detection, change watchers, perturbation classification
The system cannot sense its own state. Every process requires manual invocation. Without perception, there is no autonomous response — only a toolbox. The `GitFacet` + `wiki-compiler status` command is the minimal perception apparatus: detect what changed, classify what kind of response it requires.

**3. Response layer** — the complete process suite + the loop coordinator
Most response processes are planned but not implemented (cleanse, curate, trail collect, socratic). The loop coordinator — the process that ties them into a continuous cycle — does not exist. Without it, the individual processes remain independent tools rather than an integrated network.

### The Minimal Energy Rule as Active Constraint

Minimal energy is not just a design principle — it must be an active check in the coordinator. Before any proposal is generated, the coordinator asks: is there a simpler structure that satisfies this requirement? This is a graph query (find nodes with overlapping intent or IO), not a heuristic. If a match exists, extend it rather than create a new element. This keeps the topology minimal and the graph coherent over time.

Generated from `raw/autopoiesis_system.md`.