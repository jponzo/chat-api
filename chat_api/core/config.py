from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    LOG_FORMAT = '[module:%(name)s] [%(levelname)s] %(message)s'
    LOG_PATH = '/dev/stdout'
    LOG_LEVEL = 'DEBUG'
    JWT_SECRET = 'secret'
    JWT_ALGORITHM = 'HS256'


    class Config:
        case_sensitive = True


settings = Settings()
