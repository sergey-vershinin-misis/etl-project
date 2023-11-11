from pprint import pprint
from api.decorator import URLDecorator
from api.utils import MakeGetRequest, RequestFactory
from api.settings import ENDPOINTS, COMMANDS


class UserFactory(RequestFactory):
    endpoints = ENDPOINTS


def main():
    user_handler = UserFactory(URLDecorator, MakeGetRequest)
    additional_params = "609246"

    command = "4"
    params = COMMANDS.get(command)
    response = user_handler.make_request(*params, additional_params)

    pprint(response)


if __name__ == "__main__":
    main()
