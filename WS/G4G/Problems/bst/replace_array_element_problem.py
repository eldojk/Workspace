"""
Replace every element with the least greater element on its right
Given an array of integers, replace every element with the least greater element on its right side in the array.
If there are no greater element on right side, replace it with -1.

Examples:

I/p: [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]
O/p: [18, 63, 80, 25, 32, 43, 80, 93, 80, 25, 93, -1, 28, -1, -1]
"""

from DS.algos.graphs.bst import BST


def _replace_none(element):
    return element.key if element else -1


def replace_inorder_successor(array):
    bst = BST()
    for num in array:
        bst.add(num)

    output = [bst.search(num).in_order_successor() for num in array]
    return [_replace_none(node) for node in output]