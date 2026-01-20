def enrolment_velocity(df, enrolment_col):
    """
    Measures growth rate of enrolments.
    """
    df = df.copy()
    df["enrolment_velocity"] = df[enrolment_col].pct_change()
    return df
