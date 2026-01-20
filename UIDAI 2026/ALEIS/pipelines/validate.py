def validate_non_negative(df, col):
    if (df[col] < 0).any():
        raise ValueError(f"Negative values found in {col}")
