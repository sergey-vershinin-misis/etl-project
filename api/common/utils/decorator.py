from typing import Callable


class URLDecorator:
    """
    Класс-обертка для передачи строки запроса
    """
    def __init__(self, url, params, headers):
        self.url = url
        self.params = params
        self.headers = headers

    def __call__(self,  obj: Callable) -> Callable:
        return obj()(self.url, self.params, self.headers)