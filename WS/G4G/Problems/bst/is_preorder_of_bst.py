"""
http://www.geeksforgeeks.org/check-if-a-given-array-can-represent-preorder-traversal-of-binary-search-tree/
"""
from sys import maxint

from G4G.Problems.stacks.stack import Stack


def is_preorder(array):
    s = Stack()
    root = -maxint

    for value in array:

        if value < root:
            return False

        while not s.is_empty() and s.peek() < value:
            root = s.pop()

        s.push(value)

    return True

# print is_preorder([4, 2, 1, 3, 6, 5, 7])