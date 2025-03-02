def get_tasks(self) -> List[Task]:
    """Récupère toutes les tâches de la base SQLite"""
    conn = self._connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, status, category, expiration, title, notes FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    return [
        Task(
            id=row[0],
            status=bool(row[1]),
            category=row[2],
            expiration=row[3],  # Stocké en str
            title=row[4],
            notes=row[5],
        )
        for row in rows
    ]
