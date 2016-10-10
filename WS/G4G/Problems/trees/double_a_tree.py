"""
Write a program that converts a given tree to its Double tree. To create Double tree of the given tree, create a new
duplicate for each node, and insert the duplicate as the left child of the original node.

http://www.geeksforgeeks.org/double-tree/
"""
from G4G.Problems.bst.vertical_sum import Node


def double_node(node):
    lft = node.left
    l_node = Node(node.data)
    l_node.left = lft
    node.left = l_node


def double_tree(root):
    if root:
        left = root.left
        double_node(root)

        double_tree(left)
        double_tree(root.right)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
#
# double_tree(root)
#
# print root
# print root.left
# print root.right
# print root.right.left
# print root.left.left
# print root.left.left.left
