from scipy.stats import zscore

def detect_anomalies(series, threshold=2.5):
    z = zscore(series)
    return abs(z) > threshold
