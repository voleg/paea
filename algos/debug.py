import sys

from algos.implementations.fibonacci import *
N = int(sys.argv[1])

print(fibonacci_tre(N))

print(fibonacci_naive(N))

