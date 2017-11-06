"""
amzn

more done down

Given a Binary Tree where each node has positive and negative values.
Convert this to a tree where each node contains the sum of the left
and right sub trees in the original tree. The values of leaf nodes are
changed to 0.

For example, the following tree

                  10
               /      \
	        -2        6
           /   \      /  \
	     8    -4    7    5
should be changed to

                 20(4-2+12+6)
               /      \
	        4(8-4)      12(7+5)
           /   \      /  \
	     0      0    0    0

http://www.geeksforgeeks.org/convert-a-given-tree-to-sum-tree/
"""
from G4G.Problems.bst.vertical_sum import Node


def get_sum_tree(root):
    calculate_sum(root)
    return root


def calculate_sum(root):
    if root is None:
        return 0

    sum_left = calculate_sum(root.left)
    sum_right = calculate_sum(root.right)

    sum_of_children = sum_left + sum_right

    value = root.data
    root.data = sum_of_children
    return sum_of_children + value


def is_leaf(node):
    return node.left is None and node.right is None


if __name__ == '__main__':
    _r = Node(10)
    _r.left = Node(-2)
    _r.right = Node(6)
    _r.left.left = Node(8)
    _r.left.right = Node(-4)
    _r.right.left = Node(7)
    _r.right.right = Node(5)

    r = get_sum_tree(_r)
    print r, r.left, r.left.left


def is_sum_tree(root):
    if root is None:
        return True, 0

    is_left_st, left_sum = is_sum_tree(root.left)
    is_right_st, right_sum = is_sum_tree(root.right)

    if is_leaf(root):
        return True, root.data

    is_sum_tr = (is_left_st and is_right_st and left_sum + right_sum == root.data)
    return is_sum_tr, left_sum + right_sum + root.data


if __name__ == '__main__':
    _r = Node(26)
    _r.left = Node(10)
    _r.right = Node(3)
    _r.left.left = Node(4)
    _r.left.right = Node(6)
    _r.right.right = Node(3)

    print is_sum_tree(_r)
