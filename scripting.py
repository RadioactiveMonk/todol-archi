class DatabaseManager:
    """Gestion de la base de données avec un dispatching des actions"""

    def __init__(self):
        self.actions = {
            "add_task": self.add_task,
            "update_task": self.update_task,
            "delete_task": self.del_task,
            "get_tasks": self.get_tasks,
        }

    def execute(self, action: str, *args, **kwargs):
        """Exécute une action sur la base de données via dict dispatch."""
        return self.actions.get(action, lambda *a, **kw: None)(*args, **kwargs)
