# src/helpers/contextmanagers.py

import json
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from core.db import DB
from utils.log_utils import logger
from utils.path_utils import SETTINGS_FILE


@contextmanager
def open_db(path: Path):
    """
    Context manager for accessing the SQLite database using DB.

    Usage:
        with open_db(DB_FILE) as db:
            db.create(SQL_QUERY)
    """

    conn = sqlite3.connect(path)
    try:
        yield DB(conn)
    finally:
        conn.close()


@contextmanager
def open_settings(mode: str = "r", encoding: str = "utf-8") -> Any:
    """
    Context manager for reading or writing the settings.json file.

    Usage:
        with open_settings() as data:
            categories = data.get("categories", [])

        with open_settings("w") as f:
            json.dump(new_settings, f)
    """

    logger.debug(f"Accessing settings file in mode '{mode}': {SETTINGS_FILE}")
    with open(SETTINGS_FILE, mode, encoding=encoding) as f:
        if "r" in mode:
            yield json.load(f)
        else:
            yield f
