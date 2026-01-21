import pandas as pd

def extract(file_path):
    """
    Reads the raw CSV file into a DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Data extracted successfully: {len(df)} rows found.")
        return df
    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' was not found.")
        return pd.DataFrame()