---
identity:
  node_id: "doc:wiki/drafts/condition_variables_snapshot.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/writing-rules.md", relation_type: "documents"}
---

The condition receives a snapshot of the item at evaluation time.

## Details

The condition receives a snapshot of the item at evaluation time.
All variables are plain numbers or strings — use `{ "var": "fieldName" }` to reference them.

| Variable      | Type     | Description                                         | Example      |
|---------------|----------|-----------------------------------------------------|--------------|
| `itemId`      | string   | Item identifier                                     | `'ITEM_001'` |
| `pax`         | number   | Resolved pax count                                  | `50`         |
| `cantidad`    | number   | Resolved unit count                                 | `3`          |
| `duracionMin` | number   | Duration in minutes                                 | `120`        |
| `hora`        | string   | Start time as entered (display only)                | `'21:30'`    |
| `horaMin`     | number   | Start time as **event minutes** (use for comparisons) | `1290`     |
| `horaFinMin`  | number   | End time = `horaMin + duracionMin`                  | `1410`       |
| `dia`         | number   | Day number within the quotation (1-based)           | `2`          |

### Time Variables — Important

`hora` is a raw string (`'21:30'`, `'1:00 AM'`). **Do not use it for comparisons** — string
ordering breaks across midnight and 12h/24h format differences.

Use `horaMin` and `horaFinMin` instead. They are monotonic integers anchored to the venue's
event day (boundary: 09:00). Times before 09:00 are treated as next-day overflow (+1440):

```
09:00 →  540   (day start)
21:00 → 1260
23:59 → 1439
00:00 → 1440   (midnight → next-day)
01:00 → 1500   (1 AM → correctly > 21:00)
08:59 → 1979
```

**Common time thresholds:**

| Time       | `horaMin` | Notes                  |
|------------|-----------|------------------------|
| `09:00`    | 540       | Venue opens (boundary) |
| `18:00`    | 1080      | End of standard day    |
| `21:00`    | 1260      | Overtime threshold     |
| `00:00`    | 1440      | Midnight               |
| `01:00`    | 1500      | Late night             |

---

Generated from `raw/docs_cotizador/docs/GUIDES/writing-rules.md`.