import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    load csv file and return dataset
    """
    try:
        if not os.path.exists(path):
            raise Exception(f"file '{path}' does not exist")
        if os.path.splitext(path)[1] != '.csv':
            raise Exception("file extension should be .csv")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except Exception as e:
        print(e)
        return None
