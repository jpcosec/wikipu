---
identity:
  node_id: "doc:wiki/drafts/task_1_fix_intelligenteditor_decorations_onspanselect.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Modify: `src/components/organisms/IntelligentEditor.tsx`

The current `tag-hover` mode has broken decoration code: `EditorView.decorations.compute` with an async `import()` inside — this returns a Promise, not a DecorationSet.

Fix with a `StateField` that holds the DecorationSet synchronously. Also add `onSpanSelect` prop for B2 tagging workflow.

- [ ] **Step 1: Replace IntelligentEditor with fixed version**

Replace the entire file with:

```tsx
import { useCallback, useMemo } from 'react';
import CodeMirror from '@uiw/react-codemirror';
import { markdown } from '@codemirror/lang-markdown';
import { json } from '@codemirror/lang-json';
import { oneDark } from '@codemirror/theme-one-dark';
import { EditorView, Decoration, DecorationSet } from '@codemirror/view';
import { StateField, StateEffect } from '@codemirror/state';
import { RangeSetBuilder } from '@codemirror/state';
import { cn } from '../../utils/cn';
import type { RequirementItem } from '../../types/api.types';

type EditorMode = 'fold' | 'tag-hover' | 'diff';
type EditorLanguage = 'markdown' | 'json' | 'text';

interface Highlight {
  from: number;
  to: number;
  className?: string;
  priority?: 'must' | 'nice';
}

interface Props {
  mode: EditorMode;
  content: string;
  language?: EditorLanguage;
  highlights?: Highlight[];
  requirements?: RequirementItem[];
  readOnly?: boolean;
  onChange?: (value: string) => void;
  onSpanSelect?: (range: { start: number; end: number; text: string }) => void;
  className?: string;
}

const terranTheme = EditorView.theme({
  '&': { backgroundColor: 'transparent', fontSize: '12px' },
  '.cm-content': { fontFamily: 'JetBrains Mono, monospace', padding: '12px 0' },
  '.cm-gutters': {
    backgroundColor: 'transparent',
    borderRight: '1px solid rgba(132, 148, 149, 0.1)',
    color: '#849495',
    fontSize: '10px',
  },
  '.cm-lineNumbers .cm-gutterElement': { padding: '0 8px 0 12px', minWidth: '32px' },
  '.cm-activeLine': { backgroundColor: 'rgba(0, 242, 255, 0.05)' },
  '.cm-selectionBackground, ::selection': { backgroundColor: 'rgba(0, 242, 255, 0.2) !important' },
  '.cm-cursor': { borderLeftColor: '#00f2ff' },
});

const highlightStyles = EditorView.baseTheme({
  '.cm-highlight-must': {
    backgroundColor: 'rgba(255, 170, 0, 0.15)',
    borderLeft: '2px solid rgba(255, 170, 0, 0.5)',
    borderRight: '2px solid rgba(255, 170, 0, 0.5)',
  },
  '.cm-highlight-nice': {
    backgroundColor: 'rgba(132, 148, 149, 0.1)',
    borderLeft: '2px solid rgba(132, 148, 149, 0.3)',
    borderRight: '2px solid rgba(132, 148, 149, 0.3)',
  },
});

function buildDecorationField(highlights: Highlight[]) {
  return StateField.define<DecorationSet>({
    create() {
      if (highlights.length === 0) return Decoration.none;
      const builder = new RangeSetBuilder<Decoration>();
      const sorted = [...highlights].sort((a, b) => a.from - b.from);
      for (const h of sorted) {
        if (h.from < h.to && h.className) {
          builder.add(h.from, h.to, Decoration.mark({ class: h.className }));
        }
      }
      return builder.finish();
    },
    update(deco) { return deco; },
    provide: f => EditorView.decorations.from(f),
  });
}

export function IntelligentEditor({
  mode,
  content,
  language = 'markdown',
  highlights = [],
  requirements = [],
  readOnly = false,
  onChange,
  onSpanSelect,
  className,
}: Props) {
  const reqHighlights = useMemo(() => {
    if (mode !== 'tag-hover' || requirements.length === 0) return highlights;
    const from_reqs = requirements
      .filter(r => r.char_start != null && r.char_end != null)
      .map(r => ({
        from: r.char_start!,
        to: r.char_end!,
        className: r.priority === 'must' ? 'cm-highlight-must' : 'cm-highlight-nice',
        priority: r.priority as 'must' | 'nice',
      }));
    return [...highlights, ...from_reqs];
  }, [mode, highlights, requirements]);

  const extensions = useMemo(() => {
    const exts: Parameters<typeof CodeMirror>[0]['extensions'] = [
      terranTheme,
      highlightStyles,
      EditorView.lineWrapping,
    ];
    if (language === 'markdown') exts.push(markdown());
    else if (language === 'json') exts.push(json());

    if (mode === 'fold') {
      // fold mode: no extra extensions
    } else if (mode === 'tag-hover' && reqHighlights.length > 0) {
      exts.push(buildDecorationField(reqHighlights));
    }

    if (onSpanSelect) {
      exts.push(
        EditorView.domEventHandlers({
          mouseup(event, view) {
            const sel = view.state.selection.main;
            if (sel.empty) return;
            const text = view.state.sliceDoc(sel.from, sel.to);
            if (text.trim()) {
              onSpanSelect({ start: sel.from, end: sel.to, text });
            }
          },
        })
      );
    }

    return exts;
  }, [mode, language, reqHighlights, onSpanSelect]);

  const handleChange = useCallback((value: string) => {
    onChange?.(value);
  }, [onChange]);

  return (
    <div className={cn('h-full overflow-hidden', className)}>
      <CodeMirror
        value={content}
        height="100%"
        theme={oneDark}
        extensions={extensions}
        onChange={handleChange}
        editable={!readOnly}
        basicSetup={{
          lineNumbers: true,
          highlightActiveLineGutter: true,
          foldGutter: mode === 'fold',
          drawSelection: true,
          syntaxHighlighting: true,
          highlightActiveLine: true,
        }}
      />
    </div>
  );
}
```

- [ ] **Step 2: Verify build passes**

```bash
cd /home/jp/phd-workspaces/dev/.worktrees/ui-redesign/apps/review-workbench && npx tsc --noEmit 2>&1 | head -30
```

Expected: no errors related to IntelligentEditor.

- [ ] **Step 3: Commit**

```bash
cd /home/jp/phd-workspaces/dev/.worktrees/ui-redesign
git add apps/review-workbench/src/components/organisms/IntelligentEditor.tsx
git commit -m "fix(ui): fix IntelligentEditor decoration + add onSpanSelect (component_map)"
```

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md`.