import requests
import time


def request_check(url):

    try:
        start = time.time()
        response = requests.get(url, timeout=10)
        elapsed = round(time.time() - start, 2)


        if response.status_code == 200:
            return {"ok": True, "url": url, "code": 200, "time_to_connect": elapsed}
        else:
            return {"ok": False, "url": url, "code": (response.status_code)}
    except requests.exceptions.RequestException as e:
        return {"ok": False, "url": url, "code": str(e)}

def main():
    url = "https://www.google.com"
    result = request_check(url)
    print(result)

if __name__ == "__main__":
    main()