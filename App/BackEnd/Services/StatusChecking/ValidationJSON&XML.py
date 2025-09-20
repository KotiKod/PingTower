from zipfile import sizeEndCentDir

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
    "additionalProperties": False,
}

http_schema = {
    "type": "object",
    "properties": {
        "ok": {"type": "boolean"},
        "url": {"type": "string"},
        "code": {"type": "integer"},
        "time_to_connect": {"type": "string", "format": "date-time"},
    },
    "required": ["ok", "url"],
    "additionalProperties": False,
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
    "additionalProperties": False,
}

def validation(url, schema):
    try:
        validate(instance=url, schema=schema)
        return True
    except ValidationError as e:
        return False