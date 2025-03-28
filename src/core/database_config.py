# Requêtes SQL
# =====================================
SQL_INSERT_TASK: str = "INSERT INTO tasks (completed, category, expiration, title, notes) VALUES (?, ?, ?, ?, ?);"
SQL_SELECT_TASKS: str = "SELECT id, completed, category, expiration, title, notes FROM tasks"
SQL_DELETE_TASK: str = "DELETE FROM tasks WHERE id = ?"
SQL_DROP_TABLE: str = "DROP TABLE IF EXISTS tasks;"
SQL_CREATE_TABLE: str = """CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, completed INTEGER NOT NULL DEFAULT 0, category TEXT NOT NULL, expiration TEXT NOT NULL, title TEXT NOT NULL, notes TEXT);"""
