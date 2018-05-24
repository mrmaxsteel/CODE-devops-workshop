from unittest import TestCase
from calculator.logic import Calculator


class CalculatorTests(TestCase):
    def test_mul(self):
        c = Calculator()
        result = c.mul(22, 10)
        self.assertEqual(result, 220)

    def test_div(self):
        pass
