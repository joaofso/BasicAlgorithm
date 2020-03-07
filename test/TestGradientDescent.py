import unittest
from sympy import *
from GradientDescent import gradient_descent

ALLOWED_ERROR = 1 * 10**-10


class MyTestCase(unittest.TestCase):

    def test_one_variable(self):
        x = symbols('x')
        function = x**4 - 3*x**3 + 2
        result = gradient_descent(function, x)
        self.assertTrue(result[x] - 2.25 < ALLOWED_ERROR)


if __name__ == '__main__':
    unittest.main()
