import requests
import time


class StatusHTTP:
    def request_check(url):
        """
        Проверяет доступность URL
        Возвращает результат в том же формате что и оригинальная функция
        """
        try:
            start = time.time()
            response = requests.get(url, timeout=10)
            elapsed = round(time.time() - start, 2)

            if response.status_code == 200:
                return {"ok": True, "url": url, "code": 200, "time_to_connect": elapsed}
            else:
                return {"ok": False, "url": url, "code": response.status_code}
        except requests.exceptions.RequestException as e:
            return {"ok": False, "url": url, "code": str(e)}