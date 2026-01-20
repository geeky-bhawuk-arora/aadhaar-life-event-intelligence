def check_empty(df):
    if df.empty:
        raise ValueError("Dataset is empty")
