from importlib import reload
import backend.db_manager
import backend.db_controller
import backend.logger


def reload_all():
    """Recharge tous les modules modifiés dans IPython"""
    print("🔄 Reloading modules...")
    reload(backend.db_manager)
    reload(backend.db_controller)
    reload(backend.logger)
    print("✅ Modules reloaded successfully!")

    # Retourne les nouvelles instances si besoin
    return backend.db_manager.DbManager()
