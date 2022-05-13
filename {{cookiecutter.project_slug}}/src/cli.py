"""CLI interface."""
import fire

from train import TrainingPipeline
from data.data_loader import FileDataLoader


class Entrypoint:
    """CLI entrypoint."""

    def __init__(self) -> None:
        self.train = TrainingPipeline()
        self.data = FileDataLoader()


def cli() -> None:
    """Function to start cli."""
    fire.Fire(Entrypoint)


if __name__ == "__main__":
    cli()
