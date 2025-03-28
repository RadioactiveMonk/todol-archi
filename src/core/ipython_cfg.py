# src/core/ipython_cfg.py

from importlib import reload
from typing import Tuple

import src.core.database.db_controller as db_controller_module
import src.core.database.db_manager as db_manager_module
import src.core.logger as logger_module

# Modules à reloader
import src.models.task as task_module


def reload_all() -> Tuple[object, type]:
    """Recharge les modules critiques en live (pour IPython)"""
    print("🔄 Reloading modules...")

    reload(task_module)
    reload(db_manager_module)
    reload(db_controller_module)
    reload(logger_module)

    print("✅ Modules reloaded successfully!")

    # Réimporter les éléments utiles
    from core.database.db_manager import DbManager
    from models.task import Task

    db = DbManager()
    return db, Task
