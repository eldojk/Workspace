"""
In order successor
"""


def minimum_node(node):
    if node.left:
        return minimum_node(node.left)

    return node


def in_order_successor(node):
    if node.right:
        return minimum_node(node.right)

    else:
        q = node
        p = node.parent
        while p is not None and p.left != q:
            q = p
            p = p.parent

        return p
