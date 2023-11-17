from dotenv import load_dotenv
from pydantic import StrictStr, Field, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict
import ast

load_dotenv()


class APISettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='../.env')

    ver: StrictStr = Field("api_ver", alias="API_VER")
    homepage: HttpUrl = Field("api_homepage", alias="API_HOMEPAGE")
    headers: StrictStr = Field("api_headers", alias="API_HEADERS")


api = APISettings()
headers = ast.literal_eval(api.headers)

# API_HOMEPAGE = 'https://archive-api.open-meteo.com'
# API_KEY = ''
# API_VER = 'v1'
# HEADERS = {'accept': 'application/json'}
ADDITIONAL_PARAMS = {
    "1": ("52.52", "13.41", "2023-10-30", "2023-11-13", "temperature_2m_mean,precipitation_hours", "GMT")
}

ENDPOINTS = {
    "weather_d": "{0}/{1}{2}".format(api.homepage, api.ver,
                                     "/archive?latitude={}&longitude={}&start_date={}&end_date={}&daily={}&timezone={}"),
    # "movie_random": "{0}/{1}{2}".format(HOMEPAGE, API_VER, "/movie/random"),
    # "season": "{0}/{1}{2}".format(HOMEPAGE, API_VER, "/season"),
    # "person_id": "{0}/{1}{2}".format(HOMEPAGE, API_VER, "/person/{}"),
}

COMMANDS = {
    "1": ("weather_d", headers),
    # "2": ("movie_random", HEADERS),
    # "3": ("season", HEADERS),
    # "4": ("person_id", HEADERS),
}
