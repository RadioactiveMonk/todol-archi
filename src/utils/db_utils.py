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
