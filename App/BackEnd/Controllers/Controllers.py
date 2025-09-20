from App.BackEnd.Services.StatusChecking.StatusHTTP import StatusHTTP
from App.BackEnd.Services.StatusChecking.DNSCheck import DNSCheck
from App.BackEnd.Services.StatusChecking.CertificationSSL import CertificationSSL
from App.BackEnd.Services.StatusChecking.ValidationJSON import Validation

class Controller:
    def __init__(self, repository, website):
        self.repository = repository
        self.website = website

    def websiteChecking(self):

        if self.website.validation:
            if self.website.status_http:
                request_check = StatusHTTP.request_check(self.website.url)
                Validation.validation(request_check, Validation.http_schema)
            if self.website.dns_check:
                DNSCheck.resolve_url(self.website.url)
            if self.website.ssl_check:
                CertificationSSL.check_ssl_certificate(self.website.url)

        else:
            if self.website.status_http:
                StatusHTTP.request_check(self.website.url)
            if self.website.dns_check:
                DNSCheck.resolve_url(self.website.url)
            if self.website.ssl_check:
                CertificationSSL.check_ssl_certificate(self.website.url)
