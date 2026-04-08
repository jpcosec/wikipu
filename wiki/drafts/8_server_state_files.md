---
identity:
  node_id: "doc:wiki/drafts/8_server_state_files.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md", relation_type: "documents"}
---

```

## Details

```
~/.config/browser-os/.browseros/
  server_config.json   — ports, flags, version info (read-only reference)
  server.lock          — PID of running BrowserOS process
  server.state         — creation timestamp + PID
  browseros-server.log — server log (JSON lines, useful for debugging MCP errors)
```

### Reading the server log for MCP debugging

```bash
tail -f ~/.config/browser-os/.browseros/browseros-server.log | python3 -c "
import sys, json
for line in sys.stdin:
    try:
        obj = json.loads(line)
        if obj.get('msg') or obj.get('err'):
            print(obj)
    except: pass
"
```

---

Generated from `raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md`.