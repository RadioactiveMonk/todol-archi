def add_task(
    self, status: bool, category: str, expiration: str, title: str, notes: str
) -> Task:
    """Ajoute une tâche à la base et retourne l'objet Task correspondant."""

    query = self.db.queries["insert_task"]
    params = (status, category, expiration, title, notes)

    # ✅ Exécution de la requête et récupération du task_id
    task_id = self.db._exec_query(query, params, return_lastrowid=True)

    return Task(
        tid=task_id,
        status=status,
        category=category,
        expiration=expiration,
        title=title,
        notes=notes,
    )
