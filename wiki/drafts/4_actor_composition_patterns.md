---
identity:
  node_id: "doc:wiki/drafts/4_actor_composition_patterns.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/04_best_practices.md", relation_type: "documents"}
---

### Pattern A: Parent Owns Child Actors

## Details

### Pattern A: Parent Owns Child Actors

The most common pattern. The parent container creates child actors when items are added, manages their lifecycle, and tears them down when items are removed.

```js
// In parent container machine:
ADD_ITEM: {
  actions: assign(({ context, event }) => {
    const childDomain = ProductItem.fromDefinition(event.definition, {
      pricingFn: context.pricingFn,
      evaluator: context.evaluator,
    });
    const childActor = createActor(itemMachine, {
      input: { definition: event.definition, evaluator: context.evaluator }
    });
    childDomain.setActorRef(childActor);

    const sub = childActor.subscribe(() => {
      // Will notify parent to re-aggregate
    });
    childActor.start();

    return {
      childActors:  new Map([...context.childActors,  [event.id, childActor]]),
      childDomains: new Map([...context.childDomains, [event.id, childDomain]]),
      subscriptions: new Map([...context.subscriptions, [event.id, sub]]),
    };
  })
},

REMOVE_ITEM: {
  actions: [
    ({ context, event }) => {
      context.subscriptions.get(event.id)?.unsubscribe();
      context.childActors.get(event.id)?.stop();
    },
    assign(({ context, event }) => {
      const childActors   = new Map(context.childActors);
      const childDomains  = new Map(context.childDomains);
      const subscriptions = new Map(context.subscriptions);
      childActors.delete(event.id);
      childDomains.delete(event.id);
      subscriptions.delete(event.id);
      return { childActors, childDomains, subscriptions };
    })
  ]
}
```

### Pattern B: Peer Actors Communicating Through a Shared Parent

Two sibling items need to coordinate (e.g., one item's availability depends on another being selected). They do not communicate directly — they communicate via the parent.

```js
// Item A signals a state change upward
itemActorA.send({ type: 'SELECTION_CHANGED', selected: true, source: 'I-A' });

// Parent machine handles it:
SELECTION_CHANGED: {
  actions: ({ context, event }) => {
    const conflictId = findConflict(context.childDomains, event.source);
    if (conflictId) {
      context.childActors.get(conflictId)?.send({
        type: 'SET_CONTEXT',
        context: { conflictsWith: event.source }
      });
    }
  }
}
```

Direct peer-to-peer actor references are permitted only if the peers are truly independent and the parent does not need to coordinate them.

### Pattern C: Lazy Initialization

For expensive components (a detailed breakdown panel, a modal form), the actor is created only when first needed and torn down when dismissed:

```js
// In container machine:
OPEN_DETAIL_PANEL: {
  actions: assign(({ context, event }) => {
    if (!context.detailActor) {
      const detailActor = createActor(detailMachine, {
        input: { itemId: event.itemId }
      });
      detailActor.start();
      return { detailActor };
    }
    return {};
  })
},

CLOSE_DETAIL_PANEL: {
  actions: assign(({ context }) => {
    context.detailActor?.stop();
    return { detailActor: null };
  })
}
```

Lazy actors must be stopped on teardown — a stopped actor releases its subscriptions and timers.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/04_best_practices.md`.