import sqlite3
from typing import List, Dict, Any, Optional

from App.BackEnd.database.Repository.RepositorySQLite.BaseRepository import BaseRepository
from App.BackEnd.Models.Website import Website


class WebsiteRepository(BaseRepository):
    """Репозиторий для работы с пользователями"""

    def create(self, website: Website) -> None:
        """Сохраняет или обновляет website в базе данных"""
        # conn = self.db
        conn = sqlite3.connect("data.db")
        try:
            cursor = conn.execute('''
                        INSERT INTO websites (url, user_id, status_http, dns_check, ssl_check, 
                                             ep_check, loading_check, validation, time_period)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                website.url, website.user_id, int(website.status_http),
                int(website.dns_check), int(website.ssl_check),
                int(website.ep_check), int(website.loading_check),
                int(website.validation), website.time_period
            ))
            website.id = cursor.lastrowid
            conn.commit()
        finally:
            conn.close()

    def get_websites(self, user_id: int) -> List[Website]:
        """Получает все websites по ID пользователя"""
        conn = sqlite3.connect("data.db")
        try:
            cursor = conn.execute('''
                SELECT id, url, user_id, status_http, dns_check, ssl_check, 
                       ep_check, loading_check, validation, time_period
                FROM websites WHERE user_id = ?
                ORDER BY id
            ''', (user_id,))

            websites = []
            for row in cursor.fetchall():
                website = Website(
                    id=row[0],
                    url=row[1],
                    user_id=row[2],
                    status_http=bool(row[3]),
                    dns_check=bool(row[4]),
                    ssl_check=bool(row[5]),
                    ep_check=bool(row[6]),
                    loading_check=bool(row[7]),
                    validation=bool(row[8]),
                    time_period=row[9]
                )
                websites.append(website)
            conn.commit()
        finally:
            conn.close()
        return websites

    def delete(self, website_id: int) -> bool:
        """Удаляет website по ID"""
        with sqlite3.connect(self.db) as conn:
            cursor = conn.execute('DELETE FROM websites WHERE id = ?', (website_id,))
            return cursor.rowcount > 0
