---
identity:
  node_id: "doc:wiki/drafts/common_mistakes_to_avoid.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/creating-a-component.md", relation_type: "documents"}
---

❌ **DON'T:** Access the machine directly in UI code

## Details

❌ **DON'T:** Access the machine directly in UI code
```javascript
// Bad
const actor = component._actor.send(...);
```
✅ **DO:** Use public component API
```javascript
// Good
component.setValue(value);
```

❌ **DON'T:** Put I/O or async in domain functions
```javascript
// Bad
export function fetchData() { return fetch(...); }
```
✅ **DO:** Keep domain pure
```javascript
// Good
export function processData(data) { return transformed; }
```

❌ **DON'T:** Hardcode configuration
```javascript
// Bad
const MAX = 100;
```
✅ **DO:** Use definition parameter
```javascript
// Good
const { max = 100 } = definition;
```

---

Generated from `raw/docs_cotizador/docs/GUIDES/creating-a-component.md`.