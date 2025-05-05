# Path: utils/db_utils.py

"""
Contient des templates SQL et des helpers pour la génération dynamique de requêtes.
"""

from typing import Any

from core.log_manager import logger

# === SQL queries ===

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

SQL_SELECT_TASKS = "SELECT * FROM tasks"
SQL_SELECT_TASK_BY_ID = "SELECT * FROM tasks WHERE id = ?;"
SQL_INSERT_TASK = "INSERT INTO tasks (title, category, completed, expiration, notes) VALUES (?, ?, ?, ?, ?);"
SQL_UPDATE_TASK_BY_ID = "UPDATE tasks SET title = ?, category = ?, completed = ?, expiration = ?, notes = ? WHERE id = ?;"
SQL_DELETE_TASK_BY_ID = "DELETE FROM tasks WHERE id = ?;"

# === Dispatch ===

_QUERIES = {
    "create_table": SQL_CREATE_TASKS_TABLE,
    "select_all": SQL_SELECT_TASKS,
    "select_by_id": SQL_SELECT_TASK_BY_ID,
    "insert": SQL_INSERT_TASK,
    "update": SQL_UPDATE_TASK_BY_ID,
    "delete": SQL_DELETE_TASK_BY_ID,
}

# === Helpers ===


def get_query(key: str) -> str:
    try:
        logger.debug(f"Accessing query: {key}")
        return _QUERIES[key]
    except KeyError:
        logger.error(f"Unknown SQL query key: {key}")
        raise


def build_where_clause(filters: dict[str, Any]) -> tuple[str, list[Any]]:
    """
    Builds a dynamic WHERE clause from a dictionary.

    Returns
    -------
    str : WHERE clause (e.g., "category = ? AND completed = ?")
    list : List of values to inject into the query
    """
    if not filters:
        return "", []

    clause = " AND ".join([f"{key} = ?" for key in filters])
    values = list(filters.values())
    logger.debug(f"WHERE clause: {clause} | args={values}")
    return clause, values


def build_update_query(
    table: str, data: dict[str, Any], where_clause: str
) -> tuple[str, list[Any]]:
    """
    Generates a dynamic UPDATE query with SET and WHERE clauses.

    Parameters
    ----------
    table : str
        Name of the table (e.g., 'tasks')
    data : dict
        Data to update (e.g., {'title': 'New title', 'completed': 1})
    where_clause : str
        Final WHERE clause (e.g., 'id = ?')

    Returns
    -------
    str
        SQL query
    list
        Values to inject in order
    """
    if not data:
        raise ValueError("Empty data dict for update query")

    set_clause = ", ".join([f"{key} = ?" for key in data])
    sql = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
    args = list(data.values())

    logger.debug(f"UPDATE query: {sql} | args={args}")
    return sql, args


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

    logger.debug(f"Validating SQL query: {sql}")
    valid_commands = {"select", "insert", "update", "delete", "create", "drop"}
    return sql.strip().lower().split()[0] in valid_commands if sql.strip() else False
