import sqlite3
from backend.core.logger import logger
from configuration.constants import DB_FILE, SQL_CREATE_TABLE, SQL_DROP_TABLE
from typing import Any


class DbController:
    """Gestion des requêtes SQL brutes et de la connexion DB"""

    def __init__(self, db: str = str(DB_FILE)) -> None:
        """Setting up db path"""
        self.db = db
        self._create_table()

    def _execute_query(
        self,
        query: str,
        params: tuple = (),
        fetchone: bool = False,
        fetchall: bool = False,
        lastrowid: bool = False,
        rowcount: bool = False,
    ) -> Any:
        """Process connexion to DB, execute a query and return datas if fetchone, fetchall, lastrowid or rowcount is True

        Parameters
        ----------
        query : str
            an SQL query
        params : tuple, optional
            tupple of values to be modified (for INSERT & UPDATE, by default ())
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
        logger.debug(
            self.debug_message(
                query=query,
                params=params,
                fetchone=fetchone,
                fetchall=fetchall,
                lastrowid=lastrowid,
                rowcount=rowcount,
            )
        )
        try:
            with sqlite3.connect(self.db) as conn:
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
            logger.error(f"SQL: '{e}'")
            return None

    def _create_table(self):
        """Create an SQL table"""

        logger.debug(f"Attempting to create table")
        try:
            query = SQL_CREATE_TABLE
            self._execute_query(query)
            logger.info(f"SQL: table 'tasks' created")
        except sqlite3.DatabaseError as e:
            logger.error(f"SQL: could not create table 'tasks': {e}")

    def _drop_table(self):
        """Delete table 'tasks'"""

        logger.debug(f"Attempting to drop table")
        try:
            query = SQL_DROP_TABLE
            self._execute_query(query)
            logger.info(f"SQL: Table 'tasks' deleted")
        except sqlite3.DatabaseError as e:
            logger.error(f"SQL: Couldn't delete table 'tasks': {e}")

    def debug_message(self, **kwargs):
        """Generate a dynamic SQL debug message"""
        return " | ".join(
            [
                f"{key.upper()}: {value}"
                for key, value in kwargs.items()
                if value is not None
            ]
        )
