import asyncio

from App.BackEnd.Services.StatusChecking.StatusHTTP import StatusHTTP
from App.BackEnd.Services.StatusChecking.DNSCheck import DNSCheck
from App.BackEnd.Services.StatusChecking.CertificationSSL import CertificationSSL
from App.BackEnd.Services.StatusChecking.ValidationJSON import Validation
from App.BackEnd.Services.StatusChecking.webdriverCheck import WebdriverCheck
from App.BackEnd.Models.Check import Check


class Controller:
    def __init__(self, repository, website):
        self.repository = repository
        self.website = website

    def websiteChecking(self):
        check = Check()
        if self.website.validation:
            if self.website.status_http:
                request_check = StatusHTTP.request_check(self.website.url)
                val = Validation.validation(request_check, Validation.http_schema)
                check.status_http = request_check["ok"]
                if not val:
                    check.validation += "status_http "
            if self.website.dns_check:
                resolve_url = asyncio.run(DNSCheck.resolve_url(self.website.url))
                val = Validation.validation(resolve_url, Validation.dns_schema)
                check.dns_check = resolve_url["ok"]
                if not val:
                    check.validation += "dns_check "
            if self.website.ssl_check:
                ssl = CertificationSSL.check_ssl_certificate(self.website.url)
                val = Validation.validation(ssl, Validation.ssl_schema)
                check.ssl_check = ssl["ok"]
                if not val:
                    check.validation += "ssl_check"
        else:
            if self.website.status_http:
                request_check = StatusHTTP.request_check(self.website.url)
                check.status_http = request_check["ok"]
            if self.website.dns_check:
                resolve_url = asyncio.run(DNSCheck.resolve_url(self.website.url))
                check.dns_check = resolve_url["ok"]
            if self.website.ssl_check:
                ssl = CertificationSSL.check_ssl_certificate(self.website.url)
                check.ssl_check = ssl["ok"]

        if self.website.loading_check:
            webdriver_check = WebdriverCheck.webdriver_check(self.website.url)
            check.loading_check = webdriver_check["time_to_load"]

        return check
            