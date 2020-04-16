import unittest

from algos.implementations.factorial import factorial_naive
from algos.implementations.factorial import factorial_for_loop
from algos.implementations.factorial import factorial_while_loop
from algos.implementations.factorial import factorial_tree


class FactorialTestCase(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(1, factorial_naive(0))
        self.assertEqual(1, factorial_naive(1))
        self.assertEqual(24, factorial_naive(4))
        self.assertEqual(362880, factorial_naive(9))
        self.assertEqual(3628800, factorial_naive(10))
        self.assertEqual(6227020800, factorial_naive(13))
        self.assertEqual(355687428096000, factorial_naive(17))
        self.assertEqual(6402373705728000, factorial_naive(18))
        self.assertEqual(121645100408832000, factorial_naive(19))
        self.assertEqual(2432902008176640000, factorial_naive(20))

    def test_factorial_for_loop(self):
        self.assertEqual(1, factorial_for_loop(0))
        self.assertEqual(1, factorial_for_loop(1))
        self.assertEqual(24, factorial_for_loop(4))
        self.assertEqual(362880, factorial_for_loop(9))
        self.assertEqual(3628800, factorial_for_loop(10))
        self.assertEqual(6227020800, factorial_for_loop(13))
        self.assertEqual(355687428096000, factorial_for_loop(17))
        self.assertEqual(6402373705728000, factorial_for_loop(18))
        self.assertEqual(121645100408832000, factorial_for_loop(19))
        self.assertEqual(2432902008176640000, factorial_for_loop(20))

    def test_factorial_while_loop(self):
        self.assertEqual(1, factorial_while_loop(0))
        self.assertEqual(1, factorial_while_loop(1))
        self.assertEqual(24, factorial_while_loop(4))
        self.assertEqual(362880, factorial_while_loop(9))
        self.assertEqual(3628800, factorial_while_loop(10))
        self.assertEqual(6227020800, factorial_while_loop(13))
        self.assertEqual(355687428096000, factorial_while_loop(17))
        self.assertEqual(6402373705728000, factorial_while_loop(18))
        self.assertEqual(121645100408832000, factorial_while_loop(19))
        self.assertEqual(2432902008176640000, factorial_while_loop(20))

    def test_factorial_prod_tree(self):
        self.assertEqual(1, factorial_tree(0))
        self.assertEqual(1, factorial_tree(1))
        self.assertEqual(24, factorial_tree(4))
        self.assertEqual(362880, factorial_tree(9))
        self.assertEqual(3628800, factorial_tree(10))
        self.assertEqual(6227020800, factorial_tree(13))
        self.assertEqual(355687428096000, factorial_tree(17))
        self.assertEqual(6402373705728000, factorial_tree(18))
        self.assertEqual(121645100408832000, factorial_tree(19))
        self.assertEqual(2432902008176640000, factorial_tree(20))
