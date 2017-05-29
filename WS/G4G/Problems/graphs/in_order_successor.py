"""
amzn

In order successor
http://www.geeksforgeeks.org/inorder-successor-in-binary-search-tree/
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


def in_order_successor_wo_parent(node, root):
    if node.right:
        return minimum_node(node.right)

    succ = None

    while root is not None:
        if node.data < root.data:
            succ = root
            root = root.left

        elif node.data > root.data:
            root = root.right

        else:
            break

    return succ
