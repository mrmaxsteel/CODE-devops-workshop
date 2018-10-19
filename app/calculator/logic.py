# encoding=utf-8


class ValueTooLowException(Exception):
    pass


class ValueTooHighException(Exception):
    pass


class Calculator(object):
    def __init__(self, min_value=-1000, max_value=1000):
        if (min_value < -1000 or max_value > 1000):
            raise Exception('Out of bounds min/max values used')
        self.min_value = min_value
        self.max_value = max_value

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        return a/b
