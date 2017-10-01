from copy import copy
from unittest import TestCase

from G4G.Problems.stacks.stack import Stack

from G4G.Problems.stack.recursive_stack_sort import sort_stack


class StackTestCase(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_sorting(self):
        self.stack.push(5)
        self.stack.push(4)
        self.stack.push(88)
        self.stack.push(22)
        self.stack.push(1)
        self.stack.push(0)
        self.stack.push(3)
        self.stack.push(9)

        expected_output = copy(self.stack.get_list())
        expected_output.sort()

        observed_output = sort_stack(self.stack).get_list()

        self.assertSequenceEqual(expected_output, observed_output)
