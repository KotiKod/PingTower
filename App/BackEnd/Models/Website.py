from dataclasses import dataclass


@dataclass
class Website:
    id: int
    url: str
    user_id: int
    status_http: bool
    dns_check: bool
    ssl_check: bool
    ep_check: bool
    loading_check: bool
    validation: bool
    time_period: int
