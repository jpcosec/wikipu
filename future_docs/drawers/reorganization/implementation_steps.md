---
identity:
  node_id: "doc:wiki/standards/implementation_steps.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/proposed_zone_reorganization.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/proposed_zone_reorganization.md"
  source_hash: "d515fb1307a63d9ce25d8a0f828317f96106499f1b9ba129d60fb96b9787198b"
  compiled_at: "2026-04-11T02:42:45.651810"
  compiled_from: "wiki-compiler"
---

1. Create `desk/tasks/` directory structure

## Details

1. Create `desk/tasks/` directory structure
2. Move current `plan_docs/` issue files to remain as pure issue tracking
3. Create `future_docs/drawers/` for design storage
4. Update documentation to reflect new flow:
   - Issues block implementation → must be resolved first
   - Then pull work from: resolved issues OR ingested raw OR from drawers
   - Work appears in desk/tasks/ for execution
5. Update workflow validation to enforce "no implementation while issues exist"

Generated from `raw/proposed_zone_reorganization.md`.