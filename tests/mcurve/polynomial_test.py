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

    def test_to_string_constant(self):
        c = [3]
        s = polynomial.to_string(c)
        self.assertEqual(s, "3")

    def test_to_string_lineal(self):
        c = [0, -3]
        s = polynomial.to_string(c)
        e = "-3x"
        self.assertEqual(s, e)

    def test_to_string_lineal_x(self):
        c = [0, 1]
        s = polynomial.to_string(c)
        e = "x"
        self.assertEqual(s, e)

    def test_to_string_lineal_minus1x(self):
        c = [0, -1]
        s = polynomial.to_string(c)
        e = "-x"
        self.assertEqual(s, e)

    def test_to_string_lineal_ax_b(self):
        c = [1, -3]
        s = polynomial.to_string(c)
        e = "-3x + 1"
        self.assertEqual(s, e)

    def test_to_string_lineal_minus1x_b(self):
        c = [-3, -1]
        s = polynomial.to_string(c)
        e = "-x - 3"
        self.assertEqual(s, e)

    def test_to_string(self):
        coefficients = [4, 0, 2, 0, 0, -3, 6]
        text = polynomial.to_string(coefficients)
        s = "6x^6 - 3x^5 + 2x^2 + 4"
        self.assertEqual(text, s)

    def test_to_string_zero_term(self):
        coefficients = [0, 1, 2, 0, 0, -3, 6]
        text = polynomial.to_string(coefficients)
        s = "6x^6 - 3x^5 + 2x^2 + x"
        self.assertEqual(text, s)
