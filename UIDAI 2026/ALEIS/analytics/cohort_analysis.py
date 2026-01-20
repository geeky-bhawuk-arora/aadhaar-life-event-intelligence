def cohort_progression(df, cohort_col, value_col):
    return df.groupby(cohort_col)[value_col].sum()
