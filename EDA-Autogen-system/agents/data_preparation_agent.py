import pandas as pd

class DataPreparationAgent:
    def __init__(self, dataframe):
        self.df = dataframe

    def clean_and_preprocess(self):
        df = self.df.copy()
        df = df.drop_duplicates()
        df = df.dropna()
        # Additional cleaning steps can be added here
        return df
