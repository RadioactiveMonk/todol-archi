# test_db.py
from backend.database import DatabaseManager


def test_delete_task():
    """Test de suppression d'une tâche"""
    db = DatabaseManager()

    print("\n🔍 Tâches avant suppression:")
    for task in db.get_tasks():
        print(task)

    task_id = int(input("\n🗑️ Entrez l'ID de la tâche à supprimer : "))

    db.del_task(task_id)
    print(f"\n✅ Tâche {task_id} supprimée !")

    print("\n🔍 Tâches après suppression:")
    for task in db.get_tasks():
        print(task)


if __name__ == "__main__":
    test_delete_task()
