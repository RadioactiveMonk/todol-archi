from typing import Dict, List

from utils.log_utils import logger

TASK_TABLE_HEADERS: List[str] = [
    "Status",
    "Category",
    "Expiration",
    "Title",
    "Notes",
    "Edit",
]

# Mapping entre les noms affichés et les clés de données dans les tâches
COLUMN_MAPPING: Dict[str, str] = {
    "Status": "completed",
    "Category": "category",
    "Expiration": "expiration",
    "Title": "title",
    "Notes": "notes",
}


def get_column_index(name: str) -> int:
    """
    Returns the index of a column from its name
    """

    try:
        logger.debug(f"Accessing TASK_TABLE_HEADERS column index for {name}")
        return TASK_TABLE_HEADERS.index(name)
    except ValueError:
        logger.error(f"Column {name} not found in TASK_TABLE_HEADERS")
        raise


def get_column_name(index: int) -> str:
    """
    Returns the column name from its index
    """

    try:
        logger.debug(f"Accessing column name for index {index}")
        return TASK_TABLE_HEADERS[index]
    except IndexError:
        logger.error(f"Column index {index} out of range for TASK_TABLE_HEADERS")
        raise
