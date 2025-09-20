from App.BackEnd.Services.StatusChecking.StatusHTTP import request_check
from App.BackEnd.Services.StatusChecking.DNSCheck import resolve_url

def main():
    url_check = 'https://www.djangoproject.com/download/'
    print(request_check(url_check))
    print(resolve_url(url_check))


if __name__ == "__main__":
    main()
