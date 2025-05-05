import csv
from pathlib import Path
from typing import Mapping, Sequence

from core.log_manager import logger
from utils.path_utils import get_path


def export_to_csv(data: Sequence[Mapping], filename: str = "export.csv") -> Path:
    """
    Export the tasks as a list of dictionnaries to a CSV file.

    Parameters
    ----------
    data : Sequence[Mapping]
        A sequence of mappings (e.g., list of dicts), each representing a row.
    filename : str, optional
        The CSV file name to be created (within the data directory).

    Returns
    -------
    Path
        the full path to the generated file (data/ dir)
    """

    if not data:
        logger.warning("No data to export.")
        return get_path("data") / filename

    export_path = get_path("data") / filename

    try:
        with open(export_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
            writer.writeheader()
            writer.writerows(data)
        logger.info(f"CSV exported successfully: {export_path}")
    except Exception as e:
        logger.error(f"Failed to export CSV: {e}")

    return export_path
