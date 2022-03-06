import json
from .base import BaseTestCase


class TestMessages(BaseTestCase):

    def test_create_text_message_success(self):

        self.create_user()

        create_payload = {
            "sender": 1,
            "recipient": 2,
            "content": {
                "type": "text",
                "text": "asd"
            }
        }
        response = self.client.post("/messages",
                                    data=json.dumps(create_payload),
                                    headers=self.build_headers(self.login_user()))
        assert response.status_code == 200

    def test_create_text_message_success(self):

        self.create_user()

        create_payload = {
            "sender": 1,
            "recipient": 2,
            "content": {
                "type": "text",
                "asdasd": "asd"
            }
        }
        response = self.client.post("/messages",
                                    data=json.dumps(create_payload),
                                    headers=self.build_headers(self.login_user()))
        assert response.status_code == 422

    def test_create_video_message_success(self):

        self.create_user()

        create_payload = {
            "sender": 1,
            "recipient": 2,
            "content": {
                "type": "video",
                "source": "youtube",
                "url": "test"
            }
        }
        response = self.client.post("/messages",
                                    data=json.dumps(create_payload),
                                    headers=self.build_headers(self.login_user()))
        assert response.status_code == 200

    def test_create_video_message_error(self):

        self.create_user()

        create_payload = {
            "sender": 1,
            "recipient": 2,
            "content": {
                "type": "video",
                "url": "test"
            }
        }
        response = self.client.post("/messages",
                                    data=json.dumps(create_payload),
                                    headers=self.build_headers(self.login_user()))
        assert response.status_code == 422

    def test_create_image_message_success(self):

        self.create_user()

        create_payload = {
            "sender": 1,
            "recipient": 2,
            "content": {
                "type": "image",
                "height": 123,
                "width": 123,
                "url": "test"
            }
        }
        response = self.client.post("/messages",
                                    data=json.dumps(create_payload),
                                    headers=self.build_headers(self.login_user()))
        assert response.status_code == 200

    def test_create_image_message_error(self):

        self.create_user()

        create_payload = {
            "sender": 1,
            "recipient": 2,
            "content": {
                "type": "image",
                "width": 123,
                "url": "test"
            }
        }
        response = self.client.post("/messages",
                                    data=json.dumps(create_payload),
                                    headers=self.build_headers(self.login_user()))
        assert response.status_code == 422

    def test_get_message_by_recipient_ok(self):

        self.create_user()
        self.create_user("peter")
        self.create_message()

        response = self.client.get("/messages?recipient_id=2&message_start_id=1", headers=self.build_headers())
        assert response.status_code == 200
        assert response.text == '[{"id":1,"sender":1,"recipient":2,"content":{"type":"text","text":"asd"}}]'

        self.create_message()
        response = self.client.get("/messages?recipient_id=2&message_start_id=2", headers=self.build_headers())
        assert response.status_code == 200
        assert response.text == '[{"id":2,"sender":1,"recipient":2,"content":{"type":"text","text":"asd"}}]'



    def test_get_message_by_recipient_error(self):

        self.create_user()
        self.create_user("peter")
        self.create_message()

        response = self.client.get("/messages?recipient_id=3", headers=self.build_headers())
        assert response.status_code == 422
