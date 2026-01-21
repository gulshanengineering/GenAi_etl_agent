import pandas as pd

def transform_data(df):
    """
    Applies cleaning rules: handling dates, currency symbols, and types.
    """
    if df.empty:
        return df

    df = df.copy()

    # 1. Fill missing customer_id
    df["customer_id"] = df["customer_id"].fillna("UNKNOWN")

    # 2. Standardize order_date
    # coercion turns errors (like 'invalid-date') into NaT (Not a Time)
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce").dt.strftime("%Y-%m-%d")

    # 3. Clean amount column
    # If it's a string object, remove '$' and ','
    if df["amount"].dtype == 'object':
        df["amount"] = df["amount"].astype(str).str.replace(r'[$,]', '', regex=True)
    
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    # 4. Remove duplicates based on order_id
    df = df.drop_duplicates(subset=["order_id"])

    # 5. Drop rows where order_id is missing/NaN
    df = df.dropna(subset=["order_id"])
    
    # 6. Final Type Enforcement
    df["order_id"] = df["order_id"].astype(int)
    
    return df