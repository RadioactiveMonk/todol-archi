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
    db = DatabaseManager()

    print("\n🔍 Tâches avant modification:")
    for task in db.get_tasks():
        print(task)

    task_id = int(input("\n✏️ Entrez l'ID de la tâche à modifier : "))
    new_title = input("📝 Nouveau titre : ")

    task = db.get_tasks()[task_id - 1]  # On récupère la tâche existante
    task.title = new_title  # On modifie uniquement le titre pour le test

    db.update_task(task)

    print("\n✅ Tâche mise à jour avec succès !")
    print("\n🔍 Tâches après modification:")
    for task in db.get_tasks():
        print(task)
