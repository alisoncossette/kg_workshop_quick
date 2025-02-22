# GraphRAG in Action (80-Minute Workshop)

A fast-paced, hands-on workshop introducing Knowledge Graphs, GraphRAG patterns, and Memory Graphs using Neo4j.

## Prerequisites
- Python 3.8+
- Neo4j AuraDB account (free tier)
- Git

## Quick Start
```bash
# Clone the repo
git clone https://github.com/alisoncossette/kg_workshop_quick.git
cd kg_workshop_quick

# Set up environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt

# Configure Neo4j
cp .env.example .env
# Edit .env with your Neo4j credentials
```

## Workshop Structure (80 minutes)

### 1. Quick Setup (10 min)
- Connect to Neo4j
- Load sample data
- Verify environment

### 2. Knowledge Graph Essentials (15 min)
- CRM graph overview
- Data import demo
- Quick graph exploration

### 3. Document Processing (20 min)
- KG Builder walkthrough
- Document-to-graph connections
- Practical examples

### 4. GraphRAG Patterns (20 min)
- Customer context retrieval
- Product knowledge base
- Live pattern demos

### 5. Memory Graph Preview (10 min)
- Concept introduction
- Pre-built examples
- Analysis queries

### 6. Hands-on Challenge (5 min)
- Practical exercise
- Solution review
- Next steps

## Repository Structure
```
kg_workshop_quick/
├── data/                    # Pre-prepared datasets
│   ├── customers.csv
│   ├── products.csv
│   └── documents/
├── notebooks/              # Jupyter notebooks for each section
│   ├── 01_setup.ipynb
│   ├── 02_knowledge_graph.ipynb
│   ├── 03_document_processing.ipynb
│   ├── 04_graphrag_patterns.ipynb
│   └── 05_memory_graph.ipynb
├── slides/                 # Presentation materials
├── docs/                  # Additional documentation
├── requirements.txt       # Dependencies
└── .env.example          # Template for Neo4j credentials
```

## Pre-workshop Setup
1. Create Neo4j AuraDB instance (instructions in docs)
2. Install dependencies
3. Download workshop materials
4. Test connection

## Resources
- [Neo4j AuraDB](https://console.neo4j.io/)
- [Workshop Documentation](./docs/workshop_overview.md)
- [Setup Guide](./docs/setup.md)
- [Cypher Cheatsheet](./docs/cypher_cheatsheet.md)

## License
MIT

## Contact
Alison Cossette
- Email: alisoncossette@gmail.com
- GitHub: @alisoncossette
