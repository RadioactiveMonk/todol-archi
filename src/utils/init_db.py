"""init_db.py – Initialise la base de données si la table 'tasks' n'existe pas."""

from core.sql_schema import SQL_CREATE_TASKS_TABLE
from helpers.contextmanagers import open_db
from core.log_manager import logger
from utils.path_utils import DB_FILE


def init_db() -> None:
    """Crée la table 'tasks' si elle n'existe pas."""
    try:
        with open_db(DB_FILE) as db:
            logger.debug("Initialisation de la base de données...")
            db.create(SQL_CREATE_TASKS_TABLE)
            logger.success("✔️ Table 'tasks' prête.")
    except Exception as e:
        logger.error(f"❌ Erreur lors de l'initialisation de la DB : {e}")
