from backend.database.db_manager import DbManager
from backend.models.task import Task
from backend.core.logger import logger


def toggle_task_status(task_id: int, db: DbManager) -> bool:
    """Inverse le statut 'completed' d'une tâche donnée.

    Parameters
    ----------
    task_id : int
        ID de la tâche à modifier.
    db : DbManager
        Instance de DbManager à utiliser.

    Returns
    -------
    bool
        True si la tâche a été modifiée avec succès, False sinon.
    """

    tasks = db.get_tasks()
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        logger.warning(f"[toggle_status] Task ID {task_id} introuvable.")
        return False

    new_status = not bool(task["completed"])
    success = db.update_task(task_id=task_id, completed=new_status)

    if success:
        logger.info(f"[toggle_status] Tâche ID {task_id} -> completed = {new_status}")
    else:
        logger.warning(f"[toggle_status] Échec de mise à jour pour ID {task_id}")

    return success


