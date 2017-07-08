"""
If a sum from root to leaf is found, print that path
"""
from vertical_sum import Node


def printsum(root, sum):
    if root is None:
        return sum == 0

    else:
        lf = printsum(root.left, sum - root.data)
        if lf:
            print root.data
            return True

        rf = printsum(root.right, sum - root.data)
        if rf:
            print root.data
            return True

        return False


r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(1)
r.right.right = Node(4)

printsum(r, 8)