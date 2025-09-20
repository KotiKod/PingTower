import requests
import json

def check_rest_endpoints(endpoints, timeout=5, bearer_token=None):
    """
    Проверяет список REST API эндпоинтов.

    endpoints: список словарей вида
       {"url": "https://example.com/api/v1/users", "method": "GET"}
    """
    headers = {}
    if bearer_token:
        headers["Authorization"] = f"Bearer {bearer_token}"

    results = {}
    for ep in endpoints:
        url = ep["url"]
        method = ep["method"].upper()

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

# пример использования:
if __name__ == "__main__":
    endpoints = [
        {"url": "https://jsonplaceholder.typicode.com/posts", "method": "GET"},
        {"url": "https://jsonplaceholder.typicode.com/posts", "method": "POST"},
        {"url": "https://jsonplaceholder.typicode.com/posts/1", "method": "DELETE"},
    ]
    results = check_rest_endpoints(endpoints, timeout=5)
    print(json.dumps(results, indent=2, ensure_ascii=False))
