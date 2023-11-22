from dataclasses import dataclass
from datetime import datetime

from db.common.models import (db, AdvWorksSales, AdvWorksProducts, AdvWorksTerritories)
from typing import List, TypeVar

from api.common.utils.decorator import URLDecorator
from api.common.utils.utils import MakeGetRequest, RequestFactory
from api.common.settings import ENDPOINTS, COMMANDS, ADDITIONAL_PARAMS

from db.common.settings import DBSettings
from db.common.utils.db_connectors import ConnectionFactory, ConnectorType
from db.common.utils.db_handlers import SQLiteHandler
from db.queries.queries import select_aggr_sales_data


T = TypeVar("T", bound=datetime)
S = TypeVar("S", bound=str)

db_settings = DBSettings()


class UserFactory(RequestFactory):
    endpoints = ENDPOINTS


@dataclass
class WeatherReport:
    precipitation_hours: List
    temperature_2m_mean: List
    time: List


@dataclass
class GeoCoordinates:
    latitude: float
    longitude: float

@dataclass
class SalesAggrDataRow:
    order_date: T
    country: S
    region: S
    days_receipt: float
    latitude: float
    longitude: float


@dataclass
class DateMinMax:
    date_min: T
    date_max: T





def main():
    # user_handler = UserFactory(URLDecorator, MakeGetRequest)
    #
    # command = "1"
    # params = COMMANDS.get(command)
    # additional_params = ADDITIONAL_PARAMS.get(command)
    # response = user_handler.make_request(*params, additional_params)
    #
    # weather_rep = WeatherReport(**response[1]['daily'])
    #
    # print(weather_rep.time, weather_rep.temperature_2m_mean, weather_rep.precipitation_hours, sep="\n")

    db.connect()
    # db.create_tables([AdvWorksProducts, AdvWorksSales, AdvWorksTerritories])

    connector = ConnectionFactory.connect_db(ConnectorType.SQLite)
    sql = SQLiteHandler(connector)
    # query = select_all('advworksproducts')
    # query = select_aggr_sales_data_for_period(select_aggr_sales_data(), '1/1/2017', '1/3/2017')
    query = select_aggr_sales_data()
    # raw_result = sql.db_handle('c:\\src\\local-py\\misis\\etl-project\\db\\aworks_db', query)
    raw_result = sql.db_handle(db_settings.path, query)

    typed_result = [SalesAggrDataRow(*result) for result in raw_result]

    for result in typed_result:
        print(result)


if __name__ == "__main__":
    main()
