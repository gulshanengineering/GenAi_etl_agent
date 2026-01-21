import pandas as pd

def profile_data(df):
    """
    Creates a summary of the data for the AI to analyze.
    """
    if df.empty:
        return {}
        
    profile = {
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": df.duplicated().sum(),
        "sample_rows": df.head(3).to_dict(orient="records")
    }
    return profile