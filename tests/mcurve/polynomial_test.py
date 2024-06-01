import unittest
from mcurve import polynomial


class MyTestCase(unittest.TestCase):
    def test_evaluate_polynomial(self):
        coefficients = [4, 0, 2, 0, 0, -3, 6]
        x0 = 2
        value = polynomial.evaluate(coefficients, x0)
        expected = 300.0
        EPSILON = 0.001
        self.assertTrue(abs(value[0]-expected) < EPSILON)

    def test_to_string(self):
        coefficients = [4, 0, 2, 0, 0, -3, 6]
        text = polynomial.to_string(coefficients)
        print(text)

    def test_to_string_zero_term(self):
        coefficients = [0, 1, 2, 0, 0, -3, 6]
        text = polynomial.to_string(coefficients)
        print(text)
