import json
from .base import BaseTestCase


class TestUsers(BaseTestCase):

    def test_create_and_login_user_success(self):

        # Create User
        create_payload = {
            "name": "John Doe",
            "email": "john.doe@email.com",
            "password": "1234"
        }
        response = self.client.post("/users",
                                    data=json.dumps(create_payload),
                                    headers=self.build_headers())
        assert response.status_code == 200

        # Get User
        response = self.client.get("/users/1", headers=self.build_headers())
        assert response.status_code == 200
        assert response.text == '{"id":1,"name":"John Doe","email":"john.doe@email.com"}'

        # Login User
        login_payload = {
            "email": "john.doe@email.com",
            "password": "1234"
        }
        response = self.client.post("/users/login",
                                    data=json.dumps(login_payload),
                                    headers=self.build_headers())
        assert response.status_code == 200
        assert 'access_token' in json.loads(response.text).keys()

    def test_create_user_bad_request(self):
        payload = {
            "name": "John Doe",
            "password": "1234"
        }
        response = self.client.post("/users",
                                    data=json.dumps(payload),
                                    headers=self.build_headers())
        assert response.status_code == 422

    def test_login_unauthorized(self):
        self.create_user()
        create_payload = {
            "email": "john.doe@email.com",
            "password": "134"
        }
        response = self.client.post("/users/login",
                                    data=json.dumps(create_payload),
                                    headers=self.build_headers())
        assert response.status_code == 401
