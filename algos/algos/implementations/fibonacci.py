from math import sqrt, pow



def fibonacci_naive(n: int) -> int:
    if n <= 1:
        return n

    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def fibonacci_Binet_form(n: int) -> int:
    """
    Binet formula
    ( at n=71 produses incorrect values)
    """
    return int(
        1 / sqrt(5) * (pow((1 + sqrt(5)) / 2, n) - pow((1 - sqrt(5)) / 2, n))
    )


def fibonacci_memo(n: int, cache: dict = {}) -> int:
    if n <= 1:
        return n

    if not cache.get(n - 1):
        cache[n - 1] = fibonacci_memo(n - 1, cache=cache)

    if not cache.get(n - 2):
        cache[n - 2] = fibonacci_memo(n - 2, cache=cache)

    return cache[n - 1] + cache[n - 2]


