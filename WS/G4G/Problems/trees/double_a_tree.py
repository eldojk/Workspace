"""
Write a program that converts a given tree to its Double tree.
To create Double tree of the given tree, create a new
duplicate for each node, and insert the duplicate as the left child
of the original node.

http://www.geeksforgeeks.org/double-tree/
"""
from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array
from G4G.Problems.bst.vertical_sum import Node


def double_node(node):
    lft = node.left
    l_node = Node(node.data)
    l_node.left = lft
    node.left = l_node
    return node


def double_tree(root):
    if root is None:
        return None

    root.left = double_tree(root.left)
    root.right = double_tree(root.right)

    return double_node(root)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    double_tree(root)

    print get_inorder_array(root, [])

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    double_tree(root)

    print get_inorder_array(root, [])