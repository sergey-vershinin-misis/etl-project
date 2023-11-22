from abc import ABC, abstractmethod
from typing import Generator

from db.queries.queries import select_all
from db_connectors import ConnectionFactory, ConnectorType


class _DBHandlerAbstract(ABC):
    """Родительский класс для любого БД-хэндлера"""


class _AnyDBHandler(_DBHandlerAbstract):
    """Инициализирующий класс для любого БД-хэндлера"""

    def __init__(self, connector: ConnectionFactory, *args, **kwargs):
        self.connector = connector

    @abstractmethod
    def db_handle(self, *args, **kwargs):
        pass


class SQLiteRead:
    """SQL Lite read data query"""
    def _execute_sql(self, db_path: str, query: str) -> Generator:
        with self.connector(db_path) as connection:
            cursor = connection.cursor()
            query_result = cursor.execute(query)
        yield from query_result


class SQLiteHandler(_AnyDBHandler, SQLiteRead):
    """Run SQLite queries """

    def db_handle(self, db_name: str, query: str, *args):
        query_result = self._execute_sql(db_name, query)

        for result in query_result:
            print(*result)


connector = ConnectionFactory.connect_db(ConnectorType.SQLite)
sql = SQLiteHandler(connector)
sql.db_handle('c:\\src\\local-py\\misis\\etl\\db\\aworks_db', select_all('advworksproducts'))
