# from dataclasses import dataclass
#
#
# @dataclass
# class Check:
#     id: int
#     url: str
#     user_id: int
#     status_http: bool
#     dns_check: bool
#     ssl_check: bool
#     ep_check: bool
#     loading_check: float
#     validation: str

class Check:
    def __init__(self):
        self.status_http = False
        self.dns_check = False
        self.ssl_check = False
        self.ep_check = False
        self.loading_check = 0  # время загрузки в секундах
        self.validation = ""  # строка с ошибками валидации

    def __repr__(self):
        return (f"Check(status_http={self.status_http}, "
                f"dns_check={self.dns_check}, ssl_check={self.ssl_check}, "
                f"loading_check={self.loading_check}s, "
                f"validation='{self.validation}')")

    def to_dict(self):
        """Преобразует объект в словарь для JSON ответа"""
        return {
            'status_http': self.status_http,
            'dns_check': self.dns_check,
            'ssl_check': self.ssl_check,
            'loading_check': self.loading_check,
            'validation': self.validation
        }