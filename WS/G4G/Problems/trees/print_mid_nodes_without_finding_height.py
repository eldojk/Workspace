"""
amzn

#tricky
http://www.geeksforgeeks.org/print-middle-level-perfect-binary-tree-without-finding-height/
"""


def print_mid(a, b):
    if a is None or b is None:
        return

    if b.left is None and b.right is None:
        print a
        return

    print_mid(a.left, b.left.left)
    print_mid(a.right, b.right.right)


def print_mid_nodes(root):
    print_mid(root, root)
