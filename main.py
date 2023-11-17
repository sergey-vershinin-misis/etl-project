from dataclasses import dataclass
from db.common.models import db, AdvWorksSales, AdvWorksProducts
from typing import List

from api.utils.decorator import URLDecorator
from api.utils.utils import MakeGetRequest, RequestFactory
from api.common.settings import ENDPOINTS, COMMANDS, ADDITIONAL_PARAMS


class UserFactory(RequestFactory):
    endpoints = ENDPOINTS


@dataclass
class WeatherReport:
    precipitation_hours: List
    temperature_2m_mean: List
    time: List


def main():
    user_handler = UserFactory(URLDecorator, MakeGetRequest)

    command = "1"
    params = COMMANDS.get(command)
    additional_params = ADDITIONAL_PARAMS.get(command)
    response = user_handler.make_request(*params, additional_params)

    weather_rep = WeatherReport(**response[1]['daily'])

    print(weather_rep.time, weather_rep.temperature_2m_mean, weather_rep.precipitation_hours, sep="\n")

    db.connect()
    db.create_tables([AdvWorksProducts, AdvWorksSales])


if __name__ == "__main__":
    main()
