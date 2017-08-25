"""
amzn

http://www.geeksforgeeks.org/find-maximum-path-sum-two-leaves-binary-tree/

bottom up summing ensures efficiency
"""
from sys import maxint

from G4G.Problems.bst.vertical_sum import Node


def is_leaf(node):
    return node.left is None and node.right is None


MAX_SUM = -maxint


def max_leaf_to_root_paths(root):
    global MAX_SUM
    if root is None:
        return 0

    if is_leaf(root):
        return root.data

    left_sum = max_leaf_to_root_paths(root.left)
    right_sum = max_leaf_to_root_paths(root.right)

    curr_sum = left_sum + right_sum + root.data
    if curr_sum > MAX_SUM:
        MAX_SUM = curr_sum

    return max(left_sum, right_sum) + root.data


if __name__ == '__main__':
    r = Node(-15)
    r.left = Node(5)
    r.right = Node(6)
    r.left.left = Node(-8)
    r.left.right = Node(-1)
    r.left.left.left = Node(2)
    r.left.left.right = Node(6)
    r.right.left = Node(3)
    r.right.right = Node(9)
    r.right.right.right = Node(0)
    r.right.right.right.left = Node(4)
    r.right.right.right.right = Node(-1)
    r.right.right.right.right.left = Node(10)

    max_leaf_to_root_paths(r)
    print MAX_SUM
