from importlib import reload
from typing import Tuple

import src.core.database.db_controller
import src.core.database.db_manager
import src.core.logger
import src.models.task
from src.core.database.db_manager import DbManager
from src.models.task import Task


def reload_all() -> Tuple[DbManager, type[Task]]:
    """Recharge tous les modules modifiés dans IPython"""
    print("🔄 Reloading modules...")
    reload(src.models)
    reload(src.models.task)
    reload(src.core.database.db_manager)
    reload(src.core.database.db_controller)
    reload(src.core.logger)
    print("✅ Modules reloaded successfully!")

    from src.models.task import Task

    db = src.core.database.db_manager.DbManager()

    return db, Task
