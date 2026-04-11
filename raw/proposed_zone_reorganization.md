# Proposed Wikipu Zone Reorganization

## Problem Statement
The current `plan_docs/` structure conflates issue tracking with active task management, leading to confusion about what constitutes "blocking work" vs. "work in progress."

## Proposed Solution
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

## Implementation Steps
1. Create `desk/tasks/` directory structure
2. Move current `plan_docs/` issue files to remain as pure issue tracking
3. Create `future_docs/drawers/` for design storage
4. Update documentation to reflect new flow:
   - Issues block implementation → must be resolved first
   - Then pull work from: resolved issues OR ingested raw OR from drawers
   - Work appears in desk/tasks/ for execution
5. Update workflow validation to enforce "no implementation while issues exist"

## Benefits
- Clear separation: blocking issues vs. ready work
- Explicit consumption model for designs (drawers vs. raw)
- Prevents premature implementation while known issues exist
- Maintains raw/ as true immutable source
- Provides staging area for complete future designs

## Open Questions
- Exact location for desk/tasks/ (desk/ is preferred for consistency)
- Naming: "drawers" vs. alternative terms
- How to handle partially completed designs
- Integration with existing socratic/proposal/gate workflows