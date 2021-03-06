import sys

sys.setrecursionlimit(10**5)

from .ackermann import (
    ackerman_naive,
    ackermann_memo_func,
    ackermann_while_loop
)
from .factorial import (
    factorial_naive,
    factorial_for_loop,
    factorial_while_loop,
    factorial_tree
)
from .fibonacci import (
    fibonacci_naive,
    fibonacci_Binet_form,
    fibonacci_memo,
    fibonacci_while_loop
)

ackermann = ackermann_while_loop
factorial = factorial_for_loop
fibonacci = fibonacci_while_loop
