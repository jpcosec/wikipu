---
identity:
  node_id: "doc:wiki/drafts/port_map.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md", relation_type: "documents"}
---

| Port | Protocol | Interface | Notes |

## Details

| Port | Protocol | Interface | Notes |
|------|----------|-----------|-------|
| **9200** | HTTP | MCP server | Primary automation interface. All 60 browser tools available here. |
| **9101** | WebSocket | CDP (Chrome DevTools Protocol) | Full Chromium control: DOM events, JS injection, network, input recording. |
| **9300** | WebSocket | Chrome Extension | Requires `Upgrade: websocket`. Capabilities unknown — needs exploration. |

---

Generated from `raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md`.