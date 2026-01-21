import os
import sys

# Ensure the root directory is in the python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tools.extractor import extract
from tools.profiler import profile_data
from agents.etl_agent import generate_etl_plan
from tools.transformer import transform_data
from tools.loader import load

def main():
    # Define file path
    file_path = os.path.join("data", "sales_data.csv")

    print("🚀 --- STEP 1: EXTRACT ---")
    df = extract(file_path)
    
    if df.empty:
        print("Stopping: No data found.")
        return

    print("\n🔍 --- STEP 2: PROFILE ---")
    schema = profile_data(df)
    print(f"Data Profile: {len(schema['columns'])} columns detected.")

    print("\n🤖 --- STEP 3: AI PLAN ---")
    etl_plan = generate_etl_plan(schema)
    print("--- Agent's Suggested Plan ---")
    print(etl_plan)
    print("------------------------------")

    print("\n✨ --- STEP 4: TRANSFORM ---")
    # FIX: We only pass 'df'. We do NOT pass 'etl_plan' to avoid the TypeError.
    df_clean = transform_data(df)
    
    print("Cleaned Data Preview:")
    print(df_clean.head())

    print("\n💾 --- STEP 5: LOAD ---")
    load(df_clean)

if __name__ == "__main__":
    main()