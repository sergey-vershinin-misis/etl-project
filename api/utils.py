from typing import Callable, Tuple, Dict
from http import HTTPStatus
import requests

from abc import ABC, abstractmethod


class MakeRequestAbstract(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class MakeGetRequest(MakeRequestAbstract):
    """
    Выполнение GET-запроса к API
    """

    def __call__(self, *args, **kwargs) -> Tuple[int, str]:
        url, params, headers = args
        with requests.Session() as session:
            response = session.get(url=url, params=params, headers=headers)

        return response.status_code, response.text


class MakePostRequest(MakeRequestAbstract):
    """
    Выполнение POST-запроса к API
    """

    def __call__(self, *args, **kwargs):
        pass


class RequestFactory:

    endpoints = {}

    """Класс-фабрика запросов к API-сайта"""
    def __init__(self, path_decorator: Callable, request_handler: Callable):
        """

        :param path_decorator: класс-декоратор, который формирует строку запроса
        :param request_handler: оборачиваемый класс, выполняющий запрос
        """
        self.path_decorator = path_decorator
        self.request_handler = request_handler

    def make_request(self,
                     endpoint: str,
                     headers: Dict,
                     endpoint_params: str = "",
                     params: str = ""
                     ):
        endpoint: str = self.endpoints.get(endpoint)

        if not endpoint:
            return HTTPStatus.BAD_REQUEST, ""

        if endpoint_params:
            endpoint = endpoint.format(endpoint_params)

        return self.path_decorator(endpoint, params, headers).__call__(self.request_handler)



