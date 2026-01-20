def compute_lepi(freq, diversity, temporal, weights):
    """
    Life-Event Proxy Index (LEPI)
    """
    return (
        freq * weights["frequency_weight"]
        + diversity * weights["diversity_weight"]
        + temporal * weights["temporal_weight"]
    )
