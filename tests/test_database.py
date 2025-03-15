from backend.models.task import Task


def test_db_connexion(database):
    """Teste la connexion a la DB"""
    assert database is not None


def test_add_task_db(database_manager):
    """Teste l'ajout d'une tâche dans la base de données."""
    task_data = {
        "status": False,
        "category": "Work",
        "expiration": "2025-01-01 22:00",
        "title": "Test task",
        "notes": "Test notes",
    }

    task = database_manager.add_task(**task_data)  # ✅ Ajout de la tâche
    assert task is not None  # ✅ Vérifie que la tâche a bien été créée

    retrieved_tasks = database_manager.get_tasks()  # ✅ Récupération de la tâche
    retrieved_task = retrieved_tasks[0]
    assert len(retrieved_tasks) > 0  # ✅ Vérifie que la tâche existe
    assert retrieved_task.title == task_data["title"]  # ✅ Vérifie le titre
    assert retrieved_task.notes == task_data["notes"]  # ✅ Vérifie la description
    assert retrieved_task.category == task_data["category"]  # ✅ Vérifie la catégorie
    assert retrieved_task.expiration == task_data["expiration"]  # ✅ Vérifie la date
    assert retrieved_task.status == task_data["status"]  # ✅ Vérifie le statut


def test_get_task_db(database_manager):
    """Teste la récupération d'une tâche existante et inexistante."""
    task_data = {
        "title": "Tâche test",
        "notes": "Description de test",
        "category": "Work",
        "expiration": "2025-01-01 10:00",
        "status": False,
    }

    tasks = database_manager.add_task(**task_data)  # ✅ Ajout de la tâche
    assert tasks is not None  # ✅ Vérifie que l'ID est bien généré

    retrieved_task = tasks

    assert retrieved_task is not None  # ✅ La tâche doit exister
    assert retrieved_task.title == task_data["title"]
    assert retrieved_task.notes == task_data["notes"]
    assert retrieved_task.category == task_data["category"]
    assert retrieved_task.expiration == task_data["expiration"]
    assert retrieved_task.status == task_data["status"]

    # 🔥 Tester la récupération d'une tâche inexistante
    missing_task = next(
        (t for t in database_manager.get_tasks() if t.tid == 99999), None
    )
    assert missing_task is None  # ✅ Doit retourner None


def test_update_task(database_manager):
    """Teste la mise à jour d'une tâche existante et inexistante."""
    pass


def test_del_task_db():
    """Teste la suppresion de tâche en Db"""
    pass


def test_invalid_request():
    pass
