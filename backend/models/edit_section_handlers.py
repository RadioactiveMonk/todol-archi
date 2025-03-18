from backend.db_manager import DbManager


class TaskHandlers:
    """Manage the interaction with the db for edit sections handlers"""

    def __init__(self) -> None:
        self.db = DbManager()
        self.get_all = self.db.get_tasks()

    def delete_handler(self):
        pass

    def edit_handler(self):
        pass

    
