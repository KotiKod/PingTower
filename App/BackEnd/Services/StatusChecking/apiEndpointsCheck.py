import requests
import json
from urllib.parse import urljoin, urlparse

def resolve_base_url(openapi_url, data):
    """
    Возвращает правильный base_url даже если в servers указан относительный путь.
    """
    if "swagger" in data:  # Swagger 2.0
        base_url = data.get("host", "")
        scheme = (data.get("schemes") or ["https"])[0]
        base_url = f"{scheme}://{base_url}{data.get('basePath', '')}"
    else:  # OpenAPI 3.x
        base_url = data.get("servers", [{}])[0].get("url", "")
        if base_url.startswith("/"):  # относительный путь
            parsed = urlparse(openapi_url)
            base_url = f"{parsed.scheme}://{parsed.netloc}{base_url}"
    return base_url

def check_openapi_endpoints(openapi_url, timeout=5, bearer_token=None):
    """
    Получает все эндпоинты из OpenAPI/Swagger JSON и проверяет их.

    Параметры:
    - openapi_url (str): ссылка на OpenAPI JSON
    - timeout (int): таймаут в секундах
    - bearer_token (str): опционально, токен для Authorization: Bearer
    """
    headers = {}
    if bearer_token:
        headers["Authorization"] = f"Bearer {bearer_token}"

    try:
        response = requests.get(openapi_url, timeout=timeout, headers=headers)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Cannot get OpenAPI: {e}"}

    base_url = resolve_base_url(openapi_url, data)
    paths = data.get("paths", {})

    endpoints = []
    for path, methods in paths.items():
        for method in methods.keys():
            full_url = urljoin(base_url + "/", path.lstrip("/"))
            endpoints.append({
                "url": full_url,
                "method": method.upper()
            })

    results = {}
    for ep in endpoints:
        url = ep["url"]
        method = ep["method"]
        try:
            if method == "GET":
                r = requests.get(url, timeout=timeout, headers=headers)
            elif method == "POST":
                r = requests.post(url, json={}, timeout=timeout, headers=headers)
            elif method == "PUT":
                r = requests.put(url, json={}, timeout=timeout, headers=headers)
            elif method == "DELETE":
                r = requests.delete(url, timeout=timeout, headers=headers)
            else:
                results[url] = {"method": method, "error": "Unsupported HTTP method"}
                continue

            try:
                response_data = r.json()
            except ValueError:
                response_data = r.text

            results[url] = {
                "method": method,
                "status_code": r.status_code,
                "response": response_data
            }
        except requests.exceptions.RequestException as e:
            results[url] = {"method": method, "error": str(e)}

    return results

# пример использования
if __name__ == "__main__":
    url = "https://petstore3.swagger.io/api/v3/openapi.json"
    results = check_openapi_endpoints(url, timeout=5)
    print(json.dumps(results, indent=2, ensure_ascii=False))
