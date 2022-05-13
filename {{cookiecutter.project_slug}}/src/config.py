from pathlib import Path
import os
from typing import List

"""Infra Related Environment Variables."""
STAGE = os.getenv("STAGE", "")
GIT_COMMIT_HASH = os.getenv("GIT_COMMIT_HASH", "")
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")

AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET_NAME")
WORK_DIR = os.getenv("WORKDIR", "")


def aws_s3_bucket_name() -> str:
    """Returns AWS S3 bucket name."""
    return "{{cookiecutter.project_slug}}"


def api_keys() -> List[str]:
    """Returns list of valid API keys."""
    return [v for k, v in os.environ.items() if k.startswith("API_KEY")]


def work_dir() -> Path:
    """Get working dir."""
    if WORK_DIR == "":
        return Path(__file__).parent.parent
    else:
        return Path(WORK_DIR)

def queries_dir() -> Path:
    """Get queries dir."""
    return work_dir() / "src/data/queries"


def data_dir() -> Path:
    """Get data dir."""
    return work_dir() / "datasets"


def model_dir() -> Path:
    """Get model dir."""
    return work_dir() / "models"
