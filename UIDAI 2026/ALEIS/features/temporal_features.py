def temporal_concentration(series):
    """
    Measures how concentrated updates are in time.
    """
    return series.std() / series.mean()
