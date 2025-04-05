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
""" reload(task)
Task = task.Task """

""" test_task = Task(
    completed=True,
    category="Work",
    expiration="2025-09-07 21:00",
    title="Test task",
    notes="Test notes",
) """

# Initialisation DB
init_db()

# Connexion pour la session
conn = sqlite3.connect(DB_FILE)
conn.row_factory = sqlite3.Row
db = AskDB(conn)

# Interface
print("✅ DB session")
print("📌 help(db) for commands.")

# ================================
# Commandes pratiques IPython
# ================================


# Ajouter une tâche de test rapidement (via ask)
def insert_test_task():
    """Ajoute une tâche générique pour test rapide."""
    db.ask(
        "insert",
        SQL_INSERT_TASK,
        "Test IPython",
        "debug",
        0,
        "2025-05-01",
        "Créée via insert_test_task()",
    )
    print("✅ Tâche de test insérée.")


# Afficher toutes les tâches
def show_tasks():
    """Affiche toutes les tâches dans la table."""
    for row in db.get_all_tasks():
        print(dict(row))


# Supprimer toutes les tâches (⚠️)
def clear_tasks():
    """Efface toutes les tâches de la table (utiliser avec précaution)."""
    db.ask("delete", "DELETE FROM tasks")
    print("⚠️ Toutes les tâches ont été supprimées.")
