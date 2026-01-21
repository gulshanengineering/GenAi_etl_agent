import pandas as pd
from sqlalchemy import create_engine
import os

def verify():
    print("--- VERIFYING DATABASE CONTENT ---")
    
    # Connect to the database
    db_name = "warehouse.db"
    
    if not os.path.exists(db_name):
        print(f"❌ Error: '{db_name}' not found. Did you run main.py?")
        return

    engine = create_engine(f"sqlite:///{db_name}")
    
    # Read the table
    try:
        df = pd.read_sql("SELECT * FROM fact_sales", engine)
        
        print(f"✅ Connection successful! Found {len(df)} rows in 'fact_sales'.")
        print("\nStored Data:")
        print(df)
        
    except Exception as e:
        print(f"❌ Error reading database: {e}")

if __name__ == "__main__":
    verify()