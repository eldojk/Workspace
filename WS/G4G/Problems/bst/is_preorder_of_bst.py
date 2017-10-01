"""
amzn, msft

http://www.geeksforgeeks.org/check-if-a-given-array-can-represent-preorder-traversal-of-binary-search-tree/

This problem is similar to Next (or closest) Greater Element problem.
Here we find next greater element and after finding next greater,
if we find a smaller element, then return false.
"""
from sys import maxint

from G4G.Problems.stack.stack import Stack


def is_pre_order(array):
    s = Stack()
    root = -maxint

    for value in array:
        while not s.is_empty() and s.peek() < value:
            root = s.pop()

        if value < root:
            return False

        s.push(value)

    return True


if __name__ == '__main__':
    print is_pre_order([4, 2, 1, 3, 6, 5, 7])
    print is_pre_order([4, 2, 3, 1])
