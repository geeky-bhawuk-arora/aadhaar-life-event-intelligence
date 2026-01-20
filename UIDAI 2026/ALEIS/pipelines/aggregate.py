import pandas as pd

def aggregate_monthly(df: pd.DataFrame, group_cols: list, value_col: str):
    return (
        df.groupby(group_cols)[value_col]
        .sum()
        .reset_index()
    )
