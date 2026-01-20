def region_share(df, region_col, value_col):
    total = df[value_col].sum()
    df["region_share"] = df[value_col] / total
    return df
