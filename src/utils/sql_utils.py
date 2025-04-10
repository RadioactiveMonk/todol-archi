"""Requêtes SQL liées à la structure de la base de données (DDL).

À utiliser pour créer, supprimer ou modifier les tables.
Ces requêtes ne manipulent pas les données mais la structure de la DB.
"""

SQL_CREATE_TASKS_TABLE = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    completed INTEGER NOT NULL DEFAULT 0,
    expiration TEXT NOT NULL,
    notes TEXT
);
"""

SQL_DROP_TASKS_TABLE = "DROP TABLE IF EXISTS tasks;"
