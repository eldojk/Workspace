"""
http://algorithms.tutorialhorizon.com/construct-binary-search-tree-from-a-given-preorder-traversal-using-recursion/

In here the creation is also done in preorder fashion. First node is created, then left is created, then right is
created. The range condition passed on to every recursive call ensures that nodes are assigned correctly
"""
from sys import maxint
from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array, Node

INT_MAX = maxint
INT_MIN = -maxint

index = 0


def bst_from_pre_order(pre_order, data, _min, _max):
    global index

    root = None
    if index < len(pre_order) and (_min < data < _max):
        root = Node(data)
        index += 1

        if index < len(pre_order):
            root.left = bst_from_pre_order(pre_order, pre_order[index], _min, data)

            root.right = bst_from_pre_order(pre_order, pre_order[index], data, _max)

    return root


if __name__ == '__main__':
    r = bst_from_pre_order([10, 5, 1, 7, 40, 50], 10, INT_MIN, INT_MAX)
    print get_inorder_array(r, [])
