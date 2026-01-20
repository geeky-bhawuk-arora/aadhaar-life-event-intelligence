import pandas as pd

def load_dataset(path: str) -> pd.DataFrame:
    """
    Loads UIDAI provided aggregated dataset.
    Raw data is NEVER modified.
    """
    return pd.read_csv(path)