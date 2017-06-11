"""
amzn, msft

http://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/

using min max
"""
from G4G.Problems.bst.vertical_sum import Node
from sys import maxint


PRE_INDEX = 0


def create_bst(pre_order, _min, _max):
    global PRE_INDEX

    if PRE_INDEX >= len(pre_order):
        return None

    root = None

    data = pre_order[PRE_INDEX]

    if _min < data < _max:
        root = Node(data)
        PRE_INDEX += 1

        root.left = create_bst(pre_order, _min, data)

        root.right = create_bst(pre_order, data, _max)

    return root


if __name__ == '__main__':
    r = create_bst([10, 5, 1, 7, 40, 50], -maxint, maxint)

    print r, r.left, r.right, r.left.left, r.left.right, r.right.right
