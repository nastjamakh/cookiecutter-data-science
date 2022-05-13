""" Transformers. """
from sklearn.base import TransformerMixin, BaseEstimator
import pandas as pd


class SampleTransformer(TransformerMixin, BaseEstimator):
    """Sample transformer with sklearn interface."""

    def __init__(self, ) -> None:
        pass

    def fit(self, X: pd.DataFrame) -> "SampleTransformer":
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        pass
