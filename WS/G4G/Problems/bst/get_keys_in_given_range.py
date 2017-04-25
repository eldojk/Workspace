"""
amzn

http://www.geeksforgeeks.org/print-bst-keys-in-the-given-range/
"""


def get_keys(root, li, k1, k2):
    if root is None:
        return

    if root.data > k1:
        get_keys(root.left, li, k1, k2)

    if k1 < root.data < k2:
        li.append(root)

    if root.data < k2:
        get_keys(root.right, li, k1, k2)