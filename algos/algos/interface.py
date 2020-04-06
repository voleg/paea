from algos.implementations import factorial_naive
from algos.implementations import fibonacci_naive
from algos.implementations import ackerman_naive
from algos.implementations.ackerman import ackermann_memo_func


class AlgoTools(object):

    def __init__(self):
        self.algorithms ={
            'factorial': factorial_naive,
            'fibonacci': fibonacci_naive,
            'ackermann': ackerman_memo_func,
        }

    def get_function_by_name(self, name):
        return self.algorithms.get(name, None)
