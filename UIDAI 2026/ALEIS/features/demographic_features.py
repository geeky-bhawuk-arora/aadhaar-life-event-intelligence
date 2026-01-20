def update_diversity(row):
    """
    Counts number of update types used.
    """
    update_cols = [
        "address_updates",
        "mobile_updates",
        "name_updates",
        "dob_updates",
        "gender_updates"
    ]
    return sum(row[col] > 0 for col in update_cols)
