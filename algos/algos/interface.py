import sys
import inspect

from algos import implementations

sys.setrecursionlimit(10 ** 5)


class AlgoTools(object):

    def __init__(self):
        self.algorithms ={
            'factorial': implementations.factorial_for_loop,
            'fibonacci': implementations.fibonacci_while_loop,
            'ackermann': implementations.ackermann_while_loop,
        }

    def _get_impl(self):
        """ TODO: ability to run other implementations """
        obj = {}
        for name, obj in inspect.getmembers(implementations):
            if not name.startswith('__') and inspect.isfunction(obj):
                obj.update({name: obj})
        return obj

    def get_function_by_name(self, name):
        return self.algorithms.get(name, None)
