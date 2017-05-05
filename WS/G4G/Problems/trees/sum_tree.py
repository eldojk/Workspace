"""
amzn

Given a Binary Tree where each node has positive and negative values. Convert this to a tree where each node contains
the sum of the left and right sub trees in the original tree. The values of leaf nodes are changed to 0.

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

    if sum_of_children == 0:
        sum_node = root.data
        root.data = 0
        return sum_node

    value = root.data
    root.data = sum_of_children
    return sum_of_children + value


def is_leaf(node):
    return node.left is None and node.right is None


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(-2)
    root.right = Node(6)
    root.left.left = Node(8)
    root.left.right = Node(-4)
    root.right.left = Node(7)
    root.right.right = Node(5)

    r = get_sum_tree(root)
    print r


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
    root = Node(26)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.right = Node(3)

    print is_sum_tree(root)


