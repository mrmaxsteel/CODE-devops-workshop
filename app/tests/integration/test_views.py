from unittest import TestCase
from ..base import TestClient
from calculator.app import app


class ViewTests(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = TestClient(app)

    def test_multiply(self):
        r = self.client.get("/calc/3*10")
        self.assertEquals(r.status_code, 200)
        self.assertEquals(r.body, "30")
        
    def test_multiply_invalid(self):
        r = self.client.get("/calc/1001*10")
        self.assertEquals(r.status_code, 403)
        self.assertEquals(r.body, "Out of bounds min/max values used. Values should be >= -1000 and <= 1000")

    def test_divide(self):
        r = self.client.get("/calc/30/10")
        self.assertEquals(r.status_code, 200)
        self.assertEquals(r.body, "3")

    def test_divide_invalid(self):
        r = self.client.get("/calc/-1010/10")
        self.assertEquals(r.status_code, 403)
        self.assertEquals(r.body, "Out of bounds min/max values used. Values should be >= -1000 and <= 1000")

    def test_divide_by_zero(self):
        r = self.client.get("/calc/10/0")
        self.assertEquals(r.status_code, 403)
        self.assertEquals(r.body, "Divide by Zero error.")