from .base import BaseTestCase


class MessagesTest(BaseTestCase):

    def test_health(self):
        response = self.client.get("/health")
        assert response.status_code == 200
