import unittest

from algos.implementations import fibonacci_naive
from algos.implementations.fibonacci import fibonacci_Binet_form
from algos.implementations.fibonacci import fibonacci_memo
from .fib_data import fib

class FibonacciTestCase(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fib[0], fibonacci_naive(0))
        self.assertEqual(fib[1], fibonacci_naive(1))
        self.assertEqual(fib[2], fibonacci_naive(2))
        self.assertEqual(fib[6], fibonacci_naive(6))
        self.assertEqual(fib[9], fibonacci_naive(9))
        self.assertEqual(fib[15], fibonacci_naive(15))
        self.assertEqual(fib[17], fibonacci_naive(17))
        self.assertEqual(fib[19], fibonacci_naive(19))
        self.assertEqual(fib[33], fibonacci_naive(33))

    def test_fibonacci_polinomial(self):
        """
        test first 70 numbers of fib. seq.
        n > 71 does not produses correct values
        """
        for i in range(70):
            self.assertEqual(fib[i], fibonacci_Binet_form(i))

    def test_fibonacci_memo_func(self):
        for i in range(70):
            self.assertEqual(fib[i], fibonacci_memo(i))

