import logging

log = logging.getLogger(__name__)


def factorial_naive(n: int) -> int:
    """
    CPython: 18.5 µs ± 250 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    """
    if n <= 2:
        return n
    
    return n * factorial_naive(n - 1)


def factorial_for_loop(n: int, acc: int = 1) -> int:
    """
    CPython 10.6 µs ± 104 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    PyPy3:  3.33 µs ± 257 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    """
    if n <= 2:
        return n
    for i in range(n + 1):
        if i == 0:
            continue
        acc = acc * i
    return acc

def factorial(n):
    pass
