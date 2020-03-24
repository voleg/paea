import logging

log = logging.getLogger(__name__)


def fibonacci_naive(n: int) -> int:
    if n <= 1:
        return n

    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)
