def test_persistant_connection(in_memory_connection):
    # On crée un controller avec une base mémoire partagée
    db = in_memory_connection

    # On insère une ligne manuellement
    insert_query = """
        INSERT INTO tasks (completed, category, expiration, title, notes) VALUES (?, ?, ?, ?, ?)
    """
    params = (0, "Test", "2025-01-01 12:00", "Titre test", "Note test")

    # Renvoie l'id de la tâche
    task_id = db._execute_query(insert_query, params, lastrowid=True)

    assert isinstance(task_id, int)

    # On récupère la ligne
    select_query = "SELECT title FROM tasks WHERE id = ?"

    # On récupère le titre
    result = db._execute_query(select_query, (task_id,), fetchone=True)

    assert result[0] == "Titre test"


def test_update_task_direct_sql(in_memory_connection):
    db = in_memory_connection

    # Insertion initiale
    insert_query = """
        INSERT INTO tasks (completed, category, expiration, title, notes)
        VALUES (?, ?, ?, ?, ?)
    """
    params = (0, "Dev", "2025-05-01 12:00", "Old Title", "Old Note")
    task_id = db._execute_query(insert_query, params, lastrowid=True)

    # UPDATE
    update_query = """
        UPDATE tasks SET title = ?, notes = ? WHERE id = ?
    """
    update_params = ("New Title", "New Note", task_id)
    rows = db._execute_query(update_query, update_params, rowcount=True)

    assert rows == 1  # ✅ une ligne modifiée

    # SELECT pour confirmer
    result = db._execute_query(
        "SELECT title, notes FROM tasks WHERE id = ?", (task_id,), fetchone=True
    )
    assert result == ("New Title", "New Note")


def test_delete_task_direct_sql(in_memory_connection):
    db = in_memory_connection

    # Insertion
    task_id = db._execute_query(
        "INSERT INTO tasks (completed, category, expiration, title, notes) VALUES (?, ?, ?, ?, ?)",
        (0, "ToDelete", "2025-05-01 12:00", "Delete me", "soon"),
        lastrowid=True,
    )

    # Suppression
    rows = db._execute_query(
        "DELETE FROM tasks WHERE id = ?", (task_id,), rowcount=True
    )
    assert rows == 1

    # Vérification qu'il n'existe plus
    result = db._execute_query(
        "SELECT COUNT(*) FROM tasks WHERE id = ?", (task_id,), fetchone=True
    )
    assert result[0] == 0
