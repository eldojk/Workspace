"""
Is binary tree a BST
We can use augumented dfs with range check
CTIC 4.5 #228
"""


def is_bst(root, mn, mx):
    if root is None:
        return True

    if root.data >= mx or root.data <= mn:
        return False

    left_chk = is_bst(root.left, mn, root.data)
    right_chk = is_bst(root.right, root.data, mx)

    return left_chk and right_chk

# if __name__=='__main__':
#     mx = maxint
#     mn = -maxint
#     root = Node(5)
#     root.left = Node(3)
#     root.right = Node(7)
#     root.left.left = Node(2)
#     root.left.right = Node(4)
#     root.right.left = Node(6)
#     root.right.right = Node(8)
#
#     print is_bst(root, mn, mx)