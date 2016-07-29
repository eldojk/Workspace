"""
Given root of binary search tree and K as input, find K-th largest element in BST.
"""

# TODO: This won't work when array has duplicates, eg: [1, 2, 2, 3, 3, 3], the second largest
# TODO: element is '2' but this method will return '3'

from DS.algos.graphs.bst import BST

counter = 0
pos = 0
val = None


def inorder_custom(root):
    if root:
        inorder_custom(root.left)

        global counter, pos, val
        counter += 1
        if counter == pos:
            val = root.key

        inorder_custom(root.right)


def nth_largest_element(array, n):
    bst = BST()
    for num in array:
        bst.add(num)

    global pos, val

    # position of the nth smallest element in the sorted array
    pos = len(array) - n + 1

    inorder_custom(bst.root)
    return val
