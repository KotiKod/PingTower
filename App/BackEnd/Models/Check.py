from dataclasses import dataclass


@dataclass
class Check:
    id: int
    url: str
    user_id: int
    status_http: bool
    dns_check: bool
    ssl_check: bool
    ep_check: bool
    loading_check: float
    validation: str
