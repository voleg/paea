import sys
import time

from algos.implementations import ackerman_naive as ackerman
from algos.implementations import factorial_naive as factorial
from algos.implementations import fibonacci_naive as fibonacci

sys.setrecursionlimit(2**30)


def with_exec_time(f):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = f(*args, **kwargs)
        t2 = time.time()
        sys.stdout.write(f'{str(t2 - t1)}\t')
        return result
    return wrapper


def main():
    print('FACTORIAL')
    factorial = with_exec_time(factorial)
    for n in range(20):
        result = factorial(n)
        print(f'factorial({n}) is: {result}')


    print('FIBONACCI NUMBERS')
    fibonacci = with_exec_time(fibonacci)
    for n in range(20):
        result = fibonacci(n)
        print(f'fibonacci({n}) is: {result}')


    print('ACKERMAN FUNCTION')
    ackerman = with_exec_time(ackerman)
    for x in range(6):
        for y in range(6):
            result = ackerman(x, y) 
            print(f"ackerman ({x}, {y}) is: {result}")


if __name__ == "__main__":
    main()
