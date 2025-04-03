import importlib
import sys
from typing import Tuple

sys.path.insert(0, "src")

import core.database.db_controller as db_controller_module
import core.database.db_manager as db_manager_module
import helpers.log_utils as logger_module
import models.task as task_module


def reload_all() -> Tuple[object, type]:
    print("🔄 Reloading modules...")

    importlib.reload(task_module)
    importlib.reload(db_manager_module)
    importlib.reload(db_controller_module)
    importlib.reload(logger_module)  

    print("✅ Modules reloaded successfully!")

    from core.database.db_manager import DbManager
    from models.task import Task

    db = DbManager()
    return db, Task
