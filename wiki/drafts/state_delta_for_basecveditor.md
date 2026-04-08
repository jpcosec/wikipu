---
identity:
  node_id: "doc:wiki/drafts/state_delta_for_basecveditor.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/01_ui/cv_graph_feature_merge.md", relation_type: "documents"}
---

The following state fields need to be added to `BaseCvEditor.tsx` (currently only has `editedEntries`, `editedSkills`, `selectedNodeId`, `selectedNodeType`):

## Details

The following state fields need to be added to `BaseCvEditor.tsx` (currently only has `editedEntries`, `editedSkills`, `selectedNodeId`, `selectedNodeType`):

```ts
const [expandedGroups, setExpandedGroups] = useState<Set<string>>(() => new Set());
const [focusedEntryId, setFocusedEntryId] = useState('');
const [selectedSkillId, setSelectedSkillId] = useState('');
const [selectedGroupCategory, setSelectedGroupCategory] = useState<string | null>(null);
const [activeDropzoneCategory, setActiveDropzoneCategory] = useState<string | null>(null);
```

And the mutation handlers currently in `BaseCvEditor` (`handleEntryChange`, `handleSkillChange`) need to be extended with:
- `onAddEntry(category)`
- `onAddSkill()`
- `onAddDescription(entryId)`
- `onUpdateDescription(entryId, key, text)`
- `onToggleEssential(id, type)`
- `onConnect` (demonstrates edge)
- `onNodeDrag` / `onNodeDragStop` (reorder)
- `moveEntryInsideSelectedGroup(entryId, direction)`

---

Generated from `raw/docs_postulador_langgraph/plan/01_ui/cv_graph_feature_merge.md`.