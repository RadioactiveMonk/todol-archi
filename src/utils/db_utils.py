# utils/db_utils.py

"""
Requêtes SQL de base et helpers pour la couche d'accès aux données.
Ce module contient les requêtes statiques, un dispatch facultatif, et des fonctions d'accès.
"""

# =====================================
# Requêtes SQL constantes
# =====================================

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

SQL_SELECT_TASKS = "SELECT * FROM tasks;"
SQL_SELECT_TASK_BY_ID = "SELECT * FROM tasks WHERE id = ?;"
SQL_INSERT_TASK = "INSERT INTO tasks (title, category, completed, expiration, notes) VALUES (?, ?, ?, ?, ?);"
SQL_UPDATE_TASK_BY_ID = "UPDATE tasks SET title = ?, category = ?, completed = ?, expiration = ?, notes = ? WHERE id = ?;"
SQL_DELETE_TASK_BY_ID = "DELETE FROM tasks WHERE id = ?;"

# =====================================
# Dispatch facultatif (clé → requête)
# =====================================

_QUERIES = {
    "create_table": SQL_CREATE_TASKS_TABLE,
    "select_all": SQL_SELECT_TASKS,
    "select_by_id": SQL_SELECT_TASK_BY_ID,
    "insert": SQL_INSERT_TASK,
    "update": SQL_UPDATE_TASK_BY_ID,
    "delete": SQL_DELETE_TASK_BY_ID,
}

# =====================================
# Fonctions d'accès ou helpers
# =====================================

def get_query(key: str) -> str:
    from utils.log_utils import logger
    try:
        return _QUERIES[key]
    except KeyError:
        logger.error(f"Unknown SQL query key: {key}")
        raise

def build_where_clause():
    pass

def build_update_query():
    pass

def is_query(sql: str) -> bool:
    """
    Checks if a given SQL string starts with a valid SQL command.

    Parameters
    ----------
    sql : str
        The SQL string to check.

    Returns
    -------
    bool
        True if the SQL string starts with a valid command, False otherwise.
    """
    valid_commands = {"select", "insert", "update", "delete", "create", "drop"}
    return sql.strip().lower().split()[0] in valid_commands if sql.strip() else False


