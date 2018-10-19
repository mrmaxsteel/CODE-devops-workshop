from unittest import TestCase
from calculator.logic import Calculator


class CalculatorTests(TestCase):
    def test_mul(self):
        c = Calculator()
        assert c.mul(5,10) == 50

    def test_div(self):
        pass
