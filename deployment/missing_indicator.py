import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class MissingIndicatorImputer(BaseEstimator, TransformerMixin):
    """
    Missing values imputer similar to ```SimpleImputer``` but add a missing value flag columns to indicate missingness
    """
    def __init__(self, strategy: str="mean", fill_value=None) -> None:
        self.strategy = strategy
        self.fill_value = fill_value
        self.fill_values_ = {}
        self.new_col_str = "missing_"
        self.columns = []

    def fit(self, X, y = None):
        df = pd.DataFrame(X)

        self.columns = df.columns
        for col in df.columns:
            if self.strategy == "constant":
                self.fill_values_[col] = self.fill_value
            elif self.strategy == "mode":
                self.fill_values_[col] = df[col].mode()[0]
            elif self.strategy == "mean":
                self.fill_values_[col] = df[col].mean()
            elif self.strategy == "median":
                self.fill_values_[col] = df[col].median()
            else:
                raise ValueError("Unknown fill strategy")
        
        return self
        
    def transform(self, X):
        df = pd.DataFrame(X).copy()

        for col in self.columns:
            missing_col_name = f"{self.new_col_str}{col}"
            df[missing_col_name] = df[col].isnull().astype(int)
            df[col] = df[col].fillna(self.fill_values_[col])

        return df
    
    def get_feature_names_out(self, input_features=None):
        return [col for col in self.columns] + [f"{self.new_col_str}{col}" for col in self.columns]