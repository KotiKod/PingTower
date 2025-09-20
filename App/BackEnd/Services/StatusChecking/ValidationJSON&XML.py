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

api_schema = {
    "type": "object",
    "properties": {
        "url": {"type": "string"},
        "slovar": {"type": "object"},
    },
    "required": ["url", "slovar"],
    "additionalProperties": True,
}

webdriver_schema = {
    "type": "object",
    "properties": {
        "time_to_load": {"type": "number"},
    },
    "required": ["time_to_load"],
    "additionalProperties": True,
}

load_schema = {
      "type": "object",
  "properties": {
    "url": {
      "type": "string",
      "format": "uri"
    },
    "total_requests": {
      "type": "integer",
      "minimum": 0
    },
    "successful_requests": {
      "type": "integer",
      "minimum": 0
    },
    "failed_requests": {
      "type": "integer",
      "minimum": 0
    },
    "error_percentage": {
      "type": "number",
      "minimum": 0,
      "maximum": 100
    },
    "average_response_time_sec": {
      "type": "number",
      "minimum": 0
    },
    "total_time_sec": {
      "type": "number",
      "minimum": 0
    },
    "status_breakdown": {
      "type": "object",
      "patternProperties": {
        "^[0-9]{3}$": {
          "type": "integer",
          "minimum": 0
        }
      },
      "additionalProperties": False
    }
  },
  "required": [
    "url",
    "total_requests",
    "successful_requests",
    "failed_requests",
    "error_percentage",
    "average_response_time_sec",
    "total_time_sec",
    "status_breakdown"
  ],
  "additionalProperties": False
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