from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
import pandas as pd

def connect_to_neo4j():
    """Connect to Neo4j database using environment variables."""
    load_dotenv()
    uri = os.getenv('NEO4J_URI')
    auth = (os.getenv('NEO4J_USERNAME'), os.getenv('NEO4J_PASSWORD'))
    return GraphDatabase.driver(uri, auth=auth)

def load_customers(driver, df):
    """Load customer data into Neo4j."""
    with driver.session() as session:
        # Create Customer nodes
        session.run("""
        UNWIND $customers AS customer
        CREATE (c:Customer {
            id: customer.customer_id,
            name: customer.name,
            email: customer.email,
            join_date: date(customer.join_date)
        })
        """, customers=df.to_dict('records'))
        print("Loaded customers")

def load_products(driver, df):
    """Load product data into Neo4j."""
    with driver.session() as session:
        # Create Product and Category nodes
        session.run("""
        UNWIND $products AS product
        MERGE (cat:Category {name: product.category})
        CREATE (p:Product {
            id: product.product_id,
            name: product.name,
            price: toFloat(product.price)
        })
        CREATE (p)-[:IN_CATEGORY]->(cat)
        """, products=df.to_dict('records'))
        print("Loaded products")

def load_orders(driver, df):
    """Load order data into Neo4j."""
    with driver.session() as session:
        # Create Order nodes and relationships
        session.run("""
        UNWIND $orders AS order
        MATCH (c:Customer {id: order.customer_id})
        MATCH (p:Product {id: order.product_id})
        CREATE (o:Order {
            id: order.order_id,
            date: date(order.order_date),
            quantity: toInteger(order.quantity)
        })
        CREATE (c)-[:PLACED_ORDER]->(o)
        CREATE (o)-[:CONTAINS]->(p)
        """, orders=df.to_dict('records'))
        print("Loaded orders")

def clear_database(driver):
    """Clear all nodes and relationships from the database."""
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")
        print("Cleared database")

def main():
    # Connect to Neo4j
    driver = connect_to_neo4j()
    
    try:
        # Clear existing data
        clear_database(driver)
        
        # Load CSV files
        customers_df = pd.read_csv('data/customers.csv')
        products_df = pd.read_csv('data/products.csv')
        orders_df = pd.read_csv('data/orders.csv')
        
        # Load data into Neo4j
        load_customers(driver, customers_df)
        load_products(driver, products_df)
        load_orders(driver, orders_df)
        
        print("Data loading completed successfully!")
        
    except Exception as e:
        print(f"Error loading data: {str(e)}")
    
    finally:
        driver.close()

if __name__ == "__main__":
    main()
