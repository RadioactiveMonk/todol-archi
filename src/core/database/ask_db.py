import sqlite3

from helpers.log_utils import logger


class AskDB:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.routes = {
            "exec": self.exec,
            "create": self.create,
            "insert": self.insert,
            "select": self.select,
            "update": self.update,
            "delete": self.delete,
            "drop": self.drop,
        }

    def dispatch(self, action: str, sql: str, *args):
        logger.debug(f"Sql action route: {action} | {sql} | args={args}")

        if action not in self.routes:
            raise ValueError(f"Uknown DB action: {action}")
        return self.routes[action](sql, *args)

    def exec(self, sql: str, *args):
        logger.debug(f"Executing: {sql} | args={args}")

        self.conn.execute(sql, args)

    def create(self, sql: str):
        logger.debug(f"Executing CREATE TABLE: {sql}")

        self.conn.execute(sql)

    def insert(self, sql: str, *args):
        logger.debug(f"Executing INSERT INTO: {sql} | args={args}")

        cursor = self.conn.execute(sql, args)
        self.conn.commit()
        return cursor.lastrowid

    def select(self, sql: str, *args):
        logger.debug(f"Executing SELECT: {sql} | args={args}")

        return self.conn.execute(sql, args).fetchall()
    
    def select_one(self, sql: str, *args):
        logger.debug(f"Executing SELECT: {sql} | args={args}")

        return self.conn.execute(sql, args).fetchone()

    def update(self, sql: str, *args):
        logger.debug(f"Executing UPDATE FROM: {sql} | args={args}")

        self.conn.execute(sql, args)

    def delete(self, sql: str, *args):
        logger.debug(f"Executing DELETE FROM: {sql} | args={args}")

        self.conn.execute(sql, args)
        self.conn.commit()

    def drop(self, sql: str):
        logger.debug(f"Executing DROP TABLE: {sql}")

        self.conn.execute(sql)
