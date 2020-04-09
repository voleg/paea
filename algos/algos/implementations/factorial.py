def factorial_naive(n: int) -> int:
    """
    n = 120
    CPython: 18.5 µs ± 337 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    PyPy3: 4.2 µs ± 261 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each) 
    """
    if n == 0:
        return 1

    return n * factorial_naive(n - 1)


def factorial_for_loop(n: int, acc: int = 1) -> int:
    """
    n = 120
    CPython: 10.9 µs ± 319 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    PyPy3: 2.91 µs ± 148 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    """
    if n == 0:
        return 1
    for i in range(n + 1):
        if i == 0:
            continue
        acc = acc * i
    return acc


def factorial_while_loop(n: int, acc: int = 1) -> int:
    """
    n = 120
    CPython: 11.2 µs ± 161 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    PyPy3: 4.02 µs ± 187 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    """
    if n == 0:
        return 1
    while n:
        acc = n*acc
        n -= 1
    return acc


def _tree(l: int, r: int) -> int:
    if l > r:
        return 1
    if l == r:
        return l
    if r - l == 1:
        return l*r
    m = (l + r)//2
    return _tree(l, m) * _tree(m + 1, r)


def factorial_tree(n: int) -> int:
    """
    n = 120
    CPython: 29 µs ± 245 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    PyPy3: 1.99 µs ± 80.4 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    """
    if n < 0:
        raise ValueError('only positive integer allowed')
    if n == 0:
        return 1
    if n <= 2:
        return n
    return _tree(2, n)

