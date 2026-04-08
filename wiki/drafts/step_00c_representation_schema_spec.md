---
identity:
  node_id: "doc:wiki/drafts/step_00c_representation_schema_spec.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

### 1. Architecture Logic

## Details

### 1. Architecture Logic

The representation schema is a per-project YAML/JSON configuration that makes the editor domain-agnostic. It sits between the neo4j canonical base (all data, all attributes) and the editor (which only shows what the schema declares).

**Schema shape:**

```yaml
schema_id: string
display_name: string
theme: ./path/to/theme.css
max_nesting_depth: 3           # default 3, configurable per project

sources:
  - type: neo4j | json_file | api | yaml_file
    # source-specific config

node_types:
  <type_id>:
    label: string              # neo4j label
    display_name: string
    content_type: string       # maps to renderer (entity, container, markdown_text, etc.)
    is_container: boolean
    allowed_children: [type_id]
    container_config:              # only if is_container: true
      child_ordering: manual | attribute  # how children are ordered
      ordering_attribute: string   # if attribute-ordered
      collapse_behavior: summary | hide  # what shows when collapsed
      proxy_edge_style: dashed | dotted  # style for proxy edges
    visual:
      icon: string             # Material Symbol name
      shape: string            # circle, card, diamond, etc.
      color_from: attribute    # attribute → data-* → CSS
      color_scale:             # computed scale, CSS overrides win
        attribute: string
        palette: string
        min: number
        max: number
      size_from: attribute
      badge_from: attribute
    attributes: [string]       # subset shown in editor (graph can have more)
    render_hints:
      precompute_focus: boolean
      lazy_payload: boolean

relation_types:
  <type_id>:
    source: [node_type_id]
    target: [node_type_id]
    visual:
      style: solid | dashed | none
      color: string
      label_from: attribute
    attributes: [string]

views:
  <view_id>:
    display_name: string
    type: filter | subgraph
    # filter type:
    show_node_types: [type_id] | all
    show_relations: [type_id] | all
    # subgraph type:
    query: string              # Cypher query
    layout: preset_type
    load_attributes: [string] | all
```

**Key principles:**
- The schema is a projection — declares which attributes matter for rendering. The graph can have many more.
- Some attributes are lazy-loaded (e.g., `content_path` resolves a file at runtime).
- Multiple views within one schema: some are filters (same graph, different visibility), some are subgraphs (different Cypher query).
- Schema compiles to JSON Schema at load time for RJSF inspector forms.

**Color scale system:**
- Schema declares `color_scale` with attribute, palette name, min/max.
- Editor computes CSS variables at load time from the scale.
- CSS theme can override any specific value — CSS always wins.

### 2. Objectives

1. Schema format is defined and documented with examples
2. Schema validates at load time (missing required fields, invalid references)
3. At least two example schemas exist: CV Profile, Scraping Knowledge Graph
4. Schema compiles node_type attributes to JSON Schema for RJSF
5. Color scales compute CSS variables, CSS overrides work
6. Views of type `subgraph` declare valid Cypher queries
7. Views of type `filter` declare valid node/relation type references

### 3. Don'ts

- **Don't execute user-composed Cypher.** View queries are declared in the schema. The schema is the security boundary.
- **Don't require all attributes to be declared.** The schema is a projection. Undeclared attributes exist in neo4j but are invisible to the editor.
- **Don't couple the schema format to a specific graph database.** neo4j is the current backend, but the schema describes structure, not Cypher. Source adapters handle the database specifics.
- **Don't validate Cypher at schema parse time.** Syntax-check only. Semantic validation (do these labels exist?) happens at first query execution.

### 4. Known Gaps & Open Questions

- **GAP-SCHEMA-01** (Medium): How to handle schema evolution — what happens when a schema changes but saved data follows the old shape? Suggested: schema_version field + migration functions.
- **GAP-SCHEMA-02** (Medium): Cross-schema views (e.g., notes → skills → CV entries) — the `cross_domain` view example references node types from multiple schemas. Need to define whether this requires a merged schema or explicit cross-references.
- **GAP-SCHEMA-03** (Low): Schema inheritance — can a schema extend another? Deferred until a real use case demands it.

### 5. Library Decision Matrix

- **YAML parsing**: `js-yaml` (lightweight, well-maintained) or `yaml` package (spec-complete, heavier). Recommendation: `js-yaml` — sufficient for config files.
- **JSON Schema compilation**: Built into RJSF pipeline. Representation schema attributes → JSON Schema objects via a compile step we write.
- **Schema validation**: `ajv` (already a dependency via RJSF) for validating schema files against a meta-schema.

### 6. Test Plan

- **Unit**: Schema parses without error for both example schemas. Invalid schemas produce clear errors. Attribute → JSON Schema compilation produces correct field types. Color scale computation produces correct CSS variable values.
- **Component**: Editor loads a schema and populates the registry correctly.
- **Integration**: Load CV Profile schema → switch to Evidence view → correct subgraph renders.

### 7. Review Checklist

- [ ] Schema format documented with full reference
- [ ] Two example schemas exist and parse correctly
- [ ] Schema validates at load time with clear error messages
- [ ] Attributes compile to JSON Schema for RJSF
- [ ] Color scales compute and CSS overrides work
- [ ] View queries are schema-declared, not user-composed

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.