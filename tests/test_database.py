from backend.models.task import Task


def test_add_and_get_task(in_memory_db):
    task = Task(
        completed=False,
        category="Test",
        expiration="2025-01-01 12:00",
        title="Test task",
        notes="Test note",
    )
    in_memory_db.add_task(task)
    assert task.tid is not None

    tasks = in_memory_db.get_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test task"


def test_update_task(in_memory_db):
    task = Task(
        completed=False,
        category="Cat",
        expiration="2025-01-01 12:00",
        title="Old title",
        notes="Note",
    )

    tid = in_memory_db.add_task(task)
    task.tid = tid  # 🔥 important pour que .tid soit bien renseigné dans l'objet

    updated = in_memory_db.update_task(
        task_id=task.tid,
        completed=True,  # on peut laisser bool ici, la méthode gère le cast
        category="Test",
        expiration="2025-01-01 12:00",
        title="Test task",
        notes="Test note",
    )

    assert updated is True
    tasks = in_memory_db.get_tasks()
    assert tasks[0]["title"] == "Test task"
    assert bool(tasks[0]["completed"])


def test_delete_task(in_memory_db):
    task = Task(
        title="To delete", notes="...", category="...", expiration="2025-01-01 12:00"
    )
    in_memory_db.add_task(task)

    deleted = in_memory_db.delete_task(task.tid)
    assert deleted is True

    tasks = in_memory_db.get_tasks()
    assert len(tasks) == 0
