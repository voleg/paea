import sys
import logging

sys.setrecursionlimit(10 ** 6)

log = logging.getLogger(__name__)


def ackerman_naive(m, n):
    if m == 0:
        return (n + 1)
    elif n == 0:
        return ackerman_naive(m - 1, 1)
    else:
        return ackerman_naive(m - 1, ackerman_naive(m, n - 1))


def ackermann_memo_func(m, n, cache={}):
    """
    ~ 200 times faster then naive
    crashed at (4, 2) 
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


def ackermann_stack_loop(m, n, stack=[]):
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




