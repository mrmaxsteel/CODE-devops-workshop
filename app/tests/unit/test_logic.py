from unittest import TestCase
from calculator.logic import Calculator


class CalculatorTests(TestCase):
    def test_mul(self):
        c = Calculator()

        result = c.mul(22, 10)
        assert(result, 2)

    def test_div(self):
        pass
