# Quick Neo4j Cypher Reference

## Essential Patterns

### Basic Operations
```cypher
// Create node
CREATE (n:Person {name: 'John'})

// Find node
MATCH (n:Person {name: 'John'}) RETURN n

// Create relationship
MATCH (a:Person), (b:Product)
WHERE a.name = 'John' AND b.id = 'P1'
CREATE (a)-[:PURCHASED]->(b)
```

### Workshop Patterns

#### Customer Data
```cypher
// Get customer orders
MATCH (c:Customer)-[:PLACED_ORDER]->(o:Order)
RETURN c.name, count(o) as orders

// Get customer's products
MATCH (c:Customer)-[:PLACED_ORDER]->(:Order)-[:CONTAINS]->(p:Product)
RETURN c.name, collect(p.name) as products
```

#### Product Knowledge
```cypher
// Find product manual
MATCH (p:Product)-[:HAS_MANUAL]->(m:Document)
RETURN p.name, m.content

// Find related products
MATCH (p:Product)-[:IN_CATEGORY]->(c:Category)<-[:IN_CATEGORY]-(related:Product)
WHERE p <> related
RETURN related.name
```

#### Memory Graph
```cypher
// Get recent interactions
MATCH (c:Customer)-[:HAD_INTERACTION]->(i:Interaction)
WHERE i.timestamp > datetime() - duration('P1D')
RETURN c.name, i.content
ORDER BY i.timestamp DESC
```

## Tips
- Use parameters
- Keep queries simple
- Add comments
- Use meaningful labels
