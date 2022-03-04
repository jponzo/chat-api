from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    API_V1_STR: str = "/v1/"
    DB_URL: str = os.environ["MONGODB_URL"]
    LOG_FORMAT = '[module:%(name)s] [%(levelname)s] %(message)s'
    LOG_PATH = '/dev/stdout'
    LOG_LEVEL = 'DEBUG'

    class Config:
        case_sensitive = True


settings = Settings()
