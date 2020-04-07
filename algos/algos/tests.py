import unittest

from algos.implementations import fibonacci_naive
from algos.implementations import factorial_naive
from algos.implementations import ackerman_naive
from algos.implementations.ackermann import ackermann_memo_func
from algos.implementations.ackermann import ackermann_stack_loop


class FibonacciTestCase(unittest.TestCase):
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

class FactorialTestCase(unittest.TestCase):
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

class AckermannTest(unittest.TestCase):
    def test_ackerman_naive_function(self):
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

    def test_ackermann_memo_function(self):
        self.assertEqual(ackermann_memo_func(0,0), ackerman_naive(0, 0))
        self.assertEqual(ackermann_memo_func(0, 1), ackerman_naive(0, 1))
        self.assertEqual(ackermann_memo_func(0, 2), ackerman_naive(0, 2))
        self.assertEqual(ackermann_memo_func(0, 3), ackerman_naive(0, 3))
        self.assertEqual(ackermann_memo_func(1, 2), ackerman_naive(1, 2))
        self.assertEqual(ackermann_memo_func(1, 3), ackerman_naive(1, 3))
        self.assertEqual(ackermann_memo_func(1, 4), ackerman_naive(1, 4))
        self.assertEqual(ackermann_memo_func(2, 4), ackerman_naive(2, 4))
        self.assertEqual(ackermann_memo_func(2, 5), ackerman_naive(2, 5))
        self.assertEqual(ackermann_memo_func(3, 1), ackerman_naive(3, 1))
        self.assertEqual(ackermann_memo_func(3, 2), ackerman_naive(3, 2))
        self.assertEqual(ackermann_memo_func(3, 3), ackerman_naive(3, 3))
        self.assertEqual(ackermann_memo_func(3, 4), ackerman_naive(3, 4))
        self.assertEqual(ackermann_memo_func(3, 5), ackerman_naive(3, 5))
        self.assertEqual(65533, ackermann_memo_func(4, 1))

    def test_ackermann_stack_loop_function(self):
        self.assertEqual(ackermann_stack_loop(0, 0), ackerman_naive(0, 0))
        self.assertEqual(ackermann_stack_loop(0, 1), ackerman_naive(0, 1))
        self.assertEqual(ackermann_stack_loop(0, 2), ackerman_naive(0, 2))
        self.assertEqual(ackermann_stack_loop(0, 3), ackerman_naive(0, 3))
        self.assertEqual(ackermann_stack_loop(1, 2), ackerman_naive(1, 2))
        self.assertEqual(ackermann_stack_loop(1, 3), ackerman_naive(1, 3))
        self.assertEqual(ackermann_stack_loop(1, 4), ackerman_naive(1, 4))
        self.assertEqual(ackermann_stack_loop(2, 4), ackerman_naive(2, 4))
        self.assertEqual(ackermann_stack_loop(2, 5), ackerman_naive(2, 5))
        self.assertEqual(ackermann_stack_loop(3, 1), ackerman_naive(3, 1))
        self.assertEqual(ackermann_stack_loop(3, 2), ackerman_naive(3, 2))
        self.assertEqual(ackermann_stack_loop(3, 3), ackerman_naive(3, 3))
        self.assertEqual(ackermann_stack_loop(3, 4), ackerman_naive(3, 4))
        self.assertEqual(ackermann_stack_loop(3, 5), ackerman_naive(3, 5))
        # self.assertEqual(65533, ackermann_stack_loop(4, 1))


