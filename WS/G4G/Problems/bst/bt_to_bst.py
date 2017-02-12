"""
http://www.geeksforgeeks.org/binary-tree-to-binary-search-tree-conversion/
get_inorder, sort it, convert to bst
"""

from G4G.Problems.bst.create_bst_from_sorted_array import create_bst
from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array, Node


def convert_to_bst(root):
    in_order = get_inorder_array(root, [])
    in_order.sort()
    return create_bst(in_order, 0, len(in_order) - 1)


if __name__ == '__main__':
    r = Node(10)
    r.left = Node(2)
    r.right = Node(7)
    r.left.left = Node(8)
    r.left.right = Node(4)

    root = convert_to_bst(r)
    print get_inorder_array(root, [])
