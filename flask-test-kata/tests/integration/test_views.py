from unittest import TestCase
from ..base import TestClient
from calculator.app import app


class ViewTests(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = TestClient(app)

    def test_multiply(self):
        # r = self.client.get("/calc/3*10")
        # self.assertEquals(r.status_code, 200)
        # self.assertEquals(r.body, "30")
        pass
