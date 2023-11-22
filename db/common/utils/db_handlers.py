from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Generator

from db.queries.queries import *
# from db_connectors import ConnectionFactory  ????????????


class _DBHandlerAbstract(ABC):
    """Родительский класс для любого БД-хэндлера"""


class _AnyDBHandler(_DBHandlerAbstract):
    """Инициализирующий класс для любого БД-хэндлера"""

    def __init__(self, connector): #: ConnectionFactory, *args, **kwargs):
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
            yield result
            # c = SalesAggrDataRow(*result)
            # print(c)
            # print(*result)


# connector = ConnectionFactory.connect_db(ConnectorType.SQLite)
# sql = SQLiteHandler(connector)
# # query = select_all('advworksproducts')
# # query = select_aggr_sales_data_for_period(select_aggr_sales_data(), '1/1/2017', '1/3/2017')
# query = select_aggr_sales_data()
#
# sql.db_handle('c:\\src\\local-py\\misis\\etl-project\\db\\aworks_db', query)
