import requests
import time

def request_check(url):

    try:
        start = time.time()
        response = requests.get(url, timeout=10)
        elapsed = round(time.time() - start, 2)


        if response.status_code == 200:
            return "Success. Connection code: " + str(response.status_code) + ". Connection time: " + str(elapsed) +"s."
        else:
            return "Connection failed with code: " + str(response.status_code)
    except requests.exceptions.RequestException as e:
        return "Connection failed with exception: " + str(e)+"."

def main():
    url_check = 'https://www.djangoproject.com/download/'
    request_check(url_check)

if __name__ == "__main__":
    main()