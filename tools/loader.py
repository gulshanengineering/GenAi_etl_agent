from sqlalchemy import create_engine
import os

def load(df, db_name="warehouse.db", table_name="fact_sales"):
    """
    Saves the cleaned data to a local SQLite database.
    """
    if df.empty:
        print("⚠️ No data to load.")
        return

    try:
        # Create database URL
        db_url = f"sqlite:///{db_name}"
        engine = create_engine(db_url)
        
        # Load data (replace existing table)
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        
        print(f"✅ Data successfully loaded into '{db_name}' (Table: {table_name})")
    except Exception as e:
        print(f"❌ Error loading data: {e}")