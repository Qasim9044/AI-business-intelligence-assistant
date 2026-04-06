import pandas as pd

def load_csv(path):
    """
    Load a CSV dataset from the given path.
    """
    df = pd.read_csv(path)
    return df
