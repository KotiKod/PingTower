import asyncio

from jsonschema import validate, ValidationError
ssl_schema = {
        "type": "object",
    "properties": {
        "ok": {"type": "boolean"},
        "url": {"type": "string"},
        "host": {"type": "string"},
        "issuer": {"type": "object"},
        "subject": {"type": "object"},
        "not_before": {"type": "string", "format": "date-time"},
        "not_after": {"type": "string", "format": "date-time"},
        "expired": {"type": "boolean"},
        "valid_now": {"type": "boolean"},
        "error": {"type": "string"},
    },
    "required": ["ok", "url"],
    "additionalProperties": True,
}

http_schema = {
    "type": "object",
    "properties": {
        "ok": {"type": "boolean"},
        "url": {"type": "string"},
        "code": {"type": "integer"},
        "time_to_connect": {"type": "number"},
    },
    "required": ["ok", "url"],
    "additionalProperties": True,
}

dns_schema = {
    "type": "object",
    "properties": {
        "ok": {"type": "boolean"},
        "url": {"type": "string"},
        "results": {"type": "object"},
        "error": {"type": "string"},

    },
    "required": ["ok", "url"],
    "additionalProperties": True,
}

def validation(url, schema):
    try:
        validate(instance=url, schema=schema)
        return True
    except ValidationError as e:
        return False

def main():
    from StatusHTTP import request_check
    from DNSCheck import resolve_url
    from CertificationSSL import check_ssl_certificate
    url = "https://www.google.com"
    check_this = request_check(url)
    cheak_again = asyncio.run(resolve_url(url))
    chek = check_ssl_certificate(url)
    print(check_this)
    print(cheak_again)
    print(chek)
    print(validation(check_this, http_schema))
    print(validation(cheak_again, dns_schema))
    print(validation(chek, ssl_schema))

if __name__ == "__main__":
    main()