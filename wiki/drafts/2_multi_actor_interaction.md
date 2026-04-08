---
identity:
  node_id: "doc:wiki/drafts/2_multi_actor_interaction.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/04_best_practices.md", relation_type: "documents"}
---

Each component is logically paired with an XState actor that manages its lifecycle, event handling, and asynchronous operations. The domain object holds the calculated state; the actor holds the machine state and triggers recalculation.

## Details

Each component is logically paired with an XState actor that manages its lifecycle, event handling, and asynchronous operations. The domain object holds the calculated state; the actor holds the machine state and triggers recalculation.

### Parent-to-Child Context Flow

```
ContainerActor ──[SET_CONTEXT event]──► ChildActor
                                           │
                                    child.receiveContext(ctx)
                                    child.evaluateRules(fn)
                                    child.resolveQuantities()
                                    child.calculatePrice()
```

The `SET_CONTEXT` event pattern:

```js
// In the parent container's actor machine (action):
function propagateContextToChildren(ctx) {
  const mergedContext = { ...ctx.inheritedContext, ...ctx.ruleOutputs };
  for (const childRef of ctx.childActors.values()) {
    childRef.send({ type: 'SET_CONTEXT', context: mergedContext });
  }
}

// In the child item's actor machine (event handler):
on: {
  SET_CONTEXT: {
    actions: assign(({ context, event }) => {
      context.domainItem
        .receiveContext(event.context)
        .evaluateRules(context.evaluator)
        .resolveQuantities()
        .calculatePrice();
      return {};
    })
  }
}
```

### Child-to-Parent Snapshot Bubbling

When a child's state changes, the parent needs to re-aggregate. Use subscriptions:

```js
// In parent container setup (actor action or service):
function subscribeToChild(childRef, parentRef) {
  const subscription = childRef.subscribe((snapshot) => {
    parentRef.send({ type: 'CHILD_UPDATED', childId: snapshot.context.itemId });
  });
  return subscription; // MUST be stored for cleanup
}
```

### Subscription Lifecycle and Cleanup

**The critical rule:** every call to `childRef.subscribe()` returns an unsubscribe function. It must be stored and called when the child is removed or the parent is torn down.

```js
// Correct: store subscriptions, clean up on removal
const subscriptions = new Map();

function addChild(id, childRef) {
  const sub = childRef.subscribe(handleChildUpdate);
  subscriptions.set(id, sub);
}

function removeChild(id) {
  const sub = subscriptions.get(id);
  sub?.unsubscribe();
  subscriptions.delete(id);
}

// Wrong: subscription leaked, no cleanup possible
childRef.subscribe(handleChildUpdate);
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/04_best_practices.md`.