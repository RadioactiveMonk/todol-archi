# scripts/reload_all.py

"""Chargement rapide des modules pour IPython."""

import sqlite3
from importlib import reload

from core.database.ask_db import AskDB
from core.database.init_db import init_db
from core.database_config import SQL_INSERT_TASK
from core.path import DB_FILE
from models import task

# Rechargement du module task et instanciation
reload(task)
Task = task.Task

test_task = Task(
    completed=True,
    category="Work",
    expiration="2025-09-07 21:00",
    title="Test task",
    notes="Test notes",
)

# Initialisation DB
init_db()

# Connexion pour la session
conn = sqlite3.connect(DB_FILE)
conn.row_factory = sqlite3.Row
db = AskDB(conn)

# Interface
print("✅ DB session")
print("📌 help(db) for commands.")

# Supprimer toutes les tâches (⚠️)
def clear_tasks():
    """Efface toutes les tâches de la table (utiliser avec précaution)."""
    db.ask("delete", "DELETE FROM tasks")
    print("⚠️ Toutes les tâches ont été supprimées.")
