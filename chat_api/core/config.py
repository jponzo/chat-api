from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    LOG_FORMAT = '[module:%(name)s] [%(levelname)s] %(message)s'
    LOG_PATH = '/dev/stdout'
    LOG_LEVEL = os.environ['LOG_LEVEL']
    JWT_SECRET = os.environ['JWT_SECRET']
    JWT_ALGORITHM = 'HS256'
    DB_URL = os.environ['DB_URL']

    class Config:
        case_sensitive = True


settings = Settings()
