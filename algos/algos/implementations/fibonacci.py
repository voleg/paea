from math import sqrt, pow



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

