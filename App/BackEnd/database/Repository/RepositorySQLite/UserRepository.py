import sqlite3
from typing import List, Dict, Any, Optional

from App.BackEnd.database.Repository.RepositorySQLite.BaseRepository import BaseRepository


class UserRepository(BaseRepository):
    """Репозиторий для работы с пользователями"""

    def create(self, data: Dict[str, Any]) -> int:
        try:
            cursor = self._execute_query(
                'INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
                (data['username'], data['email'], data['password_hash'])
            )
            self._commit()
            user_id = cursor.lastrowid
            print(f"✅ Пользователь {data['username']} создан с ID: {user_id}")
            return user_id
        except sqlite3.IntegrityError:
            print(f"❌ Пользователь с username {data['username']} уже существует")
            raise

    def get_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        cursor = self._execute_query('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        return dict(user) if user else None

    def get_all(self) -> List[Dict[str, Any]]:
        cursor = self._execute_query('SELECT * FROM users ORDER BY created_at DESC')
        return [dict(user) for user in cursor.fetchall()]

    def update(self, user_id: int, data: Dict[str, Any]) -> bool:
        try:
            self._execute_query(
                'UPDATE users SET username = ?, email = ? WHERE id = ?',
                (data['username'], data['email'], user_id)
            )
            self._commit()
            return True
        except sqlite3.Error:
            return False
