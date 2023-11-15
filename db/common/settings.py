from dotenv import load_dotenv
from pydantic import StrictStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
import ast


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    path: StrictStr = Field("db_path", alias="DB_PATH")