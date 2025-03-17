import sqlite3
from backend.logger import logger
from backend.config.constants import DB_PATH
from typing import Any


class DbController:
    """Gestion des requêtes SQL brutes et de la connexion DB"""

    def __init__(self, db_path: str = str(DB_PATH)) -> None:
        """Setting up db path"""
        self.db_path = db_path

    def _execute_query(
        self,
        query: str,
        params: tuple = (),
        fetchone: bool = False,
        fetchall: bool = False,
        lastrowid: bool = False,
        rowcount: bool = False,
    ) -> Any:
        """_summary_

        Parameters
        ----------
        query : str
            an SQL query
        params : tuple, optional
            tupple of values to be modified for INSERT & UPDATE, by default ()
        fetchone : bool, optional
            True to retrieve one value, by default False
        fetchall : bool, optional
            True to retrieve all values, by default False
        lastrowid : bool, optional
            True to retrieve last row id, by default False
        rowcount : bool, optional
            true to retrieve rowcount, by default False

        Returns
        -------
        Any
            depending on boolean parameters
        """
        logger.debug(f"*SQL*: '{query}' | PARAMS: '{params}'")
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("BEGIN TRANSACTION;")
                cursor.execute(query, params)

                result_options = {
                    "fetchone": cursor.fetchone if fetchone else None,
                    "fetchall": cursor.fetchall if fetchall else None,
                    "lastrowid": cursor.lastrowid if lastrowid else None,
                    "rowcount": cursor.rowcount if rowcount else None,
                }

                result = next(
                    (
                        value() if callable(value) else value
                        for key, value in result_options.items()
                        if value
                    ),
                    None,
                )

                conn.commit()

                return result
        except sqlite3.DatabaseError as e:
            logger.error(f"Erreur SQL: '{e}'")
            return None
