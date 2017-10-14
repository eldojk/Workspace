"""
amzn

http://www.geeksforgeeks.org/print-bst-keys-in-the-given-range/
"""
from DS.algos.graphs.bst import BST


def get_keys(root, li, k1, k2):
    if root is None:
        return

    if root.key > k1:
        get_keys(root.left, li, k1, k2)

    if k1 <= root.key <= k2:
        li.append(root)

    if root.key < k2:
        get_keys(root.right, li, k1, k2)

    return li


if __name__ == '__main__':
    bst = BST()
    bst.add(20)
    bst.add(8)
    bst.add(22)
    bst.add(4)
    bst.add(12)

    root = bst.root
    print get_keys(root, [], 10, 22)
