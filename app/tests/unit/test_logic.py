from unittest import TestCase
from calculator.logic import Calculator


class CalculatorTests(TestCase):
    def test_mul_with_two_positive_numbers(self):
        c = Calculator()
        self.assertEqual(c.mul(22, 10), 220)

    def test_mul_with_two_negative_numbers(self):
        c = Calculator()
        self.assertEqual(c.mul(-1, -8), 8)

    def test_div(self):
        c = Calculator()
        pass
