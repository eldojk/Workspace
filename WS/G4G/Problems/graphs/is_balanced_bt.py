"""
Check if a Binary tree is balanced
CTIC 4.1 #220
"""


def check_height(root):
    """
    At every node we check the left and right height and return the height. If at any point we find an unbalanced
    subtree we return -1 instead of the height. In a node, if one of the subtrees has returned a -1, we stop computing
    the height of that node and return -1 upwards

    :param root:
    :return:
    """
    if root is None:
        return 0

    left_height = check_height(root.left)
    if left_height == -1:
        return -1

    right_height = check_height(root.right)
    if right_height == -1:
        return -1

    height_diff = left_height - right_height
    if abs(height_diff) > 1:
        return -1

    return 1 + max(left_height, right_height)


def is_balanced(root):
    height = check_height(root)

    if height == -1:
        return False

    return True
