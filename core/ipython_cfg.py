from importlib import reload
import backend.database.db_manager
import backend.database.db_controller
import backend.core.logger
import backend.models.task


def reload_all():
    """Recharge tous les modules modifiés dans IPython"""
    print("🔄 Reloading modules...")
    reload(backend.models)
    reload(backend.models.task)
    reload(backend.database.db_manager)
    reload(backend.database.db_controller)
    reload(backend.core.logger)
    print("✅ Modules reloaded successfully!")

    from backend.models.task import Task

    db = backend.database.db_manager.DbManager()

    return db, Task
