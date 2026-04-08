---
identity:
  node_id: "doc:wiki/drafts/tailwind_config_reference.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/design_system.md", relation_type: "documents"}
---

```js

## Details

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        bg: '#0c0e10',
        surface: '#121416',
        'surface-low': '#1a1c1e',
        'surface-container': '#1e2022',
        'surface-high': '#282a2c',
        'surface-highest': '#333537',
        primary: '#00f2ff',
        'primary-dim': '#99f7ff',
        secondary: '#ffaa00',
        'secondary-dim': '#fecb00',
        error: '#ffb4ab',
        'text-main': '#e2e2e5',
        'text-muted': '#849495',
        'text-faint': '#3a494b',
      },
      fontFamily: {
        headline: ['Space Grotesk', 'sans-serif'],
        body: ['Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      boxShadow: {
        'tactical': '0 0 15px rgba(0, 242, 255, 0.15)',
        'alert': '0 0 15px rgba(255, 170, 0, 0.15)',
      },
      animation: {
        'pulse-flow': 'pulse-flow 3s linear infinite',
      },
    },
  },
}
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/design_system.md`.