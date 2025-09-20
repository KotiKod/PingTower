import asyncio

from App.BackEnd.Services.StatusChecking.StatusHTTP import request_check
from App.BackEnd.Services.StatusChecking.DNSCheck import resolve_url

def main():
    url_check = 'https://www.djangoproject.com/download/'
    resolver = asyncio.run(resolve_url(url_check))
    print(request_check(url_check))
    print(resolver)


if __name__ == "__main__":
    main()
