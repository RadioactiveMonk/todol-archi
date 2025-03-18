from importlib import reload
import backend.db_manager
import backend.db_controller
import backend.logger
import backend.models.task


def reload_all():
    """Recharge tous les modules modifiés dans IPython"""
    print("🔄 Reloading modules...")
    reload(backend.models)
    reload(backend.models.task)
    reload(backend.db_manager)
    reload(backend.db_controller)
    reload(backend.logger)
    print("✅ Modules reloaded successfully!")

    from backend.models.task import Task

    db = backend.db_manager.DbManager()

    return db, Task
