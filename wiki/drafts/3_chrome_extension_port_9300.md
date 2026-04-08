---
identity:
  node_id: "doc:wiki/drafts/3_chrome_extension_port_9300.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md", relation_type: "documents"}
---

Requires WebSocket upgrade. Initial probe returned `426 Upgrade Required`.

## Details

Requires WebSocket upgrade. Initial probe returned `426 Upgrade Required`.

```python
import websocket  # pip install websocket-client
ws = websocket.WebSocket()
ws.connect("ws://127.0.0.1:9300")
# Send and observe what protocol it speaks
```

**Status:** Unknown capabilities. Likely the communication channel between BrowserOS server and the Chromium extension running inside the browser. May expose page state, user interactions, or extension-specific controls. **Needs exploration.**

---

Generated from `raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md`.