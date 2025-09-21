from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


class WebdriverCheck:
    def webdriver_check(url):
        options = Options()
        options.add_argument('--headless')
        service = Service(executable_path="chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)

        start = time.time()
        driver.get(url)
        end = time.time()
        return {"time_to_load": round(end - start, 2)}


# def main():
#     url = "https://www.google.com"
#     print(webdriver_check(url))
#
#
# if __name__ == "__main__":
#     main()