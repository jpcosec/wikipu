---
identity:
  node_id: "doc:wiki/drafts/step_00d_css_theme_system.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

### 1. Architecture Logic

## Details

### 1. Architecture Logic

The CSS theme is an editable file per project, Obsidian-style. The editor never hardcodes colors, shapes, or sizes — it renders structure, the theme paints it.

**Bridge between schema and CSS:** The schema's `color_from`, `size_from`, `badge_from`, `shape` declarations cause the editor to set `data-*` attributes on DOM elements. The CSS theme targets those attributes.

**Theme layers (cascading):**
1. Editor default variables (built-in fallbacks)
2. Schema-computed scales (from `color_scale` declarations)
3. Project theme file (referenced in schema's `theme` field)
4. CSS always wins — any variable can be overridden

**Default theme:** MD3 token system from the mockups — surface hierarchy, primary/secondary/tertiary containers, glass panels with backdrop-blur, Manrope headlines + Inter body, Material Symbols Outlined icons, dot grid canvas, rounded cards.

### 2. Objectives

1. All visual properties are driven by CSS variables, never hardcoded in components
2. `data-*` attributes are set on DOM elements from schema visual config
3. Default MD3 theme renders all node types correctly
4. A custom .css file can override any visual property
5. Schema color scales generate CSS variables at load time
6. Theme file is hot-reloadable during development

### 3. Don'ts

- **Don't inline styles in React components.** All visual properties via CSS variables or Tailwind utilities that reference CSS variables.
- **Don't hardcode MD3 tokens as the only option.** MD3 is the default theme. The system must work with any CSS file that defines the required variables.
- **Don't couple component structure to theme assumptions.** Components render semantic `data-*` attributes. How those look is the theme's job.

### 4. Known Gaps & Open Questions

- **GAP-THEME-01** (Medium): Dark mode. The mockups show light mode only. Need to decide: is dark mode a second theme file, or does the same theme support both via `prefers-color-scheme`? Suggested: theme files can use media queries, editor doesn't enforce either.
- **GAP-THEME-02** (Low): Theme validation — how to warn when a theme is missing required variables? Suggested: editor logs warnings in dev mode for undefined CSS variables.

### 5. Library Decision Matrix

No additional libraries. Tailwind CSS (already in use) + CSS custom properties + `data-*` attribute selectors.

### 6. Test Plan

- **Unit**: CSS variable computation from schema color scales produces expected values.
- **Component**: Default theme renders all built-in node types without unstyled elements.
- **Integration**: Load custom theme → visual overrides apply → switch back to default → overrides removed.

### 7. Review Checklist

- [ ] No hardcoded colors/sizes in React components
- [ ] `data-*` attributes present on all schema-driven elements
- [ ] Default MD3 theme renders everything
- [ ] Custom theme file overrides apply correctly
- [ ] Color scales generate correct CSS variables

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.