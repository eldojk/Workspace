"""
http://www.geeksforgeeks.org/maximum-element-two-nodes-bst/

"""
# todo. what is this?
from sys import maxint

from G4G.Problems.bst.lca_and_dist import lca, Node

curr_max = -maxint


def get_max_in_path(root, val):
    global curr_max
    if root is None:
        return

    if root.data > curr_max:
        curr_max = root.data

    if val > root.data:
        get_max_in_path(root.right, val)
    elif val < root.data:
        get_max_in_path(root.left, val)


if __name__ == '__main__':
    r = Node(18)
    r.left = Node(9)
    r.right = Node(36)
    r.left.left = Node(6)
    r.left.right = Node(12)
    r.left.left.left = Node(1)
    r.left.left.right = Node(8)
    r.left.right.left = Node(10)

    lcaNode = lca(r, 1, 10)
    get_max_in_path(lcaNode, 1)
    get_max_in_path(lcaNode, 10)
    print curr_max
