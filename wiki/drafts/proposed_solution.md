---
identity:
  node_id: "doc:wiki/drafts/proposed_solution.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/proposed_zone_reorganization.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/proposed_zone_reorganization.md"
  source_hash: "d515fb1307a63d9ce25d8a0f828317f96106499f1b9ba129d60fb96b9787198b"
  compiled_at: "2026-04-11T02:42:45.651761"
  compiled_from: "wiki-compiler"
---

Split `plan_docs/` into two distinct zones and introduce a new organizational concept:

## Details

Split `plan_docs/` into two distinct zones and introduce a new organizational concept:

### 1. Issue Tracking Zone (remains in plan_docs/ but refined)
- **Purpose**: Track gaps (existing things that are wrong/incomplete) and unimplemented features
- **Rule**: Nothing can be implemented while there are open items in this zone
- **Contents**:
  - `plan_docs/issues/gaps/` - for existing wrong/incomplete things
  - `plan_docs/issues/unimplemented/` - for designed-but-not-built features

### 2. Active Task Zone (new location: desk/tasks/)
- **Purpose**: Hold actionable work items ready for implementation
- **Sources**: 
  - Resolved issues from plan_docs/ (when gaps/unimplemented are fixed)
  - Ingested material from raw/ (consumed but not deleted)
  - Material from future_docs/ (when pulled forward)
  - Completed designs from drawers/
- **Nature**: Ephemeral - tasks deleted when completed

### 3. Drawers Concept (new: future_docs/drawers/)
- **Purpose**: Store complete future designs ready for implementation
- **Structure**: Each drawer contains a complete design package
- **Contents**: `future_docs/drawers/<design-name>/` with all necessary files
- **Rule**: When a design is taken from a drawer for implementation:
  - It is **consumed/deleted** from the drawer
  - It becomes an active task in desk/tasks/
  - Unlike raw/, drawer contents are removed when used

### 4. Material Flow Distinctions
- **raw/**: Immutable source
  - When material is taken: marked as "ingested" but **NOT deleted** from raw/
  - Can be re-ingested multiple times (reference material)
  
- **drawers/**: Consumable designs
  - When a design is taken: it is **deleted/consumed** from the drawer
  - One-time use (like taking a blueprint from a cabinet)

### 5. Desk as Working Metaphor
- `desk/tasks/` represents the clear workspace where active implementation happens
- The desk is only clear when:
  - All issues in plan_docs/ are resolved (blocking work done)
  - All active tasks in desk/tasks/ are completed
  - Then: ready to pull next design from drawers/

Generated from `raw/proposed_zone_reorganization.md`.