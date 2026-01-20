def biometric_transition_ratio(df):
    """
    Ratio of biometric updates for 15–20 age group.
    """
    return df["biometric_updates"] / df["total_enrolments"]
