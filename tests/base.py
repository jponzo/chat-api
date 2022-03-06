from fastapi.testclient import TestClient
from chat_api.app import app
import unittest
from chat_api.db.sql import drop_db, initialize_db


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        initialize_db()
        self.client = TestClient(app)

    def tearDown(self):
        drop_db()

    def build_headers(self, token=None):

        headers = {
            "content-type": "application/json"
        }

        if token:
            headers['Authorization'] = f'Bearer {token}'

        return headers
