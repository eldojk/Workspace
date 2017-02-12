"""
http://www.geeksforgeeks.org/find-the-largest-subtree-in-a-tree-that-is-also-a-bst/

a node can be a bst if and only if its left and right subtrees are bsts.
"""
from sys import maxint

MAX = maxint
MIN = -maxint


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def largest_bst(root, rang):
    if root.left:
        l_size, is_left_bst, l_range = largest_bst(root.left, (rang[0], root.data))
    if root.right:
        r_size, is_right_bst, r_range = largest_bst(root.right, (root.data, rang[1]))

    if root.left is None and root.right is None:
        return 1, True, (root.data, root.data)

    is_left_satisfied = False
    is_right_satisfied = False
    if root.left:
        is_left_satisfied = (l_range[1] <= root.data) and is_left_bst
    if root.right:
        is_right_satisfied = (r_range[0] >= root.data) and is_right_bst

    if is_left_satisfied and is_right_satisfied:
        return (l_size + r_size + 1), True, (l_range[0], r_range[1])
    else:
        return max(l_size, r_size), False, (l_range[0], r_range[1])


def largest_bst_in_btree(root):
    return largest_bst(root, (MIN, MAX))[0]


root = Node(50)
root.left = Node(30)
root.right = Node(60)
root.left.left = Node(5)
root.left.right = Node(20)
root.right.left = Node(45)
root.right.right = Node(70)
root.right.right.left = Node(65)
root.right.right.right = Node(80)

print largest_bst_in_btree(root)

root = Node(5)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(3)

print largest_bst_in_btree(root)
