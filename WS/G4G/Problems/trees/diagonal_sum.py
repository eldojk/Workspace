"""
http://www.geeksforgeeks.org/diagonal-sum-binary-tree/
"""
from G4G.Problems.bst.vertical_sum import Node


SUMS = {}
def diagonal_sum(root, level):
    global SUMS
    if root:
        SUMS[level] = root.data if SUMS.get(level) is None else SUMS[level] + root.data

        diagonal_sum(root.right, level)
        diagonal_sum(root.left, level + 1)


if __name__ == '__main__':
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    r.right.left = Node(6)
    r.right.right = Node(7)

    diagonal_sum(r, 0)
    print SUMS