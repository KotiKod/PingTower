import sqlite3
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

from App.BackEnd.database.databases import SQLite


class BaseRepository(ABC):
    """Абстрактный базовый класс для репозиториев с общими методами"""

    def __init__(self, db: SQLite):
        self.db = db

    def _execute_query(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """Выполняет SQL запрос (внутренний метод для репозиториев)"""
        conn = self.db.get_connection()
        return conn.execute(query, params)

    def _execute_many(self, query: str, params_list: list) -> None:
        """Выполняет массовую вставку данных (внутренний метод)"""
        conn = self.db.get_connection()
        conn.executemany(query, params_list)
        conn.commit()

    def _commit(self) -> None:
        """Фиксирует изменения в базе данных"""
        conn = self.db.get_connection()
        conn.commit()

    @abstractmethod
    def create(self, data: Dict[str, Any]) -> int:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_all(self) -> List[Dict[str, Any]]:
        pass