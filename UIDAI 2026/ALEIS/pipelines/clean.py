import pandas as pd

def clean_common_fields(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.lower().str.strip()
    df = df.drop_duplicates()
    return df
