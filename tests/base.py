from fastapi.testclient import TestClient
from chat_api.app import app
import unittest
from chat_api.db.sql import drop_db, initialize_db
import json


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        """
        Initialize db and test client before testing
        """
        initialize_db()
        self.client = TestClient(app)

    def tearDown(self):
        """
        Drop Database after testing
        """
        drop_db()

    def build_headers(self, token=None):

        headers = {
            "content-type": "application/json"
        }

        if token:
            headers['Authorization'] = f'Bearer {token}'

        return headers

    def create_user(self, name="john"):
        create_payload = {
            "name": name,
            "email": f"{name}@email.com",
            "password": "1234"
        }
        self.client.post("/users",
                         data=json.dumps(create_payload),
                         headers=self.build_headers())

    def login_user(self, name="john"):
        create_payload = {
            "email": f"{name}@email.com",
            "password": "1234"
        }
        response = self.client.post("/users/login",
                                    data=json.dumps(create_payload),
                                    headers=self.build_headers())
        return json.loads(response.text)['access_token']

    def create_message(self):

        create_payload = {
            "sender": 1,
            "recipient": 2,
            "content": {
                "type": "text",
                "text": "asd"
            }
        }
        self.client.post("/messages",
                         data=json.dumps(create_payload),
                         headers=self.build_headers(self.login_user()))

    def test_health(self):
        response = self.client.get("/health")
        assert response.status_code == 200
