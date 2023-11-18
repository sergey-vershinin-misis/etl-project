import logging
from abc import ABC, abstractmethod
from enum import Enum
import sqlite3
from contextlib import contextmanager
from typing import AsyncContextManager, TypeVar, Union, Type

import backoff
from pymongo import errors as mongo_errors

logger = logging.getLogger(__name__)

T = TypeVar('T', bound=AsyncContextManager)


class _DBConnectorAbstract(ABC):
    """Родительский класс для любого класса-коннектора"""

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class _SQLiteConnector(_DBConnectorAbstract):
    """SQLite-коннектор (yield)"""

    @contextmanager
    @backoff.on_exception(backoff.expo, (sqlite3.OperationalError, sqlite3.NotSupportedError), logger=logger)
    def __call__(self, db_name: str) -> T:

        try:
            _connection = sqlite3.connect(db_name)
            _connection.row_factory = sqlite3.Row

            yield _connection
        except (sqlite3.OperationalError, sqlite3.NotSupportedError) as err:
            logger.error(f'SQLite error occurred {err} {self.__class__}')

        # _connection.close()


class _MongoConnector(_DBConnectorAbstract):
    @contextmanager
    @backoff.on_exception(backoff.expo,
                          mongo_errors.ConnectionFailure,
                          logger=logger)
    def __call__(self, *args, **kwargs):
        pass


class ConnectorType(Enum):
    SQLite = "SQLite",
    MongoDB = "MongoDB"


class ConnectionFactory:
    CONNECTIONS = {
        ConnectorType.SQLite: _SQLiteConnector,
        ConnectorType.MongoDB: _MongoConnector
    }

    @classmethod
    def connect_db(cls, connector_type: ConnectorType) -> Type[_SQLiteConnector | _MongoConnector | None]:
        connector = cls.CONNECTIONS.get(connector_type)
        return connector()


if __name__ == "__main__":
    ConnectionFactory()

