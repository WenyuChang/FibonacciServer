__author__ = 'Wenyu'


import random
import unittest
from fibonacci.handlers.basehttphandler import _query_fib

class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        ii = 5
        out = _query_fib(ii)
        # should raise an exception for an immutable sequence
        self.assertEqual(out, [0, 1, 1, 2, 3], 'Failed testing on %s' % 5)

if __name__ == '__main__':
    unittest.main()