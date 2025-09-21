import sqlite3
import threading
from typing import Optional


class SQLite:
    """
    Синглтон ТОЛЬКО для управления подключением к базе данных.
    Не содержит бизнес-логики выполнения запросов.
    """

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, db_path: str = "app.db"):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.db_path = db_path
                cls._instance.connection = None
            return cls._instance

    def get_connection(self) -> sqlite3.Connection:
        """Возвращает соединение с базой данных (создает если нужно)"""
        if self.connection is None:
            try:
                self.connection = sqlite3.connect(self.db_path)
                self.connection.row_factory = sqlite3.Row
                self.connection.execute("PRAGMA foreign_keys = ON")
                print(f"✅ Подключение к базе данных {self.db_path} установлено")
            except sqlite3.Error as e:
                print(f"❌ Ошибка подключения: {e}")
                raise
        return self.connection

    def close(self) -> None:
        """Закрывает соединение с базой данных"""
        if self.connection:
            self.connection.close()
            self.connection = None
            print("✅ Соединение с базой данных закрыто")

    def initialize_database(self) -> None:
        """Инициализирует структуру базы данных"""
        try:
            conn = self.get_connection()
            with conn:
                # Таблица пользователей
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        login TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                    )
                ''')

                # Таблица сайтов
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS websites (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        url TEXT NOT NULL,
                        user_id INTEGER NOT NULL,
                        status_http BOOLEAN NOT NULL,
                        dns_check BOOLEAN NOT NULL,
                        ssl_check BOOLEAN NOT NULL,
                        ep_check BOOLEAN NOT NULL,
                        loading_check BOOLEAN NOT NULL,
                        validation BOOLEAN NOT NULL,
                        time_period INTEGER NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
                    )
                ''')

                # Таблица проверок
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS checks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        url TEXT NOT NULL,
                        user_id INTEGER NOT NULL,
                        status_http BOOLEAN,
                        dns_check BOOLEAN,
                        ssl_check BOOLEAN,
                        ep_check BOOLEAN,
                        loading_check BOOLEAN,
                        validation BOOLEAN,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
                    )
                ''')

                print("✅ Структура базы данных инициализирована")

        except sqlite3.Error as e:
            print(f"❌ Ошибка при инициализации базы данных: {e}")
            raise

    def __del__(self):
        """Деструктор - закрывает соединение при удалении объекта"""
        self.close()