import unittest
from mcurve.polynomial_oop import Polynomial


class MyTestCase(unittest.TestCase):

    def test_constructor(self):
        p = Polynomial(1, 2, 3)
        print(p)


if __name__ == '__main__':
    unittest.main()
