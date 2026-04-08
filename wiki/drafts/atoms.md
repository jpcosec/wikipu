---
identity:
  node_id: "doc:wiki/drafts/atoms.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/components.md", relation_type: "documents"}
---

### `<Button>`

## Details

### `<Button>`

**Path:** `components/atoms/Button.tsx`

**Props:**
```ts
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'ghost' | 'danger';
  size?: 'sm' | 'md';
  loading?: boolean;
}
```

**Usage:**
```tsx
<Button variant="primary" size="md">Submit</Button>
<Button variant="ghost" loading>Loading...</Button>
<Button variant="danger" size="sm">Delete</Button>
```

**Styles:**
- `primary` → `bg-primary text-primary-on tactical-glow`
- `ghost` → `bg-transparent hover:bg-primary/10`
- `danger` → `bg-error text-error-on`

---

### `<Badge>`

**Path:** `components/atoms/Badge.tsx`

**Props:**
```ts
interface BadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  variant?: 'primary' | 'secondary' | 'success' | 'muted';
  size?: 'xs' | 'sm';
}
```

**Usage:**
```tsx
<Badge variant="primary">VERIFIED</Badge>
<Badge variant="secondary" size="xs">MUST</Badge>
<Badge variant="success">COMPLETED</Badge>
<Badge variant="muted">PENDING</Badge>
```

---

### `<Tag>`

**Path:** `components/atoms/Tag.tsx`

**Props:**
```ts
interface TagProps {
  id: string;
  category: 'skill' | 'req' | 'risk';
  onHover?: (id: string) => void;
  onClick?: (id: string) => void;
}
```

**Usage:**
```tsx
<Tag id="skill_1" category="skill">Python</Tag>
<Tag id="req_1" category="req" onHover={() => setHighlighted('req_1')}>ML Experience</Tag>
```

**Styles:**
- `skill` → `border-l-4 border-primary bg-primary/5`
- `req` → `border-l-4 border-secondary bg-secondary/5`
- `risk` → `border-l-4 border-error bg-error/5`

---

### `<Icon>`

**Path:** `components/atoms/Icon.tsx`

**Props:**
```ts
interface IconProps {
  name: string;  // Lucide icon name
  size?: 'xs' | 'sm' | 'md';
  className?: string;
}
```

**Usage:**
```tsx
<Icon name="FileJson" size="sm" />
<Icon name="CheckCircle" className="text-primary" />
```

---

### `<Spinner>`

**Path:** `components/atoms/Spinner.tsx`

**Props:**
```ts
interface SpinnerProps {
  size?: 'xs' | 'sm' | 'md';
}
```

**Usage:**
```tsx
<Spinner size="sm" />
{isLoading && <Spinner />}
```

---

### `<Kbd>`

**Path:** `components/atoms/Kbd.tsx`

**Props:**
```ts
interface KbdProps {
  keys: string[];  // e.g., ['Ctrl', 'S']
}
```

**Usage:**
```tsx
<Kbd keys={['Ctrl', 'S']} />
<Kbd keys={['⌘', 'Enter']} />
```

**Styles:** `font-mono text-xs bg-surface-high border border-outline/30 px-1 rounded`

---

### `<ShortcutsModal>`

**Path:** `components/atoms/ShortcutsModal.tsx`

**Usage:**
```tsx
<ShortcutsModal isOpen={isOpen} onClose={() => setIsOpen(false)} />
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/components.md`.