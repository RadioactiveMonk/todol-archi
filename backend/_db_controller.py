import sqlite3
from backend.logger import logger
from backend.config.constants import DB_PATH
from backend.models.task import Task
from typing import List, Dict, Any


class DbController:
    """Gestion des requêtes SQL brutes et de la connexion DB"""

    def __init__(self, db_path: str = str(DB_PATH)) -> None:
        self.db_path = db_path

    def _execute_query(
        self,
        query: str,
        params: tuple = (),
        fetchone: bool = False,
        fetchall: bool = False,
        lastrowid: bool = False,
    ) -> Any:
        """Execute une requête SQL avec gestion des erreurs"""
        logger.debug(f"*SQL*: '{query}' | PARAMS: '{params}'")
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("BEGIN TRANSACTION;")
                cursor.execute(query, params)

                if fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
                elif lastrowid:
                    result = cursor.lastrowid
                else:
                    result = None

                conn.commit()
                return result
        except sqlite3.DatabaseError as e:
            logger.error(f"Erreur SQL: '{e}'")
            return None


