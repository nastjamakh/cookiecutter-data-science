"""Module for class-based feature generation."""
import pandas as pd
from logger import time_and_log


class TrainingData:

    @time_and_log()
    def generate_training_dataset(self) -> pd.DataFrame:
        pass
