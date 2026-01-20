def detect_drift(old_mean, new_mean, tolerance=0.3):
    return abs(new_mean - old_mean) / old_mean > tolerance
