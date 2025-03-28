import sqlite3
from pathlib import Path
from typing import Any

from core.database_config import SQL_CREATE_TABLE, SQL_DROP_TABLE
from core.logger import logger
from core.path import DB_FILE


class DbController:
    """Gestion des requêtes SQL brutes et de la connexion DB"""

    def __init__(self, db: Path | None = None) -> None:
        """Setting up db path"""

        self.db = db if db is not None else DB_FILE  # chemin de la base de données
        self.conn = sqlite3.connect(self.db, uri=True, check_same_thread=False)
        self._create_table()

    def _execute_query(
        self,
        query: str,
        params: tuple[Any, ...] = (),
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
        logger.debug(f"📂 Using database file: {self.db}")

        try:
            cursor = self.conn.cursor()
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
                    for _, value in result_options.items()
                    if value
                ),
                None,
            )

            self.conn.commit()
            return result

        except sqlite3.DatabaseError as e:
            logger.error(f"SQL: '{e}'")
            return None

    def _create_table(self):
        """Create table 'tasks' if it doesn't exist.
        The table contains the following columns:
            - id: integer, primary key
            - completed: integer (0 or 1)
            - category: text
            - expiration: text
            - title: text
            - notes: text
        """

        logger.debug("Attempting to create table")
        try:
            query = SQL_CREATE_TABLE
            self._execute_query(query)
            logger.info("SQL: table 'tasks' created")
        except sqlite3.DatabaseError as e:
            logger.error(f"SQL: could not create table 'tasks': {e}")

    def _drop_table(self):
        """Drop table 'tasks' if it exists (for testing purposes)"""

        logger.debug("Attempting to drop table")
        try:
            query = SQL_DROP_TABLE
            self._execute_query(query)
            logger.info("SQL: Table 'tasks' deleted")
        except sqlite3.DatabaseError as e:
            logger.error(f"SQL: Couldn't delete table 'tasks': {e}")

    def __del__(self):
        """Close the connexion or log a warning."""
        try:
            self.conn.close()
        except Exception as e:
            logger.warning(f"Error closing DB connection: {e}")

    def execute_and_confirm(
        self,
        query: str,
        params: tuple[Any, ...] = (),
        log_context: str = "",
    ) -> bool:
        """
        Execute a modifying query (UPDATE, DELETE) and confirms that at least one row was affected.
        Logs a warning if no change occurred.
        """

        try:
            cursor = self.conn.cursor()
            cursor.execute("BEGIN TRANSACTION;")
            cursor.execute(query, params)
            self.conn.commit()

            # doit être différent de 0 si il y a eu une modification
            affected = cursor.rowcount

            if affected:
                logger.info(f"✅ {log_context} (rowcount={affected})")
                return True
            else:
                logger.warning(f"⚠️ {log_context} - No row affected (rowcount=0)")
                return False

        except sqlite3.DatabaseError as e:
            logger.error(f"❌ {log_context} - SQL error: {e}")
            return False

    def debug_message(self, **kwargs: Any) -> str:
        """Generate a dynamic SQL debug message"""
        return " | ".join(
            [
                f"{key.upper()}: {value}"
                for key, value in kwargs.items()
                if value is not None
            ]
        )
