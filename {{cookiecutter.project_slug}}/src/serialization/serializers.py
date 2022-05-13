"""
    Responsabilities:
    - (De) Serialization
    - Download/Upload files to and from S3 if they dont exists locally
    - Model-Zoo
"""
from typing import Any
from pathlib import Path

from logger import time_and_log


class Serializer:
    """
    Writes object to the disk or on S3 (serialization) and return an
    object from a file (de-serialization).

    Serialization:
    - Writes the file on the disk on development
    - Writes on S3 if force_s3 is enabled
    - Write on S3 on production

    De-serialization:
    - If the file can not be found on the disk, it will retrieve it from S3
    - If it can not be found on S3, it will raise an Error
    """


    @time_and_log(True)
    def read(self, file_path: Path, from_s3: bool = False) -> Any:
        """Load file locally or from S3"""
        pass

    @time_and_log(True)
    def write(self, file_path: Path, obj: Any, to_s3: bool = False) -> None:
        """Serialize object with option to push to S3."""
        pass
