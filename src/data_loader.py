import pandas as pd


def load_dataset(path):
    """
    Load predictive maintenance dataset
    """

    df = pd.read_csv(path)

    return df