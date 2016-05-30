from unittest import TestCase

from DS.algos.math.factorial import iterative_factorial, recursive_factorial


class FactorialTestCase(TestCase):

    def test_iterative_factorial(self):
        self.assertEqual(120, iterative_factorial(5))
        self.assertEqual(1, iterative_factorial(0))
        self.assertEqual(24, iterative_factorial(4))
        self.assertEqual(1, iterative_factorial(1))

    def test_recursive_factorial(self):
        self.assertEqual(120, recursive_factorial(5))
        self.assertEqual(1, recursive_factorial(0))
        self.assertEqual(24, recursive_factorial(4))
        self.assertEqual(1, recursive_factorial(1))