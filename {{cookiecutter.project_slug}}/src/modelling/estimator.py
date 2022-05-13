"""Final estimator."""
from datetime import datetime
from typing import Any, Sized

import serialization.utils as utils
from config import model_dir
from logger import time_and_log
from serialization.serializers import Serializer


class Estimator:
    """Wrapper for LightGBM estimator."""

    def __init__(self) -> None:
        """Initialize."""
        self.model = None

    def fit(self, *args: Any, **kwargs: Any) -> None:
        """Wrapper around model fit method."""
        pass

    def predict(self, X: Sized) -> list:
        pass

    @time_and_log()
    def save(self, to_s3: bool = False) -> None:
        """Serialize the model."""
        model_path = model_dir() / "model.joblib"
        Serializer().write(file_path=model_path, object=self.model, to_s3=to_s3)

    @time_and_log()
    def load(self, from_s3: bool = False) -> Any:
        """Download model from S3."""
        # Load from local file
        Serializer().read(file_path="model.joblib", from_s3=from_s3)
