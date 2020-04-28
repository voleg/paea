from math import sqrt, pow

from .tail import TRE_stack_recall


def fibonacci_naive(n: int) -> int:
    """
    Naive recursive implementation
    n = 10
    CPython3: 20.5 µs ± 499 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    PyPy3: 920 ns ± 24.3 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    """
    if n <= 1:
        return n

    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


@TRE_stack_recall
def fibonacci_tre(n: int, curr: int = 0, next: int = 1) -> int:
    """
    Fibonacci numbers with Tail recursion elimination
    n = 10
    CPython3: 23.3 µs ± 479 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    PyPy3: 2.23 µs ± 64 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    """
    if n == 0:
        return curr
    else:
        return fibonacci_tre(n - 1, next, curr + next)


def fibonacci_Binet_form(n: int) -> int:
    """
    Binet formula
    ( at n=71 produses incorrect values)

    n = 10
    CPython3: 854 ns ± 30.8 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    PyPy3: 61.1 ns ± 1.94 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
    """
    return int(
        1 / sqrt(5) * (pow((1 + sqrt(5)) / 2, n) - pow((1 - sqrt(5)) / 2, n))
    )


def fibonacci_memo(n: int, cache: dict = {}) -> int:
    """
    Simple memoisation implementation

    n = 10
    CPython3: 410 ns ± 5.7 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    PyPy3: 17.2 ns ± 0.202 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)
    """

    if n <= 1:
        return n

    if not cache.get(n - 1):
        cache[n - 1] = fibonacci_memo(n - 1, cache=cache)

    if not cache.get(n - 2):
        cache[n - 2] = fibonacci_memo(n - 2, cache=cache)

    return cache[n - 1] + cache[n - 2]


def fibonacci_for(n):
    """
    fibonacci numbers: for loop implementation
    n = 10
    CPython3: 702 ns ± 13.1 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    PyPy3: 62.1 ns ± 0.963 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
    """
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a


def fibonacci_while_loop(n: int, stack: list = []) -> int:
    """
    fibonacci numbers: while loop implementation
    n = 10
    CPython3: 716 ns ± 4.51 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    PyPy3: 58 ns ± 2.1 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
    """
    if n < 0:
        raise ValueError('Only positive values allowed')

    if n <= 1:
        return n

    a = 0
    b = 1

    while n:
        a, b = b, a + b
        n -= 1

    return a



# from https://www.nayuki.io/page/fast-fibonacci-algorithms 
def fib_fast(n):
    """
    fibonacci numbers: implementation production tree implementation
    n = 10
    CPython3: 1.42 µs ± 22.4 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    PyPy3: 1.39 ns ± 0.0124 ns per loop (mean ± std. dev. of 7 runs, 1000000000 loops each)

    details:
    PyPy:
    In [12]: %timeit fib_fast(10)
    1.39 ns ± 0.0124 ns per loop (mean ± std. dev. of 7 runs, 1000000000 loops each)
    In [13]: %timeit fib_fast(10)
    1.44 ns ± 0.0337 ns per loop (mean ± std. dev. of 7 runs, 1000000000 loops each)
    In [14]: %timeit fib_fast(1000)
    840 ns ± 26.5 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    In [15]: %timeit fib_fast(10000)
    14.3 µs ± 327 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    In [16]: %timeit fib_fast(100000)
    624 µs ± 19.8 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    In [17]: %timeit fib_fast(1000000)
    28.4 ms ± 1.88 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
    In [18]: %timeit fib_fast(10000000)
    1.08 s ± 24.4 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

    CPython:
    In [6]: %timeit fib_fast(10)
    1.42 µs ± 22.4 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    In [7]: %timeit fib_fast(1000)
    4.74 µs ± 56.6 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    In [8]: %timeit fib_fast(10000)
    43.6 µs ± 1.96 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    In [9]: %timeit fib_fast(100000)
    1.67 ms ± 44 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    In [10]: %timeit fib_fast(1000000)
    64.3 ms ± 1e+03 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
    In [11]: %timeit fib_fast(10000000)
    2.53 s ± 24.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

    """
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]

# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)
