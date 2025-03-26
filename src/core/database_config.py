# Requêtes SQL
# =====================================
SQL_INSERT_TASK = "INSERT INTO tasks (completed, category, expiration, title, notes) VALUES (?, ?, ?, ?, ?);"
SQL_SELECT_TASKS = "SELECT id, completed, category, expiration, title, notes FROM tasks"
SQL_DELETE_TASK = "DELETE FROM tasks WHERE id = ?"
SQL_DROP_TABLE = "DROP TABLE IF EXISTS tasks;"
SQL_CREATE_TABLE = """CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, completed INTEGER NOT NULL DEFAULT 0, category TEXT NOT NULL, expiration TEXT NOT NULL, title TEXT NOT NULL, notes TEXT);"""
