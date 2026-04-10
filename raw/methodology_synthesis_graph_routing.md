# Routing: Matrix vs. Graph

The context router (doc_methodology) uses a 4D matrix (domain × stage × layer × temporal state). This works for pipeline projects where the structure is genuinely regular — a linear sequence of stages across orthogonal domains. Coordinates are a natural fit when every document has a clean home in the grid.

Reality is not always a matrix. It is closer to a graph:
- A standard applies across multiple domains and stages
- A concept is relevant to several unrelated modules
- Cross-cutting concerns (logging, error contracts, observability) have no natural domain×stage cell
- Decisions have arbitrary dependencies, not grid coordinates

Forcing graph-shaped knowledge into a matrix produces gaps (cross-cutting items with no home) and distortions (items assigned to the nearest cell rather than their true location).

## The implication for wikipu

The Librarian agent should not navigate by coordinates. It should navigate by graph traversal and facet queries. The infrastructure already exists:

- `get_node` — retrieve a node by ID
- `get_ancestors` / `get_descendants` — traverse relationships
- `StructuredQuery` + `FacetFilter` — find nodes by facet properties
- `GraphScope` — scope a query to a subgraph

The routing matrix is a special case of a graph — a regular, structured subgraph where every node has orthogonal coordinates. For a general knowledge system, the graph is the routing matrix. The "coordinates" are node IDs and edge types, not domain×stage tuples.

## What to preserve from the matrix model

The matrix's real contribution is not the coordinate system — it is the **separation of temporal state**. `runtime` vs. `plan` as a navigation axis is valuable regardless of graph or matrix. A node in the graph should carry a temporal facet: is this current truth, a plan, a deferred item, or historical?

Translated to the graph model:
- Current truth nodes → `ComplianceFacet.status = "implemented"` + no `plan/` prefix in node_id
- Plan nodes → `doc:plan_docs/...`
- Deferred nodes → `doc:future_docs/...`
- Historical nodes → ADR nodes with `adr.status = "superseded"`

The Librarian agent can then scope queries by temporal state as a facet filter, not a coordinate axis. Same separation, graph-native representation.

## Seed rule

> The knowledge graph is the routing system. Agents navigate by traversal and facet query, not by coordinate lookup. Temporal state is a facet, not an axis.
