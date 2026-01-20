def check_region_coverage(df, region_col):
    if df[region_col].nunique() < 0:
        raise Warning("Low regional coverage detected")
