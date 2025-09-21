import sqlite3
from typing import List, Dict, Any, Optional

from App.BackEnd.database.Repository.RepositorySQLite.BaseRepository import BaseRepository


class WebsiteRepository(BaseRepository):
    """Репозиторий для работы с пользователями"""

    def create(self, data: Dict[str, Any]) -> int:
        try:
            cursor = self._execute_query(
                'INSERT INTO users (login, password) VALUES (?, ?)',
                (data['login'], data['password'])
            )
            self._commit()
            user_id = cursor.lastrowid
            print(f"✅ Пользователь {data['login']} создан с ID: {user_id}")
            return user_id
        except sqlite3.IntegrityError:
            print(f"❌ Пользователь с username {data['login']} уже существует")
            raise

    def get_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        cursor = self._execute_query('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        return dict(user) if user else None

    def get_all(self) -> List[Dict[str, Any]]:
        cursor = self._execute_query('SELECT * FROM users ORDER BY id DESC')
        return [dict(user) for user in cursor.fetchall()]

    def update(self, id: int, data: Dict[str, Any]) -> bool:
        try:
            self._execute_query(
                'UPDATE users SET login = ?, password = ? WHERE id = ?',
                (data['login'], data['password'], id)
            )
            self._commit()
            return True
        except sqlite3.Error:
            return False