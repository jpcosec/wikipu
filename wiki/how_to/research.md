---
identity:
  node_id: "doc:wiki/how_to/research.md"
  node_type: "how_to"
compliance:
  status: "implemented"
  failing_standards: []
---

Researching in Wikipu means ingesting external sources — papers, documentation, analogous systems, session transcripts — into `raw/` as immutable seed material, then processing them through the pipeline to extract and promote knowledge into `wiki/`. The `raw/` directory is the only zone where external content enters the system.

# How to Research

Researching in Wikipu means ingesting external sources — papers, documentation, analogous systems, session transcripts — into `raw/` as immutable seed material, then processing them through the pipeline to extract and promote knowledge into `wiki/`. The `raw/` directory is the only zone where external content enters the system. Agents read from it; neither agents nor humans write agent output back into it. The pipeline converts raw ore into structured, typed, graph-linked wiki nodes.

## Prerequisites

- Understand the four-zone model (ID-4 in `wiki/standards/house_rules.md`): `raw/` is immutable seed; `wiki/` is current truth.
- Know the difference between ingest (parsing `raw/` into graph nodes) and build (compiling `wiki/` into `knowledge_graph.json`).
- Have `wiki-compiler` installed (`pip install -e .` from the repository root).

## Steps

1. Identify the external source to research: a paper, a system's documentation, a design transcript, or an internet resource.
2. Create a file in `raw/` with a descriptive name (e.g., `raw/autopoiesis_system.md`, `raw/socratic_protocol.md`). Use Markdown for prose sources; preserve original structure where possible.
3. Write or paste the source content into the file. Do not edit or synthesize the content yet — `raw/` holds source material, not interpretations.
4. Run `wiki-compiler ingest --source raw/<filename>` to parse the raw file into the graph as an unprocessed node.
5. Review the ingest output. Identify claims, concepts, and structures that belong in `wiki/` as knowledge nodes.
6. For each concept worth promoting, create or update a wiki node in the appropriate `wiki/` subdirectory following the process in `wiki/how_to/document.md`.
7. Link the new wiki nodes back to their source using `edges` with `relation_type: reads_from` referencing the `raw/` file node.
8. Run `wiki-compiler build` to rebuild `knowledge_graph.json` incorporating the new nodes.
9. If the research reveals a design gap or missing implementation, create a plan task per `wiki/how_to/plan.md`.

## Verification

- [ ] Any design gaps discovered during research have a corresponding task in `desk/tasks/`.
