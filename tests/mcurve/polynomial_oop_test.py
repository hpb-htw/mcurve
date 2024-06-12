import unittest
from mcurve.polynomial_oop import Polynomial


class MyTestCase(unittest.TestCase):

    def test_constructor(self):
        p = Polynomial(1, 2, 3)
        print(p)
        q = Polynomial(3, 2, 1)
        print(q)


    def test_evaluation(self):
        p = Polynomial(1, 2, 3)
        v = p.evaluate(0)
        c = v[1]
        print(type(c))

if __name__ == '__main__':
    unittest.main()
