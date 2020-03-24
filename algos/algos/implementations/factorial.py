import logging

log = logging.getLogger(__name__)


def factorial_naive(n: int) -> int:
    if n <= 2:
        return n

    return n * factorial_naive(n - 1)
