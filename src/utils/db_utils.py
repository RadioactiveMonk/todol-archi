"""SQL queries centralisées pour les opérations sur la table 'tasks'."""

# Ordre de référence : title, category, completed, expiration, notes

SQL_INSERT_TASK: str = """
INSERT INTO tasks (title, category, completed, expiration, notes)
VALUES (?, ?, ?, ?, ?);
"""

SQL_SELECT_TASKS: str = """
SELECT id, title, category, completed, expiration, notes
FROM tasks;
"""

SQL_SELECT_TASK_BY_ID: str = """
SELECT id, title, category, completed, expiration, notes
FROM tasks
WHERE id = ?;
"""

SQL_UPDATE_TASK_BY_ID: str = """
UPDATE tasks
SET title = ?, category = ?, completed = ?, expiration = ?, notes = ?
WHERE id = ?;
"""

SQL_DELETE_TASK_BY_ID: str = """
DELETE FROM tasks
WHERE id = ?;
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
