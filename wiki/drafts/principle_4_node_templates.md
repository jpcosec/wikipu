---
identity:
  node_id: "doc:wiki/drafts/principle_4_node_templates.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/wiki_construction_principles.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/wiki_construction_principles.md"
  source_hash: "adb2697fc76ec9f466878e73986e50abfad611e8104bf6edd4d6d0952660dedf"
  compiled_at: "2026-04-10T17:47:33.734790"
  compiled_from: "wiki-compiler"
---

Different types of knowledge have different required sections.

## Details

Different types of knowledge have different required sections.
A template defines what a node of that type must contain to be complete.
Missing required sections are audit violations.

### `concept`
Question: What is X?
Required: abstract, definition, examples, related_concepts

### `how_to`
Question: How do I do X?
Required: abstract, prerequisites, steps, outcome

### `standard`
Question: What is the rule for X?
Required: abstract, rule, rationale, violation_examples

### `reference`
Question: How does X work technically?
Required: abstract, signature_or_schema, fields, usage_examples

### `index`
Question: What lives in this area?
Required: abstract, node list (via transclusion only — no inline content)

The node_type field in the YAML frontmatter selects the template.
The compiler checks that required sections are present.

---

Generated from `raw/wiki_construction_principles.md`.