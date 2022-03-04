from fastapi import FastAPI
from chat_api.api.v1.api import api_router
from chat_api.db.mongodb import initialize_db, close_db
from chat_api.core.config import settings
import logging

# get root logger
logging.basicConfig(level=settings.LOG_LEVEL, format=settings.LOG_FORMAT)

app = FastAPI()
app.include_router(api_router)
app.add_event_handler("startup", initialize_db)
app.add_event_handler("shutdown", close_db)
