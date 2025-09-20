from App.BackEnd.ScriptsForChecking.requestCheck import request_check


def main():
    url_check = 'https://www.djangoproject.com/download/'
    request_check(url_check)


if __name__ == "__main__":
    main()
