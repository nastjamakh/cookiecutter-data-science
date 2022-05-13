"""Module to load data."""
from enum import Enum
from pathlib import Path
from typing import Dict

import fire
import pandas as pd
from tqdm import tqdm

from config import data_dir
from logger import time_and_log


class DatasetFilename(Enum):
    """Map dataset names to filepaths."""

    DATASET_1 = "dataset_1.gzip"
    DATASET_2 = "dataset_2.gzip"
    DATASET_3 = "dataset_3.gzip"

    @classmethod
    def from_name(cls, name: str) -> str:
        if hasattr(DatasetFilename, name.upper()):
            return getattr(DatasetFilename, name.upper()).value
        else:
            raise ValueError(f"No such dataset: {name}")


class FileDataLoader:
    """Class to load data from file."""

    DATASETS = [
        name.split(".")[0].lower() for name, _ in DatasetFilename.__members__.items()
    ]

    def __init__(self) -> None:
        """Initialize class instance."""

        # store loaded datasets
        self.datasets_: Dict[str, pd.DataFrame] = dict()

    @staticmethod
    def preprocess_dataset(df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError

    @time_and_log()
    def load_dataset(self, dataset_name: str) -> pd.DataFrame:
        raise NotImplementedError

    @time_and_log(False)
    def load_all(self) -> None:
        """List all datasets."""
        pbar = tqdm(self.DATASETS)
        for dataset in pbar:
            pbar.set_description(f"Loading dataset: {dataset}")
            self.load_dataset(dataset_name=dataset)

    @classmethod
    def list_available(cls) -> list:
        """List all availbale datasets."""
        return cls.DATASETS

    def list_loaded(self) -> list:
        """List all loaded datasets."""
        return list(self.datasets_.keys())

    @classmethod
    def get_dataset_filepath(cls, dataset_name: str) -> Path:
        """Return filepath of a dataset."""
        return data_dir() / DatasetFilename.from_name(dataset_name)

    def __getitem__(self, dataset_name: str) -> pd.DataFrame:
        """Use class as a dict with keys as dataset names."""
        assert dataset_name in self.datasets_, f"Dataset {dataset_name} is not loaded."
        return self.datasets_[dataset_name]


def cli() -> None:
    """CLI interface for Data Loader."""
    fire.Fire(FileDataLoader)


if __name__ == "__main__":
    cli()
