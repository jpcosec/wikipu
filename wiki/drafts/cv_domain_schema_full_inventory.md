---
identity:
  node_id: "doc:wiki/drafts/cv_domain_schema_full_inventory.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/D1_schema_explorer.md", relation_type: "documents"}
---

### `node_types`

## Details

### `node_types`

| id | label | render_as | color_token | abstract | variant_of |
|----|-------|-----------|-------------|----------|------------|
| CvProfileGraphPayload | CV Profile | group | root | — | — |
| CvEntry | CV Entry | node | abstract | true | — |
| CvEntry.personal_data | Personal Data | node | entity | — | CvEntry |
| CvEntry.contact | Contact | node | entity | — | CvEntry |
| CvEntry.legal_status | Legal Status | node | entity | — | CvEntry |
| CvEntry.education | Education | node | entity | — | CvEntry |
| CvEntry.job_experience | Job Experience | node | entity | — | CvEntry |
| CvEntry.project | Project | node | entity | — | CvEntry |
| CvEntry.publication | Publication | node | entity | — | CvEntry |
| CvEntry.language | Language | node | entity | — | CvEntry |
| CvDescription | Description | attribute | value | — | — |
| CvSkill | Skill | node | skill | — | — |
| CvDemonstratesEdge | Demonstrates | node | edge_node | — | — |

### Children of `CvProfileGraphPayload`

| via | type | group_by | effect |
|-----|------|----------|--------|
| entries | CvEntry | category | Creates one sub-subflow per category value (education, job_experience, etc.) |
| skills | CvSkill | — | Placed as nodes in the right column of the group |
| demonstrates | CvDemonstratesEdge | — | Placed as nodes; their edges connect entries to skills |

### `edge_types`

| id | from | to | label | color_token | cardinality |
|----|------|----|-------|-------------|-------------|
| extends | CvEntry.{variant} | CvEntry | variant of | structural | N:1 |
| demonstrates | CvEntry | CvSkill | demonstrates | semantic | N:M |
| demo_source | CvDemonstratesEdge | CvEntry | source | structural | N:1 |
| demo_target | CvDemonstratesEdge | CvSkill | target | semantic | N:1 |
| demo_keys | CvDemonstratesEdge | CvDescription | evidence | structural | N:M |

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/D1_schema_explorer.md`.