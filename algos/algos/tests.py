import unittest

from algos.implementations import fibonacci_naive
from algos.implementations import factorial_naive
from algos.implementations import ackerman_naive


class AlgorithmsCorrectnessTestCase(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(0, fibonacci_naive(0))
        self.assertEqual(1, fibonacci_naive(1))
        self.assertEqual(1, fibonacci_naive(2))
        self.assertEqual(2, fibonacci_naive(3))
        self.assertEqual(8, fibonacci_naive(6))
        self.assertEqual(34, fibonacci_naive(9))
        self.assertEqual(610, fibonacci_naive(15))
        self.assertEqual(1597, fibonacci_naive(17))
        self.assertEqual(4181, fibonacci_naive(19))
        self.assertEqual(3524578, fibonacci_naive(33))

    def test_factorial(self):
        self.assertEqual(0, factorial_naive(0))
        self.assertEqual(1, factorial_naive(1))
        self.assertEqual(24, factorial_naive(4))
        self.assertEqual(362880, factorial_naive(9))
        self.assertEqual(3628800, factorial_naive(10))
        self.assertEqual(6227020800, factorial_naive(13))
        self.assertEqual(355687428096000, factorial_naive(17))
        self.assertEqual(6402373705728000, factorial_naive(18))
        self.assertEqual(121645100408832000, factorial_naive(19))
        self.assertEqual(2432902008176640000, factorial_naive(20))

    def test_ackerman_function(self):
        self.assertEqual(1, ackerman_naive(0, 0))
        self.assertEqual(2, ackerman_naive(0, 1))
        self.assertEqual(3, ackerman_naive(0, 2))
        self.assertEqual(4, ackerman_naive(0, 3))
        self.assertEqual(4, ackerman_naive(1, 2))
        self.assertEqual(5, ackerman_naive(1, 3))
        self.assertEqual(6, ackerman_naive(1, 4))
        self.assertEqual(11, ackerman_naive(2, 4))
        self.assertEqual(13, ackerman_naive(2, 5))
        self.assertEqual(13, ackerman_naive(3, 1))
        self.assertEqual(29, ackerman_naive(3, 2))
        self.assertEqual(61, ackerman_naive(3, 3))
        self.assertEqual(125, ackerman_naive(3, 4))
        self.assertEqual(253, ackerman_naive(3, 5))
        # self.assertEqual(65533, ackerman_naive(4, 1))
