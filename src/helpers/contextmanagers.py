import sqlite3
from contextlib import contextmanager
from pathlib import Path

from core.database.ask_db import AskDB


@contextmanager
def open_db(path: Path):
    conn = sqlite3.connect(path)
    try:
        yield AskDB(conn)
    finally:
        conn.close()
