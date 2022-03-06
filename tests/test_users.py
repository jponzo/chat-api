import json
from .base import BaseTestCase


class TestUsers(BaseTestCase):

    def test_create_user(self):
        payload = {
            "name": "John Doe",
            "email": "john.doe@email.com",
            "password": "1234"
        }
        response = self.client.post("/users",
                                    data=json.dumps(payload),
                                    headers=self.build_headers())
        print(response.text)
        assert response.status_code == 200
