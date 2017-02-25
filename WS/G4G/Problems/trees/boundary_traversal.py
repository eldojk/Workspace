"""
http://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/
"""
from G4G.Problems.bst.vertical_sum import Node


def is_leaf(node):
    return node.left is None and node.right is None


def top_down_left_traversal(root):
    if root:
        if is_leaf(root):
            return

        print root,
        top_down_left_traversal(root.left)


def bottom_up_right_traversal(root):
    if root:
        if is_leaf(root):
            return

        bottom_up_right_traversal(root.right)
        print root,


def print_leaves(root):
    if root:
        print_leaves(root.left)

        if is_leaf(root):
            print root,

        print_leaves(root.right)


def boundary_traversal(root):
    top_down_left_traversal(root)
    print_leaves(root)
    bottom_up_right_traversal(root)


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    boundary_traversal(root)