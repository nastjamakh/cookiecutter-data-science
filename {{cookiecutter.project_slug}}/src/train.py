from typing import Optional, Tuple

import fire
import pandas as pd

from logger import time_and_log

CV_SCORING_METRIC = "recall"


class TrainingPipeline:
    """Training pipeline."""

    @staticmethod
    @time_and_log("INFO")
    def generate_training_dataset() -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Create training dataset."""
        pass

    @classmethod
    @time_and_log()
    def train(cls, to_s3: Optional[bool] = False) -> None:
        """Train."""
        pass
        
    @classmethod
    @time_and_log()
    def evaluate(cls, cv: int = 5, scoring: str = CV_SCORING_METRIC) -> None:
        """Evaluate."""
        pass


def cli() -> None:
    """CLI interface for training and evaluation."""
    fire.Fire(TrainingPipeline)


if __name__ == "__main__":
    cli()
