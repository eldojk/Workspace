"""
amzn

Given a binary tree, write a function to get the maximum width of the given tree. Width of a tree is maximum of widths
of all levels.

http://www.geeksforgeeks.org/maximum-width-of-a-binary-tree/
"""
from G4G.Problems.bst.vertical_sum import Node


def populate_element_sizes(root, elements_at_levels, level):
    if root:
        elements_at_levels[level] += 1

        populate_element_sizes(root.left, elements_at_levels, level + 1)
        populate_element_sizes(root.right, elements_at_levels, level + 1)


def max_width(root):
    elements_at_levels = [0 for i in range(4)]  # should be range(height)
    populate_element_sizes(root, elements_at_levels, 0)

    return max(elements_at_levels)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)

    print max_width(root)
