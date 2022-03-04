FROM python:3
EXPOSE 8000

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python setup.py develop
CMD [ "uvicorn", "chat_api.app:app", "--reload", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug"]
