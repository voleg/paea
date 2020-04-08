from algos.implementations.factorial import factorial_tree
from algos.implementations.fibonacci import fibonacci_memo
from algos.implementations import ackerman_naive
from algos.implementations import ackermann_memo_func


class AlgoTools(object):

    def __init__(self):
        self.algorithms ={
            'factorial': factorial_tree,
            'fibonacci': fibonacci_memo,
            'ackermann': ackermann_memo_func,
        }

    def get_function_by_name(self, name):
        return self.algorithms.get(name, None)
