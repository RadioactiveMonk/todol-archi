class DatabaseControler:
    """Méthodes privées pour la manipulation de la BDD"""

    def __init__(self) -> None:

        self.queries = {
            "update_task_status": "UPDATE tasks SET status = ? WHERE id = ?",
        }

    def _request(self, query_key: str, params: tuple):
        pass
    def _execute(self, query: str, params: tuple):
        pass

    