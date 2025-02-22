# Quick Workshop Setup Guide

## Requirements
- Python 3.8+
- Git
- Web browser
- Neo4j AuraDB account

## Quick Start

### 1. Neo4j Setup (5 min)
1. Visit [Neo4j AuraDB](https://console.neo4j.io)
2. Create free instance
3. Save credentials

### 2. Local Setup (5 min)
```bash
# Get code
git clone https://github.com/neo4j/kg_workshop_quick.git
cd kg_workshop_quick

# Setup Python
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt

# Configure
cp .env.example .env
# Add Neo4j credentials to .env
```

### 3. Test Connection
```python
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()
driver = GraphDatabase.driver(
    os.getenv('NEO4J_URI'),
    auth=(os.getenv('NEO4J_USERNAME'), 
          os.getenv('NEO4J_PASSWORD'))
)

with driver.session() as session:
    result = session.run("RETURN 'Connected!' as message")
    print(result.single()['message'])
```

## Quick Troubleshooting

### Connection Issues
- Check credentials
- Verify instance running
- Test in browser

### Import Issues
- Check virtual environment
- Reinstall packages
- Verify Python version

## Getting Help
- Check full workshop docs
- Post in Issues
- Ask on Discord
