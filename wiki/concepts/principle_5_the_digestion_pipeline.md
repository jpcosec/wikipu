---
identity:
  node_id: "doc:wiki/concepts/principle_5_the_digestion_pipeline.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/wiki_construction_principles.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/wiki_construction_principles.md"
  source_hash: "adb2697fc76ec9f466878e73986e50abfad611e8104bf6edd4d6d0952660dedf"
  compiled_at: "2026-04-14T16:50:28.667099"
  compiled_from: "wiki-compiler"
---

Free text is the input. Structured nodes are the output.

## Details

Free text is the input. Structured nodes are the output.
The raw text is never deleted — it is the ore. The wiki nodes are the refined metal.

Pipeline:

    raw/                    immutable free text (source material)
      ↓ wiki-compiler ingest
    wiki/drafts/            proposed atomic nodes with template stubs
      ↓ human or LLM review
    wiki/                   approved, structured, indexed nodes

The ingest step does not just create stubs. It:
1. Reads the raw text
2. Identifies concepts, processes, standards, and references within it
3. Proposes a split into atomic nodes, each with the appropriate template
4. Outputs draft nodes for review — one file per proposed concept

The review step decides: approve as-is, merge two proposals, split one further,
or reject and rephrase. Only approved nodes enter wiki/.

The raw source is archived, not deleted. The link between
a wiki node and its raw origin is an edge: raw_source → wiki_node (documents).

---

Generated from `raw/wiki_construction_principles.md`.