"""reload_all.py – Chargement rapide des modules pour IPython."""

import sqlite3
from importlib import reload

import core.database.ask_db as askdb_module
import models.task as task_module
from core.path import DB_FILE

# from helpers.contextmanagers import open_db


def reload_all():
    reload(task_module)
    reload(askdb_module)

    Task = task_module.Task
    AskDB = askdb_module.AskDB

    db = AskDB(sqlite3.connect(DB_FILE))
    return db, Task


print("✅ Modules reloaded successfully!")
