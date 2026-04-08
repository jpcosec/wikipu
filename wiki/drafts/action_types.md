---
identity:
  node_id: "doc:wiki/drafts/action_types.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/writing-rules.md", relation_type: "documents"}
---

| Action              | Effect                              | Blocks item? |

## Details

| Action              | Effect                              | Blocks item? |
|---------------------|-------------------------------------|:------------:|
| `ERROR`             | Blocks item — cannot be added       | ✅ Yes       |
| `WARNING`           | Shows caution — item still works    | ❌ No        |
| `MULTIPLY`          | Price multiplier (future)           | ❌ No        |
| `ADD_FIXED`         | Flat fee added to total (future)    | ❌ No        |
| `SET_VALUE`         | Override unit price (future)        | ❌ No        |
| `SET_TAX`           | Apply named tax rate (future)       | ❌ No        |
| `SET_DEFAULT`       | Override default quantity (future)  | ❌ No        |
| `ADD_ITEM`          | Auto-include another item (future)  | ❌ No        |
| `INVALIDATE_BASKET` | Block entire quotation (future)     | ✅ Yes       |

---

Generated from `raw/docs_cotizador/docs/GUIDES/writing-rules.md`.