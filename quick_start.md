# Quick Start Guide

## 1. Environment Setup (5 min)
```bash
# Clone repo
git clone https://github.com/yourusername/kg_workshop_quick.git
cd kg_workshop_quick

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt
```

## 2. Neo4j Setup (5 min)
1. Go to [Neo4j AuraDB](https://neo4j.com/cloud/aura-free/)
2. Create free instance
3. Download credentials
4. Copy `.env.example` to `.env`
5. Update with your credentials

## 3. Verify Setup
```python
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()
driver = GraphDatabase.driver(
    os.getenv('NEO4J_URI'),
    auth=(os.getenv('NEO4J_USERNAME'), os.getenv('NEO4J_PASSWORD'))
)

with driver.session() as session:
    result = session.run("RETURN 'Connected!' as message")
    print(result.single()['message'])
```

## 4. Workshop Materials
- `notebooks/`: Jupyter notebooks for each section
- `data/`: Sample datasets and documents
- `slides/`: Workshop presentation

## 5. Key Concepts
1. **Knowledge Graph**
   - Nodes: Customers, Products, Documents
   - Relationships: Orders, Categories, Cases

2. **Document Processing**
   - Upload documents
   - Extract information
   - Create connections

3. **GraphRAG Patterns**
   - Customer context
   - Product knowledge
   - Query patterns

4. **Memory Graph**
   - Track interactions
   - Store context
   - Analyze history

## 6. Quick Reference

### Common Cypher Patterns
```cypher
// Find customer orders
MATCH (c:Customer)-[:PLACED_ORDER]->(o:Order)
RETURN c.name, count(o) as orders

// Find product documents
MATCH (p:Product)-[:HAS_MANUAL]->(d:Document)
RETURN p.name, d.content

// Get customer context
MATCH (c:Customer {id: 'C1'})
MATCH path = (c)-[:HAD_INTERACTION|HAS_CASE]->()
RETURN path
```

### Python Helpers
```python
# Connect to Neo4j
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()
driver = GraphDatabase.driver(
    os.getenv('NEO4J_URI'),
    auth=(os.getenv('NEO4J_USERNAME'), 
          os.getenv('NEO4J_PASSWORD'))
)

# Run query
def run_query(query, params=None):
    with driver.session() as session:
        result = session.run(query, params or {})
        return list(result)
```

## 7. Troubleshooting
- Check Neo4j connection in browser
- Verify credentials in `.env`
- Ensure Python 3.8+
- Check file paths in notebooks

## 8. Next Steps
1. Complete setup before workshop
2. Review basic Cypher queries
3. Explore sample data
4. Try connecting to Neo4j

## 9. Resources
- [GraphRAG Docs](https://graphrag.com)
- [Neo4j Docs](https://neo4j.com/docs/)
- [Workshop Repo](https://github.com/...)
- [Extended Version](https://github.com/...)
