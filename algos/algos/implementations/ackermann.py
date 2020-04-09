
def ackerman_naive(m: int, n: int) -> int:
    """
    Ackermann function naive implementation
    A(2, 2)
    CPython:
    PyPy3:
    """
    if m == 0:
        return n + 1
    elif n == 0:
        return ackerman_naive(m - 1, 1)
    else:
        return ackerman_naive(m - 1, ackerman_naive(m, n - 1))


def ackermann_memo_func(m: int, n: int, cache: dict = {}) -> int:
    """
    Ackermann function naive implementation with memoisation
    ~ 200 times faster then naive
    crashed at (4, 2)

    A(2, 2)
    CPython:
    PyPy3:
    """
    if (m, n) in cache:
        return cache[(m, n)]

    if m == 0:
        return (n + 1)

    elif n == 0:
        if (m - 1, 1) in cache:
            return cache[(m - 1, 1)]
        else:
            cache[(m - 1, 1)] = ackermann_memo_func(m - 1, 1)
            return cache[(m - 1, 1)]

    else:
        if (m, n - 1) in cache:
            _n = cache[(m, n - 1)]
        else:
            cache[(m, n - 1)] = ackermann_memo_func(m, n - 1)
            _n = cache[(m, n - 1)]

        return ackermann_memo_func(m - 1, _n)


def ackermann_while_loop(m, n, stack=[]):
    """
    Ackermann function while loop implementation
    quite slow but no recursion limits; will calculate A(4,2) for ages

    A(2, 2)
    CPython:
    PyPy3:
    """
    while m >= 0:
        if m == 0:
            n = n + 1
            if stack:
                m = stack.pop()
            else:
                return n

        elif n == 0:
            n = 1
            m = m - 1

        else:
            n = n - 1
            stack.append(m - 1)
