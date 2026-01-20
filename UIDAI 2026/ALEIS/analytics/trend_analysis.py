def compute_trend(series):
    return series.rolling(window=6).mean()
